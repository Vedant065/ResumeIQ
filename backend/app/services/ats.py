import re

KEYWORDS = [
    "python", "java", "c", "c++", "sql", "mysql", "mongodb",
    "react", "reactjs", "typescript", "javascript",
    "html", "css", "tailwind", "vite",
    "fastapi", "flask", "django", "rest api",
    "git", "github", "docker",
    "aws", "azure", "cloud",
    "machine learning", "deep learning",
    "artificial intelligence", "nlp",
    "tensorflow", "pytorch",
    "api", "jwt", "authentication",
    "problem solving", "communication",
    "teamwork", "leadership",
    "data structures", "algorithms",
    "render", "postman"
]


def calculate_ats_score(text: str):

    text_lower = text.lower()

    score = 0

    strengths = []
    suggestions = []
    keywords_found = []
    missing_keywords = []

    # -----------------------------------
    # CONTACT INFORMATION (10)
    # -----------------------------------

    contact_score = 0

    if re.search(r"\S+@\S+\.\S+", text):
        contact_score += 5
    else:
        suggestions.append("Add a professional email address.")

    if re.search(r"\+?\d[\d\s\-]{8,}", text):
        contact_score += 5
    else:
        suggestions.append("Add a phone number.")

    score += contact_score

    # -----------------------------------
    # SECTIONS (20)
    # -----------------------------------

    sections = {
        "Education": "education" in text_lower,
        "Skills": "skills" in text_lower,
        "Projects": "project" in text_lower,
        "Experience": "experience" in text_lower,
        "Certifications": "certification" in text_lower,
    }

    section_analysis = []

    section_score = 0

    for name, present in sections.items():

        section_analysis.append({
            "name": name,
            "present": present
        })

        if present:
            section_score += 4
        else:
            suggestions.append(f"Add a {name} section.")

    score += section_score

    if section_score >= 16:
        strengths.append("Well-structured resume.")

    # -----------------------------------
    # KEYWORDS (30)
    # -----------------------------------

    for keyword in KEYWORDS:

        if keyword in text_lower:
            keywords_found.append(keyword)
        else:
            missing_keywords.append(keyword)

    keyword_score = min(30, len(keywords_found) * 2)

    score += keyword_score

    if keyword_score >= 24:
        strengths.append("Excellent technical keyword coverage.")
    elif keyword_score >= 16:
        strengths.append("Good technical skills.")
    else:
        suggestions.append(
            "Include more job-specific technical skills."
        )

    # -----------------------------------
    # EXPERIENCE (20)
    # -----------------------------------

    experience_score = 0

    if "experience" in text_lower:

        experience_score += 10

        numbers = len(re.findall(r"\d+%|\d+\+|\d+", text))

        if numbers >= 5:
            experience_score += 10
            strengths.append(
                "Experience includes quantified achievements."
            )

        elif numbers >= 2:
            experience_score += 7

        else:
            experience_score += 5
            suggestions.append(
                "Quantify your achievements using numbers."
            )

    else:
        suggestions.append(
            "Include internship or work experience."
        )

    score += experience_score

    # -----------------------------------
    # PROJECTS (15)
    # -----------------------------------

    project_score = 0

    project_count = len(
        re.findall(
            r"resumeiq|tokenshield|devtwin|project",
            text_lower
        )
    )

    if project_count >= 3:
        project_score = 15

    elif project_count == 2:
        project_score = 12

    elif project_count == 1:
        project_score = 8

    else:
        suggestions.append(
            "Include at least two technical projects."
        )

    score += project_score

    # -----------------------------------
    # RESUME LENGTH (5)
    # -----------------------------------

    words = len(text.split())

    if 300 <= words <= 650:

        score += 5

    elif 250 <= words < 300:

        score += 4

    elif 180 <= words < 250:

        score += 3
        suggestions.append(
            "Expand project descriptions."
        )

    elif words > 650:

        score += 3
        suggestions.append(
            "Reduce resume length."
        )

    else:

        score += 2
        suggestions.append(
            "Resume is too short."
        )

    # -----------------------------------
    # BONUS SCORE
    # -----------------------------------

    if (
        section_score >= 16 and
        keyword_score >= 24 and
        experience_score >= 15
    ):
        score += 5
        strengths.append(
            "Excellent ATS compatibility."
        )

    # -----------------------------------
    # FINAL SCORE
    # -----------------------------------

    # Normalize score
    if score >= 95:
        score = 95
    elif score >= 90:
        score = 90
    elif score >= 80:
        score = 85
    elif score >= 70:
        score = 75
    elif score >= 60:
        score = 65

    # -----------------------------------
    # RATING
    # -----------------------------------

    if score >= 90:
        strengths.append("Highly optimized for ATS.")

    elif score >= 75:
        strengths.append("Good ATS compatibility.")

    elif score >= 60:
        suggestions.append(
            "Improve keywords and achievements."
        )

    else:
        suggestions.append(
            "Resume needs significant improvement."
        )

    return {
        "score": score,
        "keywords": keywords_found,
        "strengths": strengths,
        "missing_keywords": missing_keywords[:10],
        "suggestions": suggestions,
        "section_analysis": section_analysis,
    }
