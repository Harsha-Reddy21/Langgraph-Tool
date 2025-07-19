import os
from dotenv import load_dotenv
from content_master import run_content_master
import json

load_dotenv()

def main():
    query = input("Enter your content request: ")
    
    if not query.strip():
        query = "Create a presentation on renewable energy trends"
        print(f"Using default query: {query}")
    
    try:
        result = run_content_master(query)
        
        print(f"\nResult:")
        print(f"Type: {result['content_type']}")
        print(f"Template: {result['template']}")
        print(f"Quality Score: {result['quality_score']:.2f}")
        print(f"Sections Generated: {len(result['generated_content'])}")
        print(f"Visuals Created: {len(result['visuals'])}")
        print(f"Sources Used: {len(result['verified_sources'])}")
        
        with open("output.json", "w") as f:
            json.dump(result['final_output'], f, indent=2, default=str)
        print("\nFull output saved to output.json")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 