# Fireworks Ordering System (using files)

## Introduction
Welcome to the Fireworks Ordering System! This project is designed to help you learn how to use file options in Python by creating a ordering system for "PyroManiacs" a local firework stand. Your Python application will read firework data from an Excel spreadsheet (firework inventory), sort the file so it can be used to create a menu for customers, then take the customers choices, provide a total, and a receipt. 

**Important Note: Skip sections that state *"SKIP - DO NOT MODIFY THIS FUNCTION"***

## Assignment Overview
1. **Load Script & Define Variables**: Load the script `app.py` and define the following three files:
   - `input_menu`: The input Excel file containing fireworks data (`fireworks.xlsx`).
   - `sorted_menu`: The text file where the sorted fireworks menu will be saved (`sorted_menu.txt`).
   - `order_summary`: The text file where the user's order summary will be saved (`order_summary.txt`).

2. **Read Fireworks Data**: Read data from the Excel file (`fireworks.xlsx`).

3. **Sort Fireworks**: Sort the fireworks by price in descending order, save the sorted data to `sorted_menu.txt`.

4. **Display Fireworks Menu**: Display a menu of fireworks sorted by price in the console.

5. **User Interaction**: Print the newly sorted firework selections as a menu for the user to choose which fireworks they want to purchase. Print the remaining budget balance after each user selection.

6. **Output User Order**: Print the final order in the console. Ask if the user would like to complete their order. If "Yes", output a plain-text file named `receipt.txt` containing the user's firework order and grand total. Ensure the receipt saves to the existing project folder.


## Project Setup

### Step 1: From VS Code Open Terminal

### Step 2: Clone Assignment Folder from Github
Copy/Paste this command in your terminal in VS Code then hit **Enter**

```zsh
git clone https://github.com/ronvallejo/Fireworks.git
```

### Step 2: Navigate to your Assignment
Copy/Paste this command in your terminal in VS Code then hit **Enter**

```zsh
cd Fireworks
```

### Step 3: Install the Required Packages
Copy/Paste this command in your terminal in VS Code then hit **Enter**

```zsh
pip install -r requirements.txt
```

