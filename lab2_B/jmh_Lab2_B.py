federal_tax_data = [
    [.37, 578_125],
    [.35, 231_250],
    [.32, 182_100],
    [.24, 95_375],
    [.22, 44_725],
    [.12, 11_000],
    [.10, 0]
]


class FederalTax:
    def __init__(self, federal_tax_rates):
        self.federal_tax_rates = federal_tax_rates

    def find_owed_taxes(self, income):
        owed_taxes = 0
        for rate in self.federal_tax_rates:
            if income > rate[1]:
                income_at_level = income - rate[1]
                income -= income_at_level
                owed_taxes += income_at_level * rate[0]
        return owed_taxes


def main():
    input_income = float(input("Enter your total income this year: "))

    tax = FederalTax(federal_tax_data)
    amount = tax.find_owed_taxes(input_income)

    print(f"You owe ${amount:.2f} this year.")


if __name__ == "__main__":
    main()
