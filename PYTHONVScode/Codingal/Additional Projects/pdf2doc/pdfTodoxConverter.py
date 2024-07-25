from pdf2docx import Converter

pdfFile="Codingal\Additional Projects\pdf2doc\Form.pdf"
docFile = "Codingal\Additional Projects\pdf2doc\FormDoc.doc"

converterObj = Converter(pdfFile)
converterObj.convert(docFile)
converterObj.close
