import argparse
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    # Write the merged PDF to the specified output file
    merger.write(output_path)
    merger.close()

    print(f"PDFs have been merged into {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge multiple PDFs into a single PDF.")
    parser.add_argument("pdf_files", type=str, nargs='+', help="Paths to the PDF files to merge")
    parser.add_argument("output_path", type=str, help="Path to save the merged PDF file")

    args = parser.parse_args()

    merge_pdfs(args.pdf_files, args.output_path)
