import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class SimpleCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Karichev")

        # Устанавливаем фиксированный размер окна
        self.root.geometry("300x250")
        self.root.resizable(False, False)

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        self.create_simple_calculator_tab()
        self.create_checkbox_tab()
        self.create_text_editor_tab()

        self.style = ttk.Style()
        self.style.configure("TNotebook.Tab", font=('Helvetica', 12))
        self.style.configure("TButton", font=('Helvetica', 12))
        self.style.configure("TLabel", font=('Helvetica', 12))

    def create_simple_calculator_tab(self):
        tab1 = ttk.Frame(self.notebook)
        self.notebook.add(tab1, text='Calculator')

        self.num1_entry = tk.Entry(tab1, font=('Helvetica', 14))
        self.num1_entry.pack(pady=5, padx=20, fill='x')

        self.operation_var = tk.StringVar(value='+')
        self.operation_menu = ttk.OptionMenu(tab1, self.operation_var, '+', '+', '-', '*', '/')
        self.operation_menu.pack(pady=5, padx=20, fill='x')

        self.num2_entry = tk.Entry(tab1, font=('Helvetica', 14))
        self.num2_entry.pack(pady=5, padx=20, fill='x')

        self.calculate_button = tk.Button(tab1, text='Calculate', command=self.calculate, font=('Helvetica', 14))
        self.calculate_button.pack(pady=5, padx=20, fill='x')

        self.result_label = tk.Label(tab1, text='', font=('Helvetica', 14))
        self.result_label.pack(pady=5, padx=20, fill='x')

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2

            self.result_label.config(text=f'Result: {result}')
        except ValueError:
            self.result_label.config(text='Enter valid numbers')

    def create_checkbox_tab(self):
        tab2 = ttk.Frame(self.notebook)
        self.notebook.add(tab2, text='Checkboxes')

        self.checkbox_vars = [tk.BooleanVar() for _ in range(3)]
        self.checkboxes = []

        for i, var in enumerate(self.checkbox_vars):
            checkbox = tk.Checkbutton(tab2, text=f'Variant {i+1}', variable=var, font=('Helvetica', 14))
            checkbox.pack(pady=10, anchor='center')
            self.checkboxes.append(checkbox)

        self.submit_button = tk.Button(tab2, text='Send', command=self.show_selection, font=('Helvetica', 14))
        self.submit_button.pack(pady=10, anchor='center')

    def show_selection(self):
        selected = [i+1 for i, var in enumerate(self.checkbox_vars) if var.get()]
        if selected:
            messagebox.showinfo('Choice', f'You have selected option(s): {", ".join(map(str, selected))}')
        else:
            messagebox.showinfo('Choice', 'You havent chosen anything')

    def create_text_editor_tab(self):
        tab3 = ttk.Frame(self.notebook)
        self.notebook.add(tab3, text='Text editor')

        self.text_area = tk.Text(tab3, wrap='word', font=('Helvetica', 14))
        self.text_area.pack(expand=True, fill='both', pady=10)

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='Open', command=self.open_file)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculatorApp(root)
    root.mainloop()
