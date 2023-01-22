from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)

# Draw image on Canvas and save PDF in buffer
imgPath = "Images/header.png"
can.drawImage(imgPath, 70, 680, 500, 100)    ## at (399,760) with size 160x160
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)

# create a new PDF with Reportlab
new_pdf = PdfReader(packet)
# read your existing PDF
existing_pdf = PdfReader(open("HistóricoEscolar.pdf", "rb"))
output = PdfWriter()
# add the "watermark" (which is the new pdf) on the existing page
for num_page in range(0, len(existing_pdf.pages)):
    page = existing_pdf.pages[num_page]
    if num_page == 0:
        page.merge_page(new_pdf.pages[num_page])
    output.add_page(page)
# page = existing_pdf.pages[0]
# page.merge_page(new_pdf.pages[0])
# output.add_page(page)

# finally, write "output" to a real file
output_stream = open("destination.pdf", "wb")
output.write(output_stream)
output_stream.close()