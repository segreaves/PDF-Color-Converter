# PDF-Color-Converter
Program to easily convert a PDF file to a specific color.

## Description
PDF Color Converter is a Python application with a graphical user interface (GUI) that allows you to convert any PDF file to use a single color of your choice. The program maintains the original document's structure while converting all content to the selected color.

## Features
- User-friendly GUI built with Tkinter
- Select any PDF file from your system
- Choose any color using an interactive color picker
- Converts all PDF content (text, shapes, images) to the selected color
- Preserves document layout and structure
- Saves converted PDF with a new filename (original filename + "_colored")

## Requirements
- Python 3.7 or higher
- PyMuPDF (fitz)
- Pillow (PIL)
- Tkinter (usually comes with Python)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/segreaves/PDF-Color-Converter.git
cd PDF-Color-Converter
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

Note: On Linux systems, you may need to install Tkinter separately:
```bash
sudo apt-get install python3-tk
```

## Usage

1. Run the application:
```bash
python3 pdf_color_converter.py
```

2. Click "Select PDF" to choose a PDF file from your system

3. Click "Choose Color" to select the color you want to convert your PDF to

4. Click "Convert PDF" to process the file

5. The converted PDF will be saved in the same directory as the original file with "_colored" appended to the filename

## Example
If you select a file named `document.pdf` and convert it, the output will be saved as `document_colored.pdf` in the same directory.

## Testing
A test script is included to verify the installation:
```bash
python3 test_converter.py
```

This will create a sample PDF file (`test_input.pdf`) that you can use to test the converter.

## How It Works
The converter:
1. Reads the input PDF page by page
2. Converts each page to a high-resolution image
3. Converts the image to grayscale
4. Applies the selected color as a tint based on the grayscale intensity
5. Reconstructs the PDF with the colored pages

## License
See LICENSE file for details.

