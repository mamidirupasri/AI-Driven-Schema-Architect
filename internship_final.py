import requests
import json
import os

# Your API Key
API_KEY = "AIzaSyDA-wgo3eG2U2ITMUz17-6XoIuTakvXC4E"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def run_pipeline(user_prompt):
    print(f"--- STEP 1: Designing Schema for: {user_prompt} ---")
    
    # We are asking for FULL SQL code now
    instruction = (
        f"You are a Senior DBA. Create a SQL schema for '{user_prompt}'. "
        "Provide exactly 3 tables with primary keys and clear data types. "
        "Output ONLY the SQL code. No conversational text."
    )

    payload = {
        "contents": [{"parts": [{"text": instruction}]}]
    }
    
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(URL, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            data = response.json()
            sql_output = data['candidates'][0]['content']['parts'][0]['text']
            
            # Remove any markdown formatting (```sql ... ```) if the AI adds it
            clean_sql = sql_output.replace("```sql", "").replace("```", "").strip()
            
            # STEP 2: Save to a file
            filename = "generated_schema.sql"
            with open(filename, "w") as f:
                f.write(clean_sql)
            
            print(f"\n--- SUCCESS! ---")
            print(f"File saved as: {os.path.abspath(filename)}")
            print("\nPreview of generated SQL:")
            print(clean_sql)
            
        else:
            print(f"API Error: {response.status_code}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    project_idea = "A Library Management System with Books and Members"
    run_pipeline(project_idea)