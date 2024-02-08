# class
class Laptop:
    # constructor
    def __init__(self, brand, release_year, colour, ram):
        # properties
        self.laptop_brand = brand
        self.laptop_release_year = release_year
        self.laptop_colour = colour
        self.laptop_ram = ram

    def information(self):
        return f"{self.laptop_colour} {self.laptop_brand} laptop" \
               f" was released in {self.laptop_release_year} with {self.laptop_ram}GB of RAM"


# objects
laptop_1 = Laptop("Dell", 2021, "Grey", 8)
laptop_2 = Laptop("Asus", 2022, "Black", 16)
laptop_3 = Laptop("MacBook", 2022, "Silver", 8)

print()
print(Laptop)
print(laptop_1)
print(laptop_1.information)

print()
print(laptop_1.laptop_brand)
print(laptop_1.information())
