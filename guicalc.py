import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def click(event):
    global after_result  # Use a global variable to track if the last button pressed was "="
    
    text = event.widget.cget("text")
    
    if text == "=":
        # If "=" button is clicked, evaluate the expression in the entry widget
        try:
            result = str(eval(screen.get()))  # Calculate result using eval
            screen.set(result)  # Update the entry widget with the result
            after_result = True  # Set the flag to True since "=" was pressed
        except Exception as e:
            # Display error if the input is invalid
            messagebox.showerror("Error", "Invalid Input")
            screen.set("")  # Clear the entry widget
            after_result = False
    elif text == "C":
        # Clear the entry widget if "C" button is clicked
        screen.set("")
        after_result = False  # Reset the flag
    else:
        # If a number is pressed after displaying a result, clear the entry widget
        if after_result and text.isdigit():
            screen.set("")  # Clear the entry widget
            after_result = False  # Reset the flag
        
        # If an operator is pressed after displaying a result, continue the operation
        if after_result and not text.isdigit():
            after_result = False  # Reset the flag
        
        # Append the button's text to the entry widget
        screen.set(screen.get() + text)

# Set up the main application window
root = tk.Tk()
root.title("Calculator")

# StringVar to store the expression displayed in the entry widget
screen = tk.StringVar()
after_result = False  # Initialize the flag as False

# Entry widget to display the expression and result
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Frame to hold calculator buttons
button_frame = tk.Frame(root)
button_frame.pack()

# List of button labels for the calculator
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

# Loop to create buttons for each label in the buttons list
row = 0  # Starting row for grid layout
col = 0  # Starting column for grid layout
for button in buttons:
    # Create a button with specified text and font
    btn = tk.Button(button_frame, text=button, font="lucida 15 bold")
    btn.grid(row=row, column=col, padx=10, pady=10)  # Place button in grid
    btn.bind("<Button-1>", click)  # Bind left mouse click to click function
    
    # Update column index for the next button
    col += 1
    if col == 4:
        # Move to next row after every 4 columns
        col = 0
        row += 1

# Start the Tkinter event loop
root.mainloop()
