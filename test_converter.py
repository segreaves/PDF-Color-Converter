#!/usr/bin/env python3
"""
Test script for PDF Color Converter
Creates a simple test PDF and converts it to verify functionality.
"""

import fitz
import os
from pathlib import Path


def create_test_pdf():
    """Create a simple test PDF with text and shapes."""
    # Create a new PDF
    doc = fitz.open()
    page = doc.new_page(width=595, height=842)  # A4 size
    
    # Add some text
    page.insert_text((50, 50), "PDF Color Converter Test", fontsize=20)
    page.insert_text((50, 100), "This is a test PDF with various elements:", fontsize=12)
    page.insert_text((50, 130), "- Text in different sizes", fontsize=10)
    page.insert_text((50, 150), "- Shapes and lines", fontsize=10)
    page.insert_text((50, 170), "- Multiple colors (will be converted to single color)", fontsize=10)
    
    # Add some shapes
    page.draw_rect(fitz.Rect(50, 200, 200, 250), color=(1, 0, 0), fill=(1, 0, 0))  # Red rectangle
    page.draw_circle(fitz.Point(300, 225), 25, color=(0, 0, 1), fill=(0, 0, 1))  # Blue circle
    page.draw_line(fitz.Point(50, 280), fitz.Point(545, 280), color=(0, 1, 0), width=2)  # Green line
    
    # Add more text
    page.insert_text((50, 320), "After conversion, all colors should match", fontsize=12)
    page.insert_text((50, 340), "the selected color!", fontsize=12)
    
    # Save the test PDF
    test_pdf_path = Path("test_input.pdf")
    doc.save(str(test_pdf_path))
    doc.close()
    
    print(f"Test PDF created: {test_pdf_path}")
    return test_pdf_path


def test_conversion():
    """Test the conversion function."""
    from pdf_color_converter import PDFColorConverterApp
    
    # Create test PDF
    test_pdf = create_test_pdf()
    
    # Test hex to RGB conversion
    class MockApp:
        def hex_to_rgb_normalized(self, hex_color):
            """Convert hex color to normalized RGB (0-1 range)."""
            hex_color = hex_color.lstrip('#')
            r = int(hex_color[0:2], 16) / 255.0
            g = int(hex_color[2:4], 16) / 255.0
            b = int(hex_color[4:6], 16) / 255.0
            return (r, g, b)
    
    app = MockApp()
    
    # Test color conversion
    test_colors = ["#FF0000", "#00FF00", "#0000FF", "#000000", "#FFFFFF"]
    print("\nTesting color conversion:")
    for color in test_colors:
        rgb = app.hex_to_rgb_normalized(color)
        print(f"  {color} -> RGB({rgb[0]:.2f}, {rgb[1]:.2f}, {rgb[2]:.2f})")
    
    print("\nTest PDF creation successful!")
    print(f"To test the full conversion, run the main program:")
    print(f"  python3 pdf_color_converter.py")
    print(f"Then select 'test_input.pdf' and choose a color.")
    
    return True


if __name__ == "__main__":
    test_conversion()
