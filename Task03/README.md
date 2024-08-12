# Password Generator

A simple password generator application built using the Kivy framework in Python. This app allows users to generate random passwords of specified lengths and copy them to the clipboard.

## Features

- **Generate Password**: Create a random password with a specified length.
- **Copy to Clipboard**: Copy the generated password to the clipboard for easy use.
- **Customizable Length**: Specify the length of the generated password.

## Requirements

- Python 3.x
- Kivy

## Installation

1. **Clone the repository:**
    ```bash
    https://github.com/shahidahameds/Codsoft.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd Task03
    ```

3. **Install the required packages:**
    ```bash
    pip install kivy
    ```

## Usage

1. **Run the application:**
    ```bash
    python passwordgenerator.py
    ```

2. **Use the application:**
   - **Enter Password Length**: Input the desired length of the password in the text field.
   - **Generate Password**: Click the "Generate Password" button to create a password.
   - **Copy Password**: Click the "Copy Password" button to copy the generated password to your clipboard.

## Code Overview

- **PasswordGenerator**: A custom layout class for the main interface of the application.
  - **generate_password()**: Generates a password of the specified length and updates the label.
  - **copy_password()**: Copies the generated password to the clipboard and shows a confirmation popup.
  - **show_popup(message)**: Displays a popup with a given message.
- **PasswordGeneratorApp**: The main application class extending `App` to run the Kivy application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.

---

Happy password generating!

