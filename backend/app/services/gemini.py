import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = None
if api_key:
    client = genai.Client(api_key=api_key)


def local_feedback(text: str):
    text = text.lower()

    strengths = []
    improvements = []

    # Contact
    if "@" in text:
        strengths.append("Professional email address found.")
    else:
        improvements.append("Add a professional email address.")

    if any(word in text for word in ["python", "java", "react", "fastapi", "sql"]):
        strengths.append("Good technical skills included.")
    else:
        improvements.append("Include more technical skills relevant to your field.")

    # Projects
    if "project" in text:
        strengths.append("Projects section detected.")
    else:
        improvements.append("Add a Projects section with real-world work.")

    # Experience
    if "experience" in text:
        strengths.append("Experience section present.")
    else:
        improvements.append("Include internships or practical experience.")

    # Education
    if "education" in text:
        strengths.append("Education section present.")
    else:
        improvements.append("Add an Education section.")

    # Resume length
    words = len(text.split())

    if words < 250:
        improvements.append(
            "Resume is too short. Add achievements and detailed project descriptions."
        )
    elif words > 900:
        improvements.append(
            "Resume is lengthy. Keep it concise and focused."
        )
    else:
        strengths.append("Resume length is appropriate.")

    feedback = "📋 Resume Analysis\n\n"

    feedback += "✅ Strengths\n"
    if strengths:
        for s in strengths:
            feedback += f"• {s}\n"
    else:
        feedback += "• No major strengths detected.\n"

    feedback += "\n⚠ Areas for Improvement\n"
    if improvements:
        for s in improvements:
            feedback += f"• {s}\n"
    else:
        feedback += "• Your resume is well optimized.\n"

    feedback += (
        "\n💡 Recommendation\n"
        "Tailor your resume to every job description, "
        "use measurable achievements, and include relevant keywords."
    )

    return feedback


def analyze_resume(text: str):
    if client is None:
        return local_feedback(text)

    prompt = f"""
You are an ATS Resume Expert.

Analyze this resume.

Provide:
1. Overall feedback
2. Strengths
3. Weaknesses
4. Missing skills
5. ATS improvement suggestions

Resume:

{text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        if response.text:
            return response.text

    except Exception as e:
        print("Gemini Error:", e)

    # Fallback
    return local_feedback(text)