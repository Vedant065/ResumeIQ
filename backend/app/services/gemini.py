import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_resume(text: str):
    prompt = f"""
You are an ATS Resume Expert.

Analyze this resume and provide:
1. Overall feedback
2. Strengths
3. Weaknesses
4. Missing skills
5. ATS improvement suggestions

Resume:
{text}
"""

    delays = [2, 4, 8]

    for delay in delays:
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
            )
            return response.text
        except Exception as e:
            print("Gemini Error:", e)
            time.sleep(delay)

    return "AI feedback is temporarily unavailable. Please try again later."