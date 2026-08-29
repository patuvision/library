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

def search(query, data=None):
    if data is None:
        return "insert data"
    for item in data:
        if query in item:
            return item
    return None

def dekarte(a, b):
    c = []

    for first in a.values():
        for second in b.values():
            c.append((first, second))

    return c


data = dekarte(a, b)
print(search("amir", data))
# [('ali', 'book1'), ('ali', 'book2'), ('ali', 'book3'), ('ali', 'book4'), ('amir', 'book1'), ('amir', 'book2'), ('amir', 'book3'), ('amir', 'book4'), ('mmd', 'book1'), ('mmd', 'book2'), ('mmd', 'book3'), ('mmd', 'book4'), ('saeed', 'book1'), ('saeed', 'book2'), ('saeed', 'book3'), ('saeed', 'book4')]
# ('amir', 'book1'), ('amir', 'book2'), ('amir', 'book3'), ('amir', 'book4')
