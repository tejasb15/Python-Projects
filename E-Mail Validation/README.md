# E-mail Validation

This project provides a Python-based tool to validate email addresses. It uses two methods: Conditional Logic for simple pattern matching and Regular Expressions (Regex) for more precise validation.

<div style="text-align:center;">
  <img src="./E-mail Validation Thumbnail Image.jpg" alt="email validation Project Thumbnail" width="500px" height="auto">
</div>

## Features

- Validate email addresses using both conditional logic and regular expressions.
- Simple, yet effective tool for real-world applications like user registration and form submissions.
- Provides feedback on the validity of the email format.

## Requirements

To run this project, you'll need Python 3.x and the following libraries:

- `re`: Python’s standard library for regular expression

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tejasb15/Python-Projects.git
   cd Python-Projects
   ```

2. No additional dependencies are required, as Python’s `re` module is part of the standard library.

## Usage

1. Open the project directory:

   ```bash
   cd Python-Projects/E-Mail Validation
   ```

2. Run the script to validate an email address:

   ```bash
   python email_check.py
   python email_regex_check.py
   ```

   You will be prompted to enter an email address to validate.

3. The script will output whether the provided email address is valid or invalid based on the defined rules.

## Example

To validate an email by regex:

```python
import re

def validate_email(email):
    # Regular expression for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return "Valid email address."
    else:
        return "Invalid email address."

# Example email validation
email = input("Enter an email to validate: ")
print(validate_email(email))
```

## References

This project uses the following Python module:

- [re (Regular Expression)](https://docs.python.org/3/library/re.html)

For further exploration:

- [Email Format Standards](https://en.wikipedia.org/wiki/Email_address)

## Author

**Tejas Bharambe**  
Full Stack Developer | AWS Enthusiast  
[GitHub](https://github.com/tejasb15) | [LinkedIn](https://www.linkedin.com/in/tejasb15/)
