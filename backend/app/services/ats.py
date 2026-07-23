import re

# =====================================================
# CONFIGURATION
# =====================================================

TOTAL_SCORE = 100

CONTACT_WEIGHT = 5
SECTION_WEIGHT = 10
SKILL_WEIGHT = 20
EXPERIENCE_WEIGHT = 20
PROJECT_WEIGHT = 20
ACHIEVEMENT_WEIGHT = 10
FORMAT_WEIGHT = 10
LENGTH_WEIGHT = 5


# =====================================================
# CONTACT REGEX
# =====================================================

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
PHONE_REGEX = r"(\+?\d[\d\s\-]{9,15})"
LINKEDIN_REGEX = r"linkedin\.com"
GITHUB_REGEX = r"github\.com"


# =====================================================
# SECTION HEADINGS
# =====================================================

SECTIONS = {
    "Education": ["education"],
    "Skills": ["skills", "technical skills"],
    "Projects": ["projects", "project"],
    "Experience": [
        "experience",
        "internship",
        "work experience",
        "professional experience"
    ],
    "Certifications": [
        "certification",
        "certifications"
    ]
}


# =====================================================
# SKILL CATEGORIES
# =====================================================

SKILL_CATEGORIES = {

    "Languages": [
        "python",
        "java",
        "c",
        "c++",
        "javascript",
        "typescript"
    ],

    "Frontend": [
        "html",
        "css",
        "react",
        "tailwind",
        "bootstrap",
        "angular",
        "vue"
    ],

    "Backend": [
        "fastapi",
        "flask",
        "django",
        "node",
        "express"
    ],

    "Database": [
        "mysql",
        "postgresql",
        "mongodb",
        "firebase"
    ],

    "Cloud": [
        "aws",
        "azure",
        "docker",
        "kubernetes",
        "render"
    ],

    "AI": [
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "opencv",
        "nlp"
    ]
}


ACTION_VERBS = {

    "developed",
    "built",
    "created",
    "implemented",
    "designed",
    "optimized",
    "engineered",
    "improved",
    "deployed",
    "managed",
    "led",
    "integrated",
    "automated",
    "tested",
    "configured"

}


# =====================================================
# HELPERS
# =====================================================

def word_count(text):

    return len(text.split())


def number_count(text):

    return len(
        re.findall(
            r"\d+%|\d+\+|\d+",
            text
        )
    )

IMPACT_PATTERNS = [
    r"\d+%",
    r"\d+\+",
    r"\d+\s*(users|customers|clients|downloads)",
    r"\d+\s*(ms|sec|seconds|minutes)",
    r"\d+\s*(x|times)"
]

def impact_count(text):
    count = 0
    text = text.lower()

    for pattern in IMPACT_PATTERNS:
        count += len(re.findall(pattern, text))

    return count

def action_count(text):

    text = text.lower()

    count = 0

    for verb in ACTION_VERBS:

        count += len(
            re.findall(
                r"\b"+re.escape(verb)+r"\b",
                text
            )
        )

    return count


def detect_sections(text):

    text = text.lower()

    result = {}

    for section, aliases in SECTIONS.items():

        result[section] = any(
            alias in text
            for alias in aliases
        )

    return result


def extract_skills(text):

    text = text.lower()

    found = {}

    for category, skills in SKILL_CATEGORIES.items():

        present = []

        for skill in skills:

            if re.search(
                r"\b"+re.escape(skill)+r"\b",
                text
            ):
                present.append(skill)

        found[category] = present

    return found


def flatten_skills(skill_dict):

    skills = []

    for values in skill_dict.values():

        skills.extend(values)

    return sorted(list(set(skills)))
def extract_section(text, section_names):
    text = text.replace("\r", "")
    lines = text.split("\n")

    headings = [
        "education",
        "skills",
        "projects",
        "experience",
        "internship",
        "certifications",
        "achievements"
    ]

    start = None
    end = len(lines)

    for i, line in enumerate(lines):
        if line.strip().lower() in section_names:
            start = i + 1
            break

    if start is None:
        return ""

    for j in range(start, len(lines)):
        if lines[j].strip().lower() in headings:
            end = j
            break

    return "\n".join(lines[start:end])

# =====================================================
# CONTACT SCORE (5)
# =====================================================

def score_contact(text):

    score = 0
    suggestions = []

    if re.search(EMAIL_REGEX, text):
        score += 1
    else:
        suggestions.append("Add a professional email address.")

    if re.search(PHONE_REGEX, text):
        score += 1
    else:
        suggestions.append("Add a phone number.")

    if re.search(LINKEDIN_REGEX, text.lower()):
        score += 1
    else:
        suggestions.append("Add your LinkedIn profile.")

    if re.search(GITHUB_REGEX, text.lower()):
        score += 1
    else:
        suggestions.append("Add your GitHub profile.")

    # Bonus for having both LinkedIn and GitHub
    if (
        re.search(LINKEDIN_REGEX, text.lower())
        and
        re.search(GITHUB_REGEX, text.lower())
    ):
        score += 1

    return {
        "score": min(score, CONTACT_WEIGHT),
        "suggestions": suggestions
    }


# =====================================================
# SECTION SCORE (10)
# =====================================================

def score_sections(text):

    sections = detect_sections(text)

    score = 0
    suggestions = []

    for section, present in sections.items():

        if present:
            score += 2
        else:
            suggestions.append(
                f"Add {section} section."
            )

    return {
        "score": min(score, SECTION_WEIGHT),
        "analysis": sections,
        "suggestions": suggestions
    }


# =====================================================
# SKILL SCORE (20)
# =====================================================

def score_skills(text):

    skills_text = extract_section(
        text,
        ["skills", "technical skills"]
    )

    skills = extract_skills(skills_text)

    categories_found = 0

    found_skills = []

    missing_categories = []

    for category, values in skills.items():

        if len(values) > 0:

            categories_found += 1

            found_skills.extend(values)

        else:

            missing_categories.append(category)

    # 6 categories available
    # More realistic scoring
    if categories_found >= 5:
        score = 20
    elif categories_found == 4:
        score = 16
    elif categories_found == 3:
        score = 12
    elif categories_found == 2:
        score = 8
    elif categories_found == 1:
        score = 4
    else:
        score = 0

    suggestions = []

    if score < 10:

        suggestions.append(
            "Add more technologies from different domains."
        )

    elif score < 16:

        suggestions.append(
            "Improve technical skill diversity."
        )

    return {

        "score": score,

        "keywords": sorted(list(set(found_skills))),

        "missing": missing_categories,

        "suggestions": suggestions

    }


# =====================================================
# COMMON FEEDBACK MERGER
# =====================================================

def merge_feedback(*lists):

    merged = []

    for item in lists:

        merged.extend(item)

    return list(dict.fromkeys(merged))
# =====================================================
# EXPERIENCE SCORE (20)
# =====================================================

def score_experience(text):

    experience = extract_section(
        text,
        ["experience", "internship", "work experience"]
    )
    
    score = 0
    suggestions = []
    
    if experience.strip():
        score += 5
    else:
        suggestions.append("Add internship or work experience.")
        return {"score": score, "suggestions": suggestions}

    technologies = len(flatten_skills(extract_skills(experience)))

    if technologies >= 3:
        score += 5
    elif technologies >= 2:
        score += 3
    elif technologies >= 1:
        score += 2
    else:
        suggestions.append(
            "Mention technologies used in your experience."
        )

    verbs = action_count(experience)

    if verbs >= 4:
        score += 5
    elif verbs >= 2:
        score += 3
    elif verbs >= 1:
        score += 2
    else:
        suggestions.append(
            "Use action verbs in experience."
        )

    numbers = impact_count(experience)

    if numbers >= 2:
        score += 5
    elif numbers >= 1:
        score += 3
    else:
        suggestions.append(
            "Quantify your achievements."
        )

    return {
        "score": score,
        "suggestions": suggestions
    }


# =====================================================
# PROJECT SCORE (20)
# =====================================================

def score_projects(text):

    projects = extract_section(
        text,
        ["projects", "project"]
    )

    text_lower = projects.lower()

    score = 0
    suggestions = []

    if projects.strip():
        score += 5
    else:
        suggestions.append(
            "Include at least one technical project."
        )

    technologies = len(flatten_skills(extract_skills(projects)))

    if technologies >= 3:
        score += 5
    elif technologies >= 2:
        score += 3
    elif technologies >= 1:
        score += 2
    else:
        suggestions.append(
            "Mention technologies used in projects."
        )

    verbs = action_count(projects)

    if verbs >= 3:
        score += 5
    elif verbs >= 2:
        score += 3
    elif verbs >= 1:
        score += 2

    numbers = impact_count(projects)

    if numbers >= 1:
        score += 5

    return {
        "score": score,
        "suggestions": suggestions
    }


# =====================================================
# ACHIEVEMENT SCORE (10)
# =====================================================

def score_achievements(text):

    text_lower = text.lower()

    score = 0

    if ("certification" in text_lower or
        "certifications" in text_lower):
        score += 5

    if number_count(text) >= 5:
        score += 5
    elif number_count(text) >= 2:
        score += 3

    return {
        "score": score,
        "suggestions": []
    }


# =====================================================
# FORMATTING SCORE (10)
# =====================================================

def score_formatting(text):

    score = 0
    suggestions = []

    bullet_points = len(
        re.findall(r"[•\-\*]", text)
    )

    if bullet_points >= 5:
        score += 4
    elif bullet_points >= 3:
        score += 2
    else:
        suggestions.append(
            "Use bullet points for better readability."
        )

    sections = detect_sections(text)

    if sum(sections.values()) >= 5:
        score += 4
    elif sum(sections.values()) >= 3:
        score += 2

    paragraphs = text.count("\n\n")

    if paragraphs >= 2:
        score += 2

    return {
        "score": score,
        "suggestions": suggestions
    }


# =====================================================
# LENGTH SCORE (5)
# =====================================================

def score_length(text):

    words = word_count(text)

    if 250 <= words <= 700:
        score = 5

    elif 180 <= words < 250:
        score = 4

    elif 701 <= words <= 900:
        score = 3

    elif 100 <= words < 180:
        score = 2

    else:
        score = 1

    return {
        "score": score,
        "suggestions": []
    }
# =====================================================
# MAIN ATS FUNCTION
# =====================================================

def calculate_ats_score(text: str):

    # -------------------------------
    # Run all scoring modules
    # -------------------------------

    contact = score_contact(text)

    sections = score_sections(text)

    skills = score_skills(text)

    experience = score_experience(text)

    projects = score_projects(text)

    achievements = score_achievements(text)

    formatting = score_formatting(text)

    length = score_length(text)

    # -------------------------------
    # Final Score
    # -------------------------------

    score = (
        contact["score"] +
        sections["score"] +
        skills["score"] +
        experience["score"] +
        projects["score"] +
        achievements["score"] +
        formatting["score"] +
        length["score"]
    )

    print("Contact:", contact["score"])
    print("Sections:", sections["score"])
    print("Skills:", skills["score"])
    print("Experience:", experience["score"])
    print("Projects:", projects["score"])
    print("Achievements:", achievements["score"])
    print("Formatting:", formatting["score"])
    print("Length:", length["score"])
    print("Final:", score)
    

    # -------------------------------
    # Rating
    # -------------------------------

    if score >= 90:
        rating = "Excellent"

    elif score >= 80:
        rating = "Very Good"

    elif score >= 70:
        rating = "Good"

    elif score >= 60:
        rating = "Average"

    elif score >= 50:
        rating = "Needs Improvement"

    else:
        rating = "Poor"

    # -------------------------------
    # Strengths
    # -------------------------------

    strengths = []

    if contact["score"] >= 4:
        strengths.append("Professional contact information.")

    if sections["score"] >= 8:
        strengths.append("Well-structured resume.")

    if skills["score"] >= 15:
        strengths.append("Strong technical skill set.")

    if experience["score"] >= 15:
        strengths.append("Strong work/internship experience.")

    if projects["score"] >= 15:
        strengths.append("Well-described technical projects.")

    if achievements["score"] >= 8:
        strengths.append("Good measurable achievements.")

    if formatting["score"] >= 8:
        strengths.append("ATS-friendly formatting.")

    if length["score"] == 5:
        strengths.append("Ideal resume length.")

    # -------------------------------
    # Suggestions
    # -------------------------------

    suggestions = merge_feedback(

        contact["suggestions"],

        sections["suggestions"],

        skills["suggestions"],

        experience["suggestions"],

        projects["suggestions"],

        formatting["suggestions"]

    )

    # -------------------------------
    # Section Analysis
    # -------------------------------

    section_analysis = []

    for section, present in sections["analysis"].items():

        section_analysis.append({

            "name": section,

            "present": present

        })

    # -------------------------------
    # Result
    # -------------------------------

    return {

        "score": score,

        "rating": rating,

        "keywords": skills["keywords"],

        "missing_keywords": skills["missing"],

        "strengths": strengths,

        "suggestions": suggestions,

        "section_analysis": section_analysis,

        "breakdown": {

            "Contact": contact["score"],

            "Sections": sections["score"],

            "Skills": skills["score"],

            "Experience": experience["score"],

            "Projects": projects["score"],

            "Achievements": achievements["score"],

            "Formatting": formatting["score"],

            "Length": length["score"]

        }

    }
