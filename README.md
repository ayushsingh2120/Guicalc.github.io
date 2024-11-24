# Calculator Application

A simple calculator application built using Python's `tkinter` library. This calculator can perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- **Basic Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **Clear Function**: Allows users to clear the current input or result.
- **Result Handling**: Automatically clears the result when a number button is pressed after displaying a result, enabling easy input of new calculations.
- **Error Handling**: Displays error messages for invalid inputs.

## How It Works

- **Buttons**: The calculator has buttons for numbers (0-9), operations (`+`, `-`, `*`, `/`), a clear button (`C`), and an equals button (`=`).
- **Display**: The input and results are displayed in an entry widget.
- **Events**: Button clicks are handled using event binding. Each button is mapped to an action in the `click` function.

## Code Explanation

- **`click(event)`**: This function processes each button click. It:
  - Evaluates and displays results when `=` is pressed.
  - Clears the display when `C` is pressed.
  - Appends numbers and operators to the current expression.
  - Clears the display if a number is pressed after a result, allowing new calculations without manually clearing the previous result.

- **`after_result` Flag**: A global flag to track whether the last operation displayed a result. This flag helps clear the display when a number button is pressed after a result.

## Installation

1. Clone the repository or download the code.
2. Make sure Python is installed on your system (Python 3.x is recommended).
3. Run the application:

   ```bash
   python calculator.py
## Usage

**Perform Calculations:** Click on numbers and operations to build expressions. Press = to see the result.

**Clear Display:** Press C to clear the current input or result.

**Start New Calculation:** After a result is displayed, simply press a number button to clear the display and start a new calculation.

**Example**

Click `2`, `+`, `3`, and `=`. The display will show `5`.

Press any number to clear the display and begin a new calculation.

## Error Handling

If an invalid input or operation is attempted, an error message will be shown, and the display will reset.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgments

Thanks to the Python community for providing resources and support.
Tkinter documentation for GUI development.

## Contact

For any inquiries, please reach out to **salil.16440@stu.upes.ac.in**.
