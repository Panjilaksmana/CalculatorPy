import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.resizable(False, False)

        # create the display
        self.display = tk.Entry(self.master, width=20, font=('Arial', 16), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # create the buttons
        self.buttons = {}
        button_text = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '.', '0', '=', '+', 'C', 'Del']
        button_color = ['#C5E1A5', '#C5E1A5', '#C5E1A5', '#FF8A65', '#C5E1A5', '#C5E1A5', '#C5E1A5', '#FF8A65',
                        '#C5E1A5', '#C5E1A5', '#C5E1A5', '#FF8A65', '#C5E1A5', '#C5E1A5', '#FF8A65', '#C5E1A5',
                        '#EF9A9A', '#666666', '#666666']
        positions = [(i, j) for i in range(1, 6) for j in range(4)]
        for position, text, color in zip(positions, button_text, button_color):
            if text == '=':
                self.buttons[text] = tk.Button(self.master, text=text, width=4, height=2, bg='#ff0000', fg='#ff0000',
                                               font=('Arial', 16, 'bold'),
                                               command=lambda text=text: self.button_click(text))
            elif text == 'C':
                self.buttons[text] = tk.Button(self.master, text=text, width=4, height=2, bg='#E0E0E0', fg='#000000',
                                               font=('Arial', 16), command=lambda text=text: self.button_click(text))
            elif text == 'Del':
                self.buttons[text] = tk.Button(self.master, text=text, width=4, height=2, bg='#E0E0E0', fg='#000000',
                                               font=('Arial', 16), command=lambda text=text: self.button_click(text))
            else:
                self.buttons[text] = tk.Button(self.master, text=text, width=4, height=2, bg=color, fg='#000000',
                                               font=('Arial', 16), command=lambda text=text: self.button_click(text))
            self.buttons[text].grid(row=position[0], column=position[1], padx=5, pady=5)

    def button_click(self, text):
        if text == 'C':
            self.display.delete(0, tk.END)
        elif text == 'Del':
            self.display.delete(len(self.display.get()) - 1, tk.END)
        elif text == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Error')
        else:
            self.display.insert(tk.END, text)


if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()