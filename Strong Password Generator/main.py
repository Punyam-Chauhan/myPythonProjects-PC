from tkinter import *
import string
import random
from tkinter import messagebox
cc= ''
master = Tk()
master.after(2000, master.focus_force)
master.title('Strong Password Generator!!')
master.config(bg='cyan')
master.resizable(False,False)

def pwd_gen(qq):
    global cc
    del cc
    sym = {'@',"#","$"}
    length= int(qq)
    b=1
    pwd= ''
    symbo=''
    while b<=(length+1):
        b=b+1
        number = random.randint(0,9)
        letter =  random.choice(string.ascii_letters)
        if b>= round( (length/2)+ (length/4)):
            symbo = random.choice(list(sym))
        a =str(number) + str(letter) + str(symbo)
        pwd = pwd +a
    cc = (''.join(random.sample(pwd , length+2)))
    return cc


ll = Label(text="Strong Password Generator", font= "Times 28 bold", bg='cyan',fg='blue')
ll.grid(row=0,column=0, columnspan=3,padx=10,pady=2)

Label(text='Enter length of Password:', font='Times 12 italic',bg='cyan').grid(row=1,column=0,padx=0,pady=20)
Label(text='Password Choice 1:', font='Times 12 italic',bg='cyan').grid(row=3,column=0,padx=0,pady=1)
Label(text='Password Choice 2:', font='Times 12 italic',bg='cyan').grid(row=4,column=0,padx=0,pady=0)
Label(text='Password Choice 3:', font='Times 12 italic',bg='cyan').grid(row=5,column=0,padx=0,pady=0)

leng= Entry(font='Times 12 ',bg='sky blue')
leng.grid(row=1,column=1,columnspan=2,padx=3)

c1 = Entry(font='Times 12 italic',bg='sky blue')
c1.grid(row=3,column=1,padx=0,pady=1)
c2 = Entry(font='Times 12 italic',bg='sky blue')
c2.grid(row=4,column=1,padx=0,pady=0)
c3 = Entry(font='Times 12 italic',bg='sky blue')
c3.grid(row=5,column=1,padx=0,pady=0)


def genu(ww):
    if ww.strip().isdigit():
        bq = pwd_gen(ww)  
        c1.delete(0,END)  
        if bq[0]=='@' or bq[0]=='#' or bq[0]=='$' :
            bq = bq[2:]
        else:  bq = bq[:-2]
        c1.insert(0,bq)
        

        cq = pwd_gen(ww)  
        c2.delete(0,END)  
        dd=(''.join(random.sample(cq , len(cq))))
        if dd[0]=='@' or dd[0]=='#' or dd[0]=='$' :
            dd = dd[2:]
        else:  dd = dd[:-2]
        c2.insert(0,dd)

        dq = pwd_gen(ww)  
        c3.delete(0,END)  
        c3.insert(0,(''.join(random.sample(bq , len(bq)))))

    else:   
        messagebox.showerror("Error!!", "Invalid Input")
gen = Button(text='Generate!!',font='Times 15 bold',bg='#00aeff', command=lambda: genu(leng.get()))

gen.grid(row=2,column=0,columnspan=2,padx=55, pady=15)

Label(text='  ', bg='cyan').grid(row=6)
Label(text='Made By Punyam Chauhan', bg='cyan', font='Times 10').place(relx = 0.67,rely = 1.0,anchor ='sw')


master.mainloop()