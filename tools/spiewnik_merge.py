#!/usr/bin/env python
import argparse


parser = argparse.ArgumentParser(description="compile songbook")
parser.add_argument("inputs", nargs="+", help="Input pdfs with songs")
args = parser.parse_args()

import pypdf
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def pages_count(filename):
    with open(filename, "rb") as f:
        return len(pypdf.PdfReader(f).pages)


def number_page(number):
    # Create a new canvas for adding page numbers
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    page_text = str(number)
    if number % 2 == 0:
        can.drawString(10, 10, page_text)
    else:
        can.drawString(A4[0] - 20, 10, page_text)
    can.save()
    packet.seek(0)
    new_pdf = pypdf.PdfReader(packet)
    return new_pdf.pages[0]



print(pages_count(args.inputs[0]))

current_page = 1
pdf_writer = pypdf.PdfWriter()
for input_p in args.inputs:
    if current_page % 2 == 1 and pages_count(input_p) > 1:
        pdf_writer.add_page(number_page(current_page))
        current_page += 1
    for page in pypdf.PdfReader(input_p).pages:
        page.merge_page(number_page(current_page))
        pdf_writer.add_page(page)
        current_page += 1

    print(current_page)

pdf_writer.write("out.pdf")
