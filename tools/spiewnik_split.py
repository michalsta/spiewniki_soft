#!/usr/bin/env python
import argparse
from pathlib import Path


parser = argparse.ArgumentParser(description="Split songbook into separate pdfs with songs")
parser.add_argument("input", help="Input pdf to split")
parser.add_argument("-o", "--output", help="Output dir", required=True, type=Path)
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


def new_song_page_score(page):
    text = page.extract_text()
    score = 0
    if "BPM" in text:
        score += 10
    if "Skala" in text:
        score += 10
    return score

def is_new_song_page(page):
    return new_song_page_score(page) > 5

def extract_title(page):
    text = page.extract_text()
    return text.splitlines()[1]

print(pages_count(args.input))

with open(args.input, "rb") as f:
    pages = pypdf.PdfReader(f).pages
    song_starts = [is_new_song_page(page) for page in pages] + [True]
    song_starts = [idx for idx, new_song in enumerate(song_starts) if new_song]
    for idx in range(len(song_starts)-1):
        song = pages[song_starts[idx] : song_starts[idx+1]]
        title = extract_title(song[0])
        path_title = title.replace("/", "").strip()
        pdf = pypdf.PdfWriter()
        for page in song: pdf.add_page(page)
        pdf.write(args.output / f"{path_title}.pdf")

