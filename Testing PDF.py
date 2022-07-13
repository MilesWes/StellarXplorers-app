import PyPDF2
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.tix import Select
import PyPDF2

#create file object variable
#opening method will be rb
pdffileobj=open('STLX-VIII-QR3-Team-Scores','rb')
 
#create reader variable that will read the pdffileobj
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
 
#This will store the number of pages of this pdf file
x=pdfreader.numPages
 
#create a variable that will select the selected number of pages
pageobj=pdfreader.getPage(x+1)
 
#(x+1) because python indentation starts with 0.
#create text variable which will store all text datafrom pdf file
text=pageobj.extractText()
 
#save the extracted data from pdf to a txt file
#we will use file handling here
#dont forget to put r before you put the file path
#go to the file location copy the path by right clicking on the file
#click properties and copy the location path and paste it here.
#put "\\your_txtfilename"
file1=open(r"C:\Users\wesle\Downloads\Coding\\1.txt","a")
file1.writelines(text)

"""
def open_file():
    Open a file for editing.
    filepath = askopenfilename(
        filetypes=[("PDF Files", "*.pdf"), ("Text Files", "*.txt"),("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:

        text = input_file.read()
        txt_edit.insert(tk.END, text)
    Select.title(f"Simple Text Editor - {filepath}")


def convertPDF():
    filepath = askopenfilename(
        filetypes=[("PDF Files", "*.pdf"), ("Text Files", "*.txt"),("All Files", "*.*")]
    pdffileobj=open('1.pdf','rb')
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    x=pdfreader.numPages
    text=pageobj.extractText()
    file1=open(filepath,"a")
    file1.writelines(text)
    
"""


