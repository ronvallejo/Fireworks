# Fireworks Ordering System (using files)

### Table of Contents
- [Introduction](#introduction)
- [Instructions](#instructions)
- [Setup](#setup)

## Introduction
Welcome to the Fireworks Ordering System! This project is designed to help you learn how to use file options in Python by creating an ordering system for "PyroManiacs," a local firework stand. Your Python application will read firework data from an Excel spreadsheet (firework inventory), sort the file so it can be used to create a menu for customers, then take the customers' choices, provide a total, and a receipt. 

**Important Note: Skip sections that state *"SKIP - DO NOT MODIFY THIS FUNCTION"***

## Instructions
1. **Define File Variabless**: Load the script `app.py` and define the following three files:
   - `input_fireworks`: The input Excel file containing fireworks data (`fireworks.xlsx`).
   - `output_menu`: The text file where the sorted fireworks menu will be saved (`menu.txt`).
   - `output_receipt`: The text file where the user's order summary will be saved (`receipt.txt`).

2. **Read Fireworks Data**: Read data from the Excel file (`fireworks.xlsx`).

3. **Sort Fireworks**: Sort the fireworks by price in descending order, save the sorted data to `sorted_menu.txt`.

4. **Display Fireworks Menu**: Display a menu of fireworks sorted by price in the console.

5. **User Selection**: Print the newly sorted firework selections as a menu for the user to choose which fireworks they want to purchase. Print the remaining budget balance after each user selection.

6. **Create Receipt**: Print the final order in the console. Ask if the user would like to complete their order. If "Yes", output a plain-text file named `receipt.txt` containing the user's firework order and grand total. Ensure the receipt saves to the existing project folder.

## Setup

1. **Open Vew Terminal**  
Open VS Code and then open a new terminal window

2. **Clone Assignment Folder from Github**  
In your terminal, Copy/Paste this command in your terminal in VS Code then hit **Enter**. This command will automatically grab the project files necessary for this assignment.

    ```zsh
    git clone https://github.com/ronvallejo/Fireworks.git
    ```

3. **Create Folder on you Computer**  
Create a **new folder** on your computer named *"Fireworks Ordering System"* to save the assignment files. 

4. **Open Folder in VS Code**  
In VS Code click **File** then **Open Filder** and then select your newly created folder named **"Fireworks Ordering System"**

5. **Map Fireworks Ordering System folder in Terminal**  
Copy/Paste this command in your terminal in VS Code then hit **Enter**

    ```zsh
    cd Fireworks Ordering System
    ```

6. **Install the Required Assignment Packages**  
Copy/Paste this command in your terminal in VS Code then hit **Enter**

    ```zsh
    pip install -r requirements.txt
    ```