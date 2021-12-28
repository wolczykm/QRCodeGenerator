# Modules imported

import tkinter
from tkinter import *
from tkinter.constants import PIESLICE
from PIL import Image, ImageDraw,ImageFont
import qrcode
from tkinter import filedialog




# Window settings

root = tkinter.Tk()
root.title('Generator kodów QR v0.4')
root.geometry('400x400')


# QR setup

qr = qrcode.QRCode
(
version=1,
error_correction=qrcode.constants.ERROR_CORRECT_H,
box_size=10,
border=2,
)


#Labels
lab = tkinter.Label(root, text = 'Generator kodów QR')
lab.pack()
lab1 = tkinter.Label(root, text = 'Podaj rozmiar czcionki:')
lab1.place(x=20,y=60)


#Fields
entry_1 = tkinter.Entry(root, bd = 1, width = 10)
entry_1.place(x=310,y=60)


#Read from file
lista = []
with open("test.txt", 'r') as plik:
    for line in plik:
        lista.append(line[:-1])
        continue


#Functions
def generuj_naklejki_tekst():
    for i in lista:
        n = 0
        n += 1
        qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=11,
        border=2,
        )
        qr.add_data(i)
        qr.make(fit=True)

        image = Image.new( "RGBA", ( 400, 640 ) ,"white")
        img = qr.make_image()
        image.paste(img, (1,2), img.convert("RGBA"))
        print (img.size)

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(r'c:\windows\fonts\verdana.ttf', int(entry_1.get()))
        # font = ImageFont.load_default()
        txt = i
        draw.multiline_text((80, 480), txt,(0,0,0),font = font, align='center')

        image.save(str(i) + ".png")
    root.destroy()

def generuj_naklejki_liczba():
    n = 0
    for i in lista:
        n += 1
        qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=11,
        border=2,
        )
        qr.add_data(i)
        qr.make(fit=True)

        image = Image.new( "RGBA", ( 400, 640 ) ,"white")
        img = qr.make_image()
        image.paste(img, (1,2), img.convert("RGBA"))
        print (img.size)

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(r'c:\windows\fonts\verdana.ttf', int(entry_1.get()))
        # font = ImageFont.load_default()
        txt = i
        draw.multiline_text((80, 480), txt,(0,0,0),font = font, align='center')

        image.save(str(n) + ".png")
    root.destroy()


#Buttons
b_text = tkinter.Button(root, text = 'WYGENERUJ PLIKI Z NAZWĄ', width = 50, height = 5, command = generuj_naklejki_tekst)
b_text.place(x = 20, y = 210)
b_num = tkinter.Button(root, text = 'WYGENERUJ PLIKI Z LICZNIKIEM', width = 50, height = 5, command = generuj_naklejki_liczba)
b_num.place(x = 20, y = 305)





root.mainloop()
