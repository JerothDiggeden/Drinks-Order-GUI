import pandas as pd


df = pd.read_csv("data/SchOrder.csv")
drink_names = list(df["Drink"])
minimum_drinks = list(df["Minimum Levels"])

print(minimum_drinks)
print(drink_names)
dict_drinks = {}
print(dict_drinks)
drink_new = []
print(drink_new)
for i in drink_names:
    i = str(i)
    i = i.lower()
    if " " in i:
        i = i.replace(" ", "_")
    if "&" in i:
        i = i.replace("&", "")
    drink_new.append(i)
    dict_drinks[i] = None

print(drink_new)
print(dict_drinks)

count = -1
for key in dict_drinks.keys():
    count = count + 1
    dict_drinks[key] = minimum_drinks[count]

print(dict_drinks)

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