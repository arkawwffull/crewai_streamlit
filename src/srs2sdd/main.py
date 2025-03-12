'''import sys
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfgen import canvas
from crew import Srs2Sdd

class PDF(SimpleDocTemplate):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, pagesize=letter, **kwargs)
        self.page_numbers = []  # To store headings and their page numbers

    def afterFlowable(self, flowable):
        """Registers page numbers for the table of contents."""
        if isinstance(flowable, Paragraph):
            text = flowable.getPlainText()
            style = flowable.style.name
            if style in ["Heading1", "Heading2"]:
                self.page_numbers.append((text, self.page))


def convert_txt_to_pdf(txt_file: str, pdf_file: str):
    """
    Converts a text file (txt_file) into a PDF file (pdf_file) using the ReportLab package.
    
    Args:
        txt_file (str): Path to the input text file.
        pdf_file (str): Path to the output PDF file.
    """
    # Read the content of the text file
    with open(txt_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Initialize PDF document
    doc = PDF(pdf_file)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Title'],
        fontSize=24,
        leading=30,
        alignment=TA_CENTER
    )
    heading1_style = ParagraphStyle(
        'Heading1Style',
        parent=styles['Heading1'],
        fontSize=18,
        leading=22,
        spaceAfter=12,
        bold=True  # Ensure headings are bold
    )
    heading2_style = ParagraphStyle(
        'Heading2Style',
        parent=styles['Heading2'],
        fontSize=14,
        leading=18,
        spaceAfter=10,
        bold=True  # Ensure subheadings are bold
    )
    normal_style = ParagraphStyle(
        'NormalStyle',
        parent=styles['Normal'],
        fontSize=12,
        leading=14,
        spaceAfter=6
    )
    toc_style = ParagraphStyle(
        'TOCStyle',
        parent=styles['Normal'],
        fontSize=12,
        leading=14,
        spaceAfter=6,
        leftIndent=20
    )

    story = []

    # Add a cover page
    title = Paragraph("Software Design Document", title_style)
    subtitle = Paragraph("Healthcare Management System", title_style)
    author = Paragraph(f"Prepared by: [Your Name]", title_style)
    date = Paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d')}", title_style)
    story.append(title)
    story.append(Spacer(1, 12))
    story.append(subtitle)
    story.append(Spacer(1, 12))
    story.append(author)
    story.append(Spacer(1, 6))
    story.append(date)
    story.append(Spacer(1, 24))
    story.append(PageBreak())  # Start a new page after the cover

    # Add Table of Contents
    toc_title = Paragraph("Table of Contents", heading1_style)
    story.append(toc_title)
    story.append(Spacer(1, 12))

    # Placeholder for TOC entries
    toc_entries = []

    # Split the content into lines
    lines = content.split("\n")
    in_code_block = False  # Flag to track if we're inside a code block

    # Iterate through each line and format it
    for line in lines:
        # Remove special characters (# and *)
        line = line.replace("#", "").replace("*", "")

        # Detect headings (lines that were originally marked with #)
        if line.strip().startswith("Software Design Document"):
            story.append(Paragraph(line.strip(), heading1_style))
            toc_entries.append((line.strip(), len(story)))
        elif line.strip().startswith(("1. ", "2. ", "3. ")) or line.strip().startswith("Appendix"):
            story.append(Paragraph(line.strip(), heading2_style))
            toc_entries.append((line.strip(), len(story)))
        elif line.strip().startswith("```"):
            in_code_block = not in_code_block  # Toggle code block flag
            if in_code_block:
                story.append(Spacer(1, 6))
            else:
                story.append(Spacer(1, 6))
        elif in_code_block:
            story.append(Paragraph(f"<font face='Courier'>{line.strip()}</font>", normal_style))
        else:
            story.append(Paragraph(line.strip(), normal_style))
        # Add extra spacing for blank lines
        if not line.strip():
            story.append(Spacer(1, 6))

    # Build the Table of Contents dynamically
    toc_story = []
    for entry, _ in toc_entries:
        page_number = next((page for text, page in doc.page_numbers if text == entry), "?")
        toc_entry = f"{entry} ......................... {page_number}"
        toc_story.append(Paragraph(toc_entry, toc_style))
        toc_story.append(Spacer(1, 6))

    # Insert TOC entries after the TOC title
    toc_index = story.index(toc_title) + 2
    story[toc_index:toc_index] = toc_story

    # Add a page break before the Introduction
    story.insert(toc_index + len(toc_story), PageBreak())

    # Add page numbers to footer
    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 10)
        canvas.drawRightString(doc.pagesize[0] - inch, 0.75 * inch, f"Page {doc.page}")
        canvas.restoreState()

    doc.build(story, onLaterPages=footer)
    print(f"PDF successfully saved as {pdf_file}")


def run():
    try:
        srs_to_sdd = Srs2Sdd()
        result = srs_to_sdd.crew().kickoff()
        print(result)
        # Convert the output text file to PDF
        txt_file = "sdd1.txt"
        pdf_file = "sdd1.pdf"
        convert_txt_to_pdf(txt_file, pdf_file)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


# Execute the run function
if __name__ == "__main__":
    run()'''

import sys
import warnings

from datetime import datetime

from crew import SrsToSdd

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    
    
    try:
        SrsToSdd().crew().kickoff()
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run()





