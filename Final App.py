import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.tix import Select
import PyPDF2
import plotly.graph_objects as go


"""
Opens a file for editing, interprets the text (for StellarXplorers), separates teams and scores
then runs the rest of the code (projecting the boxplot)
"""
def open_file():
    output=''
    list_output = []
    contain = []
    Scores = []
    Names = []
    filepath = askopenfilename(
        filetypes=[("PDF Files", "*.pdf"), ("Text Files", "*.txt"),("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, mode="rb") as input_file:
        pdfReader = PyPDF2.PdfFileReader(input_file)
        count = pdfReader.numPages
        #lists all contents of all pages
        for i in range(count):
            page = pdfReader.getPage(i)
            output += page.extractText()
            list_output += output.split()
        for element in list_output:
            if "STL" in element:
                contain.append(element)
            elif "." in element:
                contain.append(element)
    Select.title(f"Simple Text Editor - {filepath}")
    convert(contain, Scores, Names)
    Boxplot(Scores, Names)


def convert(list, nums, text): #Separates the strings and nums (every other element starting at index 1) and converts nums to floats
    for element in list:
        if list.index(element)%2 != 0:
            float(list[list.index(element)])
            nums.append(float(element))
        else:
            text.append(element)

def Boxplot(Data, Names): #creates the box plot
    fig = go.Figure()
    fig.add_trace(go.Box(
        x=Data, 
        name="All Points", 
        jitter=0.3, 
        pointpos=-1.8, 
        boxpoints='all', 
        marker_color='rgb(9,56,125)', 
        line_color='rgb(9,56,125)', 
        hovertext=Names ))

    fig.update_layout(title_text="StellarXplorer's Round Scores")
    fig.show(renderer='browser')
            

events=[] #main window - creates & formats
Select=tk.Tk()
Select.title("Interactable Diagram")
Select.rowconfigure(0, minsize=500, weight=1)
Select.columnconfigure(0, minsize=500, weight=1)
frm_buttons=tk.Frame(Select, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons,text="Open", width=25, height=5, command=open_file)
Lbl_Advance = tk.Label(
    text="Select 'OPEN' to get started!",
    width = 15,
    height= 5,
    bg="#00b5e2",
    fg = "Black"
)
Lbl_Advance.grid(row=0, column=0, sticky='ew', padx=150, pady=100)
btn_open.grid(row=1, column=0, sticky="ew", padx=100, pady=100)
frm_buttons.grid(row=0, column=0, sticky="ns")


Select.mainloop()












