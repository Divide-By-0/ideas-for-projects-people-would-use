import tkinter as tk
from sympy import symbols, integrate, diff, simplify, sympify, SympifyError, log, sin, cos, tan, asin, acos, atan, exp


x = symbols('x')


def parse_expression(expression):
    try: 
        return simplify(sympify(expression, {"exp": exp, "sin": sin, "cos": cos, "tan": tan, "asin": asin, "acos": acos, "atan": atan, "log": log}))
    except SympifyError:
       
        replaced_expression = expression.replace('e', 'exp')
        replaced_expression = replaced_expression.replace('sin', 'sin')
        replaced_expression = replaced_expression.replace('cos', 'cos')
        replaced_expression = replaced_expression.replace('tan', 'tan')
        replaced_expression = replaced_expression.replace('asin', 'asin')
        replaced_expression = replaced_expression.replace('acos', 'acos')
        replaced_expression = replaced_expression.replace('atan', 'atan')
        replaced_expression = replaced_expression.replace('log', 'log')
        return simplify(sympify(replaced_expression, {"exp": exp, "sin": sin, "cos": cos, "tan": tan, "asin": asin, "acos": acos, "atan": atan, "log": log}))

def solve_integral(expression):
    integral = integrate(expression, x)
    return integral

def solve_derivative(expression):
    derivative = diff(expression, x)
    return derivative 


def button1_click():
    user_input = input_entry.get()
    try:
       
        parsed_expression = parse_expression(user_input)
        print("Parsed Expression:", parsed_expression)

        integral = solve_integral(parsed_expression)
        print("Integral Result:", integral)

        
        print("Result Label Text:", "Integral: " + str(integral) if integral is not None else "Invalid input. Please enter a valid input")

       
        result_label.config(text="Integral: " + str(integral) if integral is not None else "Invalid input. Please enter a valid input")

    except (SympifyError, ValueError):
        result_label.config(text="Invalid input. Please enter a valid input")

def button2_click():
    user_input = input_entry.get()
    try:
        
        parsed_expression = parse_expression(user_input)
        print("Parsed Expression:", parsed_expression)

       
        derivative = solve_derivative(parsed_expression)
        print("Derivative Result:", derivative)

       
        print("Result Label Text:", "Derivative: " + str(derivative) if derivative is not None else "Invalid input. Please enter a valid input")

        result_label.config(text="Derivative: " + str(derivative) if derivative is not None else "Invalid input. Please enter a valid input")

    except (SympifyError, ValueError):
        result_label.config(text="Invalid input. Please enter a valid input")
        

win = tk.Tk()
win.title("FuncSol")
win.state("zoomed")
win.config(bg="black", cursor="arrow")


label1 = tk.Label(win, text = "Calculus")
label2 = tk.Label(win, text= "Reached a point of confusion and inflexion? We've got you covered!")
label3 = tk.Label(win, text = "Enter the problem here:-")

button1 = tk.Button(win, text = "> Integrate", command=button1_click)
button2 = tk.Button(win, text = "> Differentiate", command=button2_click)
back = tk.Button(win, text = "> Exit", command=win.destroy)

label1.config(font = ("Times", 40), bg = "black", fg = "white")
label2.config(font = ("Helvicta", 20), bg = "white", fg = "black")
label3.config(font = ("Arial", 20), bg = "white", fg = "black")


button1.config(font=("Arial", 12, "bold"), bg = "gold", fg = "maroon")
button2.config(font=("Arial", 12, "bold", ), bg = "gold", fg = "maroon")
back.config(font = ("Arial", 12, "bold"), bg = "grey", fg ="black")


label1.grid(row = 0, column = 0, columnspan = 3, pady = 20, sticky = "n ")
label2.grid(row = 1, column = 0, columnspan = 3, pady = 10)
label3.grid(row = 4, column = 0, pady = 10, padx = 1, sticky = "w")

button1.grid(row= 10, pady = 20, stick ="w")
button2.grid(row = 20, pady= 20, stick = "w")
back.grid(row= 30, pady=19, stick = "w")


win.columnconfigure(0, weight =1)


input_entry = tk.Entry(win, width = 50, text="here", font = ('Arial', 18))
input_entry.grid(row = 5, pady = 10, sticky = "w")


result_label = tk.Label(win, text = "", font=("Arial", 16, "bold"), height = 2, width=50)
result_label.config(bg = "white")
result_label.grid(row=25, column = 0, pady = 10, sticky = "w")


win.mainloop()
