import os
from PIL import ImageFont, ImageDraw, Image  

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
        image = Image.open("modelo.png")  
        draw = ImageDraw.Draw(image)  
        font = ImageFont.truetype("arial.ttf", 55)  
        draw.text((600, 895), nome.strip(), font=font, fill=(0,0,0,255) ) 
        image.save(DIRETORIO+"{}.png".format(nome.strip()))  

      
def main():
   remover_antigos()
   buscar_dados()
   gerar_certificado()



if __name__ == '__main__':
   main()
