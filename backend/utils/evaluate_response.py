import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_response(transcript):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content":  "You are an expert IELTS examiner simulating a real-time IELTS Speaking Test. "
                "Your task is to assess the user's speaking performance based on official IELTS criteria, "
                "including fluency, pronunciation, grammatical range and accuracy, and lexical resource (vocabulary). "
                "Provide constructive feedback with specific suggestions for improvement. "
                "Identify mistakes in grammar and pronunciation, suggest better vocabulary choices, and offer tips to improve fluency and coherence. "
                "Keep your feedback concise yet informative, helping the user to gradually enhance their speaking abilities."},
            {"role": "user", "content": transcript}
        ]
    )
    return response.choices[0].message.content
