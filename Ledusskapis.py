import pandas as pd
import tkinter as tk
from tkinter import Label, messagebox, simpledialog
from datetime import datetime, timedelta
import os
import fontstyle

# Faila nosaukumi
FRIDGE_FILE = 'fridge.csv'
SHOPPING_LIST_FILE = 'shopping_list.csv'

# Pārbauda vai faili eksistē
if not os.path.exists(FRIDGE_FILE):
    pd.DataFrame(columns=['Product', 'ExpiryDate']).to_csv(FRIDGE_FILE, index=False)
if not os.path.exists(SHOPPING_LIST_FILE):
    pd.DataFrame(columns=['Product']).to_csv(SHOPPING_LIST_FILE, index=False)

# Datu ielāde
def load_fridge():
    return pd.read_csv(FRIDGE_FILE)

def save_fridge(df):
    df.to_csv(FRIDGE_FILE, index=False)

def load_shopping_list():
    return pd.read_csv(SHOPPING_LIST_FILE)

def save_shopping_list(df):
    df.to_csv(SHOPPING_LIST_FILE, index=False)

# Produktu pievienošana
def add_product():
    product = simpledialog.askstring("Pievienot produktu", "Ievadi produkta nosaukumu:")
    expiry_str = simpledialog.askstring("Pievienot derīguma termiņu", "Ievadi derīguma termiņu (YYYY.MM.DD):")

    try:
        expiry_date = datetime.strptime(expiry_str, "%Y.%m.%d")
        df = load_fridge()
        new_row = pd.DataFrame([{'Product': product, 'ExpiryDate': expiry_date.strftime("%Y.%m.%d")}])
        df = pd.concat([df, new_row], ignore_index=True)
        save_fridge(df)
        messagebox.showinfo("Pievienots", f"{product} pievienots ledusskapim!")
    except ValueError:
        messagebox.showerror("Kļūda", "Nepareizs datuma formāts. Izmanto DD.MM.YYYY!")

# Produktu saraksta rādīšana
def show_products():
    df = load_fridge()
    products = "\n".join([f"{row['Product']} (Derīgs līdz {row['ExpiryDate']})" for idx, row in df.iterrows()])
    messagebox.showinfo("Ledusskapja Saturs", products if products else "Ledusskapis ir tukšs.")

# Produkta izņemšana
def remove_product():
    product = simpledialog.askstring("Izņemt produktu", "Ievadi produkta nosaukumu, ko izņemt:")
    df = load_fridge()
    if product in df['Product'].values:
        df = df[df['Product'] != product]
        save_fridge(df)
        messagebox.showinfo("Izņemts", f"{product} izņemts no ledusskapja!")
    else:
        messagebox.showerror("Nav atrasts", "Produkts netika atrasts ledusskapī!")

# Brīdinājumu pārbaude
def check_expiry():
    df = load_fridge()
    today = datetime.now().date()
    warnings = []
    for idx, row in df.iterrows():
        expiry_date = datetime.strptime(row['ExpiryDate'], "%Y.%m.%d").date()
        if expiry_date < today:
            warnings.append(f"{row['Product']} - BEIDZIES!")
        elif expiry_date <= today + timedelta(days=2):
            warnings.append(f"{row['Product']} - drīz beigsies ({expiry_date})")

    if warnings:
        messagebox.showwarning("Brīdinājumi!", "\n".join(warnings))
    else:
        messagebox.showinfo("Viss kārtībā", "Nav produktu ar beigušos termiņu.")

# Pievienošana iepirkumu sarakstam
def add_to_shopping_list():
    product = simpledialog.askstring("Pievienot iepirkumu sarakstam", "Ievadi produkta nosaukumu:")
    if product:
        df = load_shopping_list()
        new_row = pd.DataFrame([{'Product': product}])
        df = pd.concat([df, new_row], ignore_index=True)
        save_shopping_list(df)
        messagebox.showinfo("Pievienots", f"{product} pievienots iepirkumu sarakstam!")

# GUI izveidošana
root = tk.Tk()
root.title("Tavs ledusskapis")
root.configure(bg='#ffedf2')
label = Label(root, 
              text="Tavs ledusskapis!",
                fg='#545454',
                  font=("Tahoma", 20, "bold"),
                  bg="#a5d4b6")
label.pack()

root.configure(cursor="heart")

tk.Button(root,
           text="Pievieno produktu!", 
           command=add_product,
             width=25,
               font=("Tahoma", 10),
               activebackground="#ff79a9", ##rozā
                   activeforeground="#a5d4b6", ## kad uzspiež, burti tādā krāsā
                   anchor="center",
                   bg="#ff79a9",
                   fg="white", #tumši pelēks
                   height=1,
                   highlightthickness=2,
                   
               ).pack(pady=5)
tk.Button(root, 
          text="Rādīt ledusskapja saturu", 
          command=show_products, 
          width=25,
            font=("Tahoma", 10),
            activebackground="#ff79a9", ##rozā
                   activeforeground="#a5d4b6", ## kad uzspiež, burti tādā krāsā
                   anchor="center",
                   bg="#ff79a9",
                   fg="white", #tumši pelēks
                   height=1,
                   highlightthickness=2,
            ).pack(pady=5)


tk.Button(root, 
          text="Izņemt produktu", 
          command=remove_product, 
          width=25, 
          font=("Tahoma", 10),
          activebackground="#ff79a9", ##rozā
                   activeforeground="#a5d4b6", ## kad uzspiež, burti tādā krāsā
                   anchor="center",
                   bg="#ff79a9",
                   fg="white", #tumši pelēks
                   height=1,
                   highlightthickness=2,
          ).pack(pady=5)


tk.Button(root, 
          text="Pārbaudīt derīguma termiņus",
            command=check_expiry,
              width=25,
                font=("Tahoma", 10),
                activebackground="#ff79a9", ##rozā
                   activeforeground="#a5d4b6", ## kad uzspiež, burti tādā krāsā
                   anchor="center",
                   bg="#ff79a9",
                   fg="white", #tumši pelēks
                   height=1,
                   highlightthickness=2,
                ).pack(pady=5)


tk.Button(root,
           text="Pievienot iepirkumu sarakstam", 
           command=add_to_shopping_list,
             width=25,
               font=("Tahoma", 10),
               activebackground="#ff79a9", ##rozā
                   activeforeground="#a5d4b6", ## kad uzspiež, burti tādā krāsā
                   anchor="center",
                   bg="#ff79a9",
                   fg="white", #tumši pelēks
                   height=1,
                   highlightthickness=2,
               ).pack(pady=5)


def button_clicked():
    return button


# Creating a button with specified options
button = tk.Button(root, 
                   text="IZIET", 
                   command=root.destroy,
                   activebackground="#a5d4b6", ##zaļa
                   activeforeground="#ff79a9", ## kad uzspiež, burti tādā krāsā
                   anchor="center",
                   bg="#a5d4b6",
                   fg="#545454", #tumši pelēks
                   font=("Arial", 12, "bold"),
                   height=1,
                   highlightthickness=2,
                   width=5,
                    )

button.pack(padx=25, pady=20)

root.mainloop()
