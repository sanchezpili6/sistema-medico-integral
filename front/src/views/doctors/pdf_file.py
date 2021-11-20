from fpdf import FPDF
  
pdf = FPDF()
  
# Add a page
pdf.add_page()

pdf.set_font("Arial", size = 18)
  
pdf.cell(200, 50, txt = "Receta médica", 
         ln = 1, align = 'C')

  
pdf.cell(200, 30, txt = "Paciente: ",
         ln = 2, align = 'L')

pdf.cell(200, 30, txt = "Nombre médico: ",
         ln = 2, align = 'L')


pdf.cell(200, 30, txt = "Medicamento recetado: ",
         ln = 2, align = 'L')


pdf.cell(200, 30, txt = "Cédula profesional escrito: ",
         ln = 2, align = 'L')

pdf.output("receta.pdf")  