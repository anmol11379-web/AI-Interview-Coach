import matplotlib.pyplot as plt

def calculate_result(average):
    if average >= 8:
        return "Excellent Performance"
    elif average >= 5:
        return "Average Performance"
    else:
        return "Needs Improvement"


def show_graph(scores, labels):
    plt.figure()
    plt.plot(labels, scores, marker='o')

    plt.title("Interview Performance Graph")
    plt.xlabel("Questions")
    plt.ylabel("Score (out of 10)")
    plt.ylim(0, 10)

    plt.savefig("graph.png")
    plt.show()