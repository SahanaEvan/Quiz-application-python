import tkinter
from tkinter import *
window=Tk()
score=0;score1=0;count=0;y=0;z=0

#history
def fn1(): 
    #his=Tk()
    his=tkinter.Toplevel()
    his.title('HOW WELL DO YOU KNOW INDIAN HISTORY?')
    
    img=PhotoImage(file='history_root.png')
    canvas=Canvas(his,width=8000,height=8000)
    canvas.create_image(0,0,anchor=NW,image=img)
    canvas.grid(row=0,column=0)
    def win():
        global score
        score+=1
        a=Label(his,text="Smarty!",font=30,bg='lawngreen')
        a.place(x=1000,y=y)
    def lose():
        a=Label(his,text="Oops!",font=30,bg='firebrick1')
        a.place(x=1000,y=z)
    def final_score():
        global score
        b=Label(his,text=("Your final score :",score),font=30)
        b.place(x=1200,y=750)
        
        
    
#Add label for question and button for options
    def q1():
        global y
        global z
        y=50;z=50
        q1=Label(his,text='1.Hawa Mahal was built by :',font=30,bg='burlywood2')
        
        q1.place(x=0,y=0)
        o1=Button(his,text='Akbar',padx=10,command=lose,font=30,bg='burlywood1')
        
        o1.place(x=0,y=50)
        o2=Button(his,text='Sawai pratap singh',padx=10,command=win,font=30,bg='burlywood1')
        
        o2.place(x=100,y=50)
        o3=Button(his,text='Aurangzeb',padx=10,command=lose,font=30,bg='burlywood1')  
        o3.place(x=350,y=50)
       
        nex=Button(his,text="Next question",padx=10,command=q2,font=30,bg='burlywood1')
        nex.place(x=1000,y=100)
        
      
    def q2():
        global y
        global z
        y=250;z=250
        q2=Label(his,text='2.The _____ in jaipur is an astronomical observatory built in 18th century',font=74,bg='burlywood2')
        
        q2.place(x=0,y=200)

        o1=Button(his,text='Jantar Mantar',padx=10,command=win,font=30,bg='burlywood1')
        
        o1.place(x=0,y=250)
    
        o2=Button(his,text='Taj Mahal',padx=10,command=lose,font=30,bg='burlywood1')
            
        o2.place(x=200,y=250)

        o3=Button(his,text='Hawa Mahal',padx=10,command=lose,font=30,bg='burlywood1')  
    
        o3.place(x=400,y=250)

        nex=Button(his,text='Next Question',padx=10,command=q3,font=30,bg='burlywood1')
    
        nex.place(x=1000,y=300)

 
    def q3():
        global y,z
        y=450
        z=450
        q3=Label(his,text='Indian scholar,politician who was known as grand old man of india ',font=74,bg='burlywood2')
       
        q3.place(x=0,y=400)
        o1=Button(his,text='Dadabhai naoroji',padx=10,command=win,font=30,bg='burlywood1')
        
        o1.place(x=0,y=450)
        o2=Button(his,text='Khan Abdul Gafar Khan',padx=10,command=lose,font=30,bg='burlywood1')
        
        o2.place(x=200,y=450)
        o3=Button(his,text='Balgangadhar tilak',padx=10,command=lose,font=30,bg='burlywood1')  
       
        o3.place(x=450,y=450)
        nex=Button(his,text="Next question",padx=10,command=q4,font=30,bg='burlywood1')
       
        nex.place(x=1000,y=500)
    def q4():
        global y,z
        y=600
        z=600
        q4=Label(his,text='The britisher who drew the India-Pakistan border and divided lives and minds',font=74,bg='burlywood2')
        q4.place(x=0,y=550)
        o1=Button(his,text='John Radcliffe',padx=10,command=win,font=30,bg='burlywood1')
        o1.place(x=0,y=600)
        o2=Button(his,text='Mountbatten',padx=10,command=lose,font=30,bg='burlywood1')
        o2.place(x=200,y=600)
        o3=Button(his,text='Curzon',padx=10,command=lose,font=30,bg='burlywood1')  
        o3.place(x=400,y=600)
        nex=Button(his,text="Next question",padx=10,command=q5,font=30,bg='burlywood1')
        nex.place(x=1000,y=650)
    def q5():
        global y,z
        y=700
        z=700
        q5=Label(his,text='The british general who ordered the troops for the massacre at Jallianwala bagh',font=74,bg='burlywood2')
        q5.place(x=0,y=700)
        o1=Button(his,text='Dalhousie',padx=10,command=lose,font=30,bg='burlywood1')
        o1.place(x=0,y=750)
        o2=Button(his,text='Reginald Dyer',padx=10,command=win,font=30,bg='burlywood1')
        o2.place(x=200,y=750) 
        o3=Button(his,text='William Bentick',padx=10,command=lose,font=30,bg='burlywood1')
        o3.place(x=400,y=750)
        nex=Button(his,text="Display my result",padx=10,command=final_score,font=30,bg='burlywood1')
        nex.place(x=1000,y=750)
    q1()
    his.mainloop()
def fn2():
        import tkinter
        
        geo=tkinter.Toplevel()
        geo.title("MOTHER EARTH-THE REAL BEAUTY")
        img1=PhotoImage(file='finalgeo.png')
        #img2=PhotoImage(file='sea of stars.png')
        img=PhotoImage(file='geo_root.png')
        canvas=Canvas(geo,width=10000,height=10000)
        canvas.create_image(0,0,anchor=NW,image=img)
        #canvas.create_image(0,0,anchor=NW,image=img)
        canvas.create_image(0,300,anchor=NW,image=img1)
        #canvas.create_image(0,550,anchor=NW,image=img2)
        canvas.grid(row=0,column=0)
        def win():
            global score1
            score1+=1
            a=Label(geo,text="Smarty!",font="Castellar",fg="black",bg="green",padx=43)
            a.place(x=800,y=100)
        def lose():
            global score1
            a=Label(geo,text="Oops!",font="Castellar",padx=60,fg="pink",bg="red")
            a.place(x=800,y=100)
        def final_score():
            b=Label(geo,text=("Your final score :",score1),font=30,fg="darkgreen",bg="palegreen",)
            b.place(x=1300,y=200)
            
            
        def q1():
            
            #canvas=Canvas(geo,width=10000,height=10000)
            #canvas.create_image(0,200,anchor=NW,image=img1)
            #canvas.grid(row=100,column=0)
            q1=Label(geo,text='GUESS THE TWO LOCATIONS:',font=100,bg='limegreen',padx=500,pady=20)
            q1.place(x=100,y=10)
        
            o1=Button(geo,text='1.Kefalonia,Greece',padx=10,command=lose,font=40,)
            o1.place(x=0,y=150)
    
            o2=Button(geo,text='2.Christmas Island,Australia',padx=10,command=win,font=40)
            o2.place(x=250,y=150)
    
            
    
            o5=Button(geo,text='3.Wagait Beach,Australia',padx=10,command=lose,font=40)  
            o5.place(x=600,y=150)
    
            o6=Button(geo,text='4.Vaadhoo Beach,Maldives',padx=10,command=win,font=40)  
            o6.place(x=900,y=150) 
    
            nex=Button(geo,text="I'm Curious to know my result :P",command=final_score,font=30)
            nex.place(x=1200,y=230)
        q1()
        geo.mainloop()
def fn3():
    import tkinter
    root=tkinter.Toplevel()
    root.geometry("2000x2000")
    
    
    
    lab=Label(root,text="GUESS THE LOGOS  AND  TAGLINES",font="10").grid(row=0,column=1)
    c=Canvas(root,height=110,width=200,bg="pink")
    c.grid(row=3,column=0)
    img=PhotoImage(file="nike.png")
    c.create_image(0,3,anchor=NW,image=img)

    
    lab=Label(root,text="1. the tag line of the company is  ",font=10).grid(row=2,column=0)


    def ans():
        lab2 = Label(root, text=" the answer is true", font=5,padx=30).grid(row=7, column=0)
        global count
        count += 1


    def notans1():
        lab2 = Label(root, text="sorry the answer is wrong",font=5, padx=20).grid(row=7, column=0)

    but1 = Button(root, text="Just Do it", padx=10,font="10" ,command=ans).grid(row=4, column=0)
    but2 = Button(root, text="The Power of Dreams",font="10", padx=10, command=notans1).grid(row=5, column=0)
    but3 = Button(root, text="Broadcast Yourself",font="10", padx=10, command=notans1).grid(row=6, column=0)

    def q2():
        c1=Canvas(root,height=180,width=180,bg="pink")

        c1.create_image(0,0, anchor=NW,image=img1)
        c1.grid(row=10, column=0)

        lab=Label(root,text="2. the tag line of the company is  ",font=10).grid(row=9,column=0)


        def ans():
            lab2 = Label(root, text=" the answer is true", font=5,padx=30).grid(row=14, column=0)
            global count
            count += 1


        def notans1():
            lab2 = Label(root, text="sorry the answer is wrong",font=5, padx=20).grid(row=14, column=0)

        but1 = Button(root, text="Think Different", padx=10,font="10" ,command=ans).grid(row=11, column=0)
        but2 = Button(root, text="Behind Your Imagination",font="10", padx=10, command=notans1).grid(row=12, column=0)
        but3 = Button(root, text="Don't Do the Right Thing",font="10", padx=10, command=notans1).grid(row=13, column=0)
        butans=Button(root,text="next",command=q3,font=1).grid(row=15,column=0)
    img1=PhotoImage(file="applelogo.png.png")
    but=Button(root,text="Next",font=5,command=q2).grid(row=8,column=0)



    def q3():
        c2=Canvas(root,height=180,width=350,bg="pink")

        c2.create_image(0,0, anchor=NW,image=img2)
        c2.grid(row=3, column=1)

        lab=Label(root,text="3. the tag line of the company is  ",font=10).grid(row=2,column=1)


        def ans():
            lab2 = Label(root, text=" the answer is true", font=5,padx=30).grid(row=7, column=1)
            global count
            count += 1


        def notans1():
            lab2 = Label(root, text="sorry the answer is wrong",font=5, padx=20).grid(row=7, column=1)

        but1 = Button(root, text="Today is hard ,Tomorrow is worse but \nthe day after tommorow is sunshine", padx=10,font="10" ,command=ans).grid(row=4, column=1)
        but2 = Button(root, text="Being Ahead Through Technology ",font="10", padx=10, command=notans1).grid(row=5, column=1)
        but3 = Button(root, text="I dont care that they stole my idea...\n I care that they don't have any of their own",font="10", padx=10, command=notans1).grid(row=6, column=1)
        butans = Button(root, text="next", command=q4, font=1).grid(row=8, column=1)
    img2=PhotoImage(file="alibaba.png")
    
    def q4():
        c2=Canvas(root,height=220,width=600,bg="pink")

        c2.create_image(0,0, anchor=NW,image=img4)
        c2.grid(row=3, column=2)

        lab=Label(root,text="4.identify the above companies relating to their logos",font=10).grid(row=2,column=2)
        

        def ans():
            lab2 = Label(root, text=" the answer is true", font=5,padx=30).grid(row=8, column=2)
            global count
            count += 1
            


        def notans1():
            lab2 = Label(root, text="sorry the answer is wrong",font=5, padx=20).grid(row=8, column=2)
        def res():
            
            lab=Label(root,text="YOUR SCORE IS "+str(count)).grid(row=10,column=2)
            global logo_score
            logo_score=count
        but1 = Button(root, text="TESLA", padx=10,font="10" ,command=ans).grid(row=4, column=2)
        but2 = Button(root, text="BOING",font="10", padx=10, command=ans).grid(row=5, column=2)
        but3 = Button(root, text="NIKOLA",font="10", padx=10, command=notans1).grid(row=6, column=2)
        but4 = Button(root, text="AIRBUS", font="10", padx=10, command=notans1).grid(row=7, column=2)
        but5 = Button(root, text="COLLINS AEROSPACE", font="10", padx=10, command=notans1).grid(row=7, column=2)
        butans=Button(root,text="RESULT",command=res).grid(row=9,column=2)

    img4=PhotoImage(file="tesla_Boeing.png")
    
        

    root.mainloop()
def fn4():
    import tkinter
    ro=tkinter.Toplevel()
    ro.title('HOW WELL DO YOU KNOW COMPUTER BASICS')
    frame=Frame(master=ro,width=10000,height=10000)
    frame.place(x=0,y=0)
    img=PhotoImage(file='comp.png')
    canvas=Canvas(frame,width=10000,height=10000)
    canvas.create_image(0,0,anchor=NW,image=img)
    canvas.grid(row=0,column=0)
    
    count=0
#1
    label=Label(ro,text="First Part of the quiz \nBasic computer Quiz",bg= "goldenrod2",fg="black" ,font=3)
    label.grid(row=1,column=1)
    lb1=Label(ro,text=" 1.who is the father of quantum computing")
    lb1.grid(row=2,column=0)
    def ans():

            lab2=Label(ro,text=" the answer is true",padx=30)
            lab2.grid(row=6,column=0)
            global count
            count+=1
    def notans1():

            lab2=Label(ro,text="sorry the answer is wrong",padx=20).grid(row=6,column=0)
    def notans2():

            lab2=Label(ro,text="sorry the answer is wrong",padx=20).grid(row=6,column=0)


    but1=Button(ro,text="David Deutsch",padx=10,command=ans).grid(row=3,column=0)
    but2=Button(ro,text="Michel Faraday",padx=10,command=notans1).grid(row=4,column=0)
    but3=Button(ro,text="Nikola Tesla",padx=10,command=notans2).grid(row=5,column=0)

#2
    def next():

        lb2=Label(ro,text="2. who is the first programer in the world").grid(row=8,column=0)
        def ans1():
            lab2=Label(ro,text="correct!",padx=50).grid(row=12,column=0)
            global count
            count+=1
        def notans():
            lab2 = Label(ro, text="sorry the answer is wrong",padx=20).grid(row=12, column=0)


        but1=Button(ro,text="Ada Lovelace",padx=10,command=ans1).grid(row=9,column=0)
        but2=Button(ro,text="charles Babbage",padx=10,command=notans).grid(row=10,column=0)
        but3=Button(ro,text="dennis Ratchie",padx=10,command=notans).grid(row=11,column=0)
        but = Button(ro, text="NEXT", command=next1).grid(row=13, column=0)
    but=Button(ro,text="NEXT",command=next).grid(row=7,column=0)
#3
    def next1():
        lb2=Label(ro,text="3.Father of ‘C’ programming language").grid(row=14,column=0)
        def ans1():
            lab3=Label(ro,text="correct! upto the mark",padx=50).grid(row=18,column=0)
            global count
            count+=1
        def notans():
            lab3 = Label(ro, text="soory the answer is wrong",padx=20).grid(row=18, column=0)#18
        but1=Button(ro,text="a. Dennis Ritchie",padx=10,command=ans1).grid(row=15,column=0)
        but2=Button(ro,text="b. charles Babbage",padx=10,command=notans).grid(row=16,column=0)
        but3=Button(ro,text="c. Thomas Kurtz",padx=10,command=notans).grid(row=17,column=0)
        but = Button(ro, text="NEXT", command=next2).grid(row=19, column=0)
#4
    def next2():
        lb2=Label(ro,text="4. programing language used for the development \n of IOS appliactions").grid(row=20,column=0)
        def ans1():
            lab2=Label(ro,text="correct!",padx=50).grid(row=24,column=0)
            global count
            count+=1
        def notans():
            lab2 = Label(ro, text="soory the answer is wrong",padx=20).grid(row=24, column=0)#24


        but1=Button(ro,text="RUBY",padx=10,command=notans).grid(row=21,column=0)
        but2=Button(ro,text="SWIFT",padx=10,command=ans1).grid(row=22,column=0)
        but3=Button(ro,text="PYTHON",padx=10,command=notans).grid(row=23,column=0)
        but = Button(ro, text="NEXT", command=next3).grid(row=25, column=0)

#5
    def next3():
        lb2=Label(ro,text="5. IC chips used in computers are usually made of").grid(row=26,column=0)
        def ans1():
            lab2=Label(ro,text="correct!",padx=50).grid(row=30,column=0)
        global count
        count+=1
        def res():

            lab=Label(ro,text="YOUR SCORE IS "+str(count),padx=100,pady=20).place(x=400,y=300)
            global comp_score
            comp_score=count
       
        def notans():
            lab2 = Label(ro, text="sorry the answer is wrong",padx=20).grid(row=30, column=0)
#30
        but1=Button(ro,text="silicon",padx=10,command=ans1).grid(row=27,column=0)
        but2=Button(ro,text="lead",padx=10,command=notans).grid(row=28,column=0)
        but3=Button(ro,text="gold",padx=10,command=notans).grid(row=29,column=0)
        butt=Button(ro, text="press me to get your result", command=res).grid(row=31,column=0)
    ro.mainloop()

def fn5():
    import tkinter
        
    root=tkinter.Toplevel()
    root.title("****CONSTELLATION****")
    img=PhotoImage(file='const.png')
    canvas=Canvas(root,width=10000,height=10000)
    canvas.create_image(0,0,anchor=NW,image=img)
    canvas.grid(row=0,column=0)
    def win():
        global score
        score+=1
        a=Label(root,text="Smarty!",font="Castellar",fg="black",bg="green",padx=43)
        a.place(x=0,y=200)
    def lose():
        global score
        a=Label(root,text="Oops!",font="Castellar",padx=60,fg="pink",bg="red")
        a.place(x=0,y=200)
    def final_score():
        b=Label(root,text=("Your final score :",score),font=30,fg="white",bg="violet")
        b.place(x=0,y=300)
        global cons_score
        cons_score=score
    def q1():
        
        q1=Label(root,text='NAME THE CONSTELLATION',font=30)
        q1.place(x=0,y=10)
    
        o1=Button(root,text='Cassiopeio',padx=10,command=lose,font=30)
        o1.place(x=0,y=50)
    
        o2=Button(root,text='Ursa Major',padx=10,command=lose,font=30)
        o2.place(x=200,y=50)
    
        o3=Button(root,text='Orion',padx=10,command=win,font=30)  
        o3.place(x=0,y=100)
    
        nex=Button(root,text="I'm Curious to know my result ",command=final_score,font=30)
        nex.place(x=0,y=150)
    q1()
    root.mainloop()



def fn6():
        import tkinter
        roo=tkinter.Toplevel()
        roo.title('FUN AND FILMY')
        
        img=PhotoImage(file='film.png')
        canvas=Canvas(roo,width=8000,height=8000)
        canvas.create_image(0,0,anchor=NW,image=img)
        canvas.grid(row=0,column=0)
        
        
        def win():
            global score
            score+=1
            a1=Label(roo,text="Smarty!",font=30)
            a1.place(x=1000,y=y)
        def lose():
            global score
            a1=Label(roo,text="Oops!",font=30)
            a1.place(x=1000,y=z)
        def final_score():
            b1=Label(roo,text=("Your final score :",score),font=30)
            b1.place(x=1200,y=750)
            global film_score
            film_score=score
    
	
        def q11():
            global y
            global z
            y=50;z=50
            q11=Label(roo,text='1.For which film did Sandra Bullock win her Oscar?',font=30)
            #q1.grid(row=1,column=1)
            q11.place(x=0,y=0)
            o11=Button(roo,text="Ocean's Eight",padx=10,command=lose,font=30)
            #o1.grid(row=1,column=2)
            o11.place(x=0,y=50)
            o21=Button(roo,text='The Blind Side',padx=10,command=win,font=30)
            #o2.grid(row=1,column=4)
            o21.place(x=175,y=50)
            o31=Button(roo,text='Bird Box',padx=10,command=lose,font=30)  
            o31.place(x=350,y=50)
            #o3.grid(row=1,column=1)
            nex=Button(roo,text="Next question",padx=10,command=q21,font=30)
            nex.place(x=1000,y=100)
            #nex.grid(row=2,column=1)
      
        def q21():
            global y
            global z
            y=250;z=250
            q21=Label(roo,text='2.Which actor got his big break playing a lonely schoolboy in About A Boy?',font=74)
            #q2.grid(row=4,column=1)
            q21.place(x=0,y=200)
        
            o12=Button(roo,text='Nicholas Hoult',padx=10,command=win,font=30)
            #o1.grid(row=4,column=2)
            o12.place(x=0,y=250)
	
            o22=Button(roo,text='Dwayne Johnson',padx=10,command=lose,font=30)
            #o2.grid(row=4,column=3)
            o22.place(x=200,y=250)
		
            o32=Button(roo,text='Leonardo DiCaprio',padx=10,command=lose,font=30)  
            #o3.grid(row=4,column=4)
            o32.place(x=400,y=250)

            nex=Button(roo,text='Next Question',padx=10,command=q31,font=30)
            #nex.grid(row=5,column=5)
            nex.place(x=1000,y=300)

 
        def q31():
            global y,z
            y=450
            z=450
            q31=Label(roo,text='What is the name of the second James Bond film? ',font=74)
            #q3.grid(row=7,column=1)
            q31.place(x=0,y=400)
            o13=Button(roo,text='From Russia With Love',padx=10,command=win,font=30)
            #o1.grid(row=7,column=2)
            o13.place(x=0,y=450)
            o23=Button(roo,text='Octopussy',padx=10,command=lose,font=30)
            #o2.grid(row=7,column=4)
            o23.place(x=300,y=450)
            o33=Button(roo,text='Tomorrow Never Dies',padx=10,command=lose,font=30)  
            #o3.grid(row=7,column=5)
            o33.place(x=450,y=450)
            nexty2=Button(roo,text="Next question",padx=10,command=q41,font=30)
            #nex.grid(row=8,column=5)
            nexty2.place(x=1000,y=500)
        def q41():
            global y,z
            y=600
            z=600
            q41=Label(roo,text='Who played the lead role in the 2001 film Lara Croft: Tomb Raider?',font=74)
            #q4.grid(row=10,column=1)
            q41.place(x=0,y=550)
            o14=Button(roo,text='Angelina Jolie',padx=10,command=win,font=30)
            #o1.grid(row=10,column=2)
            o14.place(x=0,y=600)
            o24=Button(roo,text='Emma Watson',padx=10,command=lose,font=30)
            #o2.grid(row=10,column=3)
            o24.place(x=200,y=600)
            o34=Button(roo,text='Scarlett Johansson',padx=10,command=lose,font=30)  
            #o3.grid(row=10,column=4)
            o34.place(x=400,y=600)
            nexty4=Button(roo,text="Next question",padx=10,command=q51,font=30)
            #nex.grid(row=11,column=5)
            nexty4.place(x=1000,y=650)
        def q51():
            global y,z
            y=700
            z=700
            q51=Label(roo,text='What is the highest-grossing box office film of all time?',font=74)
            #q5.grid(row=12,column=1)
            q51.place(x=0,y=700)
            o15=Button(roo,text='Bahubali',padx=10,command=lose,font=30)
            #o1.grid(row=12,column=2)
            o15.place(x=0,y=750)
            o25=Button(roo,text='Avengers: Endgame',padx=10,command=win,font=30)
            #o2.grid(row=12,column=3)
            o25.place(x=200,y=750) 
            o35=Button(roo,text='Transformers',padx=10,command=lose,font=30)  
            #o3.grid(row=12,column=4)
            o35.place(x=500,y=750)
            nexty5=Button(roo,text="Display my result",padx=10,command=final_score,font=30)
            #nex.grid(row=12,column=5)
            nexty5.place(x=1000,y=750)
        q11()
        roo.mainloop()
#Below part is commented to create a screen for score board
'''
def final():
    import tkinter
    
    root=tkinter.Toplevel()
    root.title("MY SCORE BOARD")
    img=PhotoImage(file='board.png')
    canvas=Canvas(root,width=10000,height=10000)
    canvas.create_image(0,0,anchor=NW,image=img)
    canvas.grid(row=0,column=0)
    a=Label(root,text=("Your score in his quiz is",l[0]),font="Castellar",fg="black",bg="green",padx=43)
    a.place(x=0,y=200)
    root.mainloop()
'''



import tkinter

#window=tkinter.Toplevel()
window.title("Hey ! Try This Exciting Quiz and Have Fun")
img=PhotoImage(file='win_root.png')
canvas=Canvas(window,width=8000,height=8000)
canvas.create_image(0,0,anchor=NW,image=img)
canvas.grid(row=0,column=0)


#Create label form question
l=Label(window,text="What's your interest and area of expertise ?",font=('Bold',30),bg='white',fg='gold')
l.place(x=700,y=530)
#Create buttons to call the respective quiz ,font='Comic sans'
b1=Button(window,text="1. I LOVE INDIAN HISTORY!",command=fn1,fg='deepskyblue',bg='white',pady=10,font=("Comic",10,'bold'))
b1.place(x=800,y=600)

b2=Button(window,text="2. HOW ABOUT GEOGRAPHY?",command=fn2,fg='deepskyblue',bg='white',pady=10,font=("Comic",10,'bold'))
b2.place(x=800,y=650)

b3=Button(window,text="3. LOGOS AND TAGLINES:)",command=fn3,fg='deepskyblue',bg='white',pady=10,font=("ComicSans",10,'bold'))
b3.place(x=800,y=700)

b4=Button(window,text="4. HOW ABOUT COMPUTER BASICS",command=fn4,fg='deepskyblue',bg='white',pady=10,font=("ComicSans",10,'bold'))
b4.place(x=1050,y=600)

b5=Button(window,text="5. **CONSTELLATIONS**",command=fn5,fg='deepskyblue',bg='white',pady=10,font=("ComicSans",10,'bold'))
b5.place(x=1050,y=650)



b7=Button(window,text="6. FUN AND FILMY ^~^",command=fn6,fg='deepskyblue',bg='white',pady=10,font=("ComicSans",10,'bold'))
b7.place(x=1050,y=700)

#fi=Button(window,text="MY SCORE BOARD",command=final,fg='darkblue',bg='white',pady=10,font=("ComicSans",10,'bold'))
#fi.place(x=1100,y=750)


window.mainloop()
#intro.mainloop()
