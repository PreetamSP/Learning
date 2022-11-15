from person import Person

name = "Preetam"
name2 = "Pranav"


def Hello(name: str):
    print(name.upper())


def Hello2(name: str):
    print(name.upper())


# if __name__ == '__main__':
# TODO: Implement Tests
# TODO: Fix bugs
from Math import addnumbers

print("PyCharm is awesome")
print("Hello")

print("%s" % name)
print(addnumbers(2, 2))


def adrin_method(name):
    p = Person(name)
    print(p)


adrin_method("Anooj")
