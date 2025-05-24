#joshua lewis 19/3/2025

#importing all the things that i would need for the code
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

#creating a gloabal variable called "attempt" to count the amount of attemts there have been to sign in
global attempt
attempt = 0

#creadint a funtion for the first screen
def signInS () :
    
    #creating the screen and changing size and background colour
    screen = Tk()
    screen.geometry ("700x500")
    screen.configure(bg = "#0cc0df")
    screen.title ("Sgrin Mewn Cyfnodi")
    
    #creating a function to sign in
    def signIn ():
        
        #getting the text from the entry boxes
        name1 = boxName.get()
        password1 = boxPassword.get ()
        
        #creating a variable to count the number of lines
        i = 0
        
        #opening the file
        with open ("login.txt","r") as f:
            
            #reading the lines
            lines = f.readlines ()
            
            #making a loop for the lines
            for line in lines:
                
                #splitting the lines to the username then password
                item = lines[i].split(".")
                
                #adding 1 to the variable so that next time in the loop it uses the next line
                i=i+1
                
                #checking if the text in the entry box is the same as any usernames and their corrasponding passwords
                if item[0] == name1 and item[1] == password1+"\n":
                    
                    #making a message pop up to show that it has found one that is the same
                    messagebox.showinfo("accepted","welcome to the system")
                    
                    #running the funtion for the other screen and removing the current one
                    tools ()
                    screen.destroy()
                    
                    #stoping the loop
                    break
                
            #checking if the items arent the same as any usernames or passwords
            if item[0] != name1 or item[1] != password1+"\n":
                
                #showing a message that the username or password is wrong
                messagebox.showinfo("incorrect","that username or password is incorrect")
                
                #adding one to the attempts
                global attempt
                attempt = attempt+1
                
                #checking if the attempts are more than 2
                if attempt>2:
                    
                    #showing a message that tyhey have tried too many times and then closig the program
                    messagebox.showinfo("too many attepts","too many attepts please try later")
                    quit()
                    
    #a function to close the program
    def cau ():
                screen.destroy()
      
    #labelau
    title = Label (screen, width="24",text="Mewn Cofnodi I'r System", font = ("courier new",20),bg = "#0cc0df")
    name = Label(screen, width="8",text="enw : ", font = ("courier new",11),bg = "#0cc0df")
    password = Label(screen, width="12",text="cyfrinair : ", font = ("courier new",11),bg = "#0cc0df")

    #entry boxes
    boxName = Entry (screen,width=20)
    boxPassword = Entry (screen,width=20)

    #buttons
    signIn = Button (screen, text="Mewn cofnodi",command = signIn)
    cau = Button (screen, text="cau'r rhaglen",command = cau)

    #the grid
    title.grid (columnspan=5 , row=0)
    name.grid (column=0,row=1)
    boxName.grid (column=1,row=1)
    password.grid (column=0,row=2)
    boxPassword.grid (column=1,row=2)
    signIn.grid (column=0,row=3)
    cau.grid (column=0,row=4)
    
#creating a funtion to make it simpiler to move between screens
def tools ():
    #ceru function iw cau yr scrin yma
    def close ():
        signInS ()
        toolScreen.destroy ()
    ###creu gid or scrins   
    def newinf ():

        def findCost():
            boat = sizeE.get()
            time1 = amserE.get()
            aelod1 = aelodE.get()
            
            if boat!="" and time1!="" and aelod1!="":
                if boat == "dingi":
                    costA = int("5")
                elif boat == "cwch undydd":
                    costA = int("10")
                elif boat == "cwch mordeithio bach":
                    costA = int("15")
                elif boat == "cwch mordeithio":
                    costA = int("20")
                if aelod1=="na":
                    cost = int(time1) * int(costA)
                    costE.delete(0,END)
                    costE.insert(END,str(cost))
                else:
                    cost = int(time1) * int(costA)
                    cost = cost * float(0.85)
                    costE.delete(0,END)
                    costE.insert(END,str(cost))

            else:
                messagebox.showinfo("error","there must be something in every box")
        #making a function to write customer information into a file
        def wirte():
            
            ####I know it is spelt wrong I couldnt be bothered to retype it so that it is spelt correctly####
            #getting the informationg out of the boxes
            enw1 = enwE.get()
            size1 = sizeE.get()
            num1 = numE.get()
            email1 = ebostE.get()
            
            amser1 = amserE.get()
            aD1 = amserDE.get()
            dD1 = diwrnodDE.get()
            amserampm1 = amserampm.get()

            boat = sizeE.get()
            time1 = amserE.get()
            aelod1 = aelodE.get()
            
            if boat!="" and time1!="" and aelod1!="":
                if boat == "dingi":
                    costA = int("5")
                elif boat == "cwch undydd":
                    costA = int("10")
                elif boat == "cwch mordeithio bach":
                    costA = int("15")
                elif boat == "cwch mordeithio":
                    costA = int("20")

                
                if aelod1=="na":
                    
                    cost = int(time1) * int(costA)
                    #opening the file for the customer ID
                    
                    with open("number.txt","r")as g:
                        #reading whats in the file
                        
                        t=g.read()
                        #creating a file with the customer ID as the name
                        
                        with open(t+".txt","w") as p:
                            
                            cost = str(cost)
                            
                            #writing the information into the file
                            p.write(t+"\n"+enw1+"\n"+size1+"\n"+num1+"\n"+email1+"\n"+aelod1+"\n"+amser1+"\n"+aD1+amserampm1+"\n"+dD1+"\n"+"£"+cost)
                            #making a message box appear to show that it worked
                            
                            messagebox.showinfo("success","we have successfully added you to our system")
                            
                            #opening the customer ID file 
                            with open("number.txt","w")as h:
                                
                                #changing the information in it to an interger
                                t = int(t)
                                #adding 1 to the number
                                t = t+1
                                #writing the number into the file as a string
                                h.write(str(t))

                else:

                    cost = int(time1) * int(costA)
                    cost = cost * float(0.85)
                    
                    #opening the file for the customer ID
                    with open("number.txt","r")as g:
                        #reading whats in the file
                        t=g.read()
                    #creating a file with the customer ID as the name
                    
                    with open(t+".txt","w") as p:
                        cost=str(cost)
                        #writing the information into the file
                        p.write(t+"\n"+enw1+"\n"+size1+"\n"+num1+"\n"+email1+"\n"+aelod1+"\n"+amser1+"\n"+aD1+amserampm1+"\n"+dD1+"\n"+"£"+cost)
                        #making a message box appear to show that it worked
                        messagebox.showinfo("success","we have successfully added you to our system")
                
                        #opening the customer ID file 
                        with open("number.txt","w")as h:
                            #changing the information in it to an interger
                            t = int(t)
                            #adding 1 to the number
                            t = t+1
                            #writing the number into the file as a string
                            h.write(str(t))
            else:
                messagebox.showinfo("error","there must be something in every box")

            #opening the file for the customer ID
            ##with open("number.txt","r")as g:
                #reading whats in the file
                ##t=g.read()
            #creating a file with the customer ID as the name
                
            ##with open(t+".txt","w") as p:
                #writing the information into the file
                ##p.write(t+"\n"+enw1+"\n"+size1+"\n"+num1+"\n"+email1+"\n"+aelod1+"\n"+amser1+"\n"+aD1+amserampm1+"\n"+dD1+"\n"+cost)
                #making a message box appear to show that it worked
                ##messagebox.showinfo("success","we have successfully added you to our system")
                
                #opening the customer ID file 
                ##with open("number.txt","w")as h:
                    #changing the information in it to an interger
                    ##t = int(t)
                    #adding 1 to the number
                    ##t = t+1
                    #writing the number into the file as a string
                    ##h.write(str(t))
                    
        #creating a function that checks the information
                    
        def inpt():
            
            #getting the information
            enw1 = enwE.get()
            size1 = sizeE.get()
            num1 = numE.get()
            email1 = ebostE.get()
            aelod1 = aelodE.get()
            amser1 = amserE.get()
            aD1 = amserDE.get()
            dD1 = diwrnodDE.get()
            amserampm1 = amserampm.get()
            
            #trying to change the phone number to an interget to ensure that it is a number
            try:
                
                int(num1)
            except:
                
                #if it cannot change it to a number it shows an error message that it has not worked
                messagebox.showinfo("error","mae rrif ffon angen fod y rhifau")
            
            #ensuring that there is an @ in the email box
            if "@" in email1:
                
                #ensuring that all the boxes are not empty
                if enw1!= "" and size1!="" and num1!="" and email1!="" and aelod1!="" and amser1!="" and aD1!="" and dD1!="" and amserampm1!="":
                        #runnning the function to write it into the file
                        wirte()
                        ####I know it is spelt wrong I couldnt be bothered to retype it so that it is spelt correctly####

                else:
                    #creu messagebox iw wneud error for yne angen fod rhiwbeth fewn pob bocs
                    messagebox.showinfo("error","there must be something in every box")
            else:
                #creu messagebox iw wneud error iw ddweud mae angen for y symbol @ un yr email
                messagebox.showinfo("error","there must be a @ sybol in your email")

        #creu function i fynd nol ir scrin tools
        def goback():
            tools()
            newinfS.destroy()
            
        #making the screen and changing name size and background colour
        newinfS = Tk()
        newinfS.geometry ("700x500")
        newinfS.configure(bg = "#0cc0df")
        newinfS.title ("Sgrin cwsmer Newydd")
        toolScreen.destroy ()
        
        #labels
        titleL1 = Label (newinfS, width="15",text="manylion cwsmer", font = ("courier new",20),bg = "#0cc0df")
        titleL2 = Label (newinfS, width="24",text="cwsmer newyddd", font = ("courier new",15),bg = "#0cc0df")
        enwL = Label (newinfS, width="5",text="enw:", font = ("courier new",11),bg = "#0cc0df")
        sizeL = Label (newinfS, width="10",text="seis cwch:", font = ("courier new",11),bg = "#0cc0df")
        numL = Label (newinfS, width="10",text="rhif ffon:", font = ("courier new",11),bg = "#0cc0df")
        ebostL = Label (newinfS, width="7",text="ebost:", font = ("courier new",11),bg = "#0cc0df")
        aelodL = Label (newinfS, width="7",text="aelod:", font = ("courier new",11),bg = "#0cc0df")
        amserL = Label (newinfS, width="14",text="hyd yr bwciad:", font = ("courier new",11),bg = "#0cc0df")
        amserDL = Label (newinfS, width="14",text="amser ddechrau:", font = ("courier new",11),bg = "#0cc0df")
        diwrnodDL = Label (newinfS, width="15",text="diwrnod dechrau:", font = ("courier new",11),bg = "#0cc0df")

        #entrys
        enwE = Entry (newinfS,width=23)
        numE = Entry (newinfS,width=23)
        ebostE = Entry (newinfS,width=23)
        amserE = Entry (newinfS,width=23)
        diwrnodDE = Entry (newinfS,width=23)
        costE = Entry (newinfS,width=8)

        #combobox
        list4 = ("1","2","3","4","5","6","7","8","9","10","11","12")
        amserDE = Combobox (newinfS,values=list4)
        list3 = ["dingi","cwch undydd","cwch mordeithio bach","cwch mordeithio"]
        sizeE = Combobox (newinfS,values=list3)
        list2 = ["am","pm"]
        amserampm = Combobox (newinfS,values=list2,width=5)
        list1 = ["ia","na"]
        aelodE = Combobox (newinfS,values=list1)
        
        #buttons
        costB = Button (newinfS, text="Find Cost",command = findCost)
        back = Button (newinfS, text="Go Back",command = goback)
        inputbut = Button (newinfS, text="input",command = inpt)

        #the grid
        titleL1.grid (column = 0,columnspan = 2, row = 0)
        titleL2.grid (column = 0,columnspan = 2, row = 1)
        enwL.grid (column = 0, row = 2)
        enwE.grid (column = 1, row = 2)
        sizeL.grid (column = 0, row = 3)
        sizeE.grid (column = 1, row = 3)
        numL.grid (column = 0, row = 4)
        numE.grid (column = 1, row = 4)
        ebostL.grid (column = 0, row = 5)
        ebostE.grid (column = 1, row = 5)
        aelodL.grid (column = 0, row = 6)
        aelodE.grid (column = 1, row = 6)
        amserL.grid (column = 0, row = 7)
        amserE.grid (column = 1, row = 7)
        amserampm.grid (column = 2,row = 8)
        amserDL.grid (column = 0, row = 8)
        amserDE.grid (column = 1, row = 8)
        diwrnodDL.grid (column = 0, row = 9)
        diwrnodDE.grid (column = 1, row = 9)
        costB.grid (column = 2, row = 10)
        costE.grid (column = 3, row = 10)
        inputbut.grid (column = 1, row = 10)
        back.grid (column = 0, row = 10)
        

    def curinf ():

        #creu function i fynd nol ir scrin tools
        def goback():
            tools()
            curinfS.destroy()
                
        #making the screen and changing name size and background colour
        curinfS = Tk()
        curinfS.geometry ("700x500")
        curinfS.configure(bg = "#0cc0df")
        curinfS.title ("Tools Screen")
        toolScreen.destroy ()
        
        #buttons
        back = Button (curinfS, text="Go Back",command = goback)

        #the grid
        back.grid (column = 0, row = 0)
        
    def finboo ():
        def findbook():
            box.delete("0.0",END)
            boatsize = seisEn.get()
            bookingnumber = numEn.get()
            if boatsize!="":
                r=0
                with open ("number.txt","r") as f:
                    num=f.read()
                    print (num)
                    num = int(num)
                    num2=num-1
                    r=int(r)
                    while r<=num2:
                        r=str(r)
                        with open(r+".txt","r") as p:
                            if r==num2:
                                break
                            r=int(r)
                            r=r+1
                            red = p.read()
                            if boatsize in red:
                                box.insert(END,red+"\n")
                            r=int(r)
            elif bookingnumber!="":
                
                bookingnumber = str(bookingnumber)
                with open(bookingnumber+".txt","r") as f:
                    
                    content = f.read()
                    
                    box.insert(END,content+"\n")
                    
            else:
                messagebox.showinfo("error","something must be in one of the bocses")
        #creu function i fynd nol ir scrin tools
        def goback():
            tools()
            finboo.destroy()
            
        #making the screen and changing name size and background colour
        finboo = Tk()
        finboo.geometry ("700x500")
        finboo.configure(bg = "#0cc0df")
        finboo.title ("Sgrin Ffeindio bwciad")
        toolScreen.destroy ()

        #labels
        titleL1 = Label (finboo, width="15",text="Bwciadau", font = ("courier new",20),bg = "#0cc0df")
        titleL2 = Label (finboo, width="15",text="Ffeundio Bwciad", font = ("courier new",15),bg = "#0cc0df")
        seisL = Label (finboo, width="10",text="Seis Cwch:", font = ("courier new",11),bg = "#0cc0df")
        numS = Label (finboo, width="12",text="rhif cwsmer:", font = ("courier new",11),bg = "#0cc0df")

        #Entrys
        seisEn = Entry (finboo,width=15)
        numEn = Entry (finboo,width=15)
        
        #Boxes
        box = Text(finboo,height=20,width=20)
        #buttons
        back = Button (finboo, text="Go Back",command = goback)
        find = Button (finboo, text="Find Booking",command = findbook)
        #the grid
        back.grid (column = 0, row = 90)
        find.grid (column = 1, row = 90)
        titleL1.grid (columnspan = 2,row = 0)
        titleL2.grid (columnspan = 2,row = 1)
        seisL.grid (column = 0,row = 2)
        seisEn.grid (column = 1,row = 2)
        numS.grid (column = 2,row = 2)
        numEn.grid (column = 3,row = 2)
        box.grid (column = 0,row = 3)

    def fininf ():

        #creu function i fynd nol ir scrin tools
        def goback():
            tools()
            fininf.destroy()
            
        #making the screen and changing name size and background colour
        fininf = Tk()
        fininf.geometry ("700x500")
        fininf.configure(bg = "#0cc0df")
        fininf.title ("Tools Screen")
        toolScreen.destroy ()
        
        #buttons
        back = Button (fininf, text="Go Back",command = goback)

        #the grid
        back.grid (column = 0, row = 0)

    #creating the tool screen and changing the background colour and the size of it
    toolScreen = Tk ()
    toolScreen.geometry ("700x500")
    toolScreen.configure(bg = "#0cc0df")
    toolScreen.title ("Tools Screen")

    #labels
    title99 = Label (toolScreen, width="15",text="offer", font = ("courier new",20),bg = "#0cc0df")
    
    #buttons
    newinf = Button (toolScreen, text="new customer",command = newinf)
    curinf = Button (toolScreen, text="current customer",command = curinf)
    finboo = Button (toolScreen, text="find booking",command = finboo)
    fininf = Button (toolScreen, text="find customer information",command = fininf)
    close = Button (toolScreen, text="sign out",command = close)
    
    #putting it on the grid
    title99.grid(columnspan = 1,row=0)
    newinf.grid(column = 0, row = 1)
    curinf.grid(column = 0, row = 2)
    finboo.grid(column = 0, row = 3)
    fininf.grid(column = 0, row = 4)
    close.grid(column = 0, row = 5)

#running the funtion
signInS ()
