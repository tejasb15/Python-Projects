# QR Code Generator

The QR Code Generator project demonstrates how to create and save QR codes using Python, providing an efficient and user-friendly way to encode and share information such as text, URLs, contact details, and more.

---

## Features

### QR Code Generation:

- Encode data such as text, URLs, Wi-Fi credentials, and contact details into QR codes.
- Save the generated QR codes as PNG images for sharing or printing.

### Customization Options:

- Configure QR code size, border, and error correction levels.

### Lightweight and Easy-to-Use:

- Minimal dependencies for smooth setup and execution.

---

## Architecture

The project structure is straightforward, focusing on user interaction to input data, generate a QR code, and save it as an image file.

---

## Setup Guide

### Prerequisites

- Python 3.6+ installed on your system.
- Basic knowledge of Python programming.

---

### Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/tejasb15/qr-code-generator.git
cd qr-code-generator
```

#### 2. Create a Virtual Environment (Optional)

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the Script

```bash
python qr_code_generator.py
```

#### 5. Input the Data

Provide the data to be encoded (e.g., a URL or text).

#### 6. Save the QR Code

The generated QR code will be saved as a PNG file (e.g., `qrcode.png`) in the project directory.

---

## Testing

### Input Examples:

- Plain text: `"Hello, World!"`
- URL: `"https://github.com/tejasb15"`
- Wi-Fi credentials: `"WIFI:S:NetworkName;T:WPA;P:Password;;"`

### Output:

The QR code images are generated and saved in the project directory, ready to be scanned using a QR code reader.

---

## Outcomes

This project demonstrates:

- The ability to efficiently generate QR codes for various data types.
- The usage of Python libraries (`qrcode`, `Pillow`) to create dynamic QR codes.
- A simple, reusable structure for QR code generation in Python projects.

---

## References

This project leverages the following Python libraries:

- [qrcode](https://pypi.org/project/qrcode/)

For additional learning, explore:

- [QR Code Standards](https://www.qrcode.com/en/about/)

---

## Author

**Tejas Bharambe**  
Full Stack Developer | Python Enthusiast

- [GitHub](https://github.com/tejasb15)
- [LinkedIn](https://linkedin.com/in/tejasbharambe)
