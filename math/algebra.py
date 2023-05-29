import tkinter as tk
from algebra_builder import create_elements


def create_scrollable_window():
    root = tk.Tk()
    root.title("Ratio Calculator")
    root.geometry("800x600")

    def create_scrollable_window(event):
        canvas.yview_scroll(-int(event.delta/120), "units")

    # Create a Canvas widget
    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Scrollbar widget
    scrollbar = tk.Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the Canvas to use the Scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a Frame inside the Canvas to hold the content
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)

    # Add some content to the Frame (Example: Labels)
    create_elements(frame)

    # Configure the Canvas scroll region
    frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Bind the scroll wheel event to the canvas
    canvas.bind_all("<MouseWheel>", create_scrollable_window)

    root.mainloop()

create_scrollable_window()