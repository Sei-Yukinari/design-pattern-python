class Book:
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
