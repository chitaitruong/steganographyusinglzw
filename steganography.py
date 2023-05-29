import subprocess
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfilename
from tkinter import messagebox
import sys

root = Tk()  # create root window
root.title("Group02 Steganography")  # title of the GUI window
root.geometry("400x300")
root.config(bg="skyblue")
def embed():
    image_url = ""
    text_url = ""
    password = ""
    file_name1 = StringVar()
    file_name2 = StringVar()
    passw_var = StringVar()
    info_var = StringVar()
    newWindow = Toplevel(root)
    newWindow.config(bg = "skyblue")
    def open_image_file():
        file = askopenfile(parent=newWindow, mode ='r', filetypes =[('Image file', '*.bmp *.jpeg'), ('Audio file', '*.au *wav')])
        if file is not None:
            image_url = file.name
            file_name1.set(image_url)
    def open_text_file():
        file = askopenfile(parent=newWindow, mode ='r', filetypes =[('Text file', '*.txt')])
        if file is not None:
            text_url = file.name
            file_name2.set(text_url)
    # sets the title of the
    # Toplevel widget
    def center_screen():
        """ gets the coordinates of the center of the screen """
        global screen_height, screen_width, x_cordinate, y_cordinate
        window_width = 500
        window_height = 200
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
            # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        newWindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    center_screen()
    def submit():
        password = passw_var.get()
        text_url = file_name2.get()
        image_url = file_name1.get()
        if len(text_url)>0 and len(image_url)>0 and len(password)>0:
            # Nen tin can dau su dung LZW
            y = subprocess.run([f'./main -E -i {text_url}'], capture_output=True, shell=True)
            print(y.stdout.decode())
            # Giau tin da nen vao file anh
            out_url = ""
            if 'bmp' in file_name1.get():
                out_url = 'out.bmp'
            elif 'jpeg' in file_name1.get():
                out_url = 'out.jpeg'
            elif 'au' in file_name1.get():
                out_url = 'out.au'
            elif 'wav' in file_name1.get():
                out_url = 'out.wav'
            x = subprocess.run([f'steghide embed -cf {image_url} -sf {out_url}  -ef temp.txt -f -p {password}'], capture_output=True, shell=True)
            code = x.returncode
            if not code:
                messagebox.showinfo(parent = newWindow, title="Success", message = f"done embeded into {out_url}")
            else:
                messagebox.showinfo(parent = newWindow, title="Error", message = x.stderr.decode())
                return 1
            cmd = ""
            if 'linux' in sys.platform:
                cmd = 'rm -rf temp.txt'
            else:
                cmd = 'del temp.txt'
            z = subprocess.run([cmd], capture_output=True, shell=True)
            print(z.stdout.decode())
        else:
            messagebox.showinfo(parent = newWindow, title="Missing", message = "Missing data")
        # sets the geometry of toplevel
    newWindow.geometry("500x200")
    newWindow.resizable(0,0)
    # A Label widget to show in toplevel
    lb1 = Label(newWindow,
          textvariable = file_name1, bg= "skyblue")
    btn1 = Button(newWindow, text = 'Open File', command = open_image_file, width=10)
    # lb_info = Label(newWindow,
    #       textvariable = info_var, bg= "skyblue")
    lb2 = Label(newWindow,
          textvariable = file_name2, bg= "skyblue")
    btn2 = Button(newWindow, text = 'Open Text', command = open_text_file, width=10)
    # creating a label for password
    passw_label = Label(newWindow, text = 'Password', font = ('calibre',10,'bold'), bg= "skyblue")
    
    # creating a entry for password
    passw_entry= Entry(newWindow, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    
    # creating a button using the widget
    # Button that will call the submit function
    sub_btn= Button(newWindow,text = 'Submit', command = submit)
    btn1.grid(row=0,column=0)
    lb1.grid(row=0,column=1)
    #lb_info.grid(row=1,column=0)
    btn2.grid(row=1,column=0)
    lb2.grid(row=1,column=1)
    passw_label.grid(row=2,column=0)
    passw_entry.grid(row=2,column=1)
    sub_btn.grid(row=3,column=1)
def extract():
    image_url = ""
    password = ""
    file_name1 = StringVar()
    passw_var = StringVar()
    newWindow = Toplevel(root)
    newWindow.config(bg = "skyblue")
    def open_image_file():
        file = askopenfile(parent=newWindow, mode ='r', filetypes =[('Image file', '*.bmp *.jpeg'),('Audio file', '*.au *.wav')])
        if file is not None:
            image_url = file.name
            file_name1.set(image_url)
    # def open_text_file():
    #     file = askopenfile(parent=newWindow, mode ='r', filetypes =[('Text file', '*.txt')])
    #     if file is not None:
    #         text_url = file.name
    #         file_name2.set(text_url)
    # sets the title of the
    # Toplevel widget
    def center_screen():
        """ gets the coordinates of the center of the screen """
        global screen_height, screen_width, x_cordinate, y_cordinate
        window_width = 500
        window_height = 200
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
            # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        newWindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    center_screen()
    def submit():
        password = passw_var.get()
        image_url = file_name1.get()
        if len(image_url)>0 and len(password)>0:
            # Giai tin da duoc nen tu anh
            y = subprocess.run([f'steghide extract -sf {image_url} -xf temp.txt -f -p {password}'], capture_output=True, shell=True)
            code = y.returncode
            if code:
                messagebox.showinfo(parent = newWindow, title="Error", message = y.stderr.decode())
                return 1
            # Giai nen tin
            x = subprocess.run([f'./main -D -i temp.txt -o out.txt'], capture_output=True, shell=True)
            messagebox.showinfo(parent = newWindow, title="Success", message = 'wrote extracted data to "out.txt"')
            z = subprocess.run(['rm -rf temp.txt'], capture_output=True, shell=True)
            print(z.stdout.decode())
        else:
            messagebox.showinfo(parent = newWindow, title="Missing", message = "Missing data")
        
    # sets the geometry of toplevel
    newWindow.geometry("500x200")
    newWindow.resizable(0,0)
    # A Label widget to show in toplevel
    lb1 = Label(newWindow,
          textvariable = file_name1, bg= "skyblue")
    btn1 = Button(newWindow, text = 'Open File', command = open_image_file, width=10)
    # lb2 = Label(newWindow,
    #       textvariable = file_name2)
    # btn2 = Button(newWindow, text = 'Open Text', command = open_text_file, width=10)
    # creating a label for password
    passw_label = Label(newWindow, text = 'Password', font = ('calibre',10,'bold'), bg= "skyblue")
    
    # creating a entry for password
    passw_entry= Entry(newWindow, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    
    # creating a button using the widget
    # Button that will call the submit function
    sub_btn= Button(newWindow,text = 'Submit', command = submit)
    btn1.grid(row=0,column=0)
    lb1.grid(row=0,column=1)
    # btn2.grid(row=1,column=0)
    # lb2.grid(row=1,column=1)
    passw_label.grid(row=1,column=0)
    passw_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)

#x = subprocess.run(['ls -la'], capture_output=True, shell=True)
# Create left and right frames
left_frame = Frame(root, width=200, height=250, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=200, height=300, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)
# Create frames and labels in left_frame
#Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

# load image to be "edited"
image = PhotoImage(file="index.png")
original_image = image.subsample(3,3)  # resize image using subsample
#Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)
Button(left_frame, text="Embed file", command=embed).grid(row=0, column=0, padx=5, pady=5)
Button(left_frame, text="Extract file", command=extract).grid(row=1, column=0, padx=5, pady=5)
Button(left_frame, text="Exit", command=root.destroy).grid(row=2, column=0, padx=5, pady=5)
# Display image in right_frame
Label(right_frame, image=image).grid(row=0,column=0, padx=5, pady=5)
Label(right_frame, text="Developed by Group02").grid(row=1, column=0, padx=5, pady=5)

root.resizable(0,0)
root.mainloop()
