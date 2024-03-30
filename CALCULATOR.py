import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.display = tk.Entry(self, width=15, font=('Helvetica', 20), borderwidth=5, relief=tk.SUNKEN, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('Neg', 5, 1), ('$', 5, 2), ('@', 5, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, padx=20, pady=20, font=('Helvetica', 14), command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Configure column and row weights
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        current = self.display.get()

        if value == '=':
            try:
                result = eval(current)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")

        elif value == 'C':
            self.display.delete(0, tk.END)

        elif value == 'Neg':
            if current.startswith('-'):
                self.display.delete(0)
            else:
                self.display.insert(0, '-')

        elif value == '$':
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "$$$$C.$R.$E.$A.$M.$$$$")

        elif value == '@':
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "wwwwwwwwwwwwwwwwebsite")

        else:
            self.display.insert(tk.END, value)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
