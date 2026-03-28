from difflib import SequenceMatcher

def is_similar(a, b, threshold=0.7):
    return SequenceMatcher(None, a, b).ratio() > threshold


def evaluate_answer(answer, question, keywords):
    answer = answer.lower()
    score = 0
    feedback = ""
    mistakes = []
    suggestions = []

    words = answer.split()
    word_count = len(words)

    # -------- Length Scoring --------
    if word_count > 20:
        score += 4
    elif word_count > 10:
        score += 2
        feedback += "Answer could be longer. "
        mistakes.append("Answer not detailed enough")
        suggestions.append("Explain your answer with more details and examples")
    else:
        feedback += "Answer too short. "
        mistakes.append("Very short answer")
        suggestions.append("Give at least 2-3 lines explanation")

    # -------- Keyword Matching (Improved NLP) --------
    found = 0

    for key in keywords[question]:
        for w in words:
            if is_similar(w, key):
                found += 1
                break   # avoid double counting

    if found == 0:
        mistakes.append("No relevant keywords used")
        suggestions.append("Use domain-related keywords")

    score += found * 2

    # -------- Technical Words --------
    technical_words = ["project", "algorithm", "data", "system", "code"]

    tech_found = False
    for tech in technical_words:
        for w in words:
            if is_similar(w, tech):
                score += 1
                tech_found = True
                break

    if not tech_found:
        mistakes.append("Lack of technical terms")
        suggestions.append("Use words like project, system, algorithm")

    # -------- Cap Score --------
    if score > 10:
        score = 10

    # -------- Feedback --------
    if score >= 8:
        feedback += "Excellent answer."
    elif score >= 5:
        feedback += "Good answer, improve more."
    else:
        feedback += "Poor answer, add relevant points."

    return score, feedback, mistakes, suggestions