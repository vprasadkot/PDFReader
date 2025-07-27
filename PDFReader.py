import fitz

print("Welcome to PDFReader!")

def read_pdf(file_path):
    try:
        # Open the PDF file
        pdf_document = fitz.open(file_path)
        print(f"Number of pages: {pdf_document.page_count}")
        text = ""
        # Read each page and print its text
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
            print(f"--- Page {page_num + 1} ---")
            print(text)

        pdf_document.close()
        return text
    except Exception as e:
        print(f"An error occurred: {e}")

def write_to_text_file(text, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Content written to {output_file}")
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")

# Usage example
pdf_file_path = input("Enter the path to the PDF file: ")
prd_output_file = "./output.txt"
pdf_content = read_pdf(pdf_file_path)
if pdf_content is not None:
    print("PDF content read successfully.")
    write_to_text_file(pdf_content, prd_output_file)
    print(pdf_content)
else:
    print("Failed to read PDF content.")