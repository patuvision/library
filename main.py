from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter


a = {
    1: "ali",
    2: "amir",
    3: "mmd",
    4: "saeed"
}

b = {
    1: "book1",
    2: "book2",
    3: "book3",
    4: "book4"
}


def dekarte(a, b):
    data = []

    for name in a.values():
        for book in b.values():
            data.append((name, book))

    return data


data = dekarte(a, b)


# فقط اسم‌ها برای autocomplete
names = list(a.values())

completer = WordCompleter(
    names,
    ignore_case=True
)

session = PromptSession(
    completer=completer,
    complete_while_typing=True
)


def search(name):

    found = False

    for user, book in data:

        if user.lower() == name.lower():
            print(f"{user} -> {book}")
            found = True

    if not found:
        raise ValueError("User not found")


while True:

    try:

        name = session.prompt("user -> ")

        if name == "exit":
            break

        search(name)

    except ValueError as error:
        print(error)

    except KeyboardInterrupt:
        print("\nProgram stopped")
        break

