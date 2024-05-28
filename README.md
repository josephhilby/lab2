# Overview

This lab requires you to create three programs. Program A will classify triangles. Program B will calculate taxes. Program C will convert between different units of temperature. The goal of this lab is to practice conditional statements.

# Submission Instructions

After completing all programs, please submit three different .py files labeled with your 3 letter initials (three letters from your name), lab number, and program letter. 

For example: axa_Lab2_A.py, axa_Lab2_B.py,  and axa_Lab2_C.py

# Specification

## Program A
Program A will classify triangles based on their side lengths. An equilateral triangle has 3 equal sides, an isosceles triangle has 2 equal sides, and a scalene triangle has no equal sides.

### Input:
```
Side length 1: 
Side length 2: 
Side length 3: 
```
### Output (one of the following):
```
This is an equilateral triangle!
This is an isosceles triangle!
This is a scalene triangle!
```
### You may assume:
- The sides will form a valid triangle
- All inputs will be positive numbers

### Examples:
```
Side length 1: 10
Side length 2: 10
Side length 3: 10
This is an equilateral triangle!
```
```
Side length 1: 20
Side length 2: 20
Side length 3: 20.1
This is an isosceles triangle!
```
```
Side length 1: 1
Side length 2: 2
Side length 3: 3
This is a scalene triangle!
```

## Program B
Program B will be a program to calculate how much you owe in taxes based on your income. You will use the numbers from the 2023 federal tax brackets. You can also find a brief explanation of tax bracket calculations on that site.

| Tax Rate | On taxable income form... | up to...  |
|----------|---------------------------|-----------|
| 10%      | $0                        | $11,000   |
| 12%      | $11,001                   | $44,725   |
| 22%      | $44,726                   | $95,375   |
| 24%      | $95,376                   | $182,100  |
| 32%      | $182,101                  | $231,250  |
| 35%      | $231,251                  | $578,125  |
| 37%      | $578,126                  | and up... |

**All outputs should display exactly two decimal places, and should be rounded.**

### Input:
```Enter your total income this year: ```

### Output:
```You owe ${owed_taxes} this year.```

### You may assume:
- All inputs are positive numbers
- The program user is a single taxpayer
- The only factors that impact taxes are total income and the tax bracket chart.

### Examples:
```
Enter your total income this year: 1000000
You owe $330332.00 this year.
```

```
Enter your total income this year: 500000
You owe $146894.50 this year.
```

```
Enter your total income this year: 10.50
You owe $1.05 this year.
```

## Program C
Program C will be an improved version of the temperature converter created in Lab 1. It will support converting between Fahrenheit, Celsius, and Kelvin.

Use the following conversions:

| Unit | Conversion to Celsius |
| ---- | --------------------- |
| Fahrenheit | (degrees_celsius - 32) * 5/9 |
| Celsius | degrees_celsius |
| Kelvin | degrees_celsius - 273.15 |

**All outputs should be rounded to one decimal place.**

### Input:
```
Enter the unit you are converting from: 
Enter the unit you are converting to: 
Enter the temperature in {unit_from}: 
```

### Output:
```That is {temperature} degrees {unit_to}.```

### You may assume:
- The first two inputs will be either “Fahrenheit”, “Celsius”, or “Kelvin”
  - Pay attention to the capitalization
- The third input will be a valid number

### Examples:
```
Enter the unit you are converting from: Fahrenheit
Enter the unit you are converting to: Kelvin
Enter the temperature in Fahrenheit: -40.5
That is 232.9 degrees Kelvin.
```

```
Enter the unit you are converting from: Celsius
Enter the unit you are converting to: Celsius
Enter the temperature in Celsius: 20
That is 20.0 degrees Celsius.
```

```
Enter the unit you are converting from: Kelvin
Enter the unit you are converting to: Fahrenheit
Enter the temperature in Kelvin: 350
That is 170.3 degrees Fahrenheit.
```
