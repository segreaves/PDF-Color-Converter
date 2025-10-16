# PDF Color Converter - User Guide

## Quick Start

1. **Launch the application:**
   ```bash
   python3 pdf_color_converter.py
   ```

2. **Select a PDF file:**
   - Click the "Select PDF" button
   - Navigate to your PDF file and select it
   - The filename will appear in the display area

3. **Choose a color:**
   - Click the "Choose Color" button
   - Use the color picker to select your desired color
   - The selected color will be displayed in the color preview box

4. **Convert the PDF:**
   - Click the "Convert PDF" button
   - Wait for the conversion to complete
   - A success message will show the output filename

## Features in Detail

### File Selection
- Supports standard PDF files
- Displays the selected filename
- Validates file existence before conversion

### Color Selection
- Interactive color picker with RGB sliders
- Hex color code display
- Real-time color preview
- Supports all RGB colors

### Conversion Process
The converter uses a sophisticated algorithm that:
1. Renders each PDF page as a high-resolution image
2. Converts the image to grayscale
3. Applies the selected color as a tint based on pixel intensity
4. Maintains white backgrounds and lighter areas
5. Reconstructs the PDF with colored pages

### Output Files
- Original file: `document.pdf`
- Output file: `document_colored.pdf`
- Saved in the same directory as the input file

## Technical Details

### Supported PDF Content
- ✓ Text (all fonts and sizes)
- ✓ Vector graphics (lines, shapes, curves)
- ✓ Raster images and photos
- ✓ Complex layouts
- ✓ Multi-page documents

### Color Processing
The conversion algorithm:
- Preserves grayscale intensity levels
- Applies color tinting based on darkness
- Maintains readability by preserving contrast
- Blends light areas toward white for backgrounds

### Quality Settings
- Default rendering: 2x resolution multiplier
- Output format: PNG-compressed pages
- Color space: RGB

## Tips for Best Results

1. **Choose Appropriate Colors:**
   - Darker colors work best for text-heavy documents
   - Medium intensity colors work well for mixed content
   - Very light colors may reduce readability

2. **File Size Considerations:**
   - Output files are typically larger than input files
   - This is because pages are rendered as images
   - For very large PDFs, conversion may take several minutes

3. **Testing:**
   - Test with a sample page before converting large documents
   - Use the included test scripts to verify functionality

## Troubleshooting

### Common Issues

**"No module named 'tkinter'"**
- Solution: Install tkinter for your system
  - Linux: `sudo apt-get install python3-tk`
  - macOS: Tkinter comes with Python
  - Windows: Tkinter comes with Python

**"No module named 'fitz'"**
- Solution: Install PyMuPDF
  ```bash
  pip install PyMuPDF
  ```

**"File not found" error**
- Check that the PDF file path is correct
- Ensure you have read permissions for the file
- Verify the file is not corrupted

**"Permission denied" when saving**
- Check write permissions in the output directory
- Ensure the output file isn't open in another program
- Try saving to a different location

**GUI doesn't appear**
- Verify you're in a graphical environment (not SSH without X11)
- Check that DISPLAY environment variable is set (Linux)
- Try running with `sudo` if permission issues persist

### Getting Help

If you encounter issues:
1. Run the automated tests: `python3 test_automated.py`
2. Check error messages carefully
3. Verify all dependencies are installed
4. Make sure you're using Python 3.7 or higher

## Examples

### Example 1: Converting a Text Document
```bash
# Start the application
python3 pdf_color_converter.py

# In the GUI:
# 1. Select: research_paper.pdf
# 2. Choose color: Blue (#0000FF)
# 3. Click Convert
# Output: research_paper_colored.pdf (in blue tones)
```

### Example 2: Using Command Line Tests
```bash
# Create a test PDF
python3 test_converter.py

# Run automated conversion tests
python3 test_automated.py

# This creates colored versions in multiple colors
```

## Performance Notes

Conversion time depends on:
- Number of pages (1-2 seconds per page)
- Page complexity (images take longer)
- Image resolution
- System performance

Typical conversion times:
- 1-page document: 2-5 seconds
- 10-page document: 20-50 seconds
- 100-page document: 3-8 minutes

## Advanced Usage

### Batch Processing
For multiple files, you can use the headless conversion function:

```python
from test_automated import convert_pdf_headless

# Convert multiple files
files = ["doc1.pdf", "doc2.pdf", "doc3.pdf"]
for file in files:
    output = file.replace(".pdf", "_colored.pdf")
    convert_pdf_headless(file, output, "#FF0000")  # Red
```

### Custom Colors
You can use any hex color code:
- `#FF0000` - Red
- `#00FF00` - Green
- `#0000FF` - Blue
- `#800080` - Purple
- `#FFA500` - Orange
- `#964B00` - Brown
- `#FFD700` - Gold

## Credits
Built with:
- Python 3
- Tkinter (GUI)
- PyMuPDF (PDF processing)
- Pillow (Image processing)
