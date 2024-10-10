import os
import PyPDF2
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


pessoas = []
DIRETORIO = 'certificados/'

def remover_antigos():
   for i in os.listdir(DIRETORIO):
      if (i not in ['.gitignore']):
        os.remove(DIRETORIO+"{}".format(i))


def buscar_dados():
   with open('pessoas.txt') as f:
      for line in f:
          pessoas.append(line.strip())


def gerar_certificado():

   for index, nome in enumerate(pessoas):
      print(f'{index} -  {nome}')
      
      packet = io.BytesIO()
      can = canvas.Canvas(packet, pagesize=letter)
      can.setFont('Helvetica', 17)
      #X, Y e TEXTO
      can.drawString(260, 313, nome)
      can.save()

      #CURSO PARA O INICIO
      packet.seek(0)

      # CRIA NOVO PDF
      new_pdf = PyPDF2.PdfReader(packet)
      # LER O PDF
      existing_pdf = PyPDF2.PdfReader(open("modelo.pdf", "rb"))
      output = PyPDF2.PdfWriter()
      # ADICIONA O TEXTO
      page = existing_pdf.pages[0]
      page.merge_page(new_pdf.pages[0])
      output.add_page(page)
      # SALVA
      output_stream = open(DIRETORIO+'{}.pdf'.format(nome.strip()), "wb")
      output.write(output_stream)
      output_stream.close()

def main():
   remover_antigos()
   buscar_dados()
   gerar_certificado()


if __name__ == '__main__':
   main()