import requests
import json

# Your API Key
API_KEY = "AIzaSyDA-wgo3eG2U2ITMUz17-6XoIuTakvXC4E"

# 2026 CURRENT STABLE ENDPOINT
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def run_stage_1(user_prompt):
    print(f"--- AI is thinking about: {user_prompt} ---")
    
    payload = {
        "contents": [{
            "parts": [{
                "text": (
                    f"You are a Database Architect. For the idea '{user_prompt}', "
                    "list exactly 3 database tables needed with 2 columns each. "
                    "Format: Table Name (Column1, Column2)"
                )
            }]
        }]
    }
    
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(URL, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            data = response.json()
            # Extract the text from the response
            answer = data['candidates'][0]['content']['parts'][0]['text']
            return answer
        else:
            return f"Server Error {response.status_code}: {response.text}"
            
    except Exception as e:
        return f"Connection Error: {str(e)}"

if __name__ == "__main__":
    # Test it
    idea = "A library management system"
    result = run_stage_1(idea)
    
    print("\n--- STAGE 1 RESULT ---")
    print(result)