import requests
import json
import os

# Your API Key
API_KEY = "AIzaSyDA-wgo3eG2U2ITMUz17-6XoIuTakvXC4E"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def verify_sql(sql_text):
    """Phase 3: Verification Engine"""
    checks = {
        "Has CREATE": "CREATE TABLE" in sql_text.upper(),
        "Has Primary Key": "PRIMARY KEY" in sql_text.upper(),
        "Has Foreign Key": "FOREIGN KEY" in sql_text.upper()
    }
    return checks

def run_phase_3(user_prompt):
    print(f"--- PHASE 3: Executing and Verifying: {user_prompt} ---")
    
    instruction = (
        f"Generate a professional SQL schema for '{user_prompt}'. "
        "Include 3 related tables with proper data types and Foreign Key constraints. "
        "Output ONLY the SQL code."
    )

    payload = {"contents": [{"parts": [{"text": instruction}]}]}
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(URL, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            raw_sql = response.json()['candidates'][0]['content']['parts'][0]['text']
            clean_sql = raw_sql.replace("```sql", "").replace("```", "").strip()
            
            # RUN VERIFICATION
            report = verify_sql(clean_sql)
            print("\n--- VERIFICATION REPORT ---")
            for check, passed in report.items():
                status = "✅ PASSED" if passed else "❌ FAILED"
                print(f"{check}: {status}")
            
            # SAVE FINAL VERSION
            with open("final_verified_schema.sql", "w") as f:
                f.write(clean_sql)
            
            print(f"\nSUCCESS: Phase 3 Complete. File saved to D:\\ai_intern")
            
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Connection Error: {str(e)}")

if __name__ == "__main__":
    run_phase_3("Library Management System with Books, Members, and Records")