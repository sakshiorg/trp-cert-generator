
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color

import os, csv
import cgitb; cgitb.enable()

rakshins = []
file = open("assets/rakshins.csv", "r", encoding = 'utf-8')
data = csv.reader(file)
for rakshin in data:
    rakshins.append(rakshin)

for i in rakshins:
        rname = i[0]
        if not os.path.exists(rname+".pdf"):
            pdfname = (rname+".pdf")
            c = canvas.Canvas(pdfname, pagesize = (862.5, 600))
            c.setTitle(rname+"'s Certificate One")
            c.drawImage("assets/cert-2.png", 0, 0, width = 862.5, height = 600)
            pdfmetrics.registerFont(TTFont('Allura', 'assets/allura.ttf'))

            c.setFillColor(Color(0, 0, 0, alpha = 1))

            c.scale(1, 1)
            c.setFont("Allura", 40)
            c.drawCentredString(470.25, 290, rname)            

            c.showPage()
            c.save()

            print(rname + " certificate generated.")
        else:   
            print(rname + " certificate already exists.")
            
            
            


