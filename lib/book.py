class Book:
    def __init__(self, title, author, published_year):
        self._title = title
        self._author = author
        self._published_year = published_year

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty.")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not value:
            raise ValueError("Author cannot be empty.")
        self._author = value

    @property
    def published_year(self):
        return self._published_year

    @published_year.setter
    def published_year(self, value):
        if value < 0:
            raise ValueError("Published year cannot be negative.")
        self._published_year = value

    def __str__(self):
        return f"'{self.title}' by {self.author}, published in {self.published_year}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, published_year={self.published_year})"
