import PyPDF2

def file_reader(filePath):
    with open(filePath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Get the text from each page
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text