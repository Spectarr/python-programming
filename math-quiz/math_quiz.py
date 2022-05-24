import operator
import random

OPERATIONS = [("+", operator.add), 
              ("-", operator.sub)]
QUESTIONS = 10



def random_question(binary_operations, operand_range):
    """Generate a pair consisting of a random question (as a string)
    and its answer (as a number)"""
    op_sym, op_func = random.choice(binary_operations)
    n1 = random.randint(min(operand_range), max(operand_range))
    n2 = random.randint(min(operand_range), max(operand_range))
    if op_sym == "-" and n2 > n1:
        # print("debug: swapping n2 and n1 for subtraction")
        n1, n2 = n2, n1

    question = f"{n1} {op_sym} {n2}"
    answer = op_func(n1, n2)
    return question, answer


def quiz(number_of_questions):
    """Ask the specified number of questions, and return the number of correct
    answers."""
    score = 0

    while number_of_questions:
        question, answer = random_question(OPERATIONS, range(1, 99))
        if answer > 100:
            # print(f"debug: result [{answer}] is more than 100")
            continue
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
    name = input("What is yor name?\n")
    last_name = input("What is your last name?\n")
    grade = "Which grade are you in?"
    return name, last_name, grade


def menu():
    print("choose oepration:")
    menu_choice = input("1 - run quiz\n2 - exit\n")
    return menu_choice


def main():
    first_name, last_name, class_name = identify_user()
    while True:
        menu_choice = menu()

        if menu_choice == "1":  # Run quiz
            score = quiz(QUESTIONS)
            print(f"{first_name} {last_name}, you scored {score} out of {QUESTIONS * 10}")

        elif menu_choice == "2":  # Exit
            break

        else:
            print("Sorry, I don't understand. Please try again...")
            print()


if __name__ == "__main__":
    main()
