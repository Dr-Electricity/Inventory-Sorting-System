import tkinter as tk

items = {
    "Pencil Boxes" : 0,
    "Paper Boxes" : 0,
    "Eraser Boxes" : 0,
    "Sharpeners" : 0,
    "Color Boxes" : 0,
    "Books" : 0,
    "Notebooks" : 0,
    "Markers" : 0,
    "Pen Boxes" : 0
}

window = tk.Tk()
window.geometry("650x400")
window.title("Inventory Management System")

pencilBoxesLabel = tk.Label(window,text=0,font= ("Open sans", "20"), height=1)
paperBoxesLabel = tk.Label(window,text=0,font= ("Open sans", "20"), height=1)
eraserBoxesLabel = tk.Label(window,text=0,font= ("Open sans", "20"), height=1)
sharpenersLabel = tk.Label(window,text=0,font= ("Open sans", "20"), height=1)
colorBoxesLabel = tk.Label(window,text=0,font= ("Open sans", "20"), height=1)
booksLabel = tk.Label(window,text=0,font= ("Open sans", "20"), height=1)
notebooksLabel = tk.Label(window,text=0,font= ("Open sans", "20"), height=1)
markersLabel = tk.Label(window,text=0,font= ("Open sans", "20"), height=1)
penBoxesLabel = tk.Label(window,text=0,font= ("Open sans", "20"), height=1)

infoLabel = tk.Label(window, text = "Enter a number (Integer)", font= ("Open sans", "12"))

entry = tk.Entry(window, font= ("Open sans", "12"))

def pencilBoxesFunction():
    try:  
        items["Pencil Boxes"] += int(entry.get())
        if items["Pencil Boxes"] < 0:
            items["Pencil Boxes"] = 0
        pencilBoxesLabel.config(text = items["Pencil Boxes"])
    except:
       pass
    finally:
        entry.delete(0, tk.END) 
    
def eraserBoxesFunction():
    try:
        items["Eraser Boxes"] += int(entry.get())
        if items["Eraser Boxes"] < 0:
            items["Eraser Boxes"] = 0
        eraserBoxesLabel.config(text = items["Eraser Boxes"])
    except:
       pass
    finally:
        entry.delete(0, tk.END) 

def sharpenersFunction():
    try:
        items["Sharpeners"] += int(entry.get())
        if items["Sharpeners"] < 0:
            items["Sharpeners"] = 0
        sharpenersLabel.config(text = items["Sharpeners"])
    except:
       pass
    finally:
        entry.delete(0, tk.END)

def penBoxesFunction():
    try:
        items["Pen Boxes"] += int(entry.get())
        if items["Pen Boxes"] < 0:
            items["Pen Boxes"] = 0
        penBoxesLabel.config(text = items["Pen Boxes"])
    except:
       pass
    finally:
        entry.delete(0, tk.END) 

def paperBoxesFunction(): 
    try:
        items["Paper Boxes"] += int(entry.get())
        if items["Paper Boxes"] < 0:
            items["Paper Boxes"] = 0
        paperBoxesLabel.config(text = items["Paper Boxes"])
    except:
       pass
    finally:
        entry.delete(0, tk.END) 

def colorBoxesFunction():
    try:
        items["Color Boxes"] += int(entry.get())
        if items["Color Boxes"] < 0:
            items["Color Boxes"] = 0 
        colorBoxesLabel.config(text = items["Color Boxes"])
    except:
       pass
    finally:
        entry.delete(0, tk.END) 

def booksFunction():
    try:
        items["Books"] += int(entry.get())
        if items["Books"] < 0:
            items["Books"] = 0 
        booksLabel.config(text = items["Books"])
    except:
       pass
    finally:
        entry.delete(0, tk.END) 

def notebooksFunction():
    try:
        items["Notebooks"] += int(entry.get())
        if items["Notebooks"] < 0:
            items["Notebooks"] = 0 
        notebooksLabel.config(text = items["Notebooks"])
    except:
       pass
    finally:
        entry.delete(0, tk.END) 

def markersFunction():
    try:
        items["Markers"] += int(entry.get())
        if items["Markers"] < 0:
            items["Markers"] = 0 
        markersLabel.config(text = items["Markers"])
    except:
       pass
    finally:
        entry.delete(0, tk.END)

def pencilBoxesFunction2():
    try:  
        items["Pencil Boxes"] = int(entry.get())
        if items["Pencil Boxes"] < 0:
            items["Pencil Boxes"] = 0
        pencilBoxesLabel.config(text = items["Pencil Boxes"])
    except:
       pass
    finally:
        entry.delete(0, tk.END)

def eraserBoxesFunction2():
    try:  
        items["Eraser Boxes"] = int(entry.get())
        if items["Eraser Boxes"] < 0:
            items["Eraser Boxes"] = 0
        eraserBoxesLabel.config(text = items["Eraser Boxes"])
    except:
       pass
    finally:
        entry.delete(0, tk.END)
def sharpenersFunction2():
    try:  
        items["Sharpeners"] = int(entry.get())
        if items["Sharpeners"] < 0:
            items["Sharpeners"] = 0
        sharpenersLabel.config(text = items["Sharpeners"])
    except:
       pass
    finally:
        entry.delete(0, tk.END)

def penBoxesFunction2():
    try:  
        items["Pen Boxes"] = int(entry.get())
        if items["Pen Boxes"] < 0:
            items["Pen Boxes"] = 0
        penBoxesLabel.config(text = items["Pen Boxes"])
    except:
       pass
    finally:
        entry.delete(0, tk.END)

def paperBoxesFunction2():
    try:  
        items["Paper Boxes"] = int(entry.get())
        if items["Paper Boxes"] < 0:
            items["Paper Boxes"] = 0
        paperBoxesLabel.config(text = items["Paper Boxes"])
    except:
       pass
    finally:
        entry.delete(0, tk.END)

def colorBoxesFunction2():
    try:  
        items["Color Boxes"] = int(entry.get())
        if items["Color Boxes"] < 0:
            items["Color Boxes"] = 0
        colorBoxesLabel.config(text = items["Color Boxes"])
    except:
       pass
    finally:
        entry.delete(0, tk.END)

def booksFunction2():
    try:  
        items["Books"] = int(entry.get())
        if items["Books"] < 0:
            items["Books"] = 0
        booksLabel.config(text = items["Books"])
    except:
       pass
    finally:
        entry.delete(0, tk.END)        

def notebooksFunction2():
    try:  
        items["Notebooks"] = int(entry.get())
        if items["Notebooks"] < 0:
            items["Notebooks"] = 0
        notebooksLabel.config(text = items["Notebooks"])
    except:
       pass
    finally:
        entry.delete(0, tk.END)

def markersFunction2():
    try:  
        items["Markers"] = int(entry.get())
        if items["Markers"] < 0:
            items["Markers"] = 0
        markersLabel.config(text = items["Markers"])
    except:
       pass
    finally:
        entry.delete(0, tk.END)        

def exportToTXT():
    file = open("export.txt", "w")
    file.flush()
    file.write(f"Pencil Boxes:  {items['Pencil Boxes']} \n Eraser Boxes: {items['Eraser Boxes']} \n Sharpeners:  {items['Sharpeners']} \n Pen Boxes:  {items['Pen Boxes']} \n Paper Boxes:  {items['Paper Boxes']} \n Color Boxes:  {items['Color Boxes']} \n Books:  {items['Books']} \n Notebooks:  {items['Notebooks']} \n Markers:  {items['Markers']} ")
    return

pencilBoxesButton = tk.Button(window,text="Change pencil boxes amount", height=1, width= 22, command= pencilBoxesFunction)
eraserBoxesButton = tk.Button(window,text="Change eraser boxes amount", height=1, width= 22, command= eraserBoxesFunction) 
sharpenersButton = tk.Button(window,text="Change sharpeners amount", height=1, width= 22, command= sharpenersFunction) 
penBoxesButton = tk.Button(window,text="Change pen boxes amount", height=1, width= 22, command= penBoxesFunction) 
paperBoxesButton = tk.Button(window,text="Change paper boxes amount", height=1, width= 22, command= paperBoxesFunction) 
colorBoxesButton = tk.Button(window,text="Change color boxes amount", height=1, width= 22, command= colorBoxesFunction) 
booksButton = tk.Button(window,text="Change books amount", height=1, width= 22, command= booksFunction) 
notebooksButton = tk.Button(window,text="Change notebooks amount", height=1, width= 22, command= notebooksFunction) 
markersButton = tk.Button(window,text="Change markers amount", height=1, width= 22, command= markersFunction)

pencilBoxesButton2 = tk.Button(window,text="Set pencil boxes amount", height=1, width= 22, command= pencilBoxesFunction2)
eraserBoxesButton2 = tk.Button(window,text="Set eraser boxes amount", height=1, width= 22, command= eraserBoxesFunction2)
sharpenersButton2 = tk.Button(window,text="Set sharpeners amount", height=1, width= 22, command= sharpenersFunction2)
penBoxesButton2 = tk.Button(window,text="Set pen boxes amount", height=1, width= 22, command= penBoxesFunction2)
paperBoxesButton2 = tk.Button(window,text="Set paper boxes amount", height=1, width= 22, command= paperBoxesFunction2)
colorBoxesButton2 = tk.Button(window,text="Set color boxes amount", height=1, width= 22, command= colorBoxesFunction2)
booksButton2 = tk.Button(window,text="Set books amount", height=1, width= 22, command= booksFunction2)
notebooksButton2 = tk.Button(window,text="Set notebooks amount", height=1, width= 22, command= notebooksFunction2)
markersButton2 = tk.Button(window,text="Set markers amount", height=1, width= 22, command= markersFunction2)

exportButton = tk.Button(window, bg= "#00FF00",text="Export to\nText File", height=2, width= 8, command= exportToTXT)

pencilBoxesLabel.grid(column=1,row=2,padx=5)
eraserBoxesLabel.grid(column=1,row=3,padx=5)
sharpenersLabel.grid(column=1,row=4,padx=5)
penBoxesLabel.grid(column=1,row=5,padx=5)
paperBoxesLabel.grid(column=1,row=6,padx=5)
colorBoxesLabel.grid(column=1,row=7,padx=5)
booksLabel.grid(column=1,row=8,padx=5)
notebooksLabel.grid(column=1,row=9,padx=5)
markersLabel.grid(column=1,row=10,padx=5)

pencilBoxesButton.grid(column=3,row=2)
eraserBoxesButton.grid(column=3,row=3)
sharpenersButton.grid(column=3,row=4)
penBoxesButton.grid(column=3,row=5)
paperBoxesButton.grid(column=3,row=6)
colorBoxesButton.grid(column=3,row=7)
booksButton.grid(column=3,row=8)
notebooksButton.grid(column=3,row=9)
markersButton.grid(column=3,row=10)

pencilBoxesButton2.grid(column=4,row=2, padx=15)
eraserBoxesButton2.grid(column=4,row=3, padx=15)
sharpenersButton2.grid(column=4,row=4, padx=15)
penBoxesButton2.grid(column=4,row=5, padx=15)
paperBoxesButton2.grid(column=4,row=6, padx=15)
colorBoxesButton2.grid(column=4,row=7, padx=15)
booksButton2.grid(column=4,row=8, padx=15)
notebooksButton2.grid(column=4,row=9, padx=15)
markersButton2.grid(column=4,row=10, padx=15)

exportButton.grid(column=7, row=2)
infoLabel.grid(column=5, row=5)
entry.grid(column=5,row=6)

window.mainloop()
