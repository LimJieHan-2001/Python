from PyPDF2 import PdfFileWriter, PdfFileReader
def secure_pdf(file, password):
    parser = PdfFileWriter()
    pdf = PDFFileReader(file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)

