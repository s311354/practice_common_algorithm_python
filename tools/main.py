from textmewhenitsdone import TextMeWhenItsDone


def prompt(prompt) -> str:
    """docstring for prompt"""
    return input(prompt).strip()


def main():
    """docstring for main"""
    email = prompt("From: ")
    receiver = prompt("To: ").split()[0]
    password = prompt("Password: ").split()[0]

    TextMeWhenItsDone().TextMe(email, password, receiver)


if __name__ == '__main__':
    main()
