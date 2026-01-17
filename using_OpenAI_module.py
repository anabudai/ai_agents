from openai import OpenAI
from dotenv import load_dotenv
import os, json

load_dotenv()
OPEN_AI_KEY = os.getenv("AUTH_KEY_TOKEN")

client_open_ai = OpenAI(api_key = OPEN_AI_KEY,);

def generate_x_post(input):
    with open("post-generated.json", "r") as post_generated_file:
        examples = json.load(post_generated_file)
    examples_all = ""
    for i, example in enumerate(examples):
        examples_all += f"""
        <example-{i}>
            <topic>{example["topic"]}</topic>
            <generated-post>{example["post"]}</generated-post>
        </example-{i}>
        """
    prompt = f'''
                You are an expert social media manager and you excel at crafting viral and highly engaging posts social media

                Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user input 

                Keep the posts short and focused, stucture it in a clean, readable way using line breaks and empty lines

                Here's the topic provided by the user for which you need to generate the post:   
                <topic>{input}</topic>

                Here are some examples of topics and generated posts:
                <examples>
                    {examples_all}
                </examples>
                Please use the tone, language, information, content from the examples above to generate user responses
    '''  
    response = client_open_ai.responses.create(
        model = "gpt-4o",
        input = prompt
    )
    return response.output_text


def promp_ai_and_response():
    user_input = input("What should the post be about?\n")
    result = generate_x_post(user_input)
    print(f"===== Response: {result}")

if __name__ == "__main__":
    promp_ai_and_response()