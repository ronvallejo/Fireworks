import pandas as pd
import turtle
import random

# Step One: Define your files below


# Step Two: Read Fireworks Data**: Read data from the file 

# ---------------------------
# SKIP - DO NOT MODIFY THIS FUNCTION
# ---------------------------

def read_fireworks(file_path):
    fireworks = []
    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        fireworks.append({'name': row['Name'], 'price': row['Price']})
    return fireworks

def sort_fireworks(fireworks):
    return sorted(fireworks, key=lambda fw: fw['price'])

def display_fireworks_menu(fireworks):
    print("Available Fireworks:")
    for idx, firework in enumerate(fireworks, 1):
        print(f"{idx}. {firework['name']} - ${firework['price']:.2f}")

# ---------------------------
# SKIP - DO NOT MODIFY THIS FUNCTION
# ---------------------------        

def handle_selections(fireworks, budget):
    remaining_budget = budget
    while remaining_budget > 0:
        display_fireworks_menu(fireworks)
        choice = input(f"Enter the number of the firework to purchase (Remaining budget: ${remaining_budget:.2f}) or 'done' to finish: ").strip()
        if choice.lower() == 'done':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(fireworks):
                selected_firework = fireworks[choice - 1]
                if remaining_budget >= selected_firework['price']:
                    remaining_budget -= selected_firework['price']
                    print(f"Purchased {selected_firework['name']} for ${selected_firework['price']:.2f}. Remaining budget: ${remaining_budget:.2f}")
                else:
                    print("Insufficient budget for this firework. Please select a different one.")
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def draw_fireworks():
    screen = turtle.Screen()
    screen.bgcolor("black")
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]

    for _ in range(10):
        firework = turtle.Turtle()
        firework.color(random.choice(colors))
        firework.speed(0)
        firework.penup()
        firework.goto(random.randint(-200, 200), random.randint(-200, 200))
        firework.pendown()

        for _ in range(36):
            firework.forward(100)
            firework.right(170)
        firework.hideturtle()

    screen.exitonclick()

def main():
    fireworks = read_fireworks(file_path)
    sorted_fireworks = sort_fireworks(fireworks)
    handle_selections(sorted_fireworks, budget)
    draw_fireworks()

if __name__ == "__main__":
    main()