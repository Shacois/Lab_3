class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

class PaperBook(Book):
    pages: int

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Страницы{self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError
        if new_pages <= 0:
            raise ValueError
        self._pages = new_pages

class AudioBook(Book):
    duration: float

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность{self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: int) -> None:
        if not isinstance(new_duration, float):
            raise TypeError
        if new_duration <= 0:
            raise ValueError
        self._duration = new_duration
