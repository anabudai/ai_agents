import os, requests
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_KEY = os.getenv("AUTH_KEY_TOKEN")

def generate_x_post(input):

    prompt = f'''
                You are an expert social media manager and you excel at crafting viral and highly engaging posts social media

                Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user input 

                Keep the posts short and focused, stucture it in a clean, readable way using line breaks and empty lines

                Here's the topic provided by the user for which you need to generate the post:   
                <topic>{input}</topic>
'''  
    payload = {
        "model": "gpt-4o",
        "input": prompt
    }
    response = requests.post("https://api.openai.com/v1/responses",
                             json=payload,
                             headers = {
                                 "Content-Type": "application/json",
                                 "Authorization": f"Bearer {OPEN_AI_KEY}"}
                             )
    
    response_text = response.json().get("output", [{}])[0].get("content", "")[0].get("text", "")
    return response_text

def main():
    user_input = input("What should the post be about?\n")
    result = generate_x_post(user_input)
    print(f"===== Response: {result}")

if __name__ == "__main__":
    main()