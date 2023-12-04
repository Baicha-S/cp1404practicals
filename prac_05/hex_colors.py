"""
CP1404/CP5632 Practical
hex_colors.py program
"""

COLOR_CODE = {"Aqua": "#00ffff", "Beige": "#f5f5dc", "Black": "#000000", "Bright Lilac": "#d891ef",
              "Carrot Orange": "#ed9121", "Bright Lavender": "#bf94e4", "Buff": "#f0dc82", "Canary": "#ffff99",
              "Camel": "#c19a6b", "Celeste": "#b2ffff"}

color = input("Enter color: ").title()
while color != "":
    try:
        print(COLOR_CODE[color])
    except KeyError:
        print("Invalid short state")
    color = input("Enter color: ").title()
