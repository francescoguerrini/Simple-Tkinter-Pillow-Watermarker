from tkinter import *
from tkinter.messagebox import askyesno
from tkinter import filedialog, Tk
from PIL import Image, ImageDraw, ImageFont
import os

pathX = ""


############DEF FUNC##############


#choose image

def find_image():
    global pathX
    pathX=filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])


#add watermark, show preview, save(opt)

def add_watermark():
    global pathX

    image = Image.open(pathX)
    watermark= text_entry.get()
    image_width, image_height = image.size
    draw = ImageDraw.Draw(image)

    font_size = int(image_width / 10)
    font = ImageFont.truetype("arial.ttf", font_size)
    x, y = int(image_width / 2), int(image_height / 2)
    color = color_entry.get()
    draw.text((x, y), watermark, font=font, fill=color, stroke_fill="#323", anchor="ms")

    image.show()

    fn, fext = os.path.splitext(pathX)

    answer = askyesno(title="Save changes", message="Save image with watermark?")

    if answer == True:
        image.save(fn+"_marked"+fext)
    else:
        pass

############MAIN##############


window= Tk()
window.title("Watermarker")
window.config(width=700, height=500, padx=25, pady=25)

welcome_label = Label(text="Welcome to my watermak_app.\n Choose a text to display, then an image to mark and watch the preview. \n If you like the result, close an press 'yes' to save it")
welcome_label.grid(column=0, row=0)

text_entry_label = Label(width=35, text="Type some text to display")
text_entry_label.grid(column=0, row=2)
text_entry = Entry(width=35)
text_entry.grid(column=0, row=3)

color_entry_label = Label(width=35, text="Choose a color")
color_entry_label.grid(column=0, row=4)
color_entry = Entry(width=35)
color_entry.grid(column=0, row=5)

image_button = Button(text="Choose an image", command=find_image)
image_button.grid(column=0, row=6)

watermark_button = Button(width=30, text="Add your watermark", command=add_watermark)
watermark_button.grid(column=0, row=7)


window.mainloop()

