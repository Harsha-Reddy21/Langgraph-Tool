from content_master import run_content_master
import json
import os

def test_queries():
    queries = [
        "Create a presentation on renewable energy trends",
        "Generate a document about AI ethics",
        "Build a webpage about quantum computing basics"
    ]
    
    for query in queries:
        print(f"\n{'='*50}")
        print(f"Testing: {query}")
        print('='*50)
        
        try:
            result = run_content_master(query)
            print(f"Content Type: {result.content_type}")
            print(f"Template: {result.template}")
            print(f"Quality Score: {result.quality_score}")
            print(f"Sources Found: {len(result.verified_sources)}")
            print(f"Visuals Created: {len(result.visuals)}")
            print(f"Sections: {list(result.generated_content.keys())}")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = "your-api-key-here"
    test_queries() 