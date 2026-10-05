PROJECTS = [
    {"title":"AI-Based Interview Assessment System","description":"Evaluates interview answers using NLP-oriented scoring and gives structured feedback.","technologies":"Python, NLP, scikit-learn, Streamlit","difficulty":"Intermediate","domain":"Career","skills":["Python","Machine Learning","NLP"],"levels":["Intermediate","Advanced"]},
    {"title":"Resume Analyzer Using NLP","description":"Extracts resume text and compares skills with a target job description.","technologies":"Python, NLP, scikit-learn, PDF, Streamlit","difficulty":"Intermediate","domain":"Career","skills":["Python","NLP","Data Science"],"levels":["Beginner","Intermediate"]},
    {"title":"College Campus AI Assistant","description":"Answers student questions about courses, departments, facilities, and procedures.","technologies":"Python, NLP, RAG, Streamlit","difficulty":"Intermediate","domain":"Education","skills":["Python","NLP","Machine Learning"],"levels":["Intermediate","Advanced"]},
    {"title":"Student Placement Management System","description":"Manages student profiles, eligibility, companies, applications, and placement status.","technologies":"Java/Python, SQL, Streamlit","difficulty":"Beginner","domain":"Education","skills":["Python","Java","SQL"],"levels":["Beginner","Intermediate"]},
    {"title":"Student Performance Predictor","description":"Uses academic data to estimate performance and identify students who may need support.","technologies":"Python, pandas, scikit-learn, Streamlit","difficulty":"Beginner","domain":"Education","skills":["Python","Machine Learning","Data Science"],"levels":["Beginner","Intermediate"]},
    {"title":"Environmental Data Dashboard","description":"Analyzes environmental measurements and presents trends through interactive charts.","technologies":"Python, pandas, NumPy, Streamlit","difficulty":"Beginner","domain":"Environment","skills":["Python","Data Science"],"levels":["Beginner","Intermediate"]},
    {"title":"Personal Expense Analyzer","description":"Categorizes expenses and summarizes spending patterns from CSV data.","technologies":"Python, pandas, SQL, Streamlit","difficulty":"Beginner","domain":"Finance","skills":["Python","SQL","Data Science"],"levels":["Beginner","Intermediate"]},
    {"title":"Customer Churn Predictor","description":"Predicts customers likely to leave a service and shows important contributing features.","technologies":"Python, pandas, scikit-learn, Streamlit","difficulty":"Intermediate","domain":"Business","skills":["Python","Machine Learning","Data Science"],"levels":["Intermediate","Advanced"]},
]

def recommend_projects(skill, level, domain):
    scored=[]
    for p in PROJECTS:
        score=0
        if skill in p["skills"]: score += 3
        if level in p["levels"]: score += 2
        if domain == "Any" or domain == p["domain"]: score += 2
        if skill == "Java" and "Java" in p["technologies"]: score += 2
        scored.append((score,p))
    scored.sort(key=lambda x:(-x[0], x[1]["title"]))
    result=[]
    for score,p in scored[:5]:
        item=dict(p)
        item["reason"] = "Matches your selected skill and level." if score >= 4 else "A useful option for building related project skills."
        result.append(item)
    return result
