# 💰 Tip Calculator

## Description
The **Tip Calculator** is a handy Python script that solves the common awkward problem of splitting the bill after a meal. It calculates exactly how much each person owes based on the total bill, the desired tip percentage, and the number of people sharing the cost.

This project demonstrates the use of mathematical operations, type conversion, and f-strings in Python.

## Features
* **Custom Tip Percentages:** Allows users to input any tip amount (e.g., 10, 12, or 15).
* **Bill Splitting:** Automatically divides the total (including tip) by the number of people.
* **Precision Rounding:** Rounds the final amount to 2 decimal places for currency friendly output.

## Math Logic
The program uses the following logic to calculate the split:

$$\text{Pay Per Person} = \frac{\text{Bill} + (\text{Bill} \times \frac{\text{Tip}}{100})}{\text{People}}$$

## Prerequisites
* Python 3.x installed on your machine.

```plaintext
Welcome to the tip calculator!
What was the total bill? $150.00
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 5
Each person should pay: $33.6
```