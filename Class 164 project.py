from tkinter import*
from tkinter import filedialog
from PIL import ImageTk, Image
root= Tk()
root.geometry("600x600")
label= Label(root, highlightthickness= 5)
label.place(relx=0.5,rely=0.5,anchor=CENTER)
img_path=""
def openfile():
    global img_path
    img_path= filedialog.askopenfilename(title="Open Text File", filetypes= [("image files", "*.jpg *.gif *.png *.jpeg")])
    img1= Image.open(img_path)
    img2= ImageTk.PhotoImage(img1)
    label["image"]=img2
    img2.close()
def rotateimage():
    global img_path
    image1= Image.open(img_path)
    img= ImageTk.PhotoImage(image1.rotate(180))
    label["image"]= img
    img.close()
button= Button(root, text= "openimage", command= openfile)
button.place(relx=0.5, rely=0.1, anchor=CENTER)

button2= Button(root, text= "rotateimage", command= rotateimage)
button2.place(relx=0.5, rely=0.8, anchor=CENTER)
root.mainloop()