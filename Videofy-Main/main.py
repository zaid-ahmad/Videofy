import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkVideoPlayer import TkinterVideo
from ctypes import windll
from PIL import ImageTk, Image

windll.shcore.SetProcessDpiAwareness(1)
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysql@admin123',
    database = 'videofy'
)
cursor = mydb.cursor()

userData = {}
l = []
d = {}

pathAccSettings = 'C:/Users/zaidd/OneDrive/Desktop/Projects/Videofy/src/Videofy-Main/accountSettings'
pathHomeLogin = 'C:/Users/zaidd/OneDrive/Desktop/Projects/Videofy/src/Videofy-Main/homeLoggedIn'
pathHomeLogout = 'C:/Users/zaidd/OneDrive/Desktop/Projects/Videofy/src/Videofy-Main/homeLoggedOut'
pathLogin = 'C:/Users/zaidd/OneDrive/Desktop/Projects/Videofy/src/Videofy-Main/login'
pathSignup = 'C:/Users/zaidd/OneDrive/Desktop/Projects/Videofy/src/Videofy-Main/signup'
pathUploadVid = 'C:/Users/zaidd/OneDrive/Desktop/Projects/Videofy/src/Videofy-Main/uploadVideo'
pathVideoSettings = 'C:/Users/zaidd/OneDrive/Desktop/Projects/Videofy/src/Videofy-Main/videoSettings'
pathVideoPlayback = 'C:/Users/zaidd/OneDrive/Desktop/Projects/Videofy/src/Videofy-Main/videoPlayback'
pathVideoEdit = 'C:/Users/zaidd/OneDrive/Desktop/Projects/Videofy/src/Videofy-Main/videoEdit'

def btn_clicked():
    print("Button Clicked")

def signupWindow():
    def passWindow():
        window.destroy()
        loginWindow()

    window = Tk()

    def check():
        cursor.execute('select * from userdata where email="%s"'.format(entry0.get()))
        result = cursor.fetchall()
        if entry0.get() == "" or entry1.get() == "" or entry2.get() == "" or entry3.get() == "":
            messagebox.showerror(title="Error", message="Please fill the entire form") 
        elif not '@' in entry0.get():
            messagebox.showerror(title='Error', message="Invalid e-mail address")
        elif entry3.get() != entry1.get():
            messagebox.showerror(title='Error', message="Passwords do not match")
        elif result != []:
            messagebox.showinfo(title='Sign Up Error', message='Account with that email already exists')
        else:
            userData["name"] = entry2.get()
            userData["email"] = entry0.get()
            userData["pwd"] = entry3.get()
            messagebox.showinfo(title='Sucess', message=f'Welcome to Videofy {entry2.get()}')
            window.destroy()
            storeUserData()
            
    
    window.geometry("1200x900")
    window.title('Videofy | Signup')
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 900,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"{pathSignup}/background.png")
    background = canvas.create_image(
        595.5, 457.5,
        image=background_img)

    img0 = PhotoImage(file = f"{pathSignup}/img0.png")
    signin = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        fg = '#324259',
        command = check,
        cursor="left_ptr")

    signin.place(
        x = 952, y = 611,
        width = 152,
        height = 59)

    entry0_img = PhotoImage(file = f"{pathSignup}/img_textBox0.png")
    entry0_bg = canvas.create_image(
        1027.5, 372.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#e3e3e3",
        highlightthickness = 0)

    entry0.place(
        x = 918.0, y = 348,
        width = 219.0,
        height = 47)

    entry1_img = PhotoImage(file = f"{pathSignup}/img_textBox1.png")
    entry1_bg = canvas.create_image(
        1027.5, 554.5,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#e3e3e3",
        highlightthickness = 0,
        show='*')

    entry1.place(
        x = 918.0, y = 530,
        width = 219.0,
        height = 47)

    entry2_img = PhotoImage(file = f"{pathSignup}/img_textBox2.png")
    entry2_bg = canvas.create_image(
        1025.5, 281.5,
        image = entry2_img)

    entry2 = Entry(
        bd = 0,
        bg = "#e3e3e3",
        highlightthickness = 0)

    entry2.place(
        x = 916.0, y = 257,
        width = 219.0,
        height = 47)

    entry3_img = PhotoImage(file = f"{pathSignup}/img_textBox3.png")
    entry3_bg = canvas.create_image(
        1027.5, 463.5,
        image = entry3_img)

    entry3 = Entry(
        bd = 0,
        bg = "#e3e3e3",
        highlightthickness = 0,
        show="*")

    entry3.place(
        x = 918.0, y = 439,
        width = 219.0,
        height = 47)

    img1 = PhotoImage(file = f"{pathSignup}/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        fg = '#324259',
        highlightthickness = 0,
        command = passWindow,
        cursor="left_ptr")

    b1.place(
        x = 1064, y = 726,
        width = 101,
        height = 22)

    window.resizable(False, False)
    window.mainloop()

def loginWindow():
    window4 = Tk()
    def passWindow():
        window4.destroy()
        signupWindow()

    def loginUser():
        # Check if email is registered. If it is, then  
        # Check if password is correct. If it is, then
        # Redirect user to  logged in home page.

        # entry0= email
        # entr1 = password
        
        cursor.execute('select * from userdata where email=(%s)', (entry0.get(),))
        result = cursor.fetchall()

        # Check if email is registered.
        if result != []:
            cursor.execute('select * from userdata where email=(%s)', (entry0.get(),))
            result = cursor.fetchall()
            if result != []:
                userData["name"] = result[0][1]
                userData["email"] = result[0][0]
                userData["pwd"] = result[0][2]
                window4.destroy()
                homeLoggedInWindow()
            else:
                # Password incorrect
                messagebox.showerror(title='Invalid Login', message='Email/Password is incorrect')
        else:
            # User does not exist
            messagebox.showerror(title='Invalid Login', message='Email/Password is incorrect')

    window4.geometry("1200x900")
    window4.title('Videofy | Login')
    window4.configure(bg = "#ffffff")
    canvas = Canvas(
        window4,
        bg = "#ffffff",
        height = 900,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"{pathLogin}/background.png")
    background = canvas.create_image(
        600.0, 452.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"{pathLogin}/img_textBox0.png")
    entry0_bg = canvas.create_image(
        599.5, 361.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#c8dbe9",
        highlightthickness = 0)

    entry0.place(
        x = 490.0, y = 337,
        width = 219.0,
        height = 47)

    entry1_img = PhotoImage(file = f"{pathLogin}/img_textBox1.png")
    entry1_bg = canvas.create_image(
        599.5, 461.5,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        show="*",
        bg = "#c8dbe9",
        highlightthickness = 0)

    entry1.place(
        x = 490.0, y = 437,
        width = 219.0,
        height = 47)

    img0 = PhotoImage(file = f"{pathLogin}/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = passWindow,
        relief = "flat")

    b0.place(
        x = 624, y = 616,
        width = 91,
        height = 19)

    img1 = PhotoImage(file = f"{pathLogin}/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = loginUser,
        relief = "flat")

    b1.place(
        x = 529, y = 525,
        width = 141,
        height = 52)

    window4.resizable(False, False)
    window4.mainloop()

vidPath = ''
thumbPath = ''
def uploadVideoWindow(): 
    def getVideoFile():
        vidfilePath = filedialog.askopenfilename(initialdir='C:\\', title='Select the video you want to upload')
        global vidPath
        vidPath = vidfilePath
        vidName = vidfilePath.split('/')[-1]
        b3.config(text=vidName)
    
    def getThumbFile():
        thumbfilePath = filedialog.askopenfilename(initialdir='C:\\', title='Select thumbnail of the video')
        global thumbPath
        thumbPath = thumbfilePath
        thumbName = thumbfilePath.split('/')[-1]
        b4.config(text=thumbName)

    def uploadVideo():
        cursor.execute('SELECT id FROM videodata')
        videoCount = cursor.fetchall().pop()[0]
        if thumbPath == '':
            messagebox.showinfo(title='Upload the thumbnail', message="You can't upload a video without a thumbnail.")
        if vidPath == '':
            messagebox.showinfo(title='You really thought', message="Bro you gotta add a video before publishing a video smh 🤦‍♂️")

        likes = 0
        dislikes = 0
        title = entry0.get()
        description = entry1.get()
        tags = entry2.get()
        email = userData["email"]
        name = userData["name"]

        try:
            cursor.execute(f'INSERT INTO videodata VALUES("{email}", "{title}", "{thumbPath}", "{vidPath}", {likes}, {dislikes}, "{description}", "{name}", {videoCount+1})')
            mydb.commit()
            messagebox.showinfo(title='Success', message='Video uploaded successfully!')
            videoCount += 1 
        except:
            messagebox.showerror(title='Whoops', message='Some error occured, please try again later.')

    window5 = Toplevel()
    window5.geometry("1200x900")
    window5.title('Videofy | Upload Video')
    window5.configure(bg = "#ffffff")
    canvas = Canvas(
        window5,
        bg = "#ffffff",
        height = 900,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    img0 = PhotoImage(file = f"{pathUploadVid}/img0.png")
    b0 = Button(
        window5,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = getThumbFile,
        relief = "flat")

    b0.place(
        x = 757, y = 333,
        width = 204,
        height = 35)

    img1 = PhotoImage(file = f"{pathUploadVid}/img1.png")
    b1 = Button(
        window5,
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = getVideoFile,
        relief = "flat")

    b1.place(
        x = 757, y = 487,
        width = 204,
        height = 35)

    img2 = PhotoImage(file = f"{pathUploadVid}/img2.png")
    b2 = Button(
        window5,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = uploadVideo,
        relief = "flat")

    b2.place(
        x = 205, y = 731,
        width = 790,
        height = 49)

    entry0_img = PhotoImage(file = f"{pathUploadVid}/img_textBox0.png")
    entry0_bg = canvas.create_image(
        456.5, 325.5,
        image = entry0_img)

    entry0 = Entry(
        window5,
        bd = 0,
        bg = "#e3e3e3",
        highlightthickness = 0)

    entry0.place(
        x = 197, y = 305,
        width = 519,
        height = 39)

    entry1_img = PhotoImage(file = f"{pathUploadVid}/img_textBox1.png")
    entry1_bg = canvas.create_image(
        456.5, 460.5,
        image = entry1_img)

    entry1 = Entry(
        window5,
        bd = 0,
        bg = "#e3e3e3",
        highlightthickness = 0)

    entry1.place(
        x = 197, y = 394,
        width = 519,
        height = 131)

    entry2_img = PhotoImage(file = f"{pathUploadVid}/img_textBox2.png")
    entry2_bg = canvas.create_image(
        456.0, 598.0,
        image = entry2_img)

    entry2 = Entry(
        window5,
        bd = 0,
        bg = "#e3e3e3",
        highlightthickness = 0)

    entry2.place(
        x = 196, y = 578,
        width = 520,
        height = 38)

    img3 = PhotoImage(file = f"{pathUploadVid}/img3.png")
    b3 = Label(
        window5,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat",
         bg='#fff')

    b3.place(
        x = 756, y = 551,
        width = 95,
        height = 19)

    img4 = PhotoImage(file = f"{pathUploadVid}/img4.png")
    b4 = Label(
        window5,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat",
        bg='#fff')

    b4.place(
        x = 755, y = 396,
        width = 100,
        height = 19)

    background_img = PhotoImage(file = f"{pathUploadVid}/background.png")
    background = canvas.create_image(
        600.0, 311.5,
        image=background_img)

    window5.resizable(False, False)
    window5.mainloop()

def videoSettingsWindow():
    window6 = Toplevel()

    window6.geometry("1200x900")
    window6.title('Videofy | Video Settings')
    window6.configure(bg = "#ffffff")
    canvas = Canvas(
        window6,
        bg = "#ffffff",
        height = 900,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    img0 = PhotoImage(file = f"{pathVideoSettings}/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 778, y = 471,
        width = 204,
        height = 30)

    img1 = PhotoImage(file = f"{pathVideoSettings}/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b1.place(
        x = 192, y = 638,
        width = 790,
        height = 49)

    background_img = PhotoImage(file = f"{pathVideoSettings}/background.png")
    background = canvas.create_image(
        600.0, 287.5,
        image=background_img)

    img2 = PhotoImage(file = f"{pathVideoSettings}/img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b2.place(
        x = 1046, y = 16,
        width = 51,
        height = 52)

    entry0_img = PhotoImage(file = f"{pathVideoSettings}/img_textBox0.png")
    entry0_bg = canvas.create_image(
        456.5, 277.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#e3e3e3",
        highlightthickness = 0)

    entry0.place(
        x = 197, y = 257,
        width = 519,
        height = 39)

    entry1_img = PhotoImage(file = f"{pathVideoSettings}/img_textBox1.png")
    entry1_bg = canvas.create_image(
        455.5, 413.5,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#e3e3e3",
        highlightthickness = 0)

    entry1.place(
        x = 195, y = 341,
        width = 521,
        height = 143)

    entry2_img = PhotoImage(file = f"{pathVideoSettings}/img_textBox2.png")
    entry2_bg = canvas.create_image(
        456.0, 550.0,
        image = entry2_img)

    entry2 = Entry(
        bd = 0,
        bg = "#e3e3e3",
        highlightthickness = 0)

    entry2.place(
        x = 196, y = 530,
        width = 520,
        height = 38)

    window6.resizable(False, False)
    window6.mainloop()

def logout():
    global userData
    userData = {}
    l[0].destroy()
    homeLoggedOutWindow()

newThumbnail = ''
def accountSettingsWindow():
    def updateUserInfo():
        newPwd = entry1.get()
        newName = entry2.get()

        if userData["pwd"] != newPwd:
            cursor.execute("UPDATA userdata SET password=%s WHERE email=%s", (newPwd, userData["email"]))
            mydb.commit()   
            messagebox.showinfo(title="Update Successful", message=f"Password changed successfully")
        else:
            cursor.execute("UPDATE userdata SET name=%s WHERE email=%s", (newName, userData["email"]))
            mydb.commit()   
            messagebox.showinfo(title="Update Successful", message=f"Name changed successfully")

    def videoEdit(vidId):
        cursor.execute('SELECT title, description, thumbnail FROM videodata WHERE (id=%s AND email=%s)', (vidId, userData["email"]))
        stuff = cursor.fetchall()
        def getThumbPath():
            global newThumbnail
            global stuff
            thumbFilePath = filedialog.askopenfilename(initialdir=f'C:\\', title='Select new thumbnail')
            newThumbnail += thumbFilePath

            print(newThumbnail)

        def saveVideoData():
            try:
                if newThumbnail != '':
                    cursor.execute("UPDATE videodata SET title=%s, description=%s, thumbnail=%s WHERE (id=%s AND email=%s)", (entry0.get(), entry1.get(), newThumbnail, vidId, userData["email"]))
                    mydb.commit()
                    messagebox.showinfo(title='Video Changes', message='Updated sucessfully!')
                else:
                    cursor.execute("UPDATE videodata SET title=%s, description=%s WHERE (id=%s AND email=%s)", (entry0.get(), entry1.get(), vidId, userData["email"]))
                    mydb.commit()
                    messagebox.showinfo(title='Video Changes', message='Updated sucessfully!')
            except:
                messagebox.showerror(title='Whoops...', message='Some error occured')

        window = Toplevel()
        window.geometry("800x800")
        window.configure(bg = "#ffffff")
        canvas = Canvas(
            window,
            bg = "#ffffff",
            height = 800,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        img0 = PhotoImage(file = f"{pathVideoEdit}/img0.png")
        b0 = Button(
            window,
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = saveVideoData,
            relief = "flat")

        b0.place(
            x = 328, y = 690,
            width = 141,
            height = 49)

        entry0_img = PhotoImage(file = f"{pathVideoEdit}/img_textBox0.png")
        entry0_bg = canvas.create_image(
            254.5, 291.0,
            image = entry0_img)

        entry0 = Entry(
            window,
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        entry0.place(
            x = 140, y = 271,
            width = 229,
            height = 38)
        
        entry0.insert(0, stuff[0][0])

        entry1_img = PhotoImage(file = f"{pathVideoEdit}/img_textBox1.png")
        entry1_bg = canvas.create_image(
            399.0, 499.5,
            image = entry1_img)

        entry1 = Entry(
            window,
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        entry1.place(
            x = 140, y = 370,
            width = 518,
            height = 257)

        entry1.insert(0, stuff[0][1])

        background_img = PhotoImage(file = f"{pathVideoEdit}/background.png")
        background = canvas.create_image(
            600.0, 318.0,
            image=background_img)

        img1 = PhotoImage(file = f"{pathVideoEdit}/img1.png")
        b1 = Button(
            window,
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = getThumbPath,
            relief = "flat")

        b1.place(
            x = 416, y = 266,
            width = 239,
            height = 50)

        window.resizable(False, False)
        window.mainloop()


    window7 = Toplevel()

    window7.geometry("1200x900")
    window7.configure(bg = "#ffffff")
    canvas = Canvas(
        window7,
        bg = "#ffffff",
        height = 900,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    img0 = PhotoImage(file = f"{pathAccSettings}/img0.png")
    b0 = Button(
        window7,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = updateUserInfo,
        relief = "flat")

    b0.place(
        x = 666, y = 326,
        width = 141,
        height = 49)

    entry0_img = PhotoImage(file = f"{pathAccSettings}/img_textBox0.png")
    entry0_bg = canvas.create_image(
        460.5, 254.0,
        image = entry0_img)

    entry0 = Label(
        window7,
        text=userData["email"],
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0.place(
        x = 346, y = 234,
        width = 229,
        height = 38)

    entry1_img = PhotoImage(file = f"{pathAccSettings}/img_textBox1.png")
    entry1_bg = canvas.create_image(
        460.5, 351.0,
        image = entry1_img)

    entry1 = Entry(
        window7,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry1.place(
        x = 346, y = 331,
        width = 229,
        height = 38)

    entry1.insert(0, userData["pwd"])

    entry2_img = PhotoImage(file = f"{pathAccSettings}/img_textBox2.png")
    entry2_bg = canvas.create_image(
        736.5, 256.0,
        image = entry2_img)

    entry2 = Entry(
        window7,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry2.place(
        x = 622, y = 236,
        width = 229,
        height = 38)

    entry2.insert(0, userData["name"])

    background_img = PhotoImage(file = f"{pathAccSettings}/background.png")
    background = canvas.create_image(
        600.0, 244.5,
        image=background_img)

    img3 = PhotoImage(file = f"{pathAccSettings}/img3.png")
    b3 = Button(
        window7,
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = logout,
        relief = "flat")

    b3.place(
        x = 1015, y = 18,
        width = 138,
        height = 45)    

    main_frame = Frame(window7, height=200, bg="#fff")
    main_frame.pack(side="bottom", fill="x")

    my_canvas = Canvas(main_frame, height=400, bg="#fff")#, width=650, height=273)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas, bg="#fff")

    my_canvas.create_window((0,0), window=second_frame, anchor='nw')

    r = 0

    cursor.execute("SELECT * FROM videodata WHERE email=%s", (userData["email"],))
    userVideos = cursor.fetchall()
    thumbnail_paths = []
    titles = []
    likes = []
    dislikes = []
    ids = []

    edit_icon = f'{pathAccSettings}/img7.png'
    editBtn_image = Image.open(edit_icon)
    resize_edit = editBtn_image.resize((28, 28), Image.Resampling.LANCZOS)
    editBtn = ImageTk.PhotoImage(resize_edit)
 
    for j in range(len(userVideos)):
        thumbnail_paths.append(userVideos[j][2])
        titles.append(userVideos[j][1])
        likes.append(userVideos[j][4])
        dislikes.append(userVideos[j][5])
        ids.append(userVideos[j][8])

    imgs = []

    for i in range(len(userVideos)):
        image = Image.open(thumbnail_paths[i])
        resize_image = image.resize((220, 130), Image.Resampling.LANCZOS)
        x = ImageTk.PhotoImage(resize_image)
        imgs.append(x)
        b1 = Label(
            second_frame,
            image = imgs[-1],
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")
        b1.grid(
            column= 0, row = r+1, padx=500)

        b2 = Label(
            second_frame,
            text = titles[i],
            font=('Arial', 14),
            bg='#fff',
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")

        b2.grid(
            column = 0, row = r, sticky=W, padx=500, pady=5)

        b5 = Label(
            second_frame,
            text= str(likes[i]) + ' (Likes)',
            font=('Arial', 14),
            bg='#fff',
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")

        b5.grid(
            column = 0, row = r+2, sticky=W, padx=500)

        b6 = Label(
            second_frame,
            text = str(dislikes[i]) + ' (Dislikes)',
            font=('Arial', 14),
            bg='#fff',
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")

        b6.grid(
            column = 0, row = r+3, sticky=W, padx=500)

        b7 = Button(
            second_frame,
            image = editBtn,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda m=ids[i]: videoEdit(m),
            relief = "flat")

        b7.grid(
            column= 0, row = r+1, sticky=NW, padx=500)

        r += 10

    window7.resizable(False, False)
    window7.mainloop()

def homeLoggedInWindow():
    window3 = Tk()
    global l
    if len(l) != 0:
        l = []
        l.append(window3)
    else:
        l.append(window3)
    
    def closeWindow():
        window3.destroy()
        loginWindow()

    def searchVideo(e):
        main_frame.destroy()
        search_query = entry0.get()

        cursor.execute("SELECT thumbnail, id, title, name, description FROM videodata WHERE title=%s", (search_query,))
        videos = cursor.fetchall() 

        th = Image.open(videos[0][0])
        r = th.resize((330, 220), Image.Resampling.LANCZOS)
        vidImage = ImageTk.PhotoImage(r)
        if videos != []:
            b2 = Button(
                image = vidImage,
                borderwidth = 0,
                highlightthickness = 0,
                command = lambda m=videos[0][1]: videoPlayback(m),
                relief = "flat")
            b2.image = vidImage

            b2.place(
                x = 189, y = 150,
                width = 306,
                height = 175)

            b3 = Label(
                text= videos[0][2],
                font=('Arial', 14),
                bg="#fff",
                anchor=W,
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")

            b3.place(
                x = 506, y = 149,
                width = 206,
                height = 30)

            b4 = Label(
                text= "Description: " + videos[0][4],
                font=('Arial', 10),
                bg="#fff",
                fg='#2C2C2C',
                anchor=W,
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")

            b4.place(
                x = 509, y = 180,
                width = 545,
                height = 60)

            b5 = Label(
                text = videos[0][3],
                borderwidth = 0,
                font=('Arial', 11),
                bg="#fff",
                fg="#1E1E1E",
                anchor=W,
                highlightthickness = 0,
                relief = "flat")

            b5.place(
                x = 509, y = 270,
                width = 96,
                height = 21)
        else:
            messagebox.showinfo(title='Whoops...', message='No videos exist with that title')

    window3.geometry("1200x900")
    window3.title(f'Videofy | Home (Logged in as { userData["name"] })')
    window3.configure(bg = "#ffffff")
    canvas = Canvas(
        window3,
        bg = "#ffffff",
        height = 900,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"{pathHomeLogin}/background.png")
    background = canvas.create_image(
        600.0, 41.5,
        image=background_img)

    img0 = PhotoImage(file = f"{pathHomeLogin}/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = uploadVideoWindow,
        relief = "flat")

    b0.place(
        x = 1012, y = 15,
        width = 69,
        height = 58)

    img1 = PhotoImage(file = f"{pathHomeLogin}/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = accountSettingsWindow,
        relief = "flat")

    b1.place(
        x = 1099, y = 21,
        width = 50,
        height = 50)

    entry0_img = PhotoImage(file = f"{pathHomeLogin}/img_textBox0.png")
    entry0_bg = canvas.create_image(
        679.0, 42.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#f1f2f6",
        highlightthickness = 0)

    entry0.place(
        x = 426, y = 18,
        width = 506,
        height = 46)

    entry0.bind('<Return>', searchVideo)
    main_frame = Frame(window3, bg="#fff")
    main_frame.pack(fill=BOTH, expand=1, pady=100)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas, bg="#fff")

    my_canvas.create_window((0,0), window=second_frame, anchor='nw')
    # THUMBNAIL GENERATOR
    cursor.execute("SELECT thumbnail FROM videodata")
    thumbnails = cursor.fetchall()
    cursor.execute("SELECT title FROM videodata")
    titles = cursor.fetchall()
    cursor.execute("SELECT name FROM videodata")
    names = cursor.fetchall()
    cursor.execute("SELECT id FROM videodata")
    ids = cursor.fetchall()
    list_of_paths = []
    for path in thumbnails:
        list_of_paths.append(path[0])
    
    x_coord = [42, 430, 819]
    y_coord = 135
    y_title_coord = 360
    y_name_coord = 390
    counter = 0
    x_counter = 0

    imgs = []
    videoIdCounter = 0

    for i in range(len(thumbnails)):
        image = Image.open(list_of_paths[i])
        resize_image = image.resize((330, 220), Image.Resampling.LANCZOS)
        x = ImageTk.PhotoImage(resize_image)
        imgs.append(x)
        t = Button(
            second_frame,
            image=imgs[-1],
            borderwidth = 0,
            command = lambda m=ids[i][0]: videoPlayback(m),
            highlightthickness = 0,
            relief = "flat")
        t.grid(column=x_coord[x_counter], row= y_coord, padx=32, pady=5)

        n = Label(
            second_frame,
            text=titles[i][0],
            bg='#fff',
            font=('Arial', 14)
        )
        n.grid(
            column=x_coord[x_counter], row=y_title_coord
        )
        t = Label(
            second_frame,
            text= names[i][0],
            bg='#fff',
            fg='#393939',
            font=('Helvetica', 11)
        )
        t.grid(
            column=x_coord[x_counter], row=y_name_coord
        )

        counter += 1
        x_counter += 1
        videoIdCounter += 1

        if counter%3 == 0:
            y_coord += 295
            y_title_coord += 295
            y_name_coord += 295
        
        if x_counter > 2:
            x_counter = 0


    window3.resizable(False, False)
    window3.mainloop()

def homeLoggedOutWindow():
    window8 = Tk()

    def passWindow():
        window8.destroy()
        loginWindow()

    def searchVideo(e):
        main_frame.destroy()
        search_query = entry0.get()

        cursor.execute("SELECT thumbnail, id, title, name, description FROM videodata WHERE title=%s", (search_query,))
        videos = cursor.fetchall() 

        th = Image.open(videos[0][0])
        r = th.resize((330, 220), Image.Resampling.LANCZOS)
        vidImage = ImageTk.PhotoImage(r)
        if videos != []:
            b2 = Button(
                image = vidImage,
                borderwidth = 0,
                highlightthickness = 0,
                command = lambda m=videos[0][1]: videoPlayback(m),
                relief = "flat")
            b2.image = vidImage

            b2.place(
                x = 189, y = 150,
                width = 306,
                height = 175)

            b3 = Label(
                text= videos[0][2],
                font=('Arial', 14),
                bg="#fff",
                anchor=W,
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")

            b3.place(
                x = 506, y = 149,
                width = 206,
                height = 30)

            b4 = Label(
                text= "Description: " + videos[0][4],
                font=('Arial', 10),
                bg="#fff",
                fg='#2C2C2C',
                anchor=W,
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")

            b4.place(
                x = 509, y = 180,
                width = 545,
                height = 60)

            b5 = Label(
                text = videos[0][3],
                borderwidth = 0,
                font=('Arial', 11),
                bg="#fff",
                fg="#1E1E1E",
                anchor=W,
                highlightthickness = 0,
                relief = "flat")

            b5.place(
                x = 509, y = 270,
                width = 96,
                height = 21)
        else:
            messagebox.showinfo(title='Whoops...', message='No videos exist with that title')

    window8.geometry("1200x900")
    window8.title('Hello! Welcome to Videofy')
    window8.configure(bg = "#ffffff")

    canvas = Canvas(
        window8,
        bg = "#ffffff",
        height = 900,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge",
        scrollregion=(0,0, 1000, 800))
    canvas.place(x=0, y=0)

    # UI Code
    background_img = PhotoImage(file = f"{pathHomeLogout}/background.png")
    background = canvas.create_image(
        600.0, 40,
        image=background_img)

    img0 = PhotoImage(file = f"{pathHomeLogout}/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = passWindow,
        relief = "flat")

    b0.place(
        x = 1021, y = 21,
        width = 113,
        height = 41)

    entry0_img = PhotoImage(file = f"{pathHomeLogout}/img_textBox0.png")
    entry0_bg = canvas.create_image(
        679.0, 42.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#f1f2f6",
        highlightthickness = 0)

    entry0.place(
        x = 426, y = 18,
        width = 506,
        height = 46)

    entry0.bind('<Return>', searchVideo)
    main_frame = Frame(window8, bg="#fff")
    main_frame.pack(fill=BOTH, expand=1, pady=100)

    my_canvas = Canvas(main_frame, bg="#fff")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas, bg="#fff")

    my_canvas.create_window((0,0), window=second_frame, anchor='nw')
    # THUMBNAIL GENERATOR
    cursor.execute("SELECT thumbnail FROM videodata")
    thumbnails = cursor.fetchall()
    cursor.execute("SELECT title FROM videodata")
    titles = cursor.fetchall()
    cursor.execute("SELECT name FROM videodata")
    names = cursor.fetchall()
    cursor.execute("SELECT id FROM videodata")
    ids = cursor.fetchall()
    list_of_paths = []
    for path in thumbnails:
        list_of_paths.append(path[0])
    x_coord = [42, 430, 819]
    y_coord = 135
    y_title_coord = 360
    y_name_coord = 390
    counter = 0
    x_counter = 0

    imgs = []

    for i in range(len(thumbnails)):
        image = Image.open(list_of_paths[i])
        resize_image = image.resize((330, 220), Image.Resampling.LANCZOS)
        x = ImageTk.PhotoImage(resize_image)
        imgs.append(x)
        t = Button(
            second_frame,
            image=imgs[-1],
            borderwidth = 0,
            command = lambda m=ids[i][0]: videoPlayback(m),
            highlightthickness = 0,
            relief = "flat")
        t.grid(column=x_coord[x_counter], row= y_coord, padx=32, pady=5)

        n = Label(
            second_frame,
            text=titles[i][0],
            bg='#fff',
            font=('Arial', 14)
        )
        n.grid(
            column=x_coord[x_counter], row=y_title_coord
        )
        t = Label(
            second_frame,
            text= names[i][0],
            bg='#fff',
            fg='#393939',
            font=('Helvetica', 11)
        )
        t.grid(
            column=x_coord[x_counter], row=y_name_coord
        )

        counter += 1
        x_counter += 1

        if counter%3 == 0:
            y_coord += 295
            y_title_coord += 295
            y_name_coord += 295
        
        if x_counter > 2:
            x_counter = 0
    window8.resizable(False, False)
    window8.mainloop()

def storeUserData():
    if len(userData) != 0:
        cursor.execute('insert into userdata values(%s, %s, %s)', (userData['email'], userData['name'], userData['pwd']))
        mydb.commit()
        homeLoggedInWindow()

likeUnlikeForLikes = 0
likeUnlikeForDislikes = 0
clickedLike = False
clickedDislike = False
def videoPlayback(i):
    videoPlayWindow = tk.Toplevel()

    videoPlayWindow.geometry("1200x900")
    videoPlayWindow.configure(bg = "#ffffff")

    cursor.execute('SELECT * FROM videodata WHERE id=%s', (i,))
    videodata = cursor.fetchall()

    videoTitle = videodata[0][1]
    likes = videodata[0][4]  
    dislikes = videodata[0][5]  
    filePath = videodata[0][3]
    description = videodata[0][6]
    name = videodata[0][7]

    videoPlayWindow.title(f'Playing "{videoTitle}"')
    ''' FIX THE LIKE UNLIKE PROBLEM (likeunlike global variable does not change) '''
    playImage = PhotoImage(file=f'{pathVideoPlayback}/play.png')
    def play_pause():
        """ pauses and plays """
        if vid_player.is_paused():
            vid_player.play()
            b5.configure(image=img5)

        else:
            vid_player.pause()
            b5.configure(image=playImage)
    
    def like():
        global likeUnlikeForLikes
        global clickedLike
        global clickedDislike
        if userData != {}:
            clickedLike = True
            likeUnlikeForLikes = likeUnlikeForLikes + 1
            if clickedDislike:
                b3.config(text=dislikes)
                cursor.execute('UPDATE videodata SET dislikes=%s WHERE id=%s', (dislikes, i))
                mydb.commit()
            if likeUnlikeForLikes == 1:
                b1.config(text=likes+1)
                cursor.execute('UPDATE videodata SET likes=%s WHERE id=%s', (likes+1, i))
                mydb.commit()
            else:
                b1.config(text=likes)
                cursor.execute('UPDATE videodata SET likes=%s WHERE id=%s', (likes, i))
                mydb.commit()
                likeUnlikeForLikes = 0
        else:
            messagebox.showinfo(title='Whoops...', message='You need to sign in to like or dislike')

    def dislike():
        global likeUnlikeForDislikes
        global clickedLike
        global clickedDislike
        if userData != {}:
            likeUnlikeForDislikes = likeUnlikeForDislikes + 1
            clickedDislike = True
            if clickedLike:
                b1.config(text=likes)
                cursor.execute('UPDATE videodata SET likes=%s WHERE id=%s', (likes, i))
                mydb.commit()

            if likeUnlikeForDislikes == 1:
                b3.config(text=dislikes+1)
                cursor.execute('UPDATE videodata SET dislikes=%s WHERE id=%s', (dislikes+1, i))
                mydb.commit()
            else:
                b3.config(text=dislikes)
                cursor.execute('UPDATE videodata SET dislikes=%s WHERE id=%s', (dislikes, i))
                mydb.commit()
                likeUnlikeForDislikes = 0
        else:
            messagebox.showinfo(title='Oh', message='You need to sign in to like or dislike')

    canvas = Canvas(
    videoPlayWindow,
    bg = "#ffffff",
    height = 900,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)

    vid_player = TkinterVideo(master=canvas)
    vid_player.load(filePath)
    vid_player.place(x=250, y=100, width=699, height=369)

    vid_player.play()

    img0 = PhotoImage(file = f"{pathVideoPlayback}/img0.png")
    b0 = Button(
        videoPlayWindow,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: like(),
        relief = "flat")

    b0.place(
        x = 51, y = 503,
        width = 36,
        height = 32)

    b1 = Label(
        videoPlayWindow,
        text=likes,
        bg='#fff',
        font=('Arial', 15),
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    b1.place(
        x = 56, y = 538,
        width = 26,
        height = 19)

    img2 = PhotoImage(file = f"{pathVideoPlayback}/img2.png")
    b2 = Button(
        videoPlayWindow,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = dislike,
        relief = "flat")

    b2.place(
        x = 99, y = 504,
        width = 36,
        height = 32)

    b3 = Label(
        videoPlayWindow,
        text=dislikes,
        bg='#fff',
        font=('Arial', 15),
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    b3.place(
        x = 104, y = 538,
        width = 26,
        height = 19)

    background_img = PhotoImage(file = f"{pathVideoPlayback}/background.png")
    background = canvas.create_image(
        600.0, 434.5,
        image=background_img)

    b4 = Label(
        videoPlayWindow,
        text=name,
        bg='#fff',
        font=('Arial', 15),
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    b4.place(
        x = 1039, y = 573,
        width = 140,
        height = 24)

    img5 = PhotoImage(file = f"{pathVideoPlayback}/img5.png")
    b5 = Button(
        videoPlayWindow,
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = play_pause,
        relief = "flat")

    b5.place(
        x = 551, y = 512,
        width = 100,
        height = 34)

    b6 = Label(
        videoPlayWindow,
        text=description,
        bg='#F1F2F6',
        font=('Arial', 15),
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    b6.place(
        x = 63, y = 624,
        width = 1000,
        height = 38)

    videoPlayWindow.resizable(False, False)
    videoPlayWindow.mainloop()
 
def main():
    homeLoggedOutWindow()

main()
