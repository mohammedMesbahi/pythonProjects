import argparse
from PIL import Image

def convert_image_to_pdf(image_path, output_path, max_width=500):
    # Open an image file
    image = Image.open(image_path)
    
    # Calculate the new height to maintain the aspect ratio
    aspect_ratio = image.height / image.width
    new_height = int(max_width * aspect_ratio)
    
    # Resize the image using the updated resampling method
    image = image.resize((max_width, new_height), Image.Resampling.LANCZOS)
    
    # Create a new blank image with white background
    page_size = (max_width + 100, new_height + 100)  # 50 pixels padding on each side
    pdf_page = Image.new("RGB", page_size, "white")
    
    # Paste the resized image onto the blank page
    pdf_page.paste(image, (50, 50))  # Position the image with padding
    
    # Save the final image as PDF
    pdf_page.save(output_path, 'PDF', resolution=100.0)
    print(f"Image has been converted to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an image to PDF with custom width.")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    parser.add_argument("output_path", type=str, nargs='?', default="output.pdf", help="Path to save the output PDF file (default: output.pdf)")
    parser.add_argument("--width", type=int, default=500, help="Max width of the image in the PDF (default: 500 pixels)")

    args = parser.parse_args()

    convert_image_to_pdf(args.image_path, args.output_path, args.width)
