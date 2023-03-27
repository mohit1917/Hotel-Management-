# HEADER FILES
import cv2
from tkinter import *
import tkinter
import MySQLdb
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

from PIL.ImageTk import PhotoImage

db = MySQLdb.connect("localhost", "root", "", "hotel management")
cursor = db.cursor()


# for not closing window with upper close button
def disable_event():
    pass


# FOR RUN GUEST DETAIL BUTTON
# guest details button inside window code
#all login code inside this
class Close:
    pass

def select():
    def login():
        username = str(name12.get())
        password = str(password1.get())
        if (username == "mohit"):
            if (password == "4317"):
                f = tkinter.Toplevel()
                f.geometry("1317x750")
                f.configure(bg="#181a1b")
                f.resizable(0, 0)
                f.protocol("WM_DELETE_WINDOW", disable_event)

                # FOR DELETE.TE THE PARTICULAR DATA
                def dltprt():
                    db = MySQLdb.connect("localhost", "root", "", "hotel management")
                    cursor = db.cursor()
                    p = str(txt.get())
                    sql = "DELETE FROM BOOKING WHERE fullname = %s"
                    var = [p]
                    cursor.execute(sql, var)
                    db.commit()

                # FOR SEARCH BUTTON
                def search():
                    p = str(txt.get())
                    sql = "SELECT * FROM BOOKING WHERE fullname = %s"
                    var = [p]
                    cursor.execute(sql, var)

                    customers = cursor.fetchall()  # cursor is used for excute the data
                    itemsforlistbox = []

                    for name in customers:
                        customer = '{0}'.format(name[0:14])
                        itemsforlistbox.append(customer)
                    s = ttk.Style()
                    s.theme_use('clam')

                    # Add the rowheight
                    s.configure('Treeview', rowheight=40)
                    tree = ttk.Treeview(f, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14"),show='headings', height=13)

                    tree.column("# 1", anchor=CENTER, stretch=YES, width=55)
                    tree.heading("# 1", text="ID")
                    tree.column("# 2", anchor=CENTER, stretch=NO, width=100)
                    tree.heading("# 2", text="fullname")
                    tree.column("# 3", anchor=CENTER, stretch=NO, width=100)
                    tree.heading("# 3", text="contactno")
                    tree.column("# 4", anchor=CENTER, stretch=NO, width=160)
                    tree.heading("# 4", text="emailid")
                    tree.column("# 5", anchor=CENTER, stretch=NO, width=80)
                    tree.heading("# 5", text="gender")
                    tree.column("#6", anchor=CENTER, stretch=NO, width=90)
                    tree.heading("# 6", text="checkin")
                    tree.column("#7", anchor=CENTER, stretch=NO, width=90)
                    tree.heading("# 7", text="checkout")
                    tree.column("#8", anchor=CENTER, stretch=NO, width=60)
                    tree.heading("# 8", text="rooms")
                    tree.column("#9", anchor=CENTER, stretch=NO, width=60)
                    tree.heading("# 9", text="guests")
                    tree.column("#10", anchor=CENTER, stretch=NO, width=100)
                    tree.heading("# 10", text="smookingroom")
                    tree.column("#11", anchor=CENTER, stretch=NO, width=70)
                    tree.heading("# 11", text="largebed")
                    tree.column("#12", anchor=CENTER, stretch=NO, width=100)
                    tree.heading("# 12", text="earlylcheckin")
                    tree.column("#13", anchor=CENTER, stretch=NO, width=100)
                    tree.heading("# 13", text="latecheckin")
                    tree.column("#14", anchor=CENTER, stretch=NO, width=120)
                    tree.heading("# 14", text="roomonahighfloor")
                    for name in itemsforlistbox:
                        # Insert the data in Treeview widget
                        tree.insert('', 'end', text=name[0], values=name)
                    tree.place(relx=0.01, rely=0.11)
                    db.commit()

                listData = cursor.execute("SELECT * FROM BOOKING")
                customers = cursor.fetchall()  # cursor is used for excute the data
                itemsforlistbox = []

                for name in customers:
                    customer = '{0}'.format(name[0:14])
                    itemsforlistbox.append(customer)
                s = ttk.Style()
                s.theme_use('clam')

                # Add the rowheight
                s.configure('Treeview', rowheight=40)
                tree = ttk.Treeview(f, column=(
                "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14"),
                                    show='headings', height=13)

                tree.column("# 1", anchor=CENTER, stretch=YES, width=55)
                tree.heading("# 1", text="ID")
                tree.column("# 2", anchor=CENTER, stretch=NO, width=100)
                tree.heading("# 2", text="fullname")
                tree.column("# 3", anchor=CENTER, stretch=NO, width=100)
                tree.heading("# 3", text="contactno")
                tree.column("# 4", anchor=CENTER, stretch=NO, width=160)
                tree.heading("# 4", text="emailid")
                tree.column("# 5", anchor=CENTER, stretch=NO, width=80)
                tree.heading("# 5", text="gender")
                tree.column("#6", anchor=CENTER, stretch=NO, width=90)
                tree.heading("# 6", text="checkin")
                tree.column("#7", anchor=CENTER, stretch=NO, width=90)
                tree.heading("# 7", text="checkout")
                tree.column("#8", anchor=CENTER, stretch=NO, width=60)
                tree.heading("# 8", text="rooms")
                tree.column("#9", anchor=CENTER, stretch=NO, width=60)
                tree.heading("# 9", text="guests")
                tree.column("#10", anchor=CENTER, stretch=NO, width=100)
                tree.heading("# 10", text="smookingroom")
                tree.column("#11", anchor=CENTER, stretch=NO, width=70)
                tree.heading("# 11", text="largebed")
                tree.column("#12", anchor=CENTER, stretch=NO, width=100)
                tree.heading("# 12", text="earlylcheckin")
                tree.column("#13", anchor=CENTER, stretch=NO, width=100)
                tree.heading("# 13", text="latecheckin")
                tree.column("#14", anchor=CENTER, stretch=NO, width=120)
                tree.heading("# 14", text="roomonahighfloor")
                for name in itemsforlistbox:
                    # Insert the data in Treeview widget
                    tree.insert('', 'end', text=name[0], values=name)

                tree.place(relx=0.01, rely=0.11)

                # hide data in guest details button
                def hide():
                    hide = tree.selection()
                    if hide:
                        a = hide[0]
                        tree.delete(a)
                    db.commit()

                Label_middle = Label(f, text=" **********Customer Details********** ", bg="#7b5f47",
                                     font=("Algerian", 20, "bold"))
                Label_middle.place(relx=0.49, rely=0.05, anchor="center")
                # button in guest details window
                homepage = Button(f, text='Close', bg="#7b5f47", font=("Algerian", 11, "bold"), height=1, width=13,
                                  borderwidth=5, command=f.destroy)
                homepage.place(x=615, y=705)
                btn = Button(f, text=" Hide ", bg="#7b5f47", font=("Algerian", 11, "bold"), height=1, width=10,
                             borderwidth=5, command=hide)
                btn.place(x=630, y=655)
                btn = Button(f, text=" Delete all ", bg="#7b5f47", font=("Algerian", 11, "bold"), height=1, width=13,
                             borderwidth=5, command=record)
                btn.place(x=785, y=655)
                btn = Button(f, text=" Search ", bg="#7b5f47", font=("Algerian", 8, "bold"), height=1, width=9,
                             borderwidth=5, command=search)
                btn.place(x=1220, y=28)
                txt = StringVar()
                e8 = Entry(f, text=txt)
                e8.place(relx=0.82, rely=0.04)
                btn = Button(f, text=" Delete ", bg="#7b5f47", font=("Algerian", 11, "bold"), height=1, width=11,
                             borderwidth=5, command=dltprt)
                btn.place(x=460, y=655)
                db.commit()
                f.mainloop()




            else:
                print("Wrong password")
        else:
            print("Wrong username and password")
#login window code
    win = tkinter.Toplevel()
    win.geometry("700x466")
    win.protocol("WM_DELETE_WINDOW", disable_event)
    lg = ImageTk.PhotoImage(file='38.jpg')
    label = Label(win, image=lg)
    label.place(x=0, y=0)

    Label_middle = Label(win, text="  *********Admin Login*********  ",bg="#7b5f47", fg="black",font=("Algerian", 20, "bold"))
    Label_middle.place(relx=0.5, rely=0.11, anchor='center')
    btn = Button(win, text=" Close ", bg="#7b5f47", font=("Algerian", 11, "bold"), height=1, width=10,borderwidth=5,command=win.destroy)
    btn.place(x=350, y=335)
    btn = Button(win, text=" Login ", bg="#7b5f47", font=("Algerian", 11, "bold"), height=1, width=10, borderwidth=5,command=login)
    btn.place(x=215, y=335)
    Label_middle = Label(win, text=" Username ", bg="#7b5f47", font=("Algerian", 15, "bold"))
    Label_middle.place(relx=0.39, rely=0.38, anchor="center")
    Label_middle = Label(win, text=" Password ", bg="#7b5f47", font=("Algerian", 15, "bold"))
    Label_middle.place(relx=0.39, rely=0.52, anchor="center")


    name12 = StringVar()
    password1 = StringVar()
    entry1 = Entry(win, text=name12)
    entry2 = Entry(win, text=password1)

    entry1.place(relx=0.5, rely=0.36,width=130)
    entry2.place(relx=0.5, rely=0.5,width=130)

    win.mainloop()


# code for delete the all data in database using delte button in guest details
def record():
    sql = "DELETE FROM BOOKING"
    cursor.execute(sql)
    db.commit()


# for gallery window
def gallery():
    b: Tk = Toplevel()
    b.geometry("850x750")
    b.configure(bg="#181a1b")
    b.resizable(0, 0)
    b.protocol("WM_DELETE_WINDOW", disable_event)
    # FOR IMAGES IMPORT
    # for image1
    canvas = Canvas(b, width=240, height=200)
    canvas.configure(bg="#181a1b")
    canvas.place(relx=0.03, rely=.25)
    # Load an image in the script
    img = (Image.open("23.jpg"))
    # Resize the Image using resize method
    resized_image = img.resize((222, 183), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    # Add image to the Canvas Items
    canvas.create_image(10, 10, anchor=NW, image=new_image)

    # for image 2
    canvas = Canvas(b, width=240, height=200)
    canvas.configure(bg="#181a1b")
    canvas.place(relx=0.35, rely=.25)
    # Load an image in the script
    img = (Image.open("24.jpg"))
    # Resize the Image using resize method
    resized_image = img.resize((222, 183), Image.ANTIALIAS)
    new1_image = ImageTk.PhotoImage(resized_image)
    # Add image to the Canvas Items
    canvas.create_image(10, 10, anchor=NW, image=new1_image)
    # FOR IMAGE 3
    canvas = Canvas(b, width=240, height=200)
    canvas.configure(bg="#181a1b")
    canvas.place(relx=0.68, rely=.25)
    # Load an image in the script
    img = (Image.open("19.jpg"))
    # Resize the Image using resize method
    resized_image = img.resize((222, 183), Image.ANTIALIAS)
    new2_image = ImageTk.PhotoImage(resized_image)
    # Add image to the Canvas Items
    canvas.create_image(10, 10, anchor=NW, image=new2_image)

    # FOR IMAGE 4
    canvas = Canvas(b, width=240, height=200)
    canvas.configure(bg="#181a1b")
    canvas.place(relx=0.04, rely=.64)
    # Load an image in the script
    img = (Image.open("14.jpg"))
    # Resize the Image using resize method
    resized_image = img.resize((222, 183), Image.ANTIALIAS)
    new3_image = ImageTk.PhotoImage(resized_image)
    # Add image to the Canvas Items
    canvas.create_image(10, 10, anchor=NW, image=new3_image)

    # FOR IMAGE 5
    canvas = Canvas(b, width=240, height=200)
    canvas.configure(bg="#181a1b")
    canvas.place(relx=0.36, rely=.64)
    # Load an image in the script
    img = (Image.open("26.jpg"))
    # Resize the Image using resize method
    resized_image = img.resize((222, 183), Image.ANTIALIAS)
    new4_image = ImageTk.PhotoImage(resized_image)
    # Add image to the Canvas Items
    canvas.create_image(10, 10, anchor=NW, image=new4_image)

    # FOR IMAGE 6
    canvas = Canvas(b, width=240, height=200)
    canvas.configure(bg="#181a1b")
    canvas.place(relx=0.68, rely=.64)
    # Load an image in the script
    img = (Image.open("27.jpg"))
    # Resize the Image using resize method
    resized_image = img.resize((222, 183), Image.ANTIALIAS)
    new5_image = ImageTk.PhotoImage(resized_image)
    # Add image to the Canvas Items
    canvas.create_image(10, 10, anchor=NW, image=new5_image)

    # FOR LABELS
    Label_middle = Label(b, text="*********The Royal Galaxy*********", bg="#181a1b", fg="#1d97bf",
                         font=("Algerian", 20, "bold"))
    Label_middle.place(relx=0.51, rely=0.05, anchor="center")

    Label_middle = Label(b, text=" P ", bg="#181a1b", fg="#824400", font=("Gadugi", 35, "bold"))
    Label_middle.place(relx=0.06, rely=0.13, anchor="center")

    Label_middle = Label(b, text="HOTO ", bg="#181a1b", fg="#ba7325", font=("Gadugi", 15, "bold"))
    Label_middle.place(relx=0.12, rely=0.14, anchor="center")

    Label_middle = Label(b, text=" G ", bg="#181a1b", fg="#824400", font=("Gadugi", 35, "bold"))
    Label_middle.place(relx=0.19, rely=0.13, anchor="center")

    Label_middle = Label(b, text=" ALLERY ", bg="#181a1b", fg="#ba7325", font=("Gadugi", 15, "bold"))
    Label_middle.place(relx=0.26, rely=0.14, anchor="center")

    Label_middle = Label(b, text=" --> Swimming Pool ", bg="#7b5f47", font=("Forte", 18, "bold"))
    Label_middle.place(relx=0.16, rely=0.21, anchor="center")

    Label_middle = Label(b, text=" --> Restaurant ", bg="#7b5f47", font=("Forte", 18, "bold"))
    Label_middle.place(relx=0.13, rely=0.58, anchor="center")

    # for photos window
    def photowindow():
        d: Tk = Toplevel()
        d.geometry("850x750")
        d.configure(bg="#181a1b")
        d.resizable(0, 0)
        d.protocol("WM_DELETE_WINDOW", disable_event)

        # FOR IMAGES IMPORT
        # for image1
        canvas = Canvas(d, width=240, height=200)
        canvas.configure(bg="#181a1b")
        canvas.place(relx=0.03, rely=.04)
        # Load an image in the script
        img = (Image.open("2.jpg"))
        # Resize the Image using resize method
        resized_image = img.resize((222, 183), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)
        # Add image to the Canvas Items
        canvas.create_image(10, 10, anchor=NW, image=new_image)

        # for image 2
        canvas = Canvas(d, width=240, height=200)
        canvas.configure(bg="#181a1b")
        canvas.place(relx=0.35, rely=.04)
        # Load an image in the script
        img1 = (Image.open("8.jpg"))
        # Resize the Image using resize method
        resized_image = img1.resize((222, 183), Image.ANTIALIAS)
        new1_image = ImageTk.PhotoImage(resized_image)
        # Add image to the Canvas Items
        canvas.create_image(10, 10, anchor=NW, image=new1_image)

        # FOR IMAGE 3
        canvas = Canvas(d, width=240, height=200)
        canvas.configure(bg="#181a1b")
        canvas.place(relx=0.68, rely=.04)
        # Load an image in the script
        img = (Image.open("9.jpg"))
        # Resize the Image using resize method
        resized_image = img.resize((222, 183), Image.ANTIALIAS)
        new2_image = ImageTk.PhotoImage(resized_image)
        # Add image to the Canvas Items
        canvas.create_image(10, 10, anchor=NW, image=new2_image)

        # FOR IMAGE 4
        canvas = Canvas(d, width=240, height=200)
        canvas.configure(bg="#181a1b")
        canvas.place(relx=0.03, rely=.35)
        # Load an image in the script
        img = (Image.open("13.jpg"))
        # Resize the Image using resize method
        resized_image = img.resize((222, 183), Image.ANTIALIAS)
        new3_image = ImageTk.PhotoImage(resized_image)
        # Add image to the Canvas Items
        canvas.create_image(10, 10, anchor=NW, image=new3_image)

        # FOR IMAGE 5
        canvas = Canvas(d, width=240, height=200)
        canvas.configure(bg="#181a1b")
        canvas.place(relx=0.35, rely=.35)
        # Load an image in the script
        img = (Image.open("15.jpg"))
        # Resize the Image using resize method
        resized_image = img.resize((222, 183), Image.ANTIALIAS)
        new4_image = ImageTk.PhotoImage(resized_image)
        # Add image to the Canvas Items
        canvas.create_image(10, 10, anchor=NW, image=new4_image)

        # FOR IMAGE 6
        canvas = Canvas(d, width=240, height=200)
        canvas.configure(bg="#181a1b")
        canvas.place(relx=0.68, rely=.35)
        # Load an image in the script
        img = (Image.open("25.JPG"))
        # Resize the Image using resize method
        resized_image = img.resize((222, 183), Image.ANTIALIAS)
        new5_image = ImageTk.PhotoImage(resized_image)
        # Add image to the Canvas Items
        canvas.create_image(10, 10, anchor=NW, image=new5_image)

        # FOR IMAGE 7
        canvas = Canvas(d, width=240, height=200)
        canvas.configure(bg="#181a1b")
        canvas.place(relx=0.03, rely=.65)
        # Load an image in the script
        img = (Image.open("31.jpg"))
        # Resize the Image using resize method
        resized_image = img.resize((222, 183), Image.ANTIALIAS)
        new6_image = ImageTk.PhotoImage(resized_image)
        # Add image to the Canvas Items
        canvas.create_image(10, 10, anchor=NW, image=new6_image)

        # FOR IMAGE 8
        canvas = Canvas(d, width=240, height=200)
        canvas.configure(bg="#181a1b")
        canvas.place(relx=0.35, rely=.65)
        # Load an image in the script
        img = (Image.open("32.jpg"))
        # Resize the Image using resize method
        resized_image = img.resize((222, 183), Image.ANTIALIAS)
        new7_image = ImageTk.PhotoImage(resized_image)
        # Add image to the Canvas Items
        canvas.create_image(10, 10, anchor=NW, image=new7_image)

        # FOR IMAGE 9
        canvas = Canvas(d, width=240, height=200)
        canvas.configure(bg="#181a1b")
        canvas.place(relx=0.68, rely=.65)
        # Load an image in the script
        img = (Image.open("33.jpg"))
        # Resize the Image using resize method
        resized_image = img.resize((222, 183), Image.ANTIALIAS)
        new8_image = ImageTk.PhotoImage(resized_image)
        # Add image to the Canvas Items
        canvas.create_image(10, 10, anchor=NW, image=new8_image)

        # add button for exit
        homepage = Button(d, text='Close', bg="#7b5f47", font=("Algerian", 12, "bold"), width=14, command=d.destroy)
        homepage.place(relx=0.49, rely=0.96, anchor="center")

        d.mainloop()

    btn = Button(b, text="View more photos-->  ", bg="#7b5f47", font=("Algerian", 13, "bold"), borderwidth=5,
                 command=photowindow)
    btn.place(relx=0.4, rely=0.93)

    # go to home page using back button
    homepage = Button(b, text='Back', bg="#7b5f47", font=("Book Antiqua", 11, "bold"), command=b.destroy)
    homepage.place(relx=0.05, rely=0.04, anchor="center")

    b.mainloop()


# for booking window
def booka():
    def show(event):
        abc = str(e1.get())
        abc1 = str(e2.get())
        abc2 = str(e3.get())
        selectrb = str(var.get())
        abc3 = str(e4.get())
        abc4 = str(e5.get())
        menu1 = str(menu.get())
        menu2 = str(menua.get())
        cb = str(Checkbutton1.get())
        cb2 = str(Checkbutton2.get())
        cb3 = str(Checkbutton3.get())
        cb4 = str(Checkbutton4.get())
        cb5 = str(Checkbutton5.get())
        sql = "INSERT INTO BOOKING(fullname,contactno,emailid,gender,checkin,checkout,rooms,guests,smookingroom,largebed,earlylcheckin,roomonahighfloor,latecheckin) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        vara = (abc, abc1, abc2, selectrb, abc3, abc4, menu1, menu2, cb, cb2, cb3, cb4, cb5)
        cursor.execute(sql, vara)

        # popup  message box
        messagebox.showinfo("Message", "Sucessfully Booked!")

    # window for book now
    c = Toplevel()
    c.geometry("1000x667")
    c.resizable(0, 0)
    c.protocol("WM_DELETE_WINDOW", disable_event)

    ng = ImageTk.PhotoImage(file='10.jpg')
    label = Label(c, image=ng)
    label.place(x=0, y=0)

    Label_middle = Label(c, text=" *****Guest Details***** ", bg="#824400", font=("Algerian", 15, "bold"))
    Label_middle.place(relx=0.48, rely=0.04, anchor="center")

    Label_middle = Label(c, text=" Full Name ", font=("Forte", 15, "bold"))
    Label_middle.place(relx=0.11, rely=0.10, anchor="center")
    i = StringVar()
    e1 = Entry(c, text=i)
    e1.place(relx=0.18, rely=0.09, width=150)

    Label_middle = Label(c, text=" Contact No ", font=("Forte", 15, "bold"))
    Label_middle.place(relx=0.11, rely=0.17, anchor="center")
    j = StringVar()
    e2 = Entry(c, text=j)
    e2.place(relx=0.19, rely=0.15)

    Label_middle = Label(c, text=" Email ID ", font=("Forte", 15, "bold"))
    Label_middle.place(relx=0.68, rely=0.10, anchor="center")
    k = StringVar()
    e3 = Entry(c, text=k)
    e3.place(relx=0.75, rely=0.09, width=200)

    Label_middle = Label(c, text=" Gender ", font=("Forte", 15, "bold"))
    Label_middle.place(relx=0.68, rely=0.17, anchor="center")

    var = StringVar()
    Radiobutton9 = IntVar()

    Button1 = Radiobutton(c, text="Male", font=("Forte", 13, "bold"), variable=var, value="Male")
    Button1.place(relx=0.78, rely=0.17, anchor="center")
    Button1.place(relx=0.78, rely=0.17, anchor="center")
    Radiobutton9 = IntVar()
    Button1 = Radiobutton(c, text="Female", font=("Forte", 13, "bold"), variable=var, value="Female")
    Button1.place(relx=0.88, rely=0.17, anchor="center")

    Label_middle = Label(c, text="********Booking Details********", bg="#824400", font=("Algerian", 15, "bold"))
    Label_middle.place(relx=0.49, rely=0.24, anchor="center")

    Label_middle = Label(c, text=" Check In = ", font=("Forte", 15, "bold"))
    Label_middle.place(relx=0.12, rely=0.32, anchor="center")
    l = StringVar()
    e4 = Entry(c, text=l)
    e4.place(relx=0.2, rely=0.30)

    Label_middle = Label(c, text=" Check Out = ", font=("Forte", 15, "bold"))
    Label_middle.place(relx=0.12, rely=0.39, anchor="center")
    m = StringVar()
    e5 = Entry(c, text=m)
    e5.place(relx=0.2, rely=0.37)

    Label_middle = Label(c, text=" Rooms = ", font=("Forte", 15, "bold"))
    Label_middle.place(relx=0.70, rely=0.31, anchor="center")
    menu = StringVar()
    menu.set("Select the Rooms")

    drop = OptionMenu(c, menu, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    drop.pack()
    drop.place(relx=0.77, rely=0.29)

    Label_middle = Label(c, text=" Guests = ", font=("Forte", 15, "bold"))
    Label_middle.place(relx=0.70, rely=0.38, anchor="center")
    menua = StringVar()
    menua.set("No. of Guests")
    drop = OptionMenu(c, menua, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    drop.pack()
    drop.place(relx=0.77, rely=0.36)

    Label_middle = Label(c, text=" *******SPECIAL REQUEST******** ", bg="#824400", font=("Algerian", 15, "bold"))
    Label_middle.place(relx=0.49, rely=0.44, anchor="center")

    Checkbutton1 = IntVar()
    Checkbutton2 = IntVar()
    Checkbutton3 = IntVar()
    Checkbutton4 = IntVar()
    Checkbutton5 = IntVar()

    Button1 = Checkbutton(c, variable=Checkbutton1, text="Smoking room", onvalue=1, offvalue=0,
                          font=("Forte", 13, "bold"))
    Button1.place(relx=0.12, rely=0.51, anchor="center")

    Button2 = Checkbutton(c, variable=Checkbutton2, text="Late Check-in", onvalue=1, offvalue=0,
                          font=("Forte", 13, "bold"))
    Button2.place(relx=0.3, rely=0.51, anchor="center")

    Button3 = Checkbutton(c, variable=Checkbutton3, text="Early Check-in", onvalue=1, offvalue=0,
                          font=("Forte", 13, "bold"))
    Button3.place(relx=0.5, rely=0.51, anchor="center")

    Button4 = Checkbutton(c, variable=Checkbutton4, text="Room on a High Floor", onvalue=1, offvalue=0,
                          font=("Forte", 13, "bold"))
    Button4.place(relx=0.7, rely=0.51, anchor="center")

    Button5 = Checkbutton(c, variable=Checkbutton5, text="Large bed", onvalue=1, offvalue=0, font=("Forte", 13, "bold"))
    Button5.place(relx=0.9, rely=0.51, anchor="center")

    # for reset details code
    def clearFunc():
        i.set("")
        j.set("")
        k.set("")
        var.set("0")
        Radiobutton9.set("0")
        l.set("")
        m.set("")
        menu.set("No of Rooms")
        menua.set("No of Guests")
        Checkbutton1.set("0")
        Checkbutton2.set("0")
        Checkbutton3.set("0")
        Checkbutton4.set("0")
        Checkbutton5.set("0")

    btn = Button(c, text=" Reset Details ", bg="#7b5f47", font=("Matura MT Script Capitals", 13, "bold"), height=1,
                 width=12, borderwidth=5, command=clearFunc)
    btn.place(x=290, y=600)

    btn = Button(c, text="Book Now", bg="#7b5f47", font=("Matura MT Script Capitals", 13, "bold"), height=1, width=12,
                 borderwidth=5)
    btn.bind("<Button-1>", show)
    btn.place(x=510, y=600)

    Label_middle = Label(c, text=" **********IMPORTANT INFORMATION********** ", bg="#824400",
                         font=("Algerian", 15, "bold"))
    Label_middle.place(relx=0.49, rely=0.58, anchor="center")

    Label_middle = Label(c, text=" Resort Rules:- ", bg="#87790f", font=("Algerian", 15, "bold"))
    Label_middle.place(relx=0.12, rely=0.64, anchor="center")

    Label_middle = Label(c, text=" -->Guests with fever are not allowed. ", font=("Arial", 12, "bold"))
    Label_middle.place(relx=0.18, rely=0.69, anchor="center")

    Label_middle = Label(c, text=" -->Passport, Aadhar, and Govt. ID are accepted as ID proof(s). ",
                         font=("Arial", 12, "bold"))
    Label_middle.place(relx=0.27, rely=0.75, anchor="center")

    Label_middle = Label(c, text=" -->Quarantine protocols are being followed as per local government authorities. ",
                         font=("Arial", 12, "bold"))
    Label_middle.place(relx=0.34, rely=0.81, anchor="center")

    homepage = Button(c, text='Back', bg="#7b5f47", font=("Book Antiqua", 11, "bold"), command=c.destroy)
    homepage.place(relx=0.05, rely=0.04, anchor="center")
    c.mainloop()


# for main window
a = Tk()
a.geometry("1024x768")
# insert image
bg = ImageTk.PhotoImage(file='7.jpg')
label = Label(image=bg)
label.place(x=0, y=0)
a.resizable(0, 0)
a.protocol("WM_DELETE_WINDOW", disable_event)

# text on image
Label_middle = Label(a, text="************ Welcome to **************", fg="black", font=("Forte"))
Label_middle.place(relx=0.7, rely=0.75, anchor='center')
Label_middle = Label(a, text="   'The   Royal   Galaxy'  ", fg="black", font=("Algerian", 30, "bold"))
Label_middle.place(relx=0.7, rely=0.81, anchor='center')
Label_middle = Label(a, text="  Contact us for more details :-  ", fg="black", font=("Algerian", 10, "bold"))
Label_middle.place(relx=0.13, rely=0.98, anchor='center')
Label_middle = Label(a, text=" mg281809@gmail.com,6284023415  ", fg="black", font=("Franklin Gothic Demi Cond", 9),
                     width=30)
Label_middle.place(relx=0.34, rely=0.98, anchor='center')

# all buttons on MAIN WINDOW
btn = Button(a, text="View  Gallery", bg="#a95417", font=("Matura MT Script Capitals", 13, "bold"), height=1, width=12,
             command=gallery)
btn.place(x=550, y=660)
btn = Button(a, text="Book Now", bg="#a95417", font=("Matura MT Script Capitals", 13, "bold"), height=1, width=12,
             command=booka)
btn.place(x=750, y=660)
btn = Button(a, text="Exit", bg="#66594b", font=("Matura MT Script Capitals", 13, "bold"), height=1, width=6,
             command=exit)
btn.place(x=687, y=710)
btn = Button(a, text=" Guest Details ", bg="#7b5f47", font=("Algerian", 11, "bold"), height=1, width=13, borderwidth=5,
             command=select)
btn.place(x=870, y=730)

a.mainloop()

