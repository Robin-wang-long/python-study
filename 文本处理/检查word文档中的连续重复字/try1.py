from docx import Document

doc = Document('test.docx')
contents = ''.join((p.text for p in doc.paragraphs))
words = []
for index,ch in enumerate(contents[:-2]):
    if ch == contents[index+1] or ch == contents[index+2]:
        word = contents[index:index+3]
        if word not in words:
            words.append(word)
            print(word)
