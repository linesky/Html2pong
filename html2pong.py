from PIL import Image,ImageDraw,ImageFont,ImageColor
import sys
#pip install pillow


def create_colored_bmp(filename, width, height, color_index,input_text):
    try:
        y=30;
        # Verifica se o índice da cor está no intervalo válido (0-15)
        if 0 <= color_index <= 15:
                   
            # Mapeia o índice da cor para um valor RGB VGA de 16 cores
            vga_colors = [
                (0, 0, 0), (0, 0, 170), (0, 170, 0), (0, 170, 170),
                (170, 0, 0), (170, 0, 170), (170, 85, 0), (170, 170, 170),
                (85, 85, 85), (85, 85, 255), (85, 255, 85), (85, 255, 255),
                (255, 85, 85), (255, 85, 255), (255, 255, 85), (255, 255, 255)
            ]

            # Cria uma imagem em branco com as dimensões especificadas
            image = Image.new("RGB", (width, height),vga_colors[color_index] )
            iii=ImageDraw.Draw(image)
            hh=input_text.split("\n")
            for j in range(len(hh)):
                try:
                    iii.text((y, 30),hh[j])
                    y=y+40
            # Salva a imagem como um arquivo BMP de 24 bits
            image.save(filename, "PNG")

            print(f"Arquivo BMP criado com sucesso: {filename}")
        else:
            print("O índice de cor deve estar no intervalo de 0 a 15.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")



a:int=0
styles=True
scripts=True
triggers=False
triggers2=False
filename="my.html"
width=1000
height=1000
y=100;
color_index=4
input_text=""
print("\x1bc\x1b[41;30m")

if 0==0:
    if len(sys.argv) != 3:
        print("Uso: python text_to_pdf.py <arquivo_de_entrada.html> <arquivo_de_saida.pdf>")
    else:
        filename = sys.argv[1]
        output_pdf_file = sys.argv[2]


f1=open(filename,"r")
files=f1.read()
f1.close()
splits=files.split(">")
counter=0
for n in splits:
    n=n.replace("\n","")
    n=n.replace("\r","")
    tags=n.split("<")
    triggers=False
    counter=0
    if len(tags)==2 and len(tags[0])>0:
        triggers=True
        triggers2=True
    xx=True    
    for ta in tags:
        ta=ta.strip()
        if counter>0:
            varsn=ta.split(" ")
            for varn in varsn:
                varn=varn.strip()
                if len(varn)>0:
                    if varn=="style" or varn=="STYLE":
                        styles=False
                    if varn=="script" or varn=="SCRIPT":
                        scripts=False
                    if styles and scripts: 
                        xx=False
                    if varn=="/style" or varn=="/STYLE":
                        styles=True
                    if varn=="/script" or varn=="/SCRIPT":
                        scripts=True
                    if varn=="br" or varn=="BR" or varn=="p" or varn=="P" or varn=="/p" or varn=="/P":
                        input_text=input_text+"\n"
                    if varn=="a" or varn=="A":
                        
                        triggers2=False
                    if triggers2==False and (varn.find("href")>-1 or varn.find("HREF")>-1):
                        hrefs=varn.split("=")
                        if len(hrefs)>1:
                            input_text=input_text+" "+hrefs[1]+" "
                    
        else:
                   
            if len(ta)>0:
               if ta=="style" or ta=="STYLE":
                   styles=False
               if ta=="script" or ta=="SCRIPT":
                   scripts=False
               if styles and scripts:
                   if ta=="br" or ta=="BR" or ta=="p" or ta=="P" or ta=="/p" or ta=="/P":
                       input_text=input_text+" "+"\n"
                   if varn=="a" or varn=="A":
                        
                       triggers2=False



                   if triggers:
                       input_text=input_text+" "
                   
                       input_text=input_text+" "+ta
               if ta=="/style" or ta=="/STYLE":
                   styles=True
               if ta=="/script" or ta=="/SCRIPT":
                   scripts=True

        
        counter+=1

create_colored_bmp(output_pdf_file, width, height, color_index,input_text)        
   
