class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def num_equal_sides(self):
        i = 0
        if self.a == self.b:
            i += 1
        if self.b == self.c:
            i += 1
        return i

    def find_type(self):
        n = self.num_equal_sides()
        match n:
            case 0:
                print("This is a scalene triangle!")
            case 1:
                print("This is an isosceles triangle!")
            case 2:
                print("This is an equilateral triangle!")


def main():
    input_a = float(input("Side length 1: "))
    input_b = float(input("Side length 2: "))
    input_c = float(input("Side length 3: "))

    triangle = Triangle(input_a, input_b, input_c)
    triangle.find_type()


if __name__ == "__main__":
    main()
