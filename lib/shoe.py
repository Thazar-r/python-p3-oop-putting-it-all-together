class Shoe:
    def __init__(self, brand, size, price):
        self._brand = brand
        self._size = size
        self._price = price

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not value:
            raise ValueError("Brand cannot be empty.")
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value <= 0:
            raise ValueError("Size must be positive.")
        self._size = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    def __str__(self):
        return f"{self.brand} - Size {self.size}, ${self.price:.2f}"

    def __repr__(self):
        return f"Shoe(brand={self.brand!r}, size={self.size}, price={self.price:.2f})"
