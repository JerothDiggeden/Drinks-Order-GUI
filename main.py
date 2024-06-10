import pandas as pd
import numpy as np
import customtkinter as ctk


root = ctk.CTk()
root.geometry("600x600")
frame = ctk.CTkFrame(root)



def window_start():
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame1.pack(fill=ctk.BOTH, expand=True)


def window_pepsi_sml():
    frame1.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame2.pack(fill=ctk.BOTH, expand=True)


def window_pepsi_lge():
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame3.pack(fill=ctk.BOTH, expand=True)


def window_water():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame4.pack(fill=ctk.BOTH, expand=True)


def window_juices():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame5.pack(fill=ctk.BOTH, expand=True)


def window_tea():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame7.pack_forget()
    frame6.pack(fill=ctk.BOTH, expand=True)


def window_gat():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack(fill=ctk.BOTH, expand=True)


def adjust_geometry():
    # Update the geometry based on the requested width and height of the frame
    root.geometry(f"{frame.winfo_reqwidth()}x{frame.winfo_reqheight()}")


root = ctk.CTk()
root.geometry("300x500")
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

# CREATE FRAME 5
frame5 = ctk.CTkFrame(root)
frame5.pack(fill=ctk.BOTH, expand=True)

# BUTTONS
back_juice = ctk.CTkButton(frame5, text="Back", command=window_juices)
back_juice.pack(side=ctk.BOTTOM, pady=10)
juice_button = ctk.CTkButton(frame5, text="Next", command=window_tea)
juice_button.pack(side=ctk.BOTTOM, pady=10)

# CREATE FRAME 6
frame6 = ctk.CTkFrame(root)
frame6.pack(fill=ctk.BOTH, expand=True)
label_tea = ctk.CTkLabel(frame6, text="Iced Tea", font=("Helvetica", 20))
label_tea.pack(side=ctk.TOP, anchor=ctk.CENTER)
back_tea = ctk.CTkButton(frame6, text="Back", command=window_water)
back_tea.pack(side=ctk.BOTTOM, pady=10)
tea_button = ctk.CTkButton(frame6, text="Next", command=window_gat)
tea_button.pack(side=ctk.BOTTOM, pady=10)

# CREATE FRAME 7
frame7 = ctk.CTkFrame(root)
frame7.pack(fill=ctk.BOTH, expand=True)
label_gat = ctk.CTkLabel(frame7, text="Gatorade & Pop Tops", font=("Helvetica", 20))
label_gat.pack(side=ctk.TOP, anchor=ctk.CENTER)
back_gat = ctk.CTkButton(frame7, text="Back", command=window_tea)
back_gat.pack(side=ctk.BOTTOM, pady=10)
gat_button = ctk.CTkButton(frame7, text="Place Order")
gat_button.pack(side=ctk.BOTTOM, pady=10)

window_start()

root.mainloop()


# df = pd.read_csv("data/SchOrder.csv")
# print(df)
# drink_names = list(df["Drink"])
# print(drink_names)

# for i in df["Drink"].items():
#     print(f"{i} = customtkinter.CTkLabel(master=frame, text='{i}')")
# count = 0
# for i in drink_names:
#     t = i
#     i = i.lower()
#     count = count + 1
#     if " " in i:
#         i = i.replace(" ", "_")
#     # print(f"{i}.grid(column=0, row={count})")
#     print(f"{i}.grid(column=0, row={count})")


# def pepsi_lge():
#     window_pepsi_lge = customtkinter.CTkToplevel()
#     window_pepsi_lge.title("Pepsi 600ml")
#     window_pepsi_lge.focus_set()  # Set focus to the new window
#     window_pepsi_lge.grab_set()
#     title = customtkinter.CTkLabel(window_pepsi_lge, text="Pepsi 600ml", font=("Helvetica", 50))
#     title.pack(pady=10)
#
#     next_button = customtkinter.CTkButton(window_pepsi_lge, text="Next", command=pepsi_sml)
#
# def pepsi_sml():
#     window_pepsi_sml = customtkinter.CTkToplevel()
#     window_pepsi_sml.title("Pepsi 450ml")
#     window_pepsi_sml.focus_set()  # Set focus to the new window
#     window_pepsi_sml.grab_set()
#     title = customtkinter.CTkLabel(window_pepsi_sml, text="Pepsi 450ml", font=("Helvetica", 50))
#     title.pack(pady=10)
#     next_button = customtkinter.CTkButton(window_pepsi_sml, text="Next", command=pepsi_lge)
#     back_button = customtkinter.CTkButton(window_pepsi_sml, text="Back", command=pepsi_lge)
#     next_button.pack(pady=10)
#     back_button.pack(pady=10)

# root = customtkinter.CTk()
# root.geometry("1000x950")
#
# frame = customtkinter.CTkFrame(root)
# frame.pack(pady=20, padx=60, fill="both", expand=True)

# # COLUMN NAMES
# drinks = customtkinter.CTkLabel(master=frame, text="Drink")
# count = customtkinter.CTkLabel(master=frame, text="Now Count")
# on_order = customtkinter.CTkLabel(master=frame, text="On Order")
# stock = customtkinter.CTkLabel(master=frame, text="Now Stock")
# min_levels = customtkinter.CTkLabel(master=frame, text="Min Levels")
# order = customtkinter.CTkLabel(master=frame, text="Order")

# # DRINKS
# pepsi_sml = customtkinter.CTkLabel(master=frame, text='Pepsi')
# pepsi_max_sml = customtkinter.CTkLabel(master=frame, text='Pepsi Max')
# sunkist_sml = customtkinter.CTkLabel(master=frame, text='Sunkist')
# lemonade_sml = customtkinter.CTkLabel(master=frame, text='Lemonade')
# solo_sml = customtkinter.CTkLabel(master=frame, text='Solo')
# pepsi = customtkinter.CTkLabel(master=frame, text='Pepsi')
# pepsi_max = customtkinter.CTkLabel(master=frame, text='Pepsi Max')
# sunkist = customtkinter.CTkLabel(master=frame, text='Sunkist')
# lemonade = customtkinter.CTkLabel(master=frame, text='Lemonade')
# solo = customtkinter.CTkLabel(master=frame, text='Solo')
# m_dew = customtkinter.CTkLabel(master=frame, text='M Dew')
# passiona = customtkinter.CTkLabel(master=frame, text='Passiona')
# pepsi_max_rasberry = customtkinter.CTkLabel(master=frame, text='Pepsi Max Rasberry')
# vanilla_max = customtkinter.CTkLabel(master=frame, text='Vanilla Max')
# creaming_soda_max = customtkinter.CTkLabel(master=frame, text='Creaming Soda Max')
# sugar_free_sunkist = customtkinter.CTkLabel(master=frame, text='Sugar Free Sunkist')
# sugar_free_solo = customtkinter.CTkLabel(master=frame, text='Sugar Free Solo')
# sugar_free_lade = customtkinter.CTkLabel(master=frame, text='Sugar Free Lade')
# water = customtkinter.CTkLabel(master=frame, text='WATER')
# natural = customtkinter.CTkLabel(master=frame, text='Natural')
# orange = customtkinter.CTkLabel(master=frame, text='Orange')
# apple = customtkinter.CTkLabel(master=frame, text='Apple')
# apple_black = customtkinter.CTkLabel(master=frame, text='Apple & Black')
# mango_orange = customtkinter.CTkLabel(master=frame, text='Mango & Orange')
# lemon_lipton_iced_tea = customtkinter.CTkLabel(master=frame, text='Lemon Lipton Iced Tea')
# peach__lipton_iced_tea = customtkinter.CTkLabel(master=frame, text='Peach  Lipton Iced Tea')
# mango__lipton_iced_tea = customtkinter.CTkLabel(master=frame, text='Mango  Lipton Iced Tea')
# rasberry__lipton_iced_tea = customtkinter.CTkLabel(master=frame, text='Rasberry  Lipton Iced Tea')
# lemon_lime = customtkinter.CTkLabel(master=frame, text='Lemon Lime')
# grape = customtkinter.CTkLabel(master=frame, text='Grape')
# orange_pt = customtkinter.CTkLabel(master=frame, text='Orange')
# apple_pt = customtkinter.CTkLabel(master=frame, text='Apple')
# apple_black_pt = customtkinter.CTkLabel(master=frame, text='Apple & Black')
# wild_berry_pt = customtkinter.CTkLabel(master=frame, text='Wild Berry')
#
# # PLACE LABELS ON GRID
#
# title.grid(column=0, row=0, columnspan=5, padx=250, pady=5)
# drinks.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
# count.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
# on_order.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
# stock.grid(row=1, column=3, padx=5, pady=5, sticky="ew")
# min_levels.grid(row=1, column=4, padx=5, pady=5, sticky="ew")
# order.grid(row=1, column=5, padx=5, pady=5, sticky="ew")
#
# pepsi_sml.grid(column=0, row=1)
# pepsi_max_sml.grid(column=0, row=2)
# sunkist_sml.grid(column=0, row=3)
# lemonade_sml.grid(column=0, row=4)
# solo_sml.grid(column=0, row=5)
# pepsi.grid(column=0, row=6)
# pepsi_max.grid(column=0, row=7)
# sunkist.grid(column=0, row=8)
# lemonade.grid(column=0, row=9)
# solo.grid(column=0, row=10)
# m_dew.grid(column=0, row=11)
# passiona.grid(column=0, row=12)
# pepsi_max_rasberry.grid(column=0, row=13)
# vanilla_max.grid(column=0, row=14)
# creaming_soda_max.grid(column=0, row=15)
# sugar_free_sunkist.grid(column=0, row=16)
# sugar_free_solo.grid(column=0, row=17)
# sugar_free_lade.grid(column=0, row=18)
# water.grid(column=0, row=19)
# natural.grid(column=0, row=20)
# orange.grid(column=0, row=21)
# apple.grid(column=0, row=22)
# apple_black.grid(column=0, row=23)
# mango_orange.grid(column=0, row=24)
# lemon_lipton_iced_tea.grid(column=0, row=25)
# peach__lipton_iced_tea.grid(column=0, row=26)
# mango__lipton_iced_tea.grid(column=0, row=27)
# rasberry__lipton_iced_tea.grid(column=0, row=28)
# lemon_lime.grid(column=0, row=29)
# grape.grid(column=0, row=30)
# orange_pt.grid(column=0, row=31)
# apple_pt.grid(column=0, row=32)
# apple_black_pt.grid(column=0, row=33)
# wild_berry_pt.grid(column=0, row=34)
