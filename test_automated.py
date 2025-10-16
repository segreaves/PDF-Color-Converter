#!/usr/bin/env python3
"""
Automated test for PDF Color Converter core functionality.
Tests the conversion logic without requiring GUI interaction.
"""

import fitz
from pathlib import Path
from PIL import Image
import io


def hex_to_rgb_normalized(hex_color):
    """Convert hex color to normalized RGB (0-1 range)."""
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    return (r, g, b)


def convert_pdf_headless(input_file, output_file, hex_color):
    """
    Convert a PDF to use a single color without GUI.
    
    Args:
        input_file: Path to input PDF
        output_file: Path to output PDF
        hex_color: Hex color string (e.g., '#FF0000')
    """
    # Open the PDF
    pdf_document = fitz.open(input_file)
    
    # Get the RGB values from hex color
    rgb_color = hex_to_rgb_normalized(hex_color)
    
    # Create a new PDF document for the output
    new_pdf = fitz.open()
    
    # Process each page
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        
        # Create a new page with the same dimensions
        new_page = new_pdf.new_page(
            width=page.rect.width,
            height=page.rect.height
        )
        
        # Convert page to pixmap (image), then to grayscale, then colorize
        mat = fitz.Matrix(2, 2)  # 2x scale for better quality
        pix = page.get_pixmap(matrix=mat, alpha=False)
        
        # Convert to grayscale first
        img_data = pix.tobytes("png")
        
        # Open with PIL
        img = Image.open(io.BytesIO(img_data))
        
        # Convert to grayscale
        gray_img = img.convert("L")
        
        # Convert back to RGB
        rgb_img = gray_img.convert("RGB")
        
        # Apply color tint
        pixels = rgb_img.load()
        width, height = rgb_img.size
        
        # Extract RGB values from normalized color
        r_target = int(rgb_color[0] * 255)
        g_target = int(rgb_color[1] * 255)
        b_target = int(rgb_color[2] * 255)
        
        for y in range(height):
            for x in range(width):
                # Get grayscale intensity
                gray_value = pixels[x, y][0] / 255.0
                
                # Apply the target color scaled by the grayscale intensity
                new_r = int(r_target * gray_value)
                new_g = int(g_target * gray_value)
                new_b = int(b_target * gray_value)
                
                # For lighter areas, blend with white
                if gray_value > 0.9:
                    blend = (gray_value - 0.9) / 0.1
                    new_r = int(new_r * (1 - blend) + 255 * blend)
                    new_g = int(new_g * (1 - blend) + 255 * blend)
                    new_b = int(new_b * (1 - blend) + 255 * blend)
                
                pixels[x, y] = (new_r, new_g, new_b)
        
        # Save the colorized image to a bytes buffer
        img_buffer = io.BytesIO()
        rgb_img.save(img_buffer, format="PNG")
        img_buffer.seek(0)
        
        # Insert the image into the new page
        new_page.insert_image(
            new_page.rect,
            stream=img_buffer.getvalue()
        )
    
    # Save the modified PDF
    new_pdf.save(output_file)
    new_pdf.close()
    pdf_document.close()


def test_conversion():
    """Run automated tests."""
    print("Running automated conversion tests...")
    
    # Create a test PDF if it doesn't exist
    test_input = Path("test_input.pdf")
    if not test_input.exists():
        print("Creating test PDF...")
        doc = fitz.open()
        page = doc.new_page(width=595, height=842)
        page.insert_text((50, 50), "Test PDF", fontsize=20)
        page.insert_text((50, 100), "This is a test document.", fontsize=12)
        page.draw_rect(fitz.Rect(50, 150, 200, 200), color=(1, 0, 0), fill=(1, 0, 0))
        doc.save(str(test_input))
        doc.close()
        print(f"✓ Created {test_input}")
    
    # Test different colors
    test_colors = [
        ("#FF0000", "red"),
        ("#0000FF", "blue"),
        ("#00FF00", "green"),
        ("#000000", "black"),
    ]
    
    for hex_color, color_name in test_colors:
        output_file = f"test_output_{color_name}.pdf"
        print(f"\nConverting to {color_name} ({hex_color})...")
        
        try:
            convert_pdf_headless(str(test_input), output_file, hex_color)
            
            # Verify output exists
            if Path(output_file).exists():
                print(f"✓ Successfully created {output_file}")
            else:
                print(f"✗ Failed to create {output_file}")
                
        except Exception as e:
            print(f"✗ Error converting to {color_name}: {e}")
    
    print("\n" + "="*50)
    print("Test complete!")
    print("="*50)


if __name__ == "__main__":
    test_conversion()
