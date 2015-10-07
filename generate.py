# -*- encoding: utf-8 -*-

from conf import *

import StringIO
import csv

from codegen import fetch_code
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, TA_CENTER
from pyPdf import PdfFileWriter, PdfFileReader

# fonts import
pdfmetrics.registerFont(TTFont('RegularFont', FONT_NAME[0]))
pdfmetrics.registerFont(TTFont('SemiboldFont', FONT_NAME[1]))
pdfmetrics.registerFont(TTFont('HeavyFont', FONT_NAME[2]))
pdfmetrics.registerFont(TTFont('LightFont', FONT_NAME[3]))

# data import
data = csv.reader(open(CSV_FILE))

# read the column names from the first line of the file
fields = data.next()

for row in data:
    item = dict(zip(fields, row))

    # importing 'base' file on which we write stuff
    input = PdfFileReader(file(PDF_TEMPLATE, "rb"))

    packet = StringIO.StringIO()
    c = canvas.Canvas(packet, pagesize=PDF_SIZE)
    width, height = PDF_SIZE

    # word number 1
    stylesheet=getSampleStyleSheet()
    styleN = stylesheet['Normal']
    styleN.alignment = TA_CENTER
    styleN.fontSize = 35
    styleN.fontName = 'HeavyFont'
    # changing the size of the font depending on the lenght of the word

    p = Paragraph(u'<font color="blue">' + item['FirstName'].decode('utf-8').upper()+u'</font>', styleN)
    # width/height of the paragraph
    w,h = p.wrap(width, height)
    # x/y axis when the paragraph should be added
    p.drawOn(c, 0, height-HPOSITION)

    # word number 2
    stylesheet=getSampleStyleSheet()
    styleN = stylesheet['Normal']
    styleN.alignment = TA_CENTER
    styleN.fontSize = 23
    styleN.fontName = 'RegularFont'
    # changing the size of the font depending on the lenght of the word

    p = Paragraph(u'<font color="blue">' + item['LastName'].decode('utf-8').upper()+u'</font>', styleN)
    # width/height of the paragraph
    w,h = p.wrap(width, height)
    # x/y axis when the paragraph should be added
    p.drawOn(c, 0, height-HPOSITION-45)


    # word number 3
    stylesheet=getSampleStyleSheet()
    styleN = stylesheet['Normal']
    styleN.alignment = TA_CENTER
    styleN.fontSize = 16
    styleN.fontName = 'LightFont'
    # changing the size of the font depending on the lenght of the word

    p = Paragraph(u'<font color="blue">' + item['Description'].upper().decode('utf-8')+u'</font>', styleN)
    # width/height of the paragraph
    w,h = p.wrap(width, height)
    # x/y axis when the paragraph should be added
    p.drawOn(c, 0, height-HPOSITION-95)


    # saving canvas
    c.save()
    packet.seek(0)
    text = PdfFileReader(packet)
    output = PdfFileWriter()
    # merging text with base
    page = input.getPage(0)
    page.mergePage(text.getPage(0))
    output.addPage(page)

    # saving file
    if str(item['FirstName']) != "" or GENERATE_EMPTY:
        filename = item['FirstName'].replace(" ", "")[0:FILENAME_LENGTH] + fetch_code() + ".pdf"
        outputStream = file("output/" + filename, "wb")
        output.write(outputStream)
        outputStream.close()
