import pandas as pd
import os
import turtle
import random

# Define file variables


# Function to read and parse the fireworks file
def read_fireworks(file_path):
    fireworks = []
    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        fireworks.append({'name': row['Name'], 'price': row['Price']})
    return fireworks

# Function to sort fireworks by price descending


# ---------------------------
# SKIP - DO NOT MODIFY BELOW
# ---------------------------
# Function to display fireworks menu and write to file
def display_fireworks_menu(fireworks, file_path):
    with open(file_path, 'w') as file:
        file.write("Available Fireworks:\n")
        for idx, firework in enumerate(fireworks, 1):
            file.write(f"{idx}. {firework['name']} - ${firework['price']:.2f}\n")
    print("Available Fireworks:")
    for idx, firework in enumerate(fireworks, 1):
        print(f"{idx}. {firework['name']} - ${firework['price']:.2f}")

# Function to handle user selections and write to file
def handle_selections(fireworks, budget):
    remaining_budget = budget
    selections = []
    while remaining_budget > 0:
        display_fireworks_menu(fireworks, output_menu)
        choice = input(f"Enter the number of the firework to purchase (Remaining budget: ${remaining_budget:.2f}) or 'done' to finish: ").strip()
        if choice.lower() == 'done':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(fireworks):
                selected_firework = fireworks[choice - 1]
                if remaining_budget >= selected_firework['price']:
                    remaining_budget -= selected_firework['price']
                    selections.append(selected_firework)
                    print(f"Purchased {selected_firework['name']} for ${selected_firework['price']:.2f}. Remaining budget: ${remaining_budget:.2f}")
                else:
                    print("Insufficient budget for this firework. Please select a different one.")
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    with open(output_receipt, 'w') as file:
        file.write("Receipt:\n")
        for selection in selections:
            file.write(f"{selection['name']} - ${selection['price']:.2f}\n")
        file.write(f"Total spent: ${budget - remaining_budget:.2f}\n")
        file.write(f"Remaining budget: ${remaining_budget:.2f}\n")
# ---------------------------
# SKIP - DO NOT MODIFY ABOVE
# ---------------------------

# ---------------------------
# SKIP - DO NOT MODIFY BELOW
# ---------------------------

def get_color_selection():
    available_colors = ["red", "blue", "green", "yellow", "white", "purple"]
    selected_colors = []

    print("Please select 3 colors from the following options: red, blue, green, yellow, white, purple")
    while len(selected_colors) < 3:
        color = input(f"Select color {len(selected_colors) + 1}: ").strip().lower()
        if color in available_colors and color not in selected_colors:
            selected_colors.append(color)
        else:
            print("Invalid or duplicate color selection. Please try again.")

    return selected_colors

def draw_fireworks(selected_colors):
    screen = turtle.Screen()
    screen.bgcolor("black")

    for _ in range(10):
        firework = turtle.Turtle()
        firework.color(random.choice(selected_colors))
        firework.speed(0)
        firework.penup()
        firework.goto(random.randint(-200, 200), random.randint(-200, 200))
        firework.pendown()

        for _ in range(36):
            firework.forward(100)
            firework.right(170)
        firework.hideturtle()

    screen.exitonclick()

# ---------------------------
# SKIP - DO NOT MODIFY ABOVE
# ---------------------------

# Main function to execute the program
def main():
    if not os.path.exists(input_fireworks):
        print(f"Error: The file '{input_fireworks}' does not exist.")
        return

    fireworks = read_fireworks(input_fireworks)
    sorted_fireworks = sort_fireworks(fireworks)
    selections, remaining_budget = handle_selections(sorted_fireworks, budget)
    complete_order = input("Would you like to complete your order? (yes/no): ").strip().lower()
    if complete_order == 'yes':
        print("Printing receipt...")
        selected_colors = get_color_selection()
        draw_fireworks(selected_colors)  # Call the draw_fireworks function to show the fireworks animation
    else:
        print("Order not completed.")

if __name__ == "__main__":
    main()