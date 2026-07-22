import re

KEYWORDS = [
    "python",
    "java",
    "c++",
    "sql",
    "react",
    "fastapi",
    "flask",
    "docker",
    "git",
    "aws",
    "azure",
    "machine learning",
    "tensorflow",
    "pytorch",
    "api",
    "mongodb",
    "mysql",
    "html",
    "css",
    "javascript",
]


def calculate_ats_score(text: str):
    text_lower = text.lower()

    score = 0

    strengths = []
    suggestions = []
    missing_keywords = []
    keywords_found = []

    # -----------------------------
    # Contact Information
    # -----------------------------
    if re.search(r"\S+@\S+\.\S+", text):
        score += 10
    else:
        suggestions.append("Add a professional email address.")

    if re.search(r"\+?\d[\d\s\-]{8,}", text):
        score += 5
    else:
        suggestions.append("Add a phone number.")

    # -----------------------------
    # Resume Sections
    # -----------------------------
    sections = {
        "Contact Information": bool(re.search(r"\S+@\S+\.\S+", text)),
        "Education": "education" in text_lower,
        "Skills": "skills" in text_lower,
        "Projects": "projects" in text_lower,
        "Experience": "experience" in text_lower,
        "Certifications": (
            "certification" in text_lower
            or "certifications" in text_lower
        ),
    }

    section_analysis = []

    for section, present in sections.items():
        section_analysis.append(
            {
                "name": section,
                "present": present,
            }
        )

        if present:
            score += 8
            strengths.append(section)
        else:
            suggestions.append(f"Add a {section} section.")

    # -----------------------------
    # Keywords
    # -----------------------------
    for keyword in KEYWORDS:
        if keyword in text_lower:
            keywords_found.append(keyword)
            score += 2
        else:
            missing_keywords.append(keyword)

    # -----------------------------
    # Resume Length
    # -----------------------------
    words = len(text.split())

    if words >= 350:
        score += 10
    else:
        suggestions.append(
            "Resume is short. Include more achievements."
        )

    score = min(score, 100)

    return {
        "score": score,
        "keywords": keywords_found,
        "strengths": strengths,
        "missing_keywords": missing_keywords[:10],
        "suggestions": suggestions,
        "section_analysis": section_analysis,
    }