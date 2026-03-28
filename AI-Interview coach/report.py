def save_report(name, report_data, average, result):
    file = open("report.txt", "a")

    file.write("\n============================\n")
    file.write("AI INTERVIEW REPORT\n")
    file.write("============================\n")
    file.write("Name: " + name + "\n\n")

    file.write("DETAILED ANALYSIS\n\n")

    for data in report_data:
        file.write("Question: " + data["question"] + "\n")
        file.write("Your Answer: " + data["answer"] + "\n")
        file.write("Score: " + str(data["score"]) + "/10\n")

        if data["mistakes"]:
            file.write("Mistakes:\n")
            for m in data["mistakes"]:
                file.write("- " + m + "\n")


        if data["suggestions"]:
            file.write("How to Improve:\n")
            for s in data["suggestions"]:
                file.write("- " + s + "\n")

        file.write("\n-----------------------------\n")


    file.write("\nOVERALL PERFORMANCE\n")
    file.write("Final Score: " + str(round(average, 2)) + "/10\n")
    file.write("Result: " + result + "\n\n")


    file.write("PERSONALIZED FEEDBACK\n")

    if average >= 8:
        file.write(
            "- You have strong interview skills and good clarity of concepts.\n"
            "- Your answers show confidence and structure.\n"
            "- To improve further, focus on adding real-world examples and projects.\n"
            "- Practice speaking fluently and confidently for better delivery.\n"
        )

    elif average >= 5:
        file.write(
            "- Your answers are decent but lack depth and clarity.\n"
            "- Try to explain answers with examples instead of short responses.\n"
            "- Include technical keywords like 'project', 'algorithm', 'system'.\n"
            "- Work on structuring your answers (introduction → explanation → conclusion).\n"
            "- Practice common interview questions regularly.\n"
        )

    else:
        file.write(
            "- Your answers are too short and lack important details.\n"
            "- You need to improve your basic understanding of subjects.\n"
            "- Practice speaking about your skills, projects, and strengths.\n"
            "- Learn how to explain concepts clearly in simple words.\n"
            "- Start with basic questions and gradually improve.\n"
        )

    file.close()