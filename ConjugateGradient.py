from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
import numpy as np
from scipy import misc 
import matplotlib.pyplot as plt
import math
from numpy import linalg as la
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

from sympy import symbols, diff
from sympy.utilities.lambdify import lambdify
from sympy.solvers import solve

import sympy as sp
from sympy.functions import exp,log
from sympy import cos,sin,pi
from sympy.abc import x
import sys




class ConjugateGradient :
    varglob = 0
    def __init__(self, fenetr8):
        self.fenetr8=fenetr8
        #-----------le titre--------------------------------------------------#
        self.fenetr8.title(" Conjugate Gradient ")
        #-----------------la geometrerde la fenetre---------------------------#
        self.fenetr8.geometry("1000x720+150+50")
        #-----------------le coleure de bag-----------------------------------#
        self.fenetr8.config(bg="#919FA0")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        self.fenetr8.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        self.fenetr8.iconbitmap("images/logoimag.ico")
        #==============self.frame1  ===============================================#
        self.frame1 = Frame( self.fenetr8, bg="#919FA0", highlightbackground="#182350",highlightthickness=2)
        self.frame1.place(x=48,y=30, height=660,width=900)
        #===============title=================================================#
        title = Label( self.fenetr8,text=" Conjugate Gradient ",font=("Comic Sans MS", 17,"bold"), bg="#919FA0",fg="#D7E5EE").place(x=380,y=5)
       
        #----------------les entrer de l'algorithme---------------------------#
        entrer = Label(self.frame1,text="Input { ",font=("Comic Sans MS", 16,"bold"), bg="#919FA0",fg="#182350").place(x=10,y=10)
        
        #======================l'order  =======================================#
        lorder = Label(self.frame1,text="The dimension       :",font=("Comic Sans MS", 15,"bold"), bg="#919FA0").place(x=110,y=30)
        
        #---------------------------------------------------------------------#
        self.valop = IntVar() 
        self.cmb_lorder = ttk.Combobox(self.frame1, font=("times new romman", 13,"bold"),state='readonly',justify=CENTER, textvariable=self.valop)
        self.cmb_lorder['values']=(" 2 "," 3 ")
        self.cmb_lorder.place(x=440, y=33,width=120)
        self.cmb_lorder.current(0)
        
        #-----------------button ----------------------------------------------------#
        Order_Button  = Button(self.frame1,font=("times new romman",12, "bold"),text="change dimension", bg="#CBDDDD", activebackground ="#3E574F", activeforeground="#A22B2B",borderwidth = 2, command = self.chengdim).place(x=620 ,y=133,width=215)
        #=================l'intervale ========================================#
        intervale = Label(self.frame1,text="Initial point x0      :",font=("Comic Sans MS", 15,"bold"),bg="#919FA0").place(x=110,y=110)
        
        #================vale de x1 ==========================================#
        txtval1 = Label(self.frame1,text="x[0]  ",font=("Comic Sans MS", 15, "bold"), bg="#919FA0").place(x=385,y=80)
        self.txtvar1 = DoubleVar()
        self.txt_valx1 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable= self.txtvar1)
        self.txt_valx1.place(x=440,y=83, width=60)
        self.txtvar1.set("")
        
        
        #================la valeure de x2 ====================================#
        valbb2 = Label(self.frame1,text="x[1]  ",font=("Comic Sans MS", 15,"bold"), bg="#919FA0").place(x=385,y=120)
        self.txttvarr2 = DoubleVar()
        self.txt_valy2 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txttvarr2)
        self.txt_valy2.place(x=440,y=123, width=60)
        self.txttvarr2.set("")
        #================la valeure de x3====================================#
        self.vagx3 = StringVar()
        valbb2 = Label(self.frame1, font=("Comic Sans MS", 15,"bold"), bg="#919FA0", textvariable = self.vagx3 ).place(x=385,y=160)
        self.vagx3.set("")
        #===================la fonction=======================================#
        self.fonc = Label(self.frame1,text="Function             :", font=("Comic Sans MS", 16,"bold"), bg="#919FA0").place(x=110,y=210)
        self.foncFtion = Label(self.frame1,text="f(x) = ",font=("Comic Sans MS", 16,"bold"),bg="#919FA0").place(x=355,y=210)
        self.tcrrft = StringVar()
        self.txt_fonctin = Entry(self.frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350", textvariable= self.tcrrft)
        self.txt_fonctin.place(x=440,y=213,width=397 )
        self.tcrrft.set("")
      
        
        
        #=================fermer l'accolade===================================#
        self.coladfer = Label(self.frame1,text=" } Output   :",font=("Comic Sans MS", 15,"bold"),bg="#919FA0",fg="#182350").place(x=10,y=280)
        
        #==============self.frame1  ===============================================#
        self.frame2=Frame( self.frame1,bg="#C4C6C6" ,highlightbackground="#181C1B",highlightthickness=2)
        self.frame2.place(x=10, y=330,height=320,width=875)
        
        #=================================================solution ===========================================#
        #---------------la valeur exacte de la solution si l'algorithme arive a calculer x*--------------------------------#
        val_solution_exact = Label(self.frame2,text="The solution   ",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=20,y=10)
        #-----------------------------------------------x*-----------------------------------------------------------------#
        val_solNew = Label(self.frame2,text=" x*:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=240,y=20)
        self.varsolQuasiNeew = StringVar()
        self.txtSolExacNew = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="green", textvariable=self.varsolQuasiNeew)
        self.varsolQuasiNeew.set("")
        self.txtSolExacNew.place(x=290, y=23, width=550)# , height= 30
        
        
        #--------------------------------val des nomber des itoration  i ----------------------------------------#
        self.nbr_Sect_iteration = Label(self.frame2,text="Number of iterations ",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=100)
        self.txt_itera_Section = Label(self.frame2,text=" i :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=100)
        self.var_sect_itir = IntVar()
        self.txt_itera_Sect= Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="red", textvariable=self.var_sect_itir)
        self.var_sect_itir.set("")
        self.txt_itera_Sect.place(x=290,y=103,width=160)
      
        #---------------------------------------Solution----------------------------------------------------------#

        #---------------------------------------interprétation----------------------------------------------------#
        self.nbr_iterpretaSecti = Label(self.frame2,text="Interpretation   ",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=180)
        self.var_iterpreSect = StringVar()
        self.txt_iterpretatSect = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.var_iterpreSect)
        self.var_iterpreSect.set("")
        self.txt_iterpretatSect.place(x=290,y=183,width=545)

        #=========================================================== boutton Quasi New =========================================================================================================#
        QuasiNew_Button  = Button(self.frame2,font=("times new romman",16,"bold"),text=" Conjugate Gradient",bd=0,cursor="hand2", bg="#78A7B0",fg="#E5E1D6",activebackground ="#7AA1E6",activeforeground="#BF846C",borderwidth = 5, command =self.ConjugateGradient).place(x=320 ,y=240,width=240)
           
       #============================================================ Bouton le graphe de la fonction ===========================================================================================#
        graphedefa= Button(self.frame2,font=("times new romman",16,"bold"),text="graph of the fonction",bd=0,cursor="hand2",bg="#7B9764",fg="#E5E1D6",activebackground ="#CDD3C8",activeforeground="#BFF790",borderwidth = 5, command=self.graphe_de_fonction).place(x=10 ,y=240,width=240)
        
     
        #============================================================ Bouton quitt ============================================================================================================#
        quittbutnn= Button(self.frame2,font=("times new romman",16,"bold"),text="Quit ",bd=0,cursor="hand2",bg="#AD2E15", fg="#F3EEED", activebackground ="#CAE5E4",activeforeground="#E8A490",borderwidth = 5, command=self.quiter).place(x=640 ,y=240,width=200)
  
    
  #-------------Pour quiter------------------------------------#       
    def quiter(self):
        self.fenetr8.destroy()
      
        
        
     #----------------pour vider les comps------------------------------------#
    def clearChamp(self):
        self.txtSolExacNew.delete(0, END)
        self.txt_itera_Sect.delete(0, END)
        self.txt_iterpretatSect.delete(0, END)
    
  
    
  
    
  
    
    def chengdim(self):
         global varglob
         if(self.valop.get()==3): 
             varglob = 1
             
             self.txttvarr3 = DoubleVar()
             self.txt_valy3 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txttvarr3)
             self.txt_valy3.place(x=440,y=163,width=60)
             self.txttvarr3.set("")
             self.vagx3.set("x[2]")
             
         elif(self.valop.get() == 2 and varglob == 1):    
             self.txt_valy3.destroy()
             self.vagx3.set(" ")
             varglob = 0
             
      #---------------------------l'lgorithm----------------------------------#
    def function2(self, x):
        func = self.txt_fonctin.get()
        f = str(func)
        x, y= symbols('x y', real=True)
        func=eval(f)
        return func
    
    def function3(self, x):
        func = self.tcrrft.get()
        f = str(func)
        x, y, z = symbols('x y z', real=True)
        func=eval(f)
        return func
        # ----------le gradient de f --------------------------#

    def grad(self, f):
        x, y = symbols('x y', real=True)
        dx = diff(f(x), x)
        dy = diff(f(y), y)
        return np.transpose(np.array([dx, dy]))
        # ------------le gradiein en un point -----------------#

    def evalgrad(self, point, fonc):
        Res = self.grad(fonc)
        # print("Res = ", Res)
        fon1 = str(Res[0])
        fon2 = str(Res[1])
        x = point[0]
        y = point[1]

        def avalF1(x):
            x = point[0]
            y = point[1]
            t = eval(fon1)
            return t

        def avalF2(y):
            x = point[0]
            y = point[1]
            p = eval(fon2)
            return p

        y1 = avalF1(x)
        y2 = avalF2(y)
        resultt = np.array([y1, y2]).flatten()
        return resultt
    
    def hessien(self, f):
        x, y = symbols('x y', real=True)
        H = np.array([x ,y])
        Resgrad = self.grad(f)
        M = Resgrad[0]
        print(M)
        N = Resgrad[1]
        def foncM(x):
            x, y = symbols('x y', real=True)
            a = eval(str(M))
            return a
        def foncN(x):
            x, y = symbols('x y', real=True)
            b = eval(str(N))
            return b           
        dxx = diff(foncM(x), x, x)
        dxy = diff(foncM(x), x, y)
        dyx = diff(foncN(x), y, x)
        dyy = diff(foncN(x), y, y)
        H = np.array([[dxx , dxy], [dyx , dyy]])
        return H
    
      
    def ConjugateGradient(self):
        self.clearChamp()
        val1 = self.txtvar1.get()
        val2 = self.txttvarr2.get()
        func = self.tcrrft.get()
        
        if(val1 =="" or val2 ==""  or func =="" ):
             MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetr8)
        else :
             try:  
                 if(self.valop.get()==2): 
                        alpha = 1
                        dim = 2
                        x1 = float(val1)
                        x2 = float(val2)
                        x0 = np.array([x1, x2])
                        xk = x0
                        d0 = - self.evalgrad(x0 , self.function2)
                        dk = d0
                        Q = self.hessien(self.function2)
                        for k in range(dim-1):
                            dkt_dk = np.dot(np.transpose(dk),dk)
                            Qdk = np.dot(Q,dk)
                            dkt_Qdk = np.dot(np.transpose(dk), Qdk)
                            xk = xk + alpha * dk
                            beta = (np.dot(np.transpose(self.evalgrad(xk , self.function2)), Qdk))/dkt_Qdk
                            dk = - self.evalgrad(xk, self.function2) + beta*dk
                        x=xk
                        print(x)
             except Exception as es:                  
                  MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetr8) 



# f=input("donner la fonction")
# x0=input("donner le point initial")
# ConjugateGradient(f,x0)
  
    
  
  
    #======================Le gghaphe de la fonction==========================#   
    def graphe_de_fonction(self):
            fonc = self.tcrrft.get()
            if(fonc =="" ):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetr8)
            elif(self.valop.get() == 2):
                try:
                    def fon(x, y):
                        evalfon = eval(fonc)
                        return evalfon
                    fig = plt.figure(figsize=(10, 8))
                    ax = fig.gca(projection='3d')
                    ax.set_title('3D Surface Plot of ' + ' f = ' + str(fonc))
                    ax.set_xlabel('x axis')
                    ax.set_ylabel('y axis')
                    ax.set_zlabel('z axis')

                    x = np.arange(-10, 10, 0.05)
                    y = np.arange(-10, 10, 0.05)
                    x, y = np.meshgrid(x, y)
                    
                    f = fon(x,y)
                    surface = ax.plot_surface(x, y, f, cmap=cm.coolwarm, linewidth=0)
                    fig.colorbar(surface, shrink=0.5)
                    plt.show()
                    
                except Exception as es:                  
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetr8) 
                   
            elif(self.valop.get() == 3):
                 pass
                 #---le graphe de fonction 3D --------------------#
  
    
  
    
  
    
  
    
  
    
  
    
  
    
# fenetr8 = Tk()
# obj=ConjugateGradient(fenetr8)
# fenetr8.mainloop()      




 #================vale de ligne 1 ==========================================#
        # self.txtvaq11 = DoubleVar()
        # self.txt_vaq11 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable = self.txtvaq11)
        # self.txt_vaq11.place(x=110,y=93,width=50)
        # self.txtvaq11.set("")
    
        
        # self.txtq12 = DoubleVar()
        # self.txt_vq12 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txtq12)
        # self.txt_vq12.place(x=250,y=93,width=50)
        # self.txtq12.set("")
        
        # self.txtvaq13 = DoubleVar()
        # self.txt_vaq13 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable = self.txtvaq13)
        # self.txt_vaq13.place(x=180,y=93,width=50)
        # self.txtvaq13.set("")
        #================la valeure de LIGNE 2 =====================================#
       
        # self.txtq21 = DoubleVar()
        # self.txt_vq21 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txtq21)
        # self.txt_vq21.place(x=180,y=133,width=50)
        # self.txtq21.set("")
        
        # self.txtq22 = DoubleVar()
        # self.txt_vq22 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txtq21)
        # self.txt_vq22.place(x=110,y=133,width=50)
        # self.txtq22.set("")
        
        # self.txtq23 = DoubleVar()
        # self.txt_vq23 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txtq23)
        # self.txt_vq23.place(x=250, y=133,width=50)
        # self.txtq23.set("")
        
        #====================================ligne 3==================================#
        # self.txtvaq31 = DoubleVar()
        # self.txt_vaq31 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable = self.txtvaq31)
        # self.txt_vaq31.place(x=180,y=173,width=50)
        # self.txtvaq31.set("")
        
        # self.txtq32 = DoubleVar()
        # self.txt_vq32 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txtq32)
        # self.txt_vq32.place(x=110, y=173,width=50)
        # self.txtq32.set("")
        
        # self.txtq33 = DoubleVar()
        # self.txt_vq33 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txtq33)
        # self.txt_vq33.place(x=250, y=173,width=50)
        # self.txtq33.set("")
         #=================le vecteure b ========================================#
        # intervb = Label(self.frame1,text=" b:",font=("Comic Sans MS", 15,"bold"),bg="#919FA0").place(x=450,y=130)
        # #================vale de b1 ==========================================#
        # self.txtvarB1 = DoubleVar()
        # self.txt_vabx = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable = self.txtvarB1)
        # self.txt_vabx.place(x=490,y=93,width=50)
        # self.txtvarB1.set("")
        
        
        # #================la valeure de b2 =====================================#
        # self.txtvarb2 = DoubleVar()
        # self.txt_vb2 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txtvarb2)
        # self.txt_vb2.place(x=490,y=133,width=50)
        # self.txtvarb2.set("")
        
        # #================la valeure de b3 ====================================#
        # self.txtvarb3 = DoubleVar()
        # self.txt_vb3 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txtvarb2)
        # self.txt_vb3.place(x=490,y=173,width=50)
        # self.txtvarb3.set("")
       