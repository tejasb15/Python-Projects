# QR Code Generator

This project provides a simple Python-based QR code generator using the `qrcode` library. It allows users to generate QR codes from any text or URL input.

<div style="text-align:center;">
  <img src="./QR Code Generator Thumbnail.jpg" alt="qr code Project Thumbnail" width="500px" height="auto">
</div>

## Features

- Generate QR codes for any text, URL, or data.
- Customizable QR code parameters like size and error correction.
- Easily integrate with other Python projects.

## Requirements

To run this project, you'll need Python 3.x and the following libraries:

- `qrcode`: For generating QR codes.
- `pillow`: For image handling (optional).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tejasb15/Python-Projects.git
   cd Python-Projects
   ```

2. Install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Or, if you're only installing the required libraries individually:

   ```bash
   pip install qrcode
   ```

## Usage

1. Open the project directory:

   ```bash
   cd Python-Projects/QR Code Generator
   ```

2. Run the script to generate a QR code:

   ```bash
   python qr_code.py
   ```

   You will be prompted to enter the data (text, URL, etc.) you want to encode in the QR code.

3. The generated QR code will be saved as an image file in the current directory.

## Example

To generate a QR code for a URL:

```python
import qrcode

# Data to encode
data = "https://www.example.com"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Version of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save("example_qr.png")
```

## References

This project leverages the following Python libraries:

- [qrcode](https://pypi.org/project/qrcode/)

For additional learning, explore:

- [QR Code Standards](https://www.qrcode.com/en/about/)

## Author

**Tejas Bharambe**  
Full Stack Developer | AWS Enthusiast  
[GitHub](https://github.com/tejasb15) | [LinkedIn](https://www.linkedin.com/in/tejasb15/)
