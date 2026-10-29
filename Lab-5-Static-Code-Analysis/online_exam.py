
"""Demonstrate a simple online exam grading system."""

import secrets

QUESTIONS = [
    {"q": "What is 2 + 2?", "answer": "4"},
    {"q": "What keyword defines a function in Python?", "answer": "def"},
    {"q": "Name the core component of a computer.", "answer": "cpu"},
]

STUDENTS = {
    "Anil": {0: "4", 1: "def", 2: "ram"},
    "Divya": {0: "4", 1: "def", 2: "cpu"},
    "Sameer": {0: "3", 1: "function", 2: "cpu"},
}

RESULTS = {}


def normalize_answer(text):
    """Normalize an answer for case-insensitive comparison."""
    return text.strip().lower()


def pick_bonus_question():
    """Select a random bonus question."""
    return secrets.choice(QUESTIONS)["q"]


def grade_student(student_name, responses, penalties=None):
    """Calculate and store a student's exam score."""
    if penalties is None:
        penalties = {}

    score = 0
    for index, question in enumerate(QUESTIONS):
        response = responses.get(index, "")
        expected = question["answer"]

        if normalize_answer(response) == normalize_answer(expected):
            score += 2

        score -= penalties.get(index, 0)

    RESULTS[student_name] = max(score, 0)
    return RESULTS[student_name]


def get_grade(score):
    """Return a letter grade for a numerical score."""
    if score >= 4:
        return "A"
    if score >= 2:
        return "C"
    return "F"


def class_average():
    """Calculate the average score for all graded students."""
    if not RESULTS:
        return 0.0
    return sum(RESULTS.values()) / len(RESULTS)


def topper():
    """Return the name of the highest-scoring student."""
    if not RESULTS:
        return "No students"
    return max(RESULTS, key=RESULTS.get)


def main():
    """Run the sample exam and print the results."""
    print(f"Bonus question: {pick_bonus_question()}")

    for student_name, responses in STUDENTS.items():
        score = grade_student(student_name, responses)
        print(f"{student_name} scored {score} grade {get_grade(score)}")

    print(f"Class average: {class_average():.1f}")
    print(f"Topper: {topper()}")
    names = ", ".join(STUDENTS)
    print(f"Students who sat the exam: {names} | total: {len(STUDENTS)}")


if __name__ == "__main__":
    main()
