#!/usr/bin/env python3

import operator
import random
import sys
from timeit import default_timer as timer
from functools import wraps

OPERATIONS = [
    "+",
    "-",
    "*",
    "/",
]
QUESTIONS = 10
RANGE = range(2, 100)


def time(func):
    @wraps(func)
    def wrapper(*args):
        """timer function"""
        start = timer()
        result = func(*args)
        end = timer()
        print(f"You made it in {round(end - start,2)} seconds!")
        return result

    return wrapper


def hard_question():
    op_sym1 = random.choice(OPERATIONS)
    op_sym2 = random.choice(OPERATIONS)

    if op_sym1 in OPERATIONS[2:] and op_sym2 in OPERATIONS[2:]:
        op_sym2 = random.choice(OPERATIONS[:2])

    answer = 0
    while not answer in RANGE:
        n1, n2, n3 = [random.randint(min(RANGE), max(RANGE)) for _ in range(3)]
        first_pair = f"({n1} {op_sym1} {n2})"
        last_pair = f"({n2} {op_sym2} {n3})"
        if eval(first_pair) == 1 or eval(last_pair) == 1:
            continue
        # set parentheses to the first, last pair, or none
        par_positions = random.choice(["1", "2", None])
        if par_positions == "1" and not op_sym1 in OPERATIONS[2:]:
            question = f"{first_pair} {op_sym2} {n3}"
        elif par_positions == "2" and not op_sym2 in OPERATIONS[2:]:
            question = f"{n1} {op_sym1} {last_pair}"
        else:
            question = f"{n1} {op_sym1} {n2} {op_sym2} {n3}"
        try:
            eval(question)
        except ZeroDivisionError:
            continue
        answer = eval(question)
    return question, answer


def simple_question(level):
    """Generate a pair consisting of a random question (as a string)
    and its answer (as a number)"""
    answer = 0
    if level == "1":
        numbers_range = RANGE
        op_sym = random.choice(OPERATIONS[:2])
    elif level == "2":
        numbers_range = range(2, 200)
        op_sym = random.choice(OPERATIONS)
    while not answer in RANGE:
        n1 = random.randint(min(numbers_range), max(numbers_range))
        n2 = random.randint(min(numbers_range), max(numbers_range))
        if op_sym in ["-", "/"] and n2 > n1:
            # swapping n2 and n1 for subtraction
            n1, n2 = n2, n1
        question = f"{n1} {op_sym} {n2}"
        try:
            answer = eval(question)
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue
    return question, answer


@time
def quiz(level: str, name: str, number_of_questions: int):
    """Ask the specified number of questions, and return the number of correct
    answers."""
    score = 0
    questions_left = number_of_questions

    while questions_left:
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
                print(f"Incorrect!\nCorrect answer is {int(answer)}")
            num_end = "s"
            questions_left -= 1
            if questions_left == 1:
                num_end = ""
            if questions_left:
                print(f"{questions_left} question{num_end} left\n")
        except ValueError:
            print("I'm sorry that's invalid")
            continue

    print(f"{name.capitalize()}, you scored {score} out of {QUESTIONS * 10}")


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
            quiz(menu_choice, first_name, QUESTIONS)

        elif menu_choice == "4":  # Exit
            print("Bye!")
            break

        else:
            print("Sorry, I don't understand. Please try again...\n")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nBye!")
        sys.exit()
