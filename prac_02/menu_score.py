"""Menu score program."""
MENU = "(G)et a valid score\n" \
       "(P)rint result\n" \
       "(S)how stars\n" \
       "(Q)uit"
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    """Display menu."""
    score = ""
    print(MENU)
    choice = input("Choice > ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score(score)
            print(result)
        elif choice == "S":
            star = print_star(score)
            print(star)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Choice > ").upper()
    print("Farewell")


def get_valid_score():
    """Get user's valid score."""
    score = int(input("Score: "))
    while score <= 0 or score >= 100:
        print("Score must be 0-100")
        score = float(input("Score: "))
    return score


def determine_score(score):
    """Determine score based on thresholds."""
    if 0 <= score <= 100:
        if score >= EXCELLENT_THRESHOLD:
            return "Excellent"
        elif score >= PASSABLE_THRESHOLD:
            return "Passable"
        else:
            return "Bad"


def print_star(score):
    """Print stars as many as the score."""
    for star in range(0, int(score)):
        return "*" * score


main()
