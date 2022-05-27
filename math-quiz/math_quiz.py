#!/usr/bin/env python3
import operator
import random
import sys

OPERATIONS = [
        "+",
        "-",
        "*",
        "/",
    ]
QUESTIONS = 10
RANGE_MAX = range(2, 100)
RANGE_MIN = range(2, 50)


def hard_question():
    op_sym1 = op_sym2 = None

    while op_sym2 == op_sym1:
        op_sym1 = random.choice(OPERATIONS)
        op_sym2 = random.choice(OPERATIONS)

    if op_sym1 in ["*", "/"] and op_sym2 in ["*", "/"]:
        op_sym2 = random.choice(OPERATIONS[:2])

    answer = 0
    while not answer in RANGE_MAX:
        n1, n2, n3 = [random.randint(min(RANGE_MAX), max(RANGE_MAX)) for _ in range(3)]
        par_positions = random.choice(["1", "2", None])
        if par_positions == "1" and not op_sym1 in OPERATIONS[2:]:
            question = f"({n1} {op_sym1} {n2}) {op_sym2} {n3}"
        elif par_positions == "2" and not op_sym2 in OPERATIONS[2:]:
            question = f"{n1} {op_sym1} ({n2} {op_sym2} {n3})"
        else:
            question = f"{n1} {op_sym1} {n2} {op_sym2} {n3}"
        try:
            test = eval(question)
        except ZeroDivisionError:
            continue
        answer = eval(question)
    return question, answer


def simple_question(level):
    """Generate a pair consisting of a random question (as a string)
    and its answer (as a number)"""
    answer = 0
    if level == "1":
        op_sym = random.choice(OPERATIONS[:2])
        numbers_range = RANGE_MAX
    else:
        op_sym = random.choice(OPERATIONS[2:])
        numbers_range = RANGE_MIN
    while not answer in RANGE_MAX:
        n1 = random.randint(min(numbers_range), max(numbers_range))
        n2 = random.randint(min(numbers_range), max(numbers_range))
        if op_sym in ["-", "/"] and n2 > n1:
            # print("debug: swapping n2 and n1 for subtraction")
            n1, n2 = n2, n1
        question = f"{n1} {op_sym} {n2}"
        try:
            answer = eval(question)
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue
    return question, answer


def quiz(level: str, number_of_questions: int):
    """Ask the specified number of questions, and return the number of correct
    answers."""
    score = 0

    while number_of_questions:
        if level in ["1", "2"]:
            question, answer = simple_question(level)
        else:
            question, answer = hard_question()
        print("What is {}".format(question))

        try:
            user_input = float(input("Enter the answer: "))
            if answer == user_input:
                print("Correct!\n")
                score += 10
            else:
                print("Incorrect!\n")
            number_of_questions -= 1
        except ValueError:
            print("I'm sorry that's invalid")
            continue

    return score


def identify_user():
    first_name = input("What is yor name?\n")
    print(f"Hello, {first_name}!")
    return first_name


def menu():
    print("\nChoose operation:")
    menu_choice = input("1 - easy\n2 - medium\n3 - hardcore\n4 - exit\n")
    return menu_choice


def main():
    first_name = identify_user()
    while True:
        menu_choice = menu()

        if menu_choice in ["1", "2", "3"]:  # Run quiz
            score = quiz(menu_choice, QUESTIONS)
            print(f"{first_name}, you scored {score} out of {QUESTIONS * 10}")

        elif menu_choice == "4":  # Exit
            print("Bye!")
            break

        else:
            print("Sorry, I don't understand. Please try again...")
            print()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nBye!")
        sys.exit()
