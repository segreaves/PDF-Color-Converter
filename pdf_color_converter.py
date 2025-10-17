import tkinter as tk
from tkinter import filedialog, colorchooser
import fitz  # PyMuPDF
import os

def get_color_name(color_rgb):
    """Gets a user-friendly name for a given RGB color."""
    # In a real application, you might use a more sophisticated method
    # to get color names, but for this example, we'll just use the hex code.
    return f"#{int(color_rgb[0]*255):02x}{int(color_rgb[1]*255):02x}{int(color_rgb[2]*255):02x}"

def convert_pdf_to_color(input_pdf_path, color_rgb):
    """
    Converts a PDF to a single color by rendering each page as an image and tinting it.

    Args:
        input_pdf_path (str): The path to the input PDF file.
        color_rgb (tuple): A tuple of three floats (r, g, b) between 0 and 1.
    """
    try:
        color_name = get_color_name(color_rgb)
        output_pdf_path = f"{os.path.splitext(input_pdf_path)[0]}_{color_name}.pdf"

        doc = fitz.open(input_pdf_path)
        new_doc = fitz.open()

        for page in doc:
            # Render page to a pixmap without alpha channel
            pix = page.get_pixmap(dpi=150, alpha=False)

            # Create a new pixmap for the colored image
            color_pix = fitz.Pixmap(fitz.csRGB, pix.irect)

            # Convert float color (0-1) to integer (0-255)
            r, g, b = [int(c * 255) for c in color_rgb]

            # Iterate over each pixel and apply the color
            for y in range(pix.height):
                for x in range(pix.width):
                    gray_val = pix.pixel(x, y)[0]
                    # v is the gray value normalized to a float between 0.0 (black) and 1.0 (white)
                    v = gray_val / 255.0

                    # Interpolate between the selected color (for black) and white (for white)
                    new_r = int(v * 255 + (1 - v) * r)
                    new_g = int(v * 255 + (1 - v) * g)
                    new_b = int(v * 255 + (1 - v) * b)

                    color_pix.set_pixel(x, y, (new_r, new_g, new_b))

            # Create a new page and insert the tinted pixmap
            new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)
            new_page.insert_image(page.rect, pixmap=color_pix)

        new_doc.save(output_pdf_path)
        new_doc.close()
        doc.close()

        return output_pdf_path
    except Exception as e:
        return str(e)

class PDFColorConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Color Converter")

        self.file_path = ""
        self.color = ((0, 0, 1), '#0000ff') # Default to blue

        self.create_widgets()

    def create_widgets(self):
        # File selection
        self.file_label = tk.Label(self.root, text="No file selected.")
        self.file_label.pack(pady=10)
        self.file_button = tk.Button(self.root, text="Select PDF", command=self.select_file)
        self.file_button.pack(pady=5)

        # Color selection
        self.color_label = tk.Label(self.root, text=f"Selected Color: {self.color[1]}")
        self.color_label.pack(pady=10)
        self.color_button = tk.Button(self.root, text="Select Color", command=self.select_color)
        self.color_button.pack(pady=5)

        # Convert button
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert)
        self.convert_button.pack(pady=20)

        # Status label
        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack(pady=5)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(
            title="Select a PDF file",
            filetypes=(("PDF files", "*.pdf"), ("all files", "*.*"))
        )
        if self.file_path:
            self.file_label.config(text=os.path.basename(self.file_path))
            self.status_label.config(text="")

    def select_color(self):
        color_code = colorchooser.askcolor(title="Choose color")
        if color_code and color_code[0]:
            # color_code[0] is a tuple of (r, g, b) from 0-255
            # We need to convert it to a tuple of floats from 0-1 for PyMuPDF
            rgb_float = tuple(x/255.0 for x in color_code[0])
            self.color = (rgb_float, color_code[1])
            self.color_label.config(text=f"Selected Color: {self.color[1]}")
            self.status_label.config(text="")


    def convert(self):
        if not self.file_path:
            self.status_label.config(text="Please select a PDF file first.")
            return

        if not self.color:
            self.status_label.config(text="Please select a color first.")
            return

        self.status_label.config(text="Converting...")
        self.root.update_idletasks()

        result = convert_pdf_to_color(self.file_path, self.color[0])

        if result.endswith(".pdf"):
            self.status_label.config(text=f"Conversion successful! Saved as {os.path.basename(result)}")
        else:
            self.status_label.config(text=f"Error: {result}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFColorConverterApp(root)
    root.geometry("400x300")
    root.mainloop()