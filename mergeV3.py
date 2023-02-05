import os
import warnings import pandas as pd
import csv import PyPDF4
import datetime
from PyPDF4 import PdfFileMerger, PdfFileWriter, PdfFileReader

#import txt2pdf

def createWM():
    with open("wm.txt", mode='a') as file:
        file.write('Printed string %s recorded at %s.\n' %
                (scr, datetime.datetime.now()))

def put watermark (input_pdf, output pdf, watermark):
    PyPDF4.PdfFileReader(input_pdf)

    #reads the watermark pdf file through watermark_instance PdfFileReader (watermark)

    #PdfFileReader
    watermark_instance = PdfFileReader(watermark)
    # fetches the respective page of #watermark (1st page)
    watermark_page = watermark_instance.getPage(0)

    #reads the input pdf file
    pdf_reader = PdfFileReader(input_pdf)
    #It creates a pdf writer object for the
    # output file
    pdf_writer = PdfFileWriter()

    # iterates through the original pdf to
    #merge watermarks for page in range (pdf_reader.getNumPages()):
    for page in range(pdf_reader.getNumPages()):
        page= pdf_reader.getPage(page)

    # will overlay the watermark page on top
    #of the current
        page.mergePage(watermark_page)
        
    with open(outpit_pdf, 'wb') as out:
        # writes to respective ouput_pdf provided
        pdf_writer.write(out)


def merge (folder, filename):

    #on.chdir(r"C:\Users\A. Phadke\OneDrive - Shell\SAP Data Comparison IM for Assets Deepwater\Test")

    x= [a for a in os.listdir() if (a.endswith ((".pdf", ".PDF")) and (a.startswith ("5") and not "UNOFFICIAL COPY" in a))]

    merger = PdfFileMerger(strict=False)

    for pdf in x:
        merger.append(open (pdf, 'rb'))

    with open(r"result.pdf", "wb") as fout:
        merger.write (fout)
        merger.close()

    put_watermark (
            input_pdf- r"result.pdf", the original pdf
            output pdf- filename, the modified pdf with watermark watermark "C:\Users\A. Phadke\Shell\Automation\Apps\Scripts\Consolidated\wm.pdf"
            watermark= "C:\Users\A. Phadke\Shell\Automation\Apps\Scripts\Consolidated\wm.pdf" the watermark to be provided   
        )


#Ursa

data ={'fpath': ["C:\Users\A. Phadke\OneDrive Shell\SAP Data Comparison - IM for Assets Deepwater\Test\ACCESS_EGRESS",
                 r"C:\Users\A. Phadke\OneDrive Shell\SAP Data Comparison IM for Assets Deepwater\Test\AREA CLASSIFICA",
                 r"C:\Users\A. Phadke OneDrive - Shell\SAP Data Comparison - IM for Assets Deepwater\Test\FLOW DIAGRAM\ 660-SAFETY"],
                 'fname': ['532A-95-55-FULL SET - UNOFFICIAL COPY.pdf', '532A-95-450-FULL SET UNOFFICIAL COPY.pdf', '532A-95-660-FULL SET - UNOFFICIAL COPY.pdf'])

df = pd.DataFrame (data)

# ACCESS EGRESS

for ind in df.index:
    folder = df['fpath'][ind]
    fname = df['fname'][ind]
    os.chdir(folder)
    print (folder, fname)
    merge(folder, fname)







