# PDFReader

PDFReader is a simple Python script that extracts text from PDF files using the [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (`fitz`) library and writes the extracted content to a text file.

## Features

- Reads and extracts text from all pages of a PDF file
- Prints the number of pages and page-wise content to the console
- Saves the extracted text to `output.txt`

## Requirements

- Python 3.x
- [PyMuPDF](https://pypi.org/project/PyMuPDF/) (`fitz`)

## Installation

Install PyMuPDF using pip:

```sh
pip install pymupdf
```

## Usage

Run the script and provide the path to your PDF file when prompted:

```sh
python PDFReader.py
```

You will see:

```
Welcome to PDFReader!
Enter the path to the PDF file:
```

Enter the path, for example:

```
/path/to/your/file.pdf
```

The script will display the number of pages, print the extracted text, and save it to `output.txt` in the current directory.

## Output

- Extracted text is saved to `output.txt`
- Console displays page-wise content and status messages

## License

This project is for educational purposes.