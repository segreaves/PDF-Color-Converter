#!/usr/bin/env python3
"""
PDF Color Converter
A program to convert PDF files to use a single color.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import fitz  # PyMuPDF
import os
from pathlib import Path


class PDFColorConverterApp:
    """Main application window for PDF color conversion."""
    
    def __init__(self, root):
        """Initialize the application."""
        self.root = root
        self.root.title("PDF Color Converter")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        
        # Variables
        self.selected_file = None
        self.selected_color = "#000000"  # Default to black
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        """Create and arrange all UI widgets."""
        # Title label
        title_label = tk.Label(
            self.root,
            text="PDF Color Converter",
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=20)
        
        # File selection frame
        file_frame = tk.Frame(self.root)
        file_frame.pack(pady=10, padx=20, fill="x")
        
        self.file_label = tk.Label(
            file_frame,
            text="No file selected",
            width=35,
            anchor="w",
            relief="sunken",
            padx=5,
            pady=5
        )
        self.file_label.pack(side="left", padx=(0, 10))
        
        select_file_btn = tk.Button(
            file_frame,
            text="Select PDF",
            command=self.select_file,
            width=12
        )
        select_file_btn.pack(side="left")
        
        # Color selection frame
        color_frame = tk.Frame(self.root)
        color_frame.pack(pady=10, padx=20, fill="x")
        
        color_label = tk.Label(color_frame, text="Selected Color:")
        color_label.pack(side="left", padx=(0, 10))
        
        self.color_display = tk.Canvas(
            color_frame,
            width=100,
            height=30,
            bg=self.selected_color,
            relief="sunken"
        )
        self.color_display.pack(side="left", padx=(0, 10))
        
        select_color_btn = tk.Button(
            color_frame,
            text="Choose Color",
            command=self.select_color,
            width=12
        )
        select_color_btn.pack(side="left")
        
        # Convert button
        convert_btn = tk.Button(
            self.root,
            text="Convert PDF",
            command=self.convert_pdf,
            width=20,
            height=2,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold")
        )
        convert_btn.pack(pady=30)
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 9),
            fg="gray"
        )
        self.status_label.pack(pady=5)
        
    def select_file(self):
        """Open file dialog to select PDF file."""
        filename = filedialog.askopenfilename(
            title="Select a PDF file",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if filename:
            self.selected_file = filename
            # Display just the filename, not the full path
            display_name = os.path.basename(filename)
            if len(display_name) > 35:
                display_name = display_name[:32] + "..."
            self.file_label.config(text=display_name)
            self.status_label.config(text="File selected successfully")
        
    def select_color(self):
        """Open color chooser dialog."""
        color = colorchooser.askcolor(
            initialcolor=self.selected_color,
            title="Choose a color"
        )
        
        if color[1]:  # color[1] is the hex value
            self.selected_color = color[1]
            self.color_display.config(bg=self.selected_color)
            self.status_label.config(text=f"Color selected: {self.selected_color}")
    
    def hex_to_rgb_normalized(self, hex_color):
        """Convert hex color to normalized RGB (0-1 range)."""
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16) / 255.0
        g = int(hex_color[2:4], 16) / 255.0
        b = int(hex_color[4:6], 16) / 255.0
        return (r, g, b)
    
    def convert_pdf(self):
        """Convert the selected PDF to use the selected color."""
        # Validation
        if not self.selected_file:
            messagebox.showerror("Error", "Please select a PDF file first!")
            return
        
        if not os.path.exists(self.selected_file):
            messagebox.showerror("Error", "Selected file does not exist!")
            return
        
        try:
            self.status_label.config(text="Converting PDF... Please wait...")
            self.root.update()
            
            # Open the PDF
            pdf_document = fitz.open(self.selected_file)
            
            # Get the RGB values from hex color
            rgb_color = self.hex_to_rgb_normalized(self.selected_color)
            
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
                # This approach works for all PDF content types
                mat = fitz.Matrix(2, 2)  # 2x scale for better quality
                pix = page.get_pixmap(matrix=mat, alpha=False)
                
                # Convert to grayscale first
                # Get pixel data
                img_data = pix.tobytes("png")
                from PIL import Image
                import io
                
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
                        # Get grayscale intensity (all channels are the same)
                        gray_value = pixels[x, y][0] / 255.0
                        
                        # Apply the target color scaled by the grayscale intensity
                        new_r = int(r_target * gray_value)
                        new_g = int(g_target * gray_value)
                        new_b = int(b_target * gray_value)
                        
                        # For lighter areas (closer to white), blend with white
                        if gray_value > 0.9:
                            # Interpolate between color and white based on how light it is
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
            
            # Generate output filename
            file_path = Path(self.selected_file)
            output_filename = file_path.parent / f"{file_path.stem}_colored{file_path.suffix}"
            
            # Save the modified PDF
            new_pdf.save(str(output_filename))
            new_pdf.close()
            pdf_document.close()
            
            self.status_label.config(text="Conversion complete!")
            messagebox.showinfo(
                "Success",
                f"PDF converted successfully!\n\nSaved as:\n{output_filename.name}"
            )
            
        except Exception as e:
            self.status_label.config(text="Error during conversion")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")


def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = PDFColorConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
