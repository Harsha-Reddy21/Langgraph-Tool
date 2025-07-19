from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from typing import TypedDict
from database import setup_database, execute_query
import os
from dotenv import load_dotenv

load_dotenv()
def get_openai_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Please set your OpenAI API key:")
        print("export OPENAI_API_KEY=your_key_here")
        print("Or set it in the code: os.environ['OPENAI_API_KEY'] = 'your_key'")
        return "your-api-key-here"
    return api_key

os.environ["OPENAI_API_KEY"] = get_openai_key()
llm = ChatOpenAI(model="gpt-4", temperature=0)

class State(TypedDict):
    question: str
    sql: str
    results: list
    response: str
    error: str

def parse_query(state):
    prompt = f"Convert this question to SQL for students table (columns: name, subject, grade): {state['question']}"
    sql = llm.invoke(prompt).content.strip()
    return {"sql": sql}

def validate_sql(state):
    sql = state["sql"]
    if not sql.upper().startswith("SELECT"):
        return {"error": "Only SELECT queries allowed"}
    return {"error": ""}

def execute_query_node(state):
    results, error = execute_query(state["sql"])
    if error:
        return {"error": error}
    return {"results": results, "error": ""}

def generate_response(state):
    if state.get("error"):
        return {"response": f"Error: {state['error']}"}
    
    prompt = f"Convert this SQL result to natural language. Question: {state['question']}, Results: {state['results']}"
    response = llm.invoke(prompt).content
    return {"response": response}

def should_retry(state):
    return "parse" if state.get("error") and "Only SELECT" in state["error"] else "execute"

def should_respond(state):
    return "respond"

def create_graph():
    workflow = StateGraph(State)
    
    workflow.add_node("parse", parse_query)
    workflow.add_node("validate", validate_sql)
    workflow.add_node("execute", execute_query_node)
    workflow.add_node("respond", generate_response)
    
    workflow.set_entry_point("parse")
    workflow.add_edge("parse", "validate")
    workflow.add_conditional_edges("validate", should_retry, {"parse": "parse", "execute": "execute"})
    workflow.add_conditional_edges("execute", should_respond, {"respond": "respond"})
    workflow.add_edge("respond", END)
    
    return workflow.compile()

def run_agent(question):
    setup_database()
    graph = create_graph()
    result = graph.invoke({"question": question})
    return result["response"]

if __name__ == "__main__":
    print(run_agent("What grades did Alice get?"))
    print(run_agent("Who got the highest grade in Math?")) 