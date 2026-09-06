a = {
    1: "ali",
    2: "amir",
    3: "mmd",
    4: "saeed",
}

b = {
    1: "book1",
    2: "book2",
    3: "book3",
    4: "book4",
}


def suggestion(query, data):
    suggestions = {
        item for item in data
        if item.startswith(query)
    }

    if suggestions:
        print("\n  Suggestions:")

        for i, item in enumerate(sorted(suggestions), 1):
            print(f"  {i}. {item}")

    else:
        print("\n  No suggestions")


def search(query, data=None):
    if data is None:
        return "insert data"

    found = False

    for item in data:
        if query in item:
            print(item)
            found = True

    if not found:
        print("user not found")


def dekarte(a, b):
    c = []

    for first in a.values():
        for second in b.values():
            c.append((first, second))

    return c


while True:
    i = input("user -> ")

    data = dekarte(a, b)

    if i == "all":
        print(data)

    else:
        suggestion(i, a.values())