# AI Interview Coach

## Project Description

The AI Interview Simulator is a Python-based command-line application designed to help students and job seekers practice interview questions and receive automated feedback.

The system simulates a real interview environment and evaluates user responses using a rule-based AI approach enhanced with basic Natural Language Processing (NLP) techniques such as similarity matching. It analyzes answers based on structure, relevance, and technical vocabulary, and provides detailed feedback for improvement.



## Objective

* To provide a platform for interview practice
* To evaluate answers automatically using AI-inspired techniques
* To identify mistakes and suggest improvements
* To improve communication and technical explanation skills



## Requirements

* Python 3.x
* Matplotlib

Install dependency:
pip install matplotlib



## Project Structure

* main.py = Controls interview flow
* questions.py = Stores questions and keywords
* evaluator.py = AI-based answer evaluation logic
* report.py = Generates report.txt
* utils.py = Calculates result and generates graph



## AI / NLP Implementation

This project uses a rule-based AI system combined with basic NLP techniques.

Techniques used:

* Keyword-based evaluation
* Similarity matching using Python’s built-in difflib library
* Heuristic scoring system

Improvement:
Instead of exact keyword matching, the system detects similar words and allows more flexible answer evaluation.

Example:
“classes and objects” can match the keyword “class”.



## How to Run the Project

1. Clone or download the repository
2. Open terminal or command prompt
3. Navigate to the project folder
4. Run:
   python main.py
5. Enter your name
6. Answer each question



## Output

After completing the interview:

report.txt:

* Question-wise analysis
* Scores
* Mistakes
* Suggestions

graph.png:

* Performance graph across questions

Console output:

* Final score
* Result category (Excellent / Average / Needs Improvement)



## Evaluation Criteria

Each answer is scored out of 10 based on:

1. Answer length
2. Keyword relevance (with similarity matching)
3. Technical vocabulary usage



## Limitations

* Not a full machine learning model
* Uses basic NLP (no deep semantic understanding)
* Command-line based (no GUI)
* No voice input



## Future Enhancements

* Advanced NLP using NLTK or spaCy
* Machine learning-based evaluation
* Voice input integration
* Web or GUI interface
* Role-specific interview questions



## Conclusion

The AI Interview Simulator provides a simple and effective way to practice interview questions using AI-inspired evaluation techniques. By combining rule-based logic with NLP similarity matching, the system delivers structured feedback and helps users improve their performance over time.
