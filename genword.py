import fpdf
from fpdf import FPDF
from wand.image import Image as WImage
import json

#with open("recipes.json", 'r') as json_file:
#    recipes = json.load(json_file)

pdf = FPDF(orientation='P', unit='mm', format='A4')
fpdf.SYSTEM_TTFONTS = '.'
#pdf.add_font('Titans2', '', 'Titans2.ttf', uni=True)


for recipe in recipes:
    pdf.add_page()
    #pdf.image("Parchment.jpg", x=-4, y=-8, w=217, h=313)
    pdf.set_font('New Times Roman', size=28)
    pdf.cell(0, pdf.font_size * 1.8, "Hello PDF World!", ln=1, align="L")
    pdf.ln()

pdf.output("recipe-book.pdf")

