"""
Display the menu
    Coffee - $2.25
    Muffin - $2.75
    Bagel - $2.50
Collect input
    How many coffees? - int
    How many muffins? - int
    How many bagels? - int
    Enter tip percent (e.g., 10 for 10%) - float
    Create Try and except.
Calculate
    Line total: unit_price * quantity - per item
    subtotal : sum of all line totals
    tax : subtotal * 0.08875
    tip : subtotal * (tip_percent / 100)
    total : subtotal + tax + tip
Receipt
    Print each line: Q x Item @ $price = $linetotal
    Print subtotal, tax, tip , and total
    Format money with two decimal places (e.g., $2.25)
"""

import sys

coffee_p = 2.25
muffin_p = 2.75
bagel_p = 2.50

def line_total(unit_price,quantity):
    return float(unit_price) * float(quantity)

def format_currency(money):
    return f"${money:.2f}"
"""
This was my format_currency function before I saw the Discussions in Canvas.
def format_currency(money):
    return "$" + str(round(money,2))
"""

def compute_totals(subtotal, tax_rate, tip_percent):
    tax = subtotal * tax_rate
    tip = subtotal * (tip_percent / 100)
    total = subtotal + tax + tip
    return (tax, tip, total)

def campus_cafe():
    print("Cafe Menu:")
    print()
    print("Coffee - $2.25")
    print("Muffin - $2.75")
    print("Bagel - $2.50")
    print()

def user_input():
    print("Please input the amount of each item you would like to purchase:")

    try:
        coffee_q = int(input("Coffee: "))
        muffin_q = int(input("Muffin: "))
        bagel_q = int(input("Bagel: "))
        tip_percent = float(input("Enter tip percent (e.g., 10 for 10%): "))

        if (coffee_q < 0) or (muffin_q < 0) or (bagel_q < 0) or (tip_percent < 0):
            raise ValueError

    except(ValueError):
        print("Please give whole numbers >= 0. Invalid input, program terminating.")
        sys.exit(1)

    return (coffee_q, muffin_q, bagel_q, tip_percent)

def print_receipt():
    print()
    print("---Receipt---")
    print()
    print(f"{coffee_q} x Coffee @ {format_currency(coffee_p)} = {format_currency(line_total(coffee_p, coffee_q))}")  # make it respond in float so that it automatically displays two decimal point even if only one exists, meaning it should fill in a 0
    print(f"{muffin_q} x Coffee @ {format_currency(muffin_p)} = {format_currency(line_total(muffin_p, muffin_q))}")
    print(f"{bagel_q} x Coffee @ {format_currency(bagel_p)} = {format_currency(line_total(bagel_p, bagel_q))}")
    print(f"Subtotal: {format_currency(subtotal)}")
    print(f"Tax (8.875%): {format_currency(tax)}")
    print(f"Tip ({tip_percent}%): {format_currency(tip)}")
    print(f"Total: {format_currency(total)}")
    print()
    print("Thank you!")

if __name__ == "__main__":
    campus_cafe()
    coffee_q, muffin_q, bagel_q, tip_percent = user_input()
    subtotal = (line_total(coffee_p, coffee_q)) + (line_total(muffin_p, muffin_q)) + (line_total(bagel_p, bagel_q))
    tax, tip, total = compute_totals(subtotal,.08875,tip_percent)
    print_receipt()