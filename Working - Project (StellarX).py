from operator import contains
from pickletools import stringnl
import string
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.tix import Select
import PyPDF2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go


def open_file():
    output=''
    list_output = []
    contain = []
    Scores = []
    Names = []
    """Open a file for editing."""
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
    fig = go.Figure(data=[go.Box(x=Data, hovertext=Names, name='All Scores', boxpoints='all', jitter= 0.2, pointpos =-1.5)])
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












