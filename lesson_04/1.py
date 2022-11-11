names = ["Jon", "Mary", "Carl"]


def get_name():
    return "Dima"


def get_name_gen():
    for name in names:
        yield name


name = get_name()
print(name)

gen = get_name_gen()

for d in gen:
    print(d)
