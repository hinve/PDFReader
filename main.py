import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
root.title("PDF Reader")
canvas.grid(columnspan=3, rowspan=3)

# Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Instructions
instructions = tk.Label(root, text="Insert the PDF file")
instructions.grid(columnspan=3, column=0, row=1)

# Text box
text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
text_box.grid(column=1, row=3)

# Open file function
def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    i = 0
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        while i < len(read_pdf.pages):
            page = read_pdf.pages[i]
            i += 1
        page_content = page.extract_text()
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        browse_text.set("Browse")

# Browse button
browse_text = tk.StringVar()
browse_bttn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), font="Raleway", background="#E52A2A", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_bttn.grid(column=1, row=2)

root.mainloop()