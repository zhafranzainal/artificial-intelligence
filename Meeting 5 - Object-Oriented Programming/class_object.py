# class
class Laptop:

    # constructor
    def __init__(self, brand, release_year, colour, ram):
        # properties
        self.laptop_brand = brand
        self.laptop_release_year = release_year
        self.laptop_colour = colour
        self.laptop_ram = ram

    # methods

    def information(self):
        return f"{self.laptop_colour} {self.laptop_brand} laptop" \
               f" was released in {self.laptop_release_year} with {self.laptop_ram}GB of RAM"

    def coding(self):
        print("\nLaptop used for coding...")
        print("RAM usage        : 2GB")
        self.laptop_ram -= 2
        print("Remaining RAM    : " + str(self.laptop_ram) + "GB")

    def office(self):
        print("\nLaptop used for office...")
        print("RAM usage        : 1GB")
        self.laptop_ram -= 1
        print("Remaining RAM    : " + str(self.laptop_ram) + "GB")

    def editing_video(self):
        print("\nLaptop used for editing video...")
        print("RAM usage        : 3GB")
        self.laptop_ram -= 3
        print("Remaining RAM    : " + str(self.laptop_ram) + "GB")


# inheritance (GamingLaptop inherits Laptop)
class GamingLaptop(Laptop):

    def __init__(self, brand, release_year, colour, ram, vga):
        super().__init__(brand, release_year, colour, ram)
        self.laptop_vga = vga

    def gaming(self):
        print("\nLaptop used for gaming...")
        print("Using", self.laptop_vga)
        print("RAM usage        : 10GB")
        self.laptop_ram -= 10
        print("Remaining RAM    : " + str(self.laptop_ram) + "GB")


# objects
laptop_1 = Laptop("Dell", 2021, "Grey", 8)
laptop_2 = GamingLaptop("Asus", 2022, "Black", 16, "RTX 1650")
laptop_3 = Laptop("MacBook", 2022, "Silver", 8)

print()
print(Laptop)
print(laptop_1)
print(laptop_1.information)

print()
print(laptop_1.laptop_brand)
print(laptop_1.information())

laptop_1.coding()
laptop_1.office()
laptop_1.editing_video()

print("\n=======================================================")
print(laptop_2.information())
laptop_2.office()
laptop_2.gaming()

print("\n==========================================================")
print(laptop_3.information())
laptop_3.coding()
laptop_3.office()
laptop_3.editing_video()
