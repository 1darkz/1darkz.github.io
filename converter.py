import tkinter as tk
from tkinter import ttk
import customtkinter as ctk




class CurrencyConverterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("300x150")
        
        # Create labels for input and output values
        self.lbl_brl = tk.Label(self, text="BRL:")
        self.lbl_usd = tk.Label(self, text="USD:")
        self.lbl_brl.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.lbl_usd.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        # Create entry fields for input and output values
        self.entry_brl = ctk.CTkEntry(self, font=("Arial", 12), justify="center", )
        self.entry_usd = ctk.CTkEntry(self, font=("Arial", 12), justify="center", )
        self.entry_brl.grid(row=0, column=1, padx=5, pady=5)
        self.entry_usd.grid(row=1, column=1, padx=5, pady=5)
        
        # Create buttons for currency conversion
        self.btn_brl_to_usd = tk.Button(self, text="BRL to USD", command=self.convert_brl_to_usd)
        self.btn_usd_to_brl = tk.Button(self, text="USD to BRL", command=self.convert_usd_to_brl)
        self.btn_brl_to_usd.grid(row=2, column=0, padx=5, pady=5)
        self.btn_usd_to_brl.grid(row=2, column=1, padx=5, pady=5)
        
    def convert_brl_to_usd(self):
        brl = float(self.entry_brl.get())
        usd = brl / 5.51 # exchange rate as of 2023-02-28
        self.entry_usd.delete(0, tk.END)
        self.entry_usd.insert(0, "{:.2f}".format(usd))
        
    def convert_usd_to_brl(self):
        usd = float(self.entry_usd.get())
        brl = usd * 5.51 # exchange rate as of 2023-02-28
        self.entry_brl.delete(0, tk.END)
        self.entry_brl.insert(0, "{:.2f}".format(brl))

if __name__ == "__main__":
    app = CurrencyConverterGUI()
    app.mainloop()
