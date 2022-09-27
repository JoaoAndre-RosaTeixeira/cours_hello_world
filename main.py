class People:
    name: str = ""

    def __init__(self, name: str):
        self.name = name


class Intro:
    hello: str = "Hello"

    people: People = People("world")

    def print_hello(self, name):
        print(f'{self.hello} {self.people.name}, Bonne journée {name}.')


intro: Intro = Intro()
intro.print_hello('Joao')