import requests
import json
import os

# System Configuration
API_KEY = "AIzaSyDA-wgo3eG2U2ITMUz17-6XoIuTakvXC4E"
MODEL_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def fetch_architectural_design(prompt):
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(MODEL_URL, headers=headers, data=json.dumps(payload))
    return response.json()['candidates'][0]['content']['parts'][0]['text']

def validation_repair_engine(design_text, core_idea):
    """Phase 4: Automated Verification & Repair"""
    print("--- Running Design Validation ---")
    validation_flags = []
    
    # Structural checks
    if "TABLE" not in design_text.upper(): validation_flags.append("Missing Structural Components")
    if "PRIMARY KEY" not in design_text.upper(): validation_flags.append("Missing Unique Identifiers")
    
    if validation_flags:
        print(f"Structural Gaps Detected: {validation_flags}. Initiating Auto-Repair...")
        repair_prompt = f"Refine this architectural design. Fix these gaps: {validation_flags}. Original Design: {design_text}"
        return fetch_architectural_design(repair_prompt)
    
    return design_text

def run_architect_pipeline(core_idea):
    print(f"--- Initiating Pipeline for: {core_idea} ---")
    
    # 1. Component Generation
    initial_design = fetch_architectural_design(f"Design a 3-table data architecture for: {core_idea}. Output only the schema code.")
    clean_design = initial_design.replace("```sql", "").replace("```", "").strip()
    
    # 2. Validation & Repair
    final_output = validation_repair_engine(clean_design, core_idea)
    
    # 3. Secure Documentation
    output_filename = "system_architecture_design.txt"
    with open(output_filename, "w") as f:
        f.write(final_output)
    
    print(f"\n--- SUCCESS ---")
    print(f"Architectural Blueprint saved to: {os.path.abspath(output_filename)}")

if __name__ == "__main__":
    run_architect_pipeline("A Library Management System")