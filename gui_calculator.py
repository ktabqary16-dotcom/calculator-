    self.expression = ""
    self.memory = 0
    
    self.create_widgets()

def create_widgets(self):
    # Display
    self.display = tk.Entry(self.root, font=('Arial', 24), justify='right', 
                            bg='#ecf0f1', fg='#2c3e50', bd=10, relief=tk.FLAT)
    self.display.pack(fill=tk.BOTH, padx=10, pady=10, ipady=15)
    
    # Buttons frame
    buttons_frame = tk.Frame(self.root, bg='#2c3e50')
    buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Button layout
    buttons = [
        ['C', 'CE', '√', '/'],
        ['7', '8', '9', '*'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '+'],
        ['0', '.', '=', '^'],
        ['sin', 'cos', 'tan', 'log'],
        ['ln', 'abs', '(', ')'],
        ['M+', 'M-', 'MR', 'MC']
    ]
    
    for i, row in enumerate(buttons):
        for j, btn_text in enumerate(row):
            btn = tk.Button(buttons_frame, text=btn_text, font=('Arial', 12),
                            bg='#34495e', fg='white', activebackground='#2c3e50',
                            bd=0, padx=20, pady=15, cursor='hand2')
            btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
            btn.bind('<Button-1>', lambda e, text=btn_text: self.on_button_click(text))
    
    # Configure grid weights
    for i in range(len(buttons)):
        buttons_frame.grid_rowconfigure(i, weight=1)
    for j in range(4):
        buttons_frame.grid_columnconfigure(j, weight=1)

def on_button_click(self, text):
    if text == 'C':
        self.expression = ""
        self.update_display()
    elif text == 'CE':
        self.expression = self.expression[:-1]
        self.update_display()
    elif text == '=':
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.update_display()
        except:
            messagebox.showerror("Error", "Invalid expression!")
            self.expression = ""
            self.update_display()
    elif text == '√':
        self.expression += 'math.sqrt('
        self.update_display()
    elif text == '^':
        self.expression += '**'
        self.update_display()
    elif text == 'sin':
        self.expression += 'math.sin(math.radians('
        self.update_display()
    elif text == 'cos':
        self.expression += 'math.cos(math.radians('
        self.update_display()
    elif text == 'tan':
        self.expression += 'math.tan(math.radians('
        self.update_display()
    elif text == 'log':
        self.expression += 'math.log10('
        self.update_display()
    elif text == 'ln':
        self.expression += 'math.log('
        self.update_display()
    elif text == 'abs':
        self.expression += 'abs('
        self.update_display()
    elif text == 'M+':
        try:
            self.memory += float(eval(self.expression) if self.expression else 0)
            messagebox.showinfo("Memory", f"Memory: {self.memory}")
        except:
            messagebox.showerror("Error", "Invalid value!")
    elif text == 'M-':
        try:
            self.memory -= float(eval(self.expression) if self.expression else 0)
            messagebox.showinfo("Memory", f"Memory: {self.memory}")
        except:
            messagebox.showerror("Error", "Invalid value!")
    elif text == 'MR':
        self.expression += str(self.memory)
        self.update_display()
    elif text == 'MC':
        self.memory = 0
        messagebox.showinfo("Memory", "Memory cleared!")
    else:
        self.expression += text
        self.update_display()

def update_display(self):
    self.display.delete(0, tk.END)
    self.display.insert(0, self.expression)
