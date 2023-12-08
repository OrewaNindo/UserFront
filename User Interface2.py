from tkinter import *  
from PIL import Image, ImageTk
import sys

bckground = '#A9A9A9'
foeground = 'WHITE'
lbackground =  '#CA0123'

root = Tk()
root.title('Power Parts Ranking')
root.geometry('1080x600')
root.attributes('-fullscreen', True)

def on_f11(event):
    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
    else:
        root.attributes('-fullscreen', True)

root.bind('<F11>', on_f11)

main_canvas = Canvas(
    root, bg=bckground
)
main_canvas.pack(expand=True,fill='y')
main_canvas.config(width=1920, highlightthickness=0, border=0)
main_canvas.pack_propagate(False)
label_frame = LabelFrame(
    main_canvas, bg=lbackground, width=1920,height=85
)

label = Label(label_frame, text='Power Parts Ranking', font=('Arial', 35))
label.pack(pady=5,padx=80, side='left')
label.config(
    bg=lbackground, 
    fg='WHITE',
    border=0,
    highlightthickness=0
)

power_button = ImageTk.PhotoImage(Image.open("White power button.png"))
power_button_hower = ImageTk.PhotoImage(Image.open("png-clipart-computer-icons-logo-button-power-symbol-button-logo-desktop-wallpaper-thumbnail-removebg-preview(2).png")) 

power_button_label = Label(
    label_frame, bg=lbackground, width=50, height=50, image=power_button
)

def on_enter(event):
    power_button_label.config(
        image=power_button_hower
    )

def on_leave(event):
    power_button_label.config(
        image=power_button
    )

def on_image_click(event):
    sys.exit(0)

power_button_label.place(relx=0.96, rely=0.15)

power_button_label.bind('<Enter>', on_enter)
power_button_label.bind('<Leave>', on_leave)
power_button_label.bind('<Button-1>', on_image_click)

options = ['Motherboard', 'Processor', 'Air Cooler', 'RAM', 'Graphic Card', 'Power Supply']
variable = StringVar()
variable.set("Select Component")

component_option = OptionMenu(
    label_frame, variable, *options
)

component_option.config(
    bg=lbackground,
    fg='WHITE',
    activebackground='#800020',
    activeforeground='WHITE',
    border=0,
    highlightthickness=0,
    indicatoron=0,
    font=('Arial',26)
)

component_option['menu'].config(
    bg='#C41E3A',
    fg='WHITE',
    activebackground='#D22B2B',
    font=('Arial',22),
    border=0,
    activeborder=0,
    bd=0,            # Set this to 0 to remove the border
    relief='flat'
)
component_option.place(relx=0.375, rely=0.4)

label_frame.pack_propagate(False)
label_frame.pack(pady=10)


root.mainloop()