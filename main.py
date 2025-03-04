import customtkinter as ctk
import json
from fpdf import FPDF


order_result = []
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0


def read_json(file_path):
    with open(file_path, "r") as file_min_obj:
        file_min = json.load(file_min_obj)
    return file_min


def edit_dict(order_dict):
    for k, v in order_dict.items():
        # Modify the key as needed
        new_key = k.replace("__", " ")
        new_key = k.replace("_", " ")
        new_key = new_key.title()
        new_key = new_key.replace("Pt", "PT")
        new_key = new_key.replace("  ", " ")
        new_order_dict[new_key] = v


def edit_values():
    for value, key in zip(order_result, new_order_dict.keys()):
        new_order_dict[key] = value


# Function to append string values from the dictionary to the list
def minimum():
    for k, v in file_min_read.items():
        string = str(v)
        min_stock.append(string)


def calc():
    min_stock_length = len(min_stock)

    for count in range(min_stock_length):  # Iterate up to the length of min_stock
        x = min_stock[count]
        x = float(x)
        y = float(order_lst[count])
        z = x - y
        order_result.append(z)
    for val in range(len(order_result)):
        val_dict[val] = order_result[val]



def append_pepsi_sml():
    pepsi_sml_lst.append(int(pepsi_sml_box.get()))
    pepsi_sml_lst.append(int(pepsi_max_sml_box.get()))
    pepsi_sml_lst.append(int(sunkist_sml_box.get()))
    pepsi_sml_lst.append(int(lemonade_sml_box.get()))
    pepsi_sml_lst.append(int(solo_sml_box.get()))


def append_pepsi_sml_chck():
    pepsi_sml_lst_chck.append(int(pepsi_sml_box.get()))
    pepsi_sml_lst_chck.append(int(pepsi_max_sml_box.get()))
    pepsi_sml_lst_chck.append(int(sunkist_sml_box.get()))
    pepsi_sml_lst_chck.append(int(lemonade_sml_box.get()))
    pepsi_sml_lst_chck.append(int(solo_sml_box.get()))


def append_pepsi_lge():
    pepsi_lge_lst.append(int(pepsi_lge_box.get()))
    pepsi_lge_lst.append(int(pepsi_max_lge_box.get()))
    pepsi_lge_lst.append(int(sunkist_lge_box.get()))
    pepsi_lge_lst.append(int(lemonade_lge_box.get()))
    pepsi_lge_lst.append(int(solo_lge_box.get()))


def append_pepsi_lge_chck():
    pepsi_lge_lst_chck.append(int(pepsi_lge_box.get()))
    pepsi_lge_lst_chck.append(int(pepsi_max_lge_box.get()))
    pepsi_lge_lst_chck.append(int(sunkist_lge_box.get()))
    pepsi_lge_lst_chck.append(int(lemonade_lge_box.get()))
    pepsi_lge_lst_chck.append(int(solo_lge_box.get()))

def append_water():
    water_lst.append(int(water_box.get()))
    water_lst.append(int(spring_box.get()))
    water_lst.append(int(orange_box.get()))
    water_lst.append(int(apple_box.get()))
    water_lst.append(int(black_box.get()))
    water_lst.append(int(mango_box.get()))

def append_water_chck():
    water_lst_chck.append(int(water_box.get()))
    water_lst_chck.append(int(spring_box.get()))
    water_lst_chck.append(int(orange_box.get()))
    water_lst_chck.append(int(apple_box.get()))
    water_lst_chck.append(int(black_box.get()))
    water_lst_chck.append(int(mango_box.get()))


def append_tea():
    tea_lst.append(int(lemon_tea_box.get()))
    tea_lst.append(int(peach_tea_box.get()))
    tea_lst.append(int(mango_tea_box.get()))
    tea_lst.append(int(rasp_tea_box.get()))


def append_tea_chck():
    tea_lst_chck.append(int(lemon_tea_box.get()))
    tea_lst_chck.append(int(peach_tea_box.get()))
    tea_lst_chck.append(int(mango_tea_box.get()))
    tea_lst_chck.append(int(rasp_tea_box.get()))


def append_gat_pop():
    gat_pop_lst.append(int(lime_box.get()))
    gat_pop_lst.append(int(grape_box.get()))
    gat_pop_lst.append(int(orange_pt_box.get()))
    gat_pop_lst.append(int(apple_pt_box.get()))
    gat_pop_lst.append(int(black_pt_box.get()))
    gat_pop_lst.append(int(berry_pt_box.get()))


def append_gat_pop_chck():
    gat_pop_lst_chck.append(int(lime_box.get()))
    gat_pop_lst_chck.append(int(grape_box.get()))
    gat_pop_lst_chck.append(int(orange_pt_box.get()))
    gat_pop_lst_chck.append(int(apple_pt_box.get()))
    gat_pop_lst_chck.append(int(black_pt_box.get()))
    gat_pop_lst_chck.append(int(berry_pt_box.get()))


def concat():
    order_lst.extend(pepsi_sml_lst)
    order_lst.extend(pepsi_lge_lst)
    order_lst.extend(water_lst)
    order_lst.extend(tea_lst)
    order_lst.extend(gat_pop_lst)


def window_start():
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame8.pack_forget()
    frame1.pack(fill=ctk.BOTH, expand=True)
    adjust_window_size(frame1)


def window_pepsi_sml():
    global counter1
    counter1 += 1
    frame1.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame8.pack_forget()
    frame2.pack(fill=ctk.BOTH, expand=True)
    adjust_window_size(frame2)


def window_pepsi_lge():
    global counter1
    counter1 += 1
    if counter1 == 2:
        append_pepsi_sml()
    elif counter1 > 2:
        if len(pepsi_sml_lst) == 5:
            pepsi_sml_lst_chck.clear()
            append_pepsi_sml_chck()
            del pepsi_sml_lst_chck[5:]
            for i in range(len(pepsi_sml_lst)):
                pepsi_sml_lst[i] = pepsi_sml_lst_chck[i]
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame8.pack_forget()
    frame3.pack(fill=ctk.BOTH, expand=True)
    adjust_window_size(frame3)


def window_water():
    global counter2
    counter2 += 1
    if counter2 <= 1:
        append_pepsi_lge()
    elif counter2 > 1:
        if len(pepsi_lge_lst) == 5:
            append_pepsi_lge_chck()
            temp = pepsi_lge_lst_chck[-5:]
            for i in range(len(pepsi_lge_lst)):
                pepsi_lge_lst[i] = temp[i]
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame8.pack_forget()
    frame4.pack(fill=ctk.BOTH, expand=True)
    adjust_window_size(frame4)


def window_tea():
    global counter3
    counter3 += 1
    if counter3 <= 1:
        append_water()
    elif counter3 > 1:
        if len(water_lst) == 6:
            append_water_chck()
            temp = water_lst_chck[-6:]
            for i in range(len(water_lst)):
                water_lst[i] = temp[i]
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame7.pack_forget()
    frame8.pack_forget()
    frame6.pack(fill=ctk.BOTH, expand=True)
    adjust_window_size(frame6)


def window_gat():
    global counter4
    counter4 += 1
    if counter4 <= 1:
        append_tea()
    elif counter4 > 1:
        if len(tea_lst) == 4:
            append_tea_chck()
            temp = tea_lst_chck[-4:]
            for i in range(len(tea_lst)):
                tea_lst[i] = temp[i]
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()
    frame8.pack_forget()
    frame7.pack(fill=ctk.BOTH, expand=True)
    adjust_window_size(frame7)


def window_final():
    global counter5
    counter5 += 1
    if counter5 <= 1:
        append_gat_pop()
    elif counter5 > 1:
        if len(gat_pop_lst) == 6:
            append_gat_pop_chck()
            temp = gat_pop_lst_chck[-6:]
            for i in range(len(gat_pop_lst)):
                gat_pop_lst[i] = temp[i]
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame8.pack(fill=ctk.BOTH, expand=True)
    adjust_window_size(frame8)


def place_order():
    min_stock = read_json(file_min_path)
    concat()
    minimum()
    calc()
    edit_dict(new_order_dict)
    edit_values()
    print("ORDER:", new_order_dict)


def adjust_window_size(frame):
    width = frame.winfo_reqwidth()
    height = frame.winfo_reqheight()
    root.geometry(f"{width + 10}x{height + 10}")


pepsi_sml_lst = []
pepsi_lge_lst = []
water_lst = []
tea_lst = []
gat_pop_lst = []
pepsi_sml_lst_chck = []
pepsi_lge_lst_chck = []
water_lst_chck = []
tea_lst_chck = []
gat_pop_lst_chck = []
order_lst = []
temp = []
val_dict = {}
order_dict = {}
new_order_dict = {'Pepsi': 0, 'Pepsi Max': 0, 'Sunkist': 0, 'Lemonade': 0, 'Solo': 0, 'Pepsi Large': 0, 'Pepsi Max Large': 0, 'Sunkist Large': 0, 'Lemonade Large': 0, 'Solo Large': 0, 'Water': 0, 'Natural': 0, 'Orange': 0, 'Apple': 0, 'Apple Black': 0, 'Mango Orange': 0, 'Lemon Lipton Iced Tea': 0, 'Peach Lipton Iced Tea': 0, 'Mango Lipton Iced Tea': 0, 'Rasberry Lipton Iced Tea': 0, 'Lemon Lime': 0, 'Grape': 0, 'Orange PT': 0, 'Apple PT': 0, 'Apple Black PT': 0, 'Wild Berry PT': 0}

with open("data/now_count.txt", "r") as file_now_obj:
    file_min = file_now_obj.read()

file_min_path = "data/min.json"
file_min_read = read_json(file_min_path)
order_dic = file_min_read
min_stock = []

root = ctk.CTk()
root.geometry("300x600")
root.title("Bucking Bull Ordering")

# CREATE FRAME 1
frame1 = ctk.CTkFrame(root)
frame1.pack(fill=ctk.BOTH, expand=True)
label_start = ctk.CTkLabel(frame1, text="Start Order", font=("Helvetica", 20))
label_start.pack(fill=ctk.BOTH, anchor=ctk.CENTER)
start_button = ctk.CTkButton(frame1, text="Start Order", command=window_pepsi_sml)
start_button.pack(side=ctk.BOTTOM, pady=10, anchor=ctk.CENTER)

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
pepsi_sml_box = ctk.CTkEntry(master=frame2, width=40, font=("Helvetica", 20))
pepsi_sml_box.pack()

pepsi_max_sml = ctk.CTkLabel(master=frame2, text='Pepsi Max 450ml')
pepsi_max_sml.pack()
pepsi_max_sml_box = ctk.CTkEntry(master=frame2, width=40, font=("Helvetica", 20))
pepsi_max_sml_box.pack()

sunkist_sml = ctk.CTkLabel(master=frame2, text='Sunkist 450ml')
sunkist_sml.pack()
sunkist_sml_box = ctk.CTkEntry(master=frame2, width=40, font=("Helvetica", 20))
sunkist_sml_box.pack()

lemonade_sml = ctk.CTkLabel(master=frame2, text='Lemonade 450ml')
lemonade_sml.pack()
lemonade_sml_box = ctk.CTkEntry(master=frame2, width=40, font=("Helvetica", 20))
lemonade_sml_box.pack()

solo_sml = ctk.CTkLabel(master=frame2, text='Solo 450ml', justify=ctk.LEFT)
solo_sml.pack()
solo_sml_box = ctk.CTkEntry(master=frame2, width=40, font=("Helvetica", 20))
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
blank = ctk.CTkLabel(frame3, text="", font=("Helvetica", 40))
blank.pack(side=ctk.TOP, anchor=ctk.CENTER)
# LABELS & ENTRY
pepsi_lge = ctk.CTkLabel(master=frame3, text='Pepsi 600ml')
pepsi_lge.pack()
pepsi_lge_box = ctk.CTkEntry(master=frame3, width=40, font=("Helvetica", 20))
pepsi_lge_box.pack()

pepsi_max_lge = ctk.CTkLabel(master=frame3, text='Pepsi Max 600ml')
pepsi_max_lge.pack()
pepsi_max_lge_box = ctk.CTkEntry(master=frame3, width=40, font=("Helvetica", 20))
pepsi_max_lge_box.pack()

sunkist_lge = ctk.CTkLabel(master=frame3, text='Sunkist 600ml')
sunkist_lge.pack()
sunkist_lge_box = ctk.CTkEntry(master=frame3, width=40, font=("Helvetica", 20))
sunkist_lge_box.pack()

lemonade_lge = ctk.CTkLabel(master=frame3, text='Lemonade 600ml')
lemonade_lge.pack()
lemonade_lge_box = ctk.CTkEntry(master=frame3, width=40, font=("Helvetica", 20))
lemonade_lge_box.pack()

solo_lge = ctk.CTkLabel(master=frame3, text='Solo 600ml', justify=ctk.LEFT)
solo_lge.pack()
solo_lge_box = ctk.CTkEntry(master=frame3, width=40, font=("Helvetica", 20))
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
# TITLE
label_water = ctk.CTkLabel(frame4, text="", font=("Helvetica", 20))
label_water.pack(side=ctk.TOP, anchor=ctk.CENTER)
label_water = ctk.CTkLabel(frame4, text="Water", font=("Helvetica", 20))
label_water.pack(side=ctk.TOP, anchor=ctk.CENTER)
label_water = ctk.CTkLabel(frame4, text="", font=("Helvetica", 20))
label_water.pack(side=ctk.TOP, anchor=ctk.CENTER)
# LABELS & ENTRY
label_water = ctk.CTkLabel(frame4, text="Cool Ridge")
label_water.pack(side=ctk.TOP, anchor=ctk.CENTER)
water_box = ctk.CTkEntry(master=frame4, width=40, font=("Helvetica", 20))
water_box.pack()

label_spring = ctk.CTkLabel(frame4, text="Natural Spring Water")
label_spring.pack(side=ctk.TOP, anchor=ctk.CENTER)
spring_box = ctk.CTkEntry(master=frame4, width=40, font=("Helvetica", 20))
spring_box.pack()
# TITLE
label_water = ctk.CTkLabel(frame4, text="", font=("Helvetica", 20))
label_water.pack(side=ctk.TOP, anchor=ctk.CENTER)
label_water = ctk.CTkLabel(frame4, text="Juice", font=("Helvetica", 20))
label_water.pack(side=ctk.TOP, anchor=ctk.CENTER)
label_water = ctk.CTkLabel(frame4, text="", font=("Helvetica", 20))
label_water.pack(side=ctk.TOP, anchor=ctk.CENTER)
# LABELS & ENTRY
label_orange = ctk.CTkLabel(frame4, text="Orange")
label_orange.pack(side=ctk.TOP, anchor=ctk.CENTER)
orange_box = ctk.CTkEntry(master=frame4, width=40, font=("Helvetica", 20))
orange_box.pack()

label_apple = ctk.CTkLabel(frame4, text="Apple")
label_apple.pack(side=ctk.TOP, anchor=ctk.CENTER)
apple_box = ctk.CTkEntry(master=frame4, width=40, font=("Helvetica", 20))
apple_box.pack()

label_black = ctk.CTkLabel(frame4, text="Apple & Blackcurrent")
label_black.pack(side=ctk.TOP, anchor=ctk.CENTER)
black_box = ctk.CTkEntry(master=frame4, width=40, font=("Helvetica", 20))
black_box.pack()

label_mango = ctk.CTkLabel(frame4, text="Mango & Orange")
label_mango.pack(side=ctk.TOP, anchor=ctk.CENTER)
mango_box = ctk.CTkEntry(master=frame4, width=40, font=("Helvetica", 20))
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
lemon_tea_box = ctk.CTkEntry(master=frame6, width=40, font=("Helvetica", 20))
lemon_tea_box.pack()

label_peach_tea = ctk.CTkLabel(frame6, text="Peach")
label_peach_tea.pack(side=ctk.TOP, anchor=ctk.CENTER)
peach_tea_box = ctk.CTkEntry(master=frame6, width=40, font=("Helvetica", 20))
peach_tea_box.pack()

label_mango_tea = ctk.CTkLabel(frame6, text="Mango")
label_mango_tea.pack(side=ctk.TOP, anchor=ctk.CENTER)
mango_tea_box = ctk.CTkEntry(master=frame6, width=40, font=("Helvetica", 20))
mango_tea_box.pack()

label_rasp = ctk.CTkLabel(frame6, text="Raspberry")
label_rasp.pack(side=ctk.TOP, anchor=ctk.CENTER)
rasp_tea_box = ctk.CTkEntry(master=frame6, width=40, font=("Helvetica", 20))
rasp_tea_box.pack()

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
lime_box = ctk.CTkEntry(master=frame7, width=40, font=("Helvetica", 20))
lime_box.pack()

label_grape = ctk.CTkLabel(frame7, text="Grape")
label_grape.pack(side=ctk.TOP, anchor=ctk.CENTER)
grape_box = ctk.CTkEntry(master=frame7, width=40, font=("Helvetica", 20))
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
orange_pt_box = ctk.CTkEntry(master=frame7, width=40, font=("Helvetica", 20))
orange_pt_box.pack()

label_apple_pt = ctk.CTkLabel(frame7, text="Apple")
label_apple_pt.pack(side=ctk.TOP, anchor=ctk.CENTER)
apple_pt_box = ctk.CTkEntry(master=frame7, width=40, font=("Helvetica", 20))
apple_pt_box.pack()

label_black_pt = ctk.CTkLabel(frame7, text="Black")
label_black_pt.pack(side=ctk.TOP, anchor=ctk.CENTER)
black_pt_box = ctk.CTkEntry(master=frame7, width=40, font=("Helvetica", 20))
black_pt_box.pack()

label_berry_pt = ctk.CTkLabel(frame7, text="Wild Berry")
label_berry_pt.pack(side=ctk.TOP, anchor=ctk.CENTER)
berry_pt_box = ctk.CTkEntry(master=frame7, width=40, font=("Helvetica", 20))
berry_pt_box.pack()

# BUTTONS
back_gat = ctk.CTkButton(frame7, text="Back", command=window_tea)
back_gat.pack(side=ctk.BOTTOM, pady=10)
gat_button = ctk.CTkButton(frame7, text="Next", command=window_final)
gat_button.pack(side=ctk.BOTTOM, pady=10)

# CREATE FRAME 8
frame8 = ctk.CTkFrame(root)
frame8.pack(fill=ctk.BOTH, expand=True)

# TITLE
label_gat = ctk.CTkLabel(frame8, text="Place Order", font=("Helvetica", 20))
label_gat.pack(side=ctk.TOP, anchor=ctk.CENTER)
label_gat = ctk.CTkLabel(frame8, text="", font=("Helvetica", 20))
label_gat.pack(side=ctk.TOP, anchor=ctk.CENTER)

# BUTTONS
back_gat = ctk.CTkButton(frame8, text="Back", command=window_gat)
back_gat.pack(side=ctk.BOTTOM, pady=10)
gat_button = ctk.CTkButton(frame8, text="Place Order", command=place_order)
gat_button.pack(side=ctk.BOTTOM, pady=10)

window_start()
root.mainloop()
