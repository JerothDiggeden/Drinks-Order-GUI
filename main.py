import pandas as pd
import numpy as np
import customtkinter as ctk


# VARIABLES
with open("data/min.txt", "r") as file_min:
    file_min = file_min.read()

with open("data/now_count.txt", "r") as file_now:
    file_now = file_now.read()

print(file_min)
print(file_now)
pepsi_sml_lst = []


def append_pepsi_sml():
    pepsi_sml_lst.append(pepsi_sml_box.get())
    pepsi_sml_lst.append(pepsi_max_sml_box.get())
    pepsi_sml_lst.append(sunkist_sml_box.get())
    pepsi_sml_lst.append(lemonade_sml_box.get())
    pepsi_sml_lst.append(solo_sml_box.get())
    print(pepsi_sml_lst)

def window_start():
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame1.pack(fill=ctk.BOTH, expand=True)


def window_pepsi_sml():
    frame1.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame2.pack(fill=ctk.BOTH, expand=True)


def window_pepsi_lge():
    append_pepsi_sml()
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame3.pack(fill=ctk.BOTH, expand=True)


def window_water():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame4.pack(fill=ctk.BOTH, expand=True)


def window_tea():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame7.pack_forget()
    frame6.pack(fill=ctk.BOTH, expand=True)


def window_gat():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()
    frame7.pack(fill=ctk.BOTH, expand=True)


def adjust_geometry():
    # Update the geometry based on the requested width and height of the frame
    root.geometry(f"{frame.winfo_reqwidth()}x{frame.winfo_reqheight()}")


root = ctk.CTk()
root.geometry("300x600")
root.title("Bucking Bull Ordering")

# CREATE FRAME 1
frame1 = ctk.CTkFrame(root)
frame1.pack(fill=ctk.BOTH, expand=True)
label_start = ctk.CTkLabel(frame1, text="Start Order", font=("Helvetica", 20))
label_start.pack(fill=ctk.BOTH, anchor=ctk.CENTER)
start_button = ctk.CTkButton(frame1, text="Start Order", command=window_pepsi_sml)
start_button.pack(side=ctk.TOP, pady=10, anchor=ctk.CENTER)

# CREATE FRAME 2
frame2 = ctk.CTkFrame(root)
frame2.pack(fill=ctk.BOTH, expand=True)
# TITLE
label_pepsi_sml = ctk.CTkLabel(frame2, text="Schweppes 450ml", font=("Helvetica", 20))
label_pepsi_sml.pack(side=ctk.TOP, anchor=ctk.CENTER)
blank = ctk.CTkLabel(frame2, text="", font=("Helvetica", 20))
blank.pack(side=ctk.TOP, anchor=ctk.CENTER)
# LABELS & ENTRY
pepsi_sml = ctk.CTkLabel(master=frame2, text='Pepsi 450ml')
pepsi_sml.pack()
pepsi_sml_box = ctk.CTkEntry(master=frame2, width=20, font=("Helvetica", 20))
pepsi_sml_box.pack()

pepsi_max_sml = ctk.CTkLabel(master=frame2, text='Pepsi Max 450ml')
pepsi_max_sml.pack()
pepsi_max_sml_box = ctk.CTkEntry(master=frame2, width=20, font=("Helvetica", 20))
pepsi_max_sml_box.pack()

sunkist_sml = ctk.CTkLabel(master=frame2, text='Sunkist 450ml')
sunkist_sml.pack()
sunkist_sml_box = ctk.CTkEntry(master=frame2, width=20, font=("Helvetica", 20))
sunkist_sml_box.pack()

lemonade_sml = ctk.CTkLabel(master=frame2, text='Lemonade 450ml')
lemonade_sml.pack()
lemonade_sml_box = ctk.CTkEntry(master=frame2, width=20, font=("Helvetica", 20))
lemonade_sml_box.pack()

solo_sml = ctk.CTkLabel(master=frame2, text='Solo 450ml', justify=ctk.LEFT)
solo_sml.pack()
solo_sml_box = ctk.CTkEntry(master=frame2, width=20, font=("Helvetica", 20))
solo_sml_box.pack()
# BUTTONS
back_start_button = ctk.CTkButton(frame2, text="Back", command=window_start)
back_start_button.pack(side=ctk.BOTTOM, pady=10)
pepsi_sml_button = ctk.CTkButton(frame2, text="Next", command=window_pepsi_lge)
pepsi_sml_button.pack(side=ctk.BOTTOM, pady=10)

# CREATE FRAME 3
frame3 = ctk.CTkFrame(root)
frame3.pack(fill=ctk.BOTH, expand=True)
# TITLE
label_pepsi_lge = ctk.CTkLabel(frame3, text="Schweppes 600ml", font=("Helvetica", 20))
label_pepsi_lge.pack(side=ctk.TOP, anchor=ctk.CENTER)
blank = ctk.CTkLabel(frame3, text="", font=("Helvetica", 20))
blank.pack(side=ctk.TOP, anchor=ctk.CENTER)
# LABELS & ENTRY
pepsi_lge = ctk.CTkLabel(master=frame3, text='Pepsi 600ml')
pepsi_lge.pack()
pepsi_lge_box = ctk.CTkEntry(master=frame3, width=20, font=("Helvetica", 20))
pepsi_lge_box.pack()

pepsi_max_lge = ctk.CTkLabel(master=frame3, text='Pepsi Max 600ml')
pepsi_max_lge.pack()
pepsi_max_lge_box = ctk.CTkEntry(master=frame3, width=20, font=("Helvetica", 20))
pepsi_max_lge_box.pack()

sunkist_lge = ctk.CTkLabel(master=frame3, text='Sunkist 600ml')
sunkist_lge.pack()
sunkist_lge_box = ctk.CTkEntry(master=frame3, width=20, font=("Helvetica", 20))
sunkist_lge_box.pack()

lemonade_lge = ctk.CTkLabel(master=frame3, text='Lemonade 600ml')
lemonade_lge.pack()
lemonade_lge_box = ctk.CTkEntry(master=frame3, width=20, font=("Helvetica", 20))
lemonade_lge_box.pack()

solo_lge = ctk.CTkLabel(master=frame3, text='Solo 600ml', justify=ctk.LEFT)
solo_lge.pack()
solo_lge_box = ctk.CTkEntry(master=frame3, width=20, font=("Helvetica", 20))
solo_lge_box.pack()
# BUTTONS
back_start_button = ctk.CTkButton(frame3, text="Back", command=window_pepsi_sml)
back_start_button.pack(side=ctk.BOTTOM, pady=10)
pepsi_lge_button = ctk.CTkButton(frame3, text="Next", command=window_water)
pepsi_lge_button.pack(side=ctk.BOTTOM, pady=10)

# CREATE FRAME 4
frame4 = ctk.CTkFrame(root)
frame4.pack(fill=ctk.BOTH, expand=True)
# TITLE
label_water = ctk.CTkLabel(frame4, text="Water & Juice", font=("Helvetica", 20))
label_water.pack(side=ctk.TOP, anchor=ctk.CENTER)
label_water = ctk.CTkLabel(frame4, text="", font=("Helvetica", 20))
label_water.pack(side=ctk.TOP, anchor=ctk.CENTER)
# LABELS & ENTRY
label_water = ctk.CTkLabel(frame4, text="Cool Ridge")
label_water.pack(side=ctk.TOP, anchor=ctk.CENTER)
water_box = ctk.CTkEntry(master=frame4, width=20, font=("Helvetica", 20))
water_box.pack()

label_spring = ctk.CTkLabel(frame4, text="Natural Spring Water")
label_spring.pack(side=ctk.TOP, anchor=ctk.CENTER)
spring_box = ctk.CTkEntry(master=frame4, width=20, font=("Helvetica", 20))
spring_box.pack()
# LABELS & ENTRY
label_orange = ctk.CTkLabel(frame4, text="Orange")
label_orange.pack(side=ctk.TOP, anchor=ctk.CENTER)
orange_box = ctk.CTkEntry(master=frame4, width=20, font=("Helvetica", 20))
orange_box.pack()

label_apple = ctk.CTkLabel(frame4, text="Apple")
label_apple.pack(side=ctk.TOP, anchor=ctk.CENTER)
spring_apple = ctk.CTkEntry(master=frame4, width=20, font=("Helvetica", 20))
spring_apple.pack()

label_black = ctk.CTkLabel(frame4, text="Apple & Blackcurrent")
label_black.pack(side=ctk.TOP, anchor=ctk.CENTER)
black_box = ctk.CTkEntry(master=frame4, width=20, font=("Helvetica", 20))
black_box.pack()

label_mango = ctk.CTkLabel(frame4, text="Mango & Orange")
label_mango.pack(side=ctk.TOP, anchor=ctk.CENTER)
mango_box = ctk.CTkEntry(master=frame4, width=20, font=("Helvetica", 20))
mango_box.pack()

# BUTTONS
back_water = ctk.CTkButton(frame4, text="Back", command=window_pepsi_lge)
back_water.pack(side=ctk.BOTTOM, pady=10)
water_button = ctk.CTkButton(frame4, text="Next", command=window_tea)
water_button.pack(side=ctk.BOTTOM, pady=10)

# CREATE FRAME 6
frame6 = ctk.CTkFrame(root)
frame6.pack(fill=ctk.BOTH, expand=True)
# TITLE
label_tea = ctk.CTkLabel(frame6, text="Iced Tea", font=("Helvetica", 20))
label_tea.pack(side=ctk.TOP, anchor=ctk.CENTER)
label_tea = ctk.CTkLabel(frame6, text="", font=("Helvetica", 20))
label_tea.pack(side=ctk.TOP, anchor=ctk.CENTER)
# LABELS & ENTRY
label_lemon_tea = ctk.CTkLabel(frame6, text="Lemon Tea")
label_lemon_tea.pack(side=ctk.TOP, anchor=ctk.CENTER)
lemon_tea_box = ctk.CTkEntry(master=frame6, width=20, font=("Helvetica", 20))
lemon_tea_box.pack()

label_peach_tea = ctk.CTkLabel(frame6, text="Peach")
label_peach_tea.pack(side=ctk.TOP, anchor=ctk.CENTER)
peach_tea_box = ctk.CTkEntry(master=frame6, width=20, font=("Helvetica", 20))
peach_tea_box.pack()

label_mango_tea = ctk.CTkLabel(frame6, text="Mango")
label_mango_tea.pack(side=ctk.TOP, anchor=ctk.CENTER)
mango_tea_box = ctk.CTkEntry(master=frame6, width=20, font=("Helvetica", 20))
mango_tea_box.pack()

label_rasp = ctk.CTkLabel(frame6, text="Raspberry")
label_rasp.pack(side=ctk.TOP, anchor=ctk.CENTER)
rasp_box = ctk.CTkEntry(master=frame6, width=20, font=("Helvetica", 20))
rasp_box.pack()

# BUTTONS
back_tea = ctk.CTkButton(frame6, text="Back", command=window_water)
back_tea.pack(side=ctk.BOTTOM, pady=10)
tea_button = ctk.CTkButton(frame6, text="Next", command=window_gat)
tea_button.pack(side=ctk.BOTTOM, pady=10)

# CREATE FRAME 7
frame7 = ctk.CTkFrame(root)
frame7.pack(fill=ctk.BOTH, expand=True)
# TITLE
label_gat = ctk.CTkLabel(frame7, text="Gatorade", font=("Helvetica", 20))
label_gat.pack(side=ctk.TOP, anchor=ctk.CENTER)
label_gat = ctk.CTkLabel(frame7, text="", font=("Helvetica", 20))
label_gat.pack(side=ctk.TOP, anchor=ctk.CENTER)
# LABELS & ENTRY
label_lime = ctk.CTkLabel(frame7, text="Lemon Limey")
label_lime.pack(side=ctk.TOP, anchor=ctk.CENTER)
lime_box = ctk.CTkEntry(master=frame7, width=20, font=("Helvetica", 20))
lime_box.pack()

label_grape = ctk.CTkLabel(frame7, text="Grape")
label_grape.pack(side=ctk.TOP, anchor=ctk.CENTER)
grape_box = ctk.CTkEntry(master=frame7, width=20, font=("Helvetica", 20))
grape_box.pack()
# TITLE
label_gat = ctk.CTkLabel(frame7, text="", font=("Helvetica", 20))
label_gat.pack(side=ctk.TOP, anchor=ctk.CENTER)
label_gat = ctk.CTkLabel(frame7, text="Pop Tops", font=("Helvetica", 20))
label_gat.pack(side=ctk.TOP, anchor=ctk.CENTER)
label_gat = ctk.CTkLabel(frame7, text="", font=("Helvetica", 20))
label_gat.pack(side=ctk.TOP, anchor=ctk.CENTER)
# LABELS & ENTRY
label_orange_pt = ctk.CTkLabel(frame7, text="Orange")
label_orange_pt.pack(side=ctk.TOP, anchor=ctk.CENTER)
orange_pt_box = ctk.CTkEntry(master=frame7, width=20, font=("Helvetica", 20))
orange_pt_box.pack()

label_apple_pt = ctk.CTkLabel(frame7, text="Apple")
label_apple_pt.pack(side=ctk.TOP, anchor=ctk.CENTER)
apple_pt_box = ctk.CTkEntry(master=frame7, width=20, font=("Helvetica", 20))
apple_pt_box.pack()

label_black_pt = ctk.CTkLabel(frame7, text="Black")
label_black_pt.pack(side=ctk.TOP, anchor=ctk.CENTER)
black_pt_box = ctk.CTkEntry(master=frame7, width=20, font=("Helvetica", 20))
black_pt_box.pack()

label_berry_pt = ctk.CTkLabel(frame7, text="Wild Berry")
label_berry_pt.pack(side=ctk.TOP, anchor=ctk.CENTER)
berry_pt_box = ctk.CTkEntry(master=frame7, width=20, font=("Helvetica", 20))
berry_pt_box.pack()

# BUTTONS
back_gat = ctk.CTkButton(frame7, text="Back", command=window_tea)
back_gat.pack(side=ctk.BOTTOM, pady=10)
gat_button = ctk.CTkButton(frame7, text="Place Order")
gat_button.pack(side=ctk.BOTTOM, pady=10)

window_start()

root.mainloop()
