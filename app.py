import requests
import json

# GLOBAL VARIABLES - MUST BE AT THE TOP
API_KEY = "AIzaSyA1RSFVAQqZH7Yt4aGSoIx6lq2hwkzH9lo"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def fetch_architectural_design(prompt):
    headers = {'Content-Type': 'application/json'}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    
    # This is Line 14 (will match your error line 10 logic)
    response = requests.post(API_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    return f"Error: {response.status_code}"

def run_architect_pipeline(core_idea):
    # This is Line 22 (will match your error line 45 logic)
    print(f"--- Initiating Pipeline for: {core_idea} ---")
    initial_design = fetch_architectural_design(f"Design a 3-table data architecture for: {core_idea}. Output only the schema code.")
    print(initial_design)

if __name__ == "__main__":
    # This is Line 28 (will match your error line 60 logic)
    run_architect_pipeline("A Library Management System")