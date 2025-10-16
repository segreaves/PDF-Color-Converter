# Quick Reference

## Installation
```bash
git clone https://github.com/segreaves/PDF-Color-Converter.git
cd PDF-Color-Converter
pip install -r requirements.txt
```

## Basic Usage
```bash
python3 pdf_color_converter.py
```

## Running Tests
```bash
# Automated tests
python3 test_automated.py

# Create sample PDF
python3 test_converter.py
```

## Common Colors
| Color Name | Hex Code  | RGB Values      |
|------------|-----------|-----------------|
| Black      | #000000   | (0, 0, 0)       |
| White      | #FFFFFF   | (255, 255, 255) |
| Red        | #FF0000   | (255, 0, 0)     |
| Green      | #00FF00   | (0, 255, 0)     |
| Blue       | #0000FF   | (0, 0, 255)     |
| Yellow     | #FFFF00   | (255, 255, 0)   |
| Cyan       | #00FFFF   | (0, 255, 255)   |
| Magenta    | #FF00FF   | (255, 0, 255)   |
| Orange     | #FFA500   | (255, 165, 0)   |
| Purple     | #800080   | (128, 0, 128)   |
| Brown      | #A52A2A   | (165, 42, 42)   |
| Gray       | #808080   | (128, 128, 128) |

## File Locations
- **Input:** Any PDF file on your system
- **Output:** Same directory, filename + "_colored.pdf"
- **Example:** 
  - Input: `/home/user/docs/report.pdf`
  - Output: `/home/user/docs/report_colored.pdf`

## Keyboard Shortcuts (in file dialogs)
- **Tab** - Navigate between fields
- **Enter** - Confirm selection
- **Esc** - Cancel operation
- **Ctrl+A** - Select all (in text fields)

## Tips
1. **Test First** - Try a single page before converting large files
2. **Dark Colors** - Work best for text-heavy documents
3. **Backup** - Keep original files safe
4. **Check Output** - Verify the result before deleting originals

## Troubleshooting Quick Fix
```bash
# If tkinter is missing
sudo apt-get install python3-tk

# If PyMuPDF is missing
pip install --user PyMuPDF

# If Pillow is missing
pip install --user Pillow

# Verify installation
python3 -c "import tkinter, fitz, PIL; print('All OK')"
```

## File Structure
```
PDF-Color-Converter/
├── pdf_color_converter.py  # Main application
├── requirements.txt        # Dependencies
├── test_automated.py       # Automated tests
├── test_converter.py       # Test helper
├── README.md              # Main docs
├── USER_GUIDE.md          # User manual
├── GUI_LAYOUT.md          # GUI docs
├── IMPLEMENTATION.md      # Tech details
└── QUICK_REFERENCE.md     # This file
```

## Support
- Issues: GitHub Issues
- Documentation: See markdown files in repo
- Testing: Run `test_automated.py`

## One-Line Commands
```bash
# Install and run
pip install PyMuPDF Pillow && python3 pdf_color_converter.py

# Test everything
python3 test_automated.py && echo "All tests passed!"

# Check Python version
python3 --version  # Need 3.7+
```
