import tkinter as tk
from tkinter import font

# Create variables
dummy_question = "The number of mangoes to the number of pears in a box was 5:8. After 45 pears was sold and 38 mangoes were added, the ratio became 6:5. How many mangoes were there in the end?"
ratio1 = {
    "u":0,
    "x":0,
    "p":0,
    'op':'+',
    "u2":0,
    "x2":0,
    "p2":0,

}
ratio2 = {
    "u":0,
    "x":0,
    "p":0,
    'op':'+',
    "u2":0,
    "x2":0,
    "p2":0,
}


# GUI functions


def apply_multiplier(eq_num):
    pass


def substitute_equations():
    pass


def create_elements(root):

    def on_option_change1(*args):
        print("Selected option:", selected_option1.get())
        on_op1_change()

    def on_option_change2(*args):
        print("Selected option:", selected_option2.get())
        on_op2_change()

    def generate_equations():
        try:

            # Build equatuion
            # Equation = u + x = p
            # e.g.      5u + 38 = 6p
            # e.g.      7u - 34 = 5p
            eq1 = "{}u {} {} = {}p".format(ratio1['u'],ratio1['op'],ratio1['x'],ratio1['p'])
            eq2 = "{}u {} {} = {}p".format(ratio2['u'],ratio2['op'],ratio2['x'],ratio2['p'])

            # Show equation
            operation1_placeholder.config(text=eq1)
            operation2_placeholder.config(text=eq2)

        except:
            pass

    def subtract_equations():
        p1 = ratio1['p2']
        p2 = ratio2['p2']
        x1 = ratio1['x2']
        x2 = ratio2['x2']

        if ratio1['op'] == '-':
            x1 *= -1
        if ratio2['op'] == '-':
            x2 *= -1
        
        final_p = max(p1,p2) - min(p1,p2)
        final_value = max(x1,x2) - min(x1,x2)

        operation_result.config(text=f"{final_p}p = {final_value}")


    def equate_equations():
        eq = "{}u {} {} = {}u {} {}".format(ratio1['u2'],ratio1['op'],ratio1['x2'],ratio2['u2'],ratio2['op'],ratio2['x2'])
        operation_result.config(text=eq)

    def on_r1u_change(*args):
        try:
            num = int(r1u.get())
            ratio1['u'] = num
            
        except Exception as e:
            pass
        print(r1u.get())
    def on_r1x_change(*args):
        try:
            num = int(r1x.get())
            if num >= 0:
                ratio1['op'] = '+'
            else:
                ratio1['op'] = '-'
            ratio1['x'] = abs(num)
            
        except Exception as e:
            pass
        print(r1x.get())
    def on_r1p_change(*args):
        try:
            num = int(r1p.get())
            ratio1['p'] = num
            
        except Exception as e:
            pass
        print(r1p.get())
    def on_r2u_change(*args):
        try:
            num = int(r2u.get())
            ratio2['u'] = num
            
        except Exception as e:
            pass
        print(r2u.get())
    def on_r2x_change(*args):
        try:
            num = int(r2x.get())
            if num >= 0:
                ratio2['op'] = '+'
            else:
                ratio2['op'] = '-'
            ratio2['x'] = abs(num)
            
        except Exception as e:
            pass
        print(r2x.get())
    def on_r2p_change(*args):
        try:
            num = int(r2p.get())
            ratio2['p'] = num
            
        except Exception as e:
            pass
        print(r2p.get())
    def on_op1_change(*args):
        try:
            num = int(op1.get())

            # if selected_option1.get() is multiply
            if selected_option1.get() == "x":
                u = ratio1['u'] * num
                x = ratio1['x'] * num
                p = ratio1['p'] * num
            else:
                u = ratio1['u'] / num
                x = ratio1['x'] / num
                p = ratio1['p'] / num
                
            ratio1['u2'] = u
            ratio1['x2'] = x
            ratio1['p2'] = p

            eq1 = "{}u {} {} = {}p".format(u,ratio1['op'],x,p)
            operation1_placeholder.config(text=eq1)
                
        except:
            pass
    def on_op2_change(*args):
        try:
            num = int(op2.get())
            if selected_option2.get() == "x":
                u = ratio2['u'] * num
                x = ratio2['x'] * num
                p = ratio2['p'] * num
                
            else:
                u = ratio2['u'] / num
                x = ratio2['x'] / num
                p = ratio2['p'] / num
                
            ratio2['u2'] = u
            ratio2['x2'] = x
            ratio2['p2'] = p
            
            eq2 = "{}u {} {} = {}p".format(u,ratio2['op'],x,p)
            operation2_placeholder.config(text=eq2)


        except:
            pass
    
    # Create a StringVar to associate with the Entry
    r1u = tk.StringVar()
    r1x = tk.StringVar()
    r1p = tk.StringVar()
    r2u = tk.StringVar()
    r2x = tk.StringVar()
    r2p = tk.StringVar()
    op1 = tk.StringVar()
    op2 = tk.StringVar()

    # Header font
    header_font = font.Font(family="Arial", size=12, underline=True)
    title_font = font.Font(family="Arial", size=18)

    # Define the variable to hold the selected option
    selected_option1 = tk.StringVar(root)
    selected_option1.trace('w', on_option_change1)

    selected_option2 = tk.StringVar(root)
    selected_option2.trace('w', on_option_change2)

    options = ("x", "÷")

    # Create elements
    title = tk.Label(root, text="Ratio Calculator", font=title_font)
    description = tk.Label(root, text="This is a ratio calculator used to help me and my \n friends in calculating the ratio in difficult math questions")

    question_label = tk.Label(root, text="Input your question here")
    question = tk.Text(root, height=4, width=50, wrap="word")
    question.insert(tk.END, dummy_question)
    before_label = tk.Label(root, text="Before", font=header_font)
    instruction1 = tk.Label(root, text="Write down the names \n for the ratio mentioned")
    name1_label = tk.Label(root, text="Name 1")
    name1_entry = tk.Entry(root)
    colon1 = tk.Label(root, text=":")
    name2_label = tk.Label(root, text="Name 2")
    name2_entry = tk.Entry(root)

    title.grid(row=0,column=0,columnspan=4)
    description.grid(row=1,column=0,columnspan=4)

    question_label.grid(row=2,column=0,columnspan=4, pady=(20,0))
    question.grid(row=3,column=0,columnspan=4)


    before_label.grid(row=4,column=0,columnspan=4, pady=(10,10))
    name1_label.grid(row=5,column=1)
    name2_label.grid(row=5,column=3)

    instruction1.grid(row=6,column=0,padx=15)
    name1_entry.grid(row=6,column=1)
    colon1.grid(row=6,column=2)
    name2_entry.grid(row=6,column=3)

    instruction2 = tk.Label(root, text="Write down the initial \n ratios of the 2 people")
    before_ratio1_label = tk.Label(root, text="Before ratio 1")
    before_ratio1_entry = tk.Entry(root, textvariable=r1u)
    colon2 = tk.Label(root, text=":")
    before_ratio2_label = tk.Label(root, text="Before ratio 2")
    before_ratio2_entry = tk.Entry(root, textvariable=r2u)

    before_ratio1_label.grid(row=7,column=1)
    before_ratio2_label.grid(row=7,column=3)

    instruction2.grid(row=8,column=0,padx=15)
    before_ratio1_entry.grid(row=8,column=1)
    colon2.grid(row=8,column=2)
    before_ratio2_entry.grid(row=8,column=3)

    instruction3 = tk.Label(root, text="Write down the changes that \n happen to the 2 people")
    change1_label = tk.Label(root, text="Change 1")
    change1_entry = tk.Entry(root, textvariable=r1x)
    colon3 = tk.Label(root, text=":")
    change2_label = tk.Label(root, text="Change 2")
    change2_entry = tk.Entry(root, textvariable=r2x)

    change1_label.grid(row=9,column=1)
    change2_label.grid(row=9,column=3)

    instruction3.grid(row=10,column=0,padx=15)
    change1_entry.grid(row=10,column=1)
    colon3.grid(row=10,column=2)
    change2_entry.grid(row=10,column=3)

    after_label = tk.Label(root, text="After", font=header_font)
    after_label.grid(row=11,column=0,columnspan=4, pady=(10,10))

    instruction4 = tk.Label(root, text="Write down the new ratio")
    after_ratio1_label = tk.Label(root, text="After ratio 1")
    after_ratio1_entry = tk.Entry(root, textvariable=r1p)
    colon3 = tk.Label(root, text=":")
    after_ratio2_label = tk.Label(root, text="After ratio 2")
    after_ratio2_entry = tk.Entry(root, textvariable=r2p)
    generate_button = tk.Button(root, text="Generate", command=generate_equations)

    after_ratio1_label.grid(row=12,column=1)
    after_ratio2_label.grid(row=12,column=3)

    instruction4.grid(row=13,column=0,padx=15)
    after_ratio1_entry.grid(row=13,column=1)
    colon3.grid(row=13,column=2)
    after_ratio2_entry.grid(row=13,column=3)
    generate_button.grid(row=14,column=0, pady=(10,10))


    equations_label = tk.Label(root, text="Equations", font=header_font)

    operation1_placeholder = tk.Label(root, text="(equation 1)")
    operation2_placeholder = tk.Label(root, text="(equation 2)")
    operation1_label = tk.Label(root, text="Operation for equation 1")
    operation2_label = tk.Label(root, text="Operation for equation 2")
    dropdown1 = tk.OptionMenu(root, selected_option1, *options)
    dropdown2 = tk.OptionMenu(root, selected_option2, *options)
    operation1_entry = tk.Entry(root, textvariable=op1)
    operation2_entry = tk.Entry(root, textvariable=op2)


    equations_label.grid(row=15,column=0,columnspan=4, pady=(10,10))

    operation1_placeholder.grid(row=16,column=0)
    operation1_label.grid(row=17,column=0)
    dropdown1.grid(row=17,column=1)
    selected_option1.set(options[0])
    operation1_entry.grid(row=17,column=2)

    operation2_placeholder.grid(row=18,column=0)
    operation2_label.grid(row=19,column=0)
    dropdown2.grid(row=19,column=1)
    selected_option2.set(options[0])
    operation2_entry.grid(row=19,column=2)

    operations_label = tk.Label(root, text="Operations", font=header_font)
    operation_result = tk.Label(root, text="(operation)")
    subtract_button = tk.Button(root, text="Subtract", command=subtract_equations)
    equate_button = tk.Button(root, text="Equate", command=equate_equations)

    operations_label.grid(row=20,column=0,columnspan=4, pady=(10,10))
    operation_result.grid(row=21,column=0)
    subtract_button.grid(row=21,column=1)
    equate_button.grid(row=21,column=2)

    r1u.trace("w", on_r1u_change)
    r1x.trace("w", on_r1x_change)
    r1p.trace("w", on_r1p_change)
    r2u.trace("w", on_r2u_change)
    r2x.trace("w", on_r2x_change)
    r2p.trace("w", on_r2p_change)
    op1.trace("w", on_op1_change)
    op2.trace("w", on_op2_change)
    

# root.mainloop()
