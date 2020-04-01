import os

import fpdf  # https://pyfpdf.readthedocs.io/en/latest/index.html

from lib.main import PageSpec

if __name__ == '__main__':
    pdf = fpdf.FPDF()
    for img_file in ['refactoringBook.jpg', 'gangs-of-four-design-patterns-book.png']:
        pdf.add_page()
        pdf.image(img_file, x=0, y=0, w=PageSpec.A4.width, h=PageSpec.A4.height)
    os.makedirs('output', exist_ok=True)
    pdf.output('output/out.pdf')
