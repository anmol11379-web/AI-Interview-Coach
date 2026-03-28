from questions import questions, keywords
from evaluator import evaluate_answer
from report import save_report
from utils import calculate_result, show_graph

def run_interview():
    name = input("Enter your name: ")

    total_score = 0
    report_data = []
    scores_list = []
    question_labels = []

    print("\n--- Interview Started ---\n")

    for i, q in enumerate(questions):
        print("Question:", q)
        answer = input("Your Answer: ")
        print("---------------------------")
        score, feedback, mistakes, suggestions = evaluate_answer(answer, q, keywords)

        total_score += score
        scores_list.append(score)
        question_labels.append("Q" + str(i + 1))

        report_data.append({
            "question": q,
            "answer": answer,
            "score": score,
            "feedback": feedback,
            "mistakes": mistakes,
            "suggestions": suggestions
        })

    average = total_score / len(questions)
    result = calculate_result(average)

    save_report(name, report_data, average, result)

    print("\n✅ Interview Completed!")
    print("📄 Report saved in report.txt")
    print("📊 Graph saved as graph.png")
    print("⭐ Final Score:", round(average, 2))
    print("🏁 Result:", result)

    show_graph(scores_list, question_labels)

run_interview()