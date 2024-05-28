class Temperature:
    def __init__(self, degree, type):
        self.degree = degree
        self.type = type

    def convert_to_celsius(self):
        match self.type:
            case "Fahrenheit":
                self.degree = (self.degree - 32) * 5/9
            case "Kelvin":
                self.degree = self.degree - 273.15
            case _:
                if self.type != 'Celsius':
                    return 1
        self.type = 'Celsius'

    def convert_from_celsius(self, new_type):
        match new_type:
            case "Fahrenheit":
                self.type = new_type
                self.degree = (self.degree * (9/5)) + 32
            case "Kelvin":
                self.type = new_type
                self.degree = self.degree + 273.15
            case _:
                if self.type != 'Celsius':
                    return 1


def main():
    input_unit_one = input("Enter the unit you are converting from: ")
    input_unit_two = input("Enter the unit you are converting to: ")
    input_temp = float(input(f"Enter the temperature in {input_unit_one}: "))

    temp = Temperature(input_temp, input_unit_one)
    temp.convert_to_celsius()
    temp.convert_from_celsius(input_unit_two)

    print(f"That is {temp.degree:.1f} degrees {temp.type}.")


if __name__ == '__main__':
    main()
