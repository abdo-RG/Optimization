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


sti = "false"
sjk = "false"
l = "false"
class quasiNewton :
    def __init__(self,fenetre7):
        self.fenetre7=fenetre7
        #-----------le titre--------------------------------------------------#
        self.fenetre7.title(" Quasi Newthon ")
        #-----------------la geometrerde la fenetre---------------------------#
        self.fenetre7.geometry("1000x720+150+50")
        #-----------------le coleure de bag-----------------------------------#
        self.fenetre7.config(bg="#BDC29C")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        self.fenetre7.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        self.fenetre7.iconbitmap("images/logoimag.ico")
        #==============self.frame1  ==========================================#
        self.frame1 = Frame( self.fenetre7, bg="#BDC29C", highlightbackground="#182350", highlightthickness=2)
        self.frame1.place(x=48,y=30, height=660,width=900)
        #===============title=================================================#
        title = Label( self.fenetre7,text=" Quasi Newton ",font=("Comic Sans MS", 17,"bold"), bg="#BDC29C",fg="green").place(x=390,y=5)
       
        #----------------les entrer de l'algorithme---------------------------#
        entrer = Label(self.frame1,text="Input { ",font=("Comic Sans MS", 16,"bold"), bg="#BDC29C",fg="#182350").place(x=10,y=10)
        
        #======================l'order  ======================================#
        lorder = Label(self.frame1,text="The dimension       :",font=("Comic Sans MS", 15,"bold"), bg="#BDC29C").place(x=110,y=10)
        
        #---------------------------------------------------------------------#
        self.valop = IntVar() 
        self.cmb_lorder = ttk.Combobox(self.frame1, font=("times new romman", 13,"bold"),state='readonly',justify=CENTER, textvariable=self.valop)
        self.cmb_lorder['values']=(" 2 "," 3 ")
        self.cmb_lorder.place(x=440, y=13,width=160)
        self.cmb_lorder.current(0)
        
         #--------------------------------le chois de pas---------------------#
        labdepas = Label(self.frame1,text="Line Search          :",font=("Comic Sans MS", 15,"bold"), bg="#BDC29C").place(x=110,y=50)
        
        self.valdespas = StringVar() 
        self.cmb_pad = ttk.Combobox(self.frame1, font=("times new romman", 13,"bold"),state='readonly',justify=CENTER, textvariable=self.valdespas)
        self.cmb_pad['values']=( 'Fixe', 'Approcher', 'Optimal')
        self.cmb_pad.place(x=440, y=53,width=160)
        self.cmb_pad.current(0)
        
        #---------------------------------------------------------------------#
        self.var_fixe = IntVar()
        self.txt_fixe_Sect= Entry(self.frame1,font=("times new romman",14,"bold"),  bg="lightgray", fg="#182350", textvariable=self.var_fixe)
        self.txt_fixe_Sect.place(x=660, y=53,width=190)
        self.var_fixe.set("")
        
        #-----------------button ---------------------------------------------#
        Order_Button  = Button(self.frame1,font=("times new romman",12, "bold"),text="change dimension", bg="#CBDDDD", activebackground ="#3E574F", activeforeground="#A22B2B",borderwidth = 2, command =self.changdim).place(x=660 ,y=130,width=190)
        #=================l'intervale ========================================#
        intervale = Label(self.frame1,text="Initial point x0      :",font=("Comic Sans MS", 15,"bold"),bg="#BDC29C").place(x=110,y=110)
        
        #================vale de x1 ==========================================#
        self.txt_val = Label(self.frame1,text="x[0]  ",font=("Comic Sans MS", 15,"bold"),bg="#BDC29C").place(x=385,y=90)
        self.txtvar = DoubleVar()
        self.txt_valx = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable= self.txtvar)
        self.txt_valx.place(x=440,y=93,width=160)
        self.txtvar.set("")
        
        
        #================la valeure de x2 =====================================#
        self.val_b = Label(self.frame1,text="x[1]  ",font=("Comic Sans MS", 15,"bold"),bg="#BDC29C").place(x=385,y=130)
        self.txttvarr = DoubleVar()
        self.txt_valy = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txttvarr)
        self.txt_valy.place(x=440,y=133,width=160)
        self.txttvarr.set("")
       
        #===================la fonction=======================================#
        self.fonc = Label(self.frame1,text="Function             :",font=("Comic Sans MS", 16,"bold"),bg="#BDC29C").place(x=110,y=205)
        self.foncFtion = Label(self.frame1,text="f(x) = ",font=("Comic Sans MS", 16,"bold"),bg="#BDC29C").place(x=355,y=205)
        self.tcrrft = DoubleVar()
        self.txt_fonctin = Entry(self.frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350", textvariable= self.tcrrft)
        self.txt_fonctin.place(x=440,y=208,width=397 )
        self.tcrrft.set("")
        
        #================la tolérence  =======================================#
        self.delt = Label(self.frame1,text="Tolerance            :",font=("Comic Sans MS", 15,"bold"),bg="#BDC29C").place(x=110,y=280)
        self.delT = Label(self.frame1,text="delta =",font=("Comic Sans MS", 15,"bold"),bg="#BDC29C").place(x=360,y=280)
        self.tolerenfonc = DoubleVar()
        self.txt_toler = Entry(self.frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350", textvariable=self.tolerenfonc)
        self.tolerenfonc.set(0.01)
        self.txt_toler.place(x=440,y=283,width=160)
        
        
        #=================fermer l'accolade===================================#
        self.coladfer = Label(self.frame1,text=" } Output   :",font=("Comic Sans MS", 15,"bold"),bg="#BDC29C",fg="#182350").place(x=10,y=315)
        
        #===================frame1============================================#
        self.frame2=Frame( self.frame1,bg="#C4C6C6" ,highlightbackground="#182350", highlightthickness=3)
        self.frame2.place(x=10,y=360,height=285,width=875)
        
        #================= ================solution===========================#
        #---------------la valeur exacte de la solution si l'algorithme arive a calculer x*--------------------------------#
        val_solution_exact = Label(self.frame2,text="The solution   ",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=10,y=10)
        #-----------------------------------------------x*-----------------------------------------------------------------#
        val_solNew = Label(self.frame2,text=" x*:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=240,y=10)
        self.varsolQuasiNeew = StringVar()
        self.txtSolExacNew = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="green", textvariable=self.varsolQuasiNeew)
        self.varsolQuasiNeew.set("")
        self.txtSolExacNew.place(x=290, y=13, width=550)
        
        
        #--------------------------------val des nomber des itoration  i ----------------------------------------#
        self.nbr_Sect_iteration = Label(self.frame2,text="Number of iterations ",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=80)
        self.txt_itera_Section = Label(self.frame2,text=" i :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=80)
        self.var_sect_itir = IntVar()
        self.txt_itera_Sect= Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="red", textvariable=self.var_sect_itir)
        self.var_sect_itir.set("")
        self.txt_itera_Sect.place(x=290,y=83,width=160)
      
        #----------------------------Solution---------------------------------#

        #---------------------------interprétation----------------------------#
        self.nbr_iterpretaSecti = Label(self.frame2,text="Interpretation   ",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=150)
        self.var_iterpreSect = StringVar()
        self.txt_iterpretatSect = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.var_iterpreSect)
        self.var_iterpreSect.set("")
        self.txt_iterpretatSect.place(x=290,y=153,width=545)

        #=========================================================== boutton Quasi New =========================================================================================================#
        QuasiNew_Button  = Button(self.frame2,font=("times new romman",16,"bold"),text="Quasi Newton ",bd=0,cursor="hand2",bg="#7F7526",fg="#E5E1D6",activebackground ="#7AA1E6",activeforeground="#BF846C",borderwidth = 5, command =self.quasi_Newton).place(x=320 ,y=220,width=240)
           
        #============================================================ Bouton le graphe de la fonction ===========================================================================================#
        graphedefa= Button(self.frame2,font=("times new romman",16,"bold"),text="graph of the fonction",bd=0,cursor="hand2",bg="#7B9764",fg="#E5E1D6",activebackground ="#CDD3C8",activeforeground="#BFF790",borderwidth = 5, command=self.graphe_de_fonction).place(x=10 ,y=220,width=240)
        
     
        #============================================================ Bouton quit ============================================================================================================#
        quitbutt= Button(self.frame2,font=("times new romman",16,"bold"),text="Quit ",bd=0,cursor="hand2",bg="#AD2E15", fg="#F3EEED", activebackground ="#CAE5E4",activeforeground="#E8A490",borderwidth = 5, command=self.quiter).place(x=640 ,y=220,width=200)
  
    
   #----------------------------dimention-------------------------------------#
    def changsepas(self):
        global cmb_valApp
        global valAppproch
        global sti
        global  sjk 
        if(self.valdespas.get() == 'Fixe'):
            if(sti == "true"):
                cmb_valApp.destroy()
            elif(sjk == "true"):
                return
            self.txt_fixe_Sect= Entry(self.frame1,font=("times new romman",14,"bold"),  bg="lightgray", fg="#182350", textvariable=self.var_fixe)
            self.txt_fixe_Sect.place(x=660, y=53,width=190)
            self.var_fixe.set("")
            sjk = "true"
            
        elif(self.valdespas.get() == 'Approcher'):
            if(sjk == "true"):
                self.txt_fixe_Sect.destroy()
            elif(sti == "true"):
                 return
            valAppproch = StringVar() 
            cmb_valApp = ttk.Combobox(self.frame1, font=("times new romman", 14,"bold"),state='readonly',justify=CENTER, textvariable=valAppproch)
            cmb_valApp['values'] = ('Armijo', 'Wolf', 'Goldstein')
            cmb_valApp.current(0)
            cmb_valApp.place(x=660, y=53,width=190)
            sti = "true"
            
            
            
    def changdim(self):
        global txt_valx3
        global vardetext
        global l
        self.changsepas()
        self.txtVarx3 = DoubleVar()
        if(self.valop.get()==3):  
            l = "true"
            vardetext = StringVar() 
            txt_val = Label(self.frame1, font=("Comic Sans MS", 15,"bold"),bg="#BDC29C", textvariable= vardetext).place(x=385,y=170)
            vardetext.set("x[2]")
            txt_valx3 = Entry(self.frame1,font=("times new romman", 14,"bold"), bg="lightgray",fg="#182350", textvariable= self.txtVarx3)
            txt_valx3.place(x=440,y=173,width=160)
            self.txtVarx3.set("")
        elif(self.valop.get() == 2):
            if(l == "true"):
                vardetext.set("")
                txt_valx3.destroy()
            else:
                return
       
            
    #-------------Pour quiter------------------------------------#       
    def quiter(self):
        self.fenetre7.destroy()
        
        
        
    #----------------pour vider les comps-------------------------------------#
    def clearChamp(self):
        self.txtSolExacNew.delete(0, END)
        self.txt_itera_Sect.delete(0, END)
        self.txt_iterpretatSect.delete(0, END)
        

    
   
     
        
    def fon(self, x):
        func = self.txt_fonctin.get()
        fonc = str(func)
        x, y = symbols('x y', real=True)
        evalfon = eval(fonc)
        return evalfon
    #----------le gradient de f ----------------------------------------------#
    def grad(self, f):
        x, y = symbols('x y', real=True)
        dx = diff(f(x), x)
        dy = diff(f(y), y)
        return np.transpose( np.array([[ dx , dy]]))
    #------------le gradiein en un point -------------------------------------#
    def evalgred(self, point, fonc):
        Res = self.grad(fonc)
        #print("Res = ", Res)
        fon1 = Res[0]
        fon2 = Res[1]
        x = point[0]
        y = point[1]
        def avalF1(x):
            x = point[0]
            y = point[1]
            t = eval(str(fon1))
            return t
        def avalF2(y):
            x = point[0]
            y = point[1]
            p = eval(str(fon2))
            return p
        y1 = avalF1(x)
        y2 = avalF2(y)
        resultt = np.array( [y1 , y2] ).flatten()
        return resultt
    
    #---------fonc de alpha--------------------------------------------------#
    def foncdealpha(self, table):
         func = self.txt_fonctin.get()
         fonc = str(func)
         x = table[0]
         y = table[1]
         resalpha = eval(fonc)
         return resalpha[0]
    #-------------------------3dm---------------------------------------------#
    def fonction(self, x):
        func = self.txt_fonctin.get()
        fonct = str(func)
        x, y, z = symbols('x y z', real=True)
        evalfonct = eval(fonct)
        return evalfonct
    
    #----------le gradient de f ----------------------------------------------#
    def graddeF(self, f):
        x, y, z = symbols('x y z ', real=True)
        dx = diff(f(x), x)
        dy = diff(f(y), y)
        dz = diff(f(z), z)
        return np.transpose( np.array([[ dx , dy, dz]]))
   
    #------------le gradiein en un point -------------------------------------#
    def evalgradF(self, point, fonc):
        Res = self.graddeF(fonc)
        #print("Res = ", Res)
        fon1 = Res[0]
        fon2 = Res[1]
        fon3 = Res[2]
        x = point[0]
        y = point[1]
        z = point[2]
        def avalF1(x):
            x = point[0]
            y = point[1]
            z = point[2]
            t = eval(str(fon1))
            return t
        def avalF2(y):
            x = point[0]
            y = point[1]
            z = point[2]
            p = eval(str(fon2))
            return p
        def avalF3(z):
            x = point[0]
            y = point[1]
            z = point[2]
            m = eval(str(fon3))
            return m
        y1 = avalF1(x)
        y2 = avalF2(y)
        y3 = avalF3(z)
        resultdeF = np.array( [y1 , y2, y3] ).flatten()
        return resultdeF
    
     #---------fonc de alpha--------------------------------------------------#
    def fodepha(self, tab):
         func = self.txt_fonctin.get()
         fonct = str(func)
         x = tab[0]
         y = tab[1]
         z = tab[2]
         resopha = eval(fonct)
         return resopha[0]
      
    #---------------Algorithma de quasi Newton -------------------------------#
    def quasi_Newton(self):
        self.clearChamp()
        val1 = self.txt_valx.get()
        val2 = self.txt_valy.get()
        func = self.txt_fonctin.get()
        delt = self.txt_toler.get()
        if(val1 =="" or val2 ==""  or func ==""  or delt =="" ):
             MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre7)
        else :
            # try:
                  if(self.valop.get() == 2 ):
                        x1 = float(val1)
                        x2 = float(val2)
                        delTT = float(delt)
                        x, y = symbols('x y', real=True)
                        
                        xzero =np.transpose( np.array([[x1, x2]]))
                        #print("xzero = ", xzero)
                        #--------------initialisation de gde0 ----------------#
                        gde0 = np.transpose(  np.array([self.evalgred(xzero , self.fon)]))
                        #print("gde0 = ", gde0)
                        #--------------initialisation de Hed0 ----------------#
                        Hed0 = np.eye(2)
                        #---------Debut --------------------------------------#
                        gdek = gde0
                        HdeK = Hed0
                        xk = xzero
                        #-------------le pas fixe ----------------------------#
                        if( self.valdespas.get() == 'Fixe'):
                                nbrAlpha = self.txt_fixe_Sect.get()
                                if( nbrAlpha == ""):
                                      MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre7)
                                else:
                                    Alphak = float(nbrAlpha)
                                    k = 1
                                    #-------------la boucle while --------------------------------#
                                    while(la.norm(gdek) > delTT):        
                                        d_dek = - HdeK.dot(gdek)
                                        #print("d_dek = ", d_dek)
                                        #----------la calcule de xkPlus1 ------------------------#
                                        xkPlus1  =  xk + Alphak * d_dek
                                        #print("xkPlus1 = ", xkPlus1)
                                        #-------------la calcule de gk_plus1 ----------------------#
                                        gk_plus1 = np.transpose(np.array([self.evalgred(xkPlus1 , self.fon)]))
                                        #print("gk_plus1 = ", gk_plus1)
                                        if(la.norm(gk_plus1) <= delTT):
                                            xk = xkPlus1 
                                            break
                                        else:
                                            #----------initialisation de yk-----------------------#
                                            yk = gk_plus1 - gdek
                                            #print("yk = ", yk)
                                            #-------------calcul de Ak ---------------------------#
                                            dkT = np.transpose(d_dek)
                                            #print("dktransposee dkT = ", dkT)
                                            Aa1 = Alphak * d_dek.dot(dkT)
                                            Aa2 = dkT.dot(yk)
                                            #----------------------Res AK--------------------------#
                                            Ade_k = Aa1 / Aa2
                                            #---------------------la calcul de Bk ----------------#
                                            Bk1 = HdeK.dot(yk)
                                            Bk2 = np.transpose(Bk1)
                                            ResB1 = - Bk1.dot(Bk2)
                                            yktran =np.transpose(yk)
                                            ResulB2= yktran.dot(Bk1)
                                        
                                            #----------------------Res BK-------------------------#
                                            Bdek = ResB1 / ResulB2
                                            #-----------determination de Hk_plus1-----------------#
                                            Hk_plus1 = HdeK + Ade_k + Bdek
                                            #print("Hk_plus1 = ", Hk_plus1)
                                        
                                            #--------incrementation de k -------------------------#
                                            gdek = gk_plus1
                                            HdeK = Hk_plus1
                                            xk = xkPlus1  
                                            k+=1
                                            
                                    solution =  xk.flatten()
                                    self.varsolQuasiNeew.set(solution)
                                    self.var_sect_itir.set(k)
                                    self.var_iterpreSect.set("Qusi-Newton : la solution est trouvée avec succés !")
                                    
                         #----------------le pas optimal ---------------------#           
                        elif(self.valdespas.get() == 'Optimal'):
                                k = 1
                                #-------------la boucle while --------------------------------#
                                while(la.norm(gdek) > delTT):        
                                    d_dek = - HdeK.dot(gdek)
                                    #--determiner alphak tel que alpha_k = argmin{f(xk + alpha dk)}
                                    x = symbols('x', real=True)
                                    Respas =  xzero + x*d_dek 
                                    #print("Respas = ", Respas)
                                    funrez = self.foncdealpha(Respas)
                                    #print("u = ", funrez)
                                    #--recherche de min par fib-----------------------------#
                                    voizimin = self.fibonacci(0, 100, str(funrez), 100)
                                    #print("voizimin = ", voizimin)
                                    Alphak = self.newtonraphson(voizimin, str(funrez), 0.01, 100)
                                    print("le pas optimal dans l'itération  "+str(k)+"  est : ", Alphak)
                                    
                                    #----------la calcule de xkPlus1 ------------------------#
                                    xkPlus1  =  xk + Alphak * d_dek
                                    #print("xkPlus1 = ", xkPlus1)
                                    #-------------la calcule de gk_plus1 ----------------------#
                                    gk_plus1 = np.transpose(np.array([self.evalgred(xkPlus1 , self.fon)]))
                                    #print("gk_plus1 = ", gk_plus1)
                                    if(la.norm(gk_plus1) <= delTT):
                                        xk = xkPlus1 
                                        break
                                    else:
                                        #----------initialisation de yk-----------------------#
                                        yk = gk_plus1 - gdek
                                        #print("yk = ", yk)
                                        #-------------calcul de Ak ---------------------------#
                                        dkT = np.transpose(d_dek)
                                        #print("dktransposee dkT = ", dkT)
                                        Aa1 = Alphak * d_dek.dot(dkT)
                                        Aa2 = dkT.dot(yk)
                                        #----------------------Res AK--------------------------#
                                        Ade_k = Aa1 / Aa2
                                        #---------------------la calcul de Bk ----------------#
                                        Bk1 = HdeK.dot(yk)
                                        Bk2 = np.transpose(Bk1)
                                        ResB1 = - Bk1.dot(Bk2)
                                        yktran =np.transpose(yk)
                                        ResulB2= yktran.dot(Bk1)
                                    
                                        #----------------------Res BK-------------------------#
                                        Bdek = ResB1 / ResulB2
                                        #-----------determination de Hk_plus1-----------------#
                                        Hk_plus1 = HdeK + Ade_k + Bdek
                                        #print("Hk_plus1 = ", Hk_plus1)
                                    
                                        #--------incrementation de k -------------------------#
                                        gdek = gk_plus1
                                        HdeK = Hk_plus1
                                        xk = xkPlus1  
                                        k+=1
                                        
                                solution =  xk.flatten()
                                self.varsolQuasiNeew.set(solution)
                                self.var_sect_itir.set(k)
                                self.var_iterpreSect.set("Qusi-Newton : la solution est trouvée avec succés !")
                  elif(self.valop.get()== 3):
                     val3 = txt_valx3.get()
                     if(val3 == ""):
                         MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre7)
                     else:
                        a1 = float(val1)
                        a2 = float(val2)
                        a3 = float(val3)
                        delTT = float(delt)
                        x, y, z = symbols('x y z', real=True)
               
                        #---------Debut ----------------------------------------------#
                        x0 = np.transpose( np.array([[a1, a2, a3]]))
                        #print("x0 = ", x0)
                        #--------------initialisation de gde0 -----------------------#
                        gde0 = np.transpose(  np.array([self.evalgradF(x0 , self.fonction)]) )
                        #print("gde0 = ", gde0)
                        #--------------initialisation de Hde0 -----------------------#
                        Hde0 = np.eye(3)
                        #-------------------------------------------------------------#
                        gk = gde0
                        Hk = Hde0
                        x_k = x0
                        #-------------le pas fixe ----------------------------#
                        if( self.valdespas.get()== 'Fixe'):
                                nbAlpha = self.txt_fixe_Sect.get()
                                if( nbAlpha == ""):
                                      MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre7)
                                else:
                                    Alfk = float(nbAlpha)
                                    k = 1
                                    #-------------la boucle while --------------------------------#
                                    while(la.norm(gk) > delTT):
                                        Ddek = - Hk.dot(gk)
                                        #print("Ddek = ", Ddek)
                                        #----------la calcule de xkPlus1 ------------------------#
                                        xk_Plus1  =  x_k + Alfk * Ddek
                                        #print("xk_Plus1 = ", xk_Plus1)
                                        #-------------la calcule de gkplus1 ----------------------#
                                        gkplus1 = np.transpose(np.array([self.evalgradF(xk_Plus1 , self.fonction)]))
                                        #print("gkplus1 = ", gkplus1)
                                        if(la.norm(gkplus1) <= delTT):  
                                            x_k = xk_Plus1
                                            break
                                        else:
                                            #----------initialisation de yk-----------------------#
                                            y_k = gkplus1 - gk
                                            #print("yk = ", y_k)
                                            #-------------calcul de Ak ---------------------------#
                                            dkTrans = np.transpose(Ddek)
                                            #print("dktransposee dkTrans = ", dkTrans)
                                            Akde1 = Alfk * Ddek.dot(dkTrans)
                                            Akea2 = dkTrans.dot(y_k)
                                            #----------------------Res AK--------------------------#
                                            ResAdek = Akde1 / Akea2
                                            #---------------------la calcul de Bk ----------------#
                                            RB1 = Hk.dot(y_k)
                                            #print("RB1 = ", RB1)                        
                                            RBk2 = np.transpose(RB1)
                                            Res_B1 = - RB1.dot(RBk2)
                                            yTran =np.transpose(y_k)
                                            ResulB2= yTran.dot(RB1)
                                            #----------------------Res BK-------------------------#
                                            ResFinB = Res_B1 / ResulB2
                                            #-----------determination de HkPlus1-----------------#
                                            HkPlus1 = Hk + ResAdek + ResFinB
                                            #print("HkPlus1 = ", HkPlus1)
                                   
                                            #--------incrementation de k -------------------------#
                                            gk = gkplus1
                                            Hk = HkPlus1
                                            x_k = xk_Plus1
                                            k+=1
                                    sol =  x_k.flatten()
                                    self.varsolQuasiNeew.set(sol)
                                    self.var_sect_itir.set(k)
                                    self.var_iterpreSect.set("Qusi-Newton : la solution est trouvée avec succés !")
                        #----------------le pas optimal ---------------------#           
                        elif(self.valdespas.get() =='Optimal'):
                                    k = 1
                                    #-------------la boucle while --------------------------------#
                                    while(la.norm(gk) > delTT):
                                         Ddek = - Hk.dot(gk)
                                         #print("Ddek = ", Ddek)
                                         x = symbols('x', real=True)
                                         Restpas =  x0 + x* Ddek 
                                         #print("Restpas = ", Restpas)
                                         fuze = self.fodepha(Restpas)
                                         #print("phi de alpha  =  ", fuze)
                                         #--recherche de min par fib-----------------------------#
                                         voizn = self.fibonacci(0, 2, str(fuze), 100)
                                         #print("voizn fibonacci = ", voizn)
                                         Alfk = self.newtonraphson(voizn, str(fuze), 0.01, 100)
                                         print("le pas optimal dans l'itération  "+str(k)+"  est : ", Alfk)
                                         #----------la calcule de xkPlus1 ------------------------#
                                         xk_Plus1  =  x_k + Alfk * Ddek
                                         #print("xk_Plus1 = ", xk_Plus1)
                                         #-------------la calcule de gkplus1 ----------------------#
                                         gkplus1 = np.transpose(np.array([self.evalgradF(xk_Plus1 , self.fonction)]))
                                         #print("gkplus1 = ", gkplus1)
                                         if(la.norm(gkplus1) <= delTT):  
                                             x_k = xk_Plus1
                                             break
                                         else:
                                             #----------initialisation de yk-----------------------#
                                             y_k = gkplus1 - gk
                                             #print("yk = ", y_k)
                                             #-------------calcul de Ak ---------------------------#
                                             dkTrans = np.transpose(Ddek)
                                             #print("dktransposee dkTrans = ", dkTrans)
                                             Akde1 = Alfk * Ddek.dot(dkTrans)
                                             Akea2 = dkTrans.dot(y_k)
                                             #----------------------Res AK--------------------------#
                                             ResAdek = Akde1 / Akea2
                                             #---------------------la calcul de Bk ----------------#
                                             RB1 = Hk.dot(y_k)
                                             #print("RB1 = ", RB1)                        
                                             RBk2 = np.transpose(RB1)
                                             Res_B1 = - RB1.dot(RBk2)
                                             yTran =np.transpose(y_k)
                                             ResulB2= yTran.dot(RB1)
                                             #----------------------Res BK-------------------------#
                                             ResFinB = Res_B1 / ResulB2
                                             #-----------determination de HkPlus1-----------------#
                                             HkPlus1 = Hk + ResAdek + ResFinB
                                             #print("HkPlus1 = ", HkPlus1)
                                   
                                             #--------incrementation de k -------------------------#
                                             gk = gkplus1
                                             Hk = HkPlus1
                                             x_k = xk_Plus1
                                             k+=1
                
                                    sol =  x_k.flatten()
                                    self.varsolQuasiNeew.set(sol)
                                    self.var_sect_itir.set(k)
                                    self.var_iterpreSect.set("Qusi-Newton : la solution est trouvée avec succés !")
                                    
                        elif(self.valdespas.get() == 'Approcher') :
                                if(valAppproch.get() == 'Armijo'):
                                    pass
                                elif(valAppproch.get() == 'Wolf'):
                                    pass
                                elif(valAppproch.get() == 'Goldstein'):
                                    pass
           #  except Exception as es:                  
            #       MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre7) 
  
    

    #----------Fibonacci -------------------------------------------------------#
    def fibonacci(self, xL1 : float, xU1 : float, f, n : int):
              xLk = xL1
              xUk = xU1
              def func(x):
                 func = eval(f)
                 return func
              x = sp.Symbol('x')
              deriv1 = sp.diff(func(x),x)
              deriv2 = sp.diff(func(x),x,x)
              def deriv1er(x):
                  deriv1er = eval(str(deriv1))
                  return deriv1er
              def deriv2eme(x):
                  deriv2eme = eval(str(deriv2))
                  return deriv2eme
              
              if((deriv1er(xL1)<0 and deriv1er(xU1)<0) or (deriv1er(xL1)>0 and deriv1er(xU1)>0)):
                  print("La fonction est monotone ou multimodale dans l'intervale [",xL1,",",xU1,"]")
                  sys.exit()
              xa1 = 0
              xb1 = 0
              fa1 = 0
              fb1 = 0
              F = []
              F.insert(0, 1)
              F.insert(1, 1)
              for k in range(2,n):
                valFk = F[k-1] + F[k-2]
                F.insert(k,valFk)
              z = len(F) - 1
              I = []
              I1 = xU1 - xL1
              I2 = (F[z-1]/F[z])*I1
              I.insert(0, 0)
              I.insert(1, I1)
              I.insert(2, I2)
              xa1 = xU1 - I[1]
              xb1 = xL1 + I[2]
              fa1 = func(xa1)
              fb1 = func(xb1)
              
              k = 1
              q = n - 2
              for j in range(n):
                  Ik2 = (F[n-k-1]/F[n-k])*I[k+1]
                  I.insert(k+2, Ik2)
                  if( fa1 >= fb1 ):
                        xLk = xa1
                        xa1 = xb1
                        xb1 = xLk + I[k+2]
                        fa1 = fb1
                        fb1 = func(xb1)
                        if( (k == q) or (xa1 > xb1)):
                            xapproch = xa1
                            fxapproch = func(xapproch)
                            #print("[",xb1,",",xa1,"] le point x* : ",xapproch," f(x*) :",fxapproch)
                            return xapproch
                            break
                        else:
                            k = k + 1
                  elif( fa1 < fb1 ):
                      xUK = xb1
                      xa1 = xUK - I[k+2]
                      xb1 = xa1
                      fb1 = fa1
                      fa1 = func(xa1)
                      if( (k == q) or (xa1 > xb1)):
                          xmin = xa1
                          fmin = func(xa1)
                          #print("le point x* : ",xmin," f(x*) :",fmin)
                          return xmin
                          break
                      else:
                          k = k + 1
           
    #------------Newton-------------------------------------------------------#
    def newtonraphson(self, xk : float, f, tole : float, nbrIter : int):
        xmoins = xk - 1
        xkplus = 0
        def func(x):
            func = eval(f)
            return func
        x = sp.Symbol('x')
        deriv1 = sp.diff(func(x),x)
        deriv2 = sp.diff(func(x),x,x)
        def deriv1er(x):
            deriv1er = eval(str(deriv1))
            return deriv1er
        def deriv2eme(x):
            deriv2eme = eval(str(deriv2))
            return deriv2eme
        for n in range(0,nbrIter):
            f1 = deriv1er(xk)
            f2 = deriv2eme(xk)
            if(f2 == 0):
                print("Impossible la derivee seconde egale à 0")
                break
            else :
                dist = xk - xmoins
                if(abs(dist)>=tole):
                    direction = -1 * f1/f2
                    xkplus = xk + direction
                    xmoinx = xk
                    xk = xkplus 
                else:
                    #print("La valeur apres ",n," iteration")
                    #print(xk)
                    break
                    return xk
        if(f2 > 0):
            #print("apres ",n," iteration le minimum est ",xk)
            return xk
        elif(f2 < 0):
            #print("apres ",n," iteration le maximum est ",xk)
            return xk
    

  
    
  
    
  # 0.5*x**2 - 4*x + 5*y**2 + 30*y
    #======================Le gghaphe de la fonction==========================#   
    def graphe_de_fonction(self):
            fonc = self.txt_fonctin.get()
            if(fonc =="" ):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre7)
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
                    surface = ax.plot_surface(x, y, f, cmap=cm.inferno , linewidth=0)
                    fig.colorbar(surface, shrink=0.5)
                    plt.show()
                    
                except Exception as es:                  
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre7) 
                   
            elif(self.valop.get() == 3):
                 pass
                 #---le graphe de fonction 3D --------------------#
               
        
    # def hessienDeF(f):
    #     x, y = symbols('x y', real=True)
    #     H = np.array([x ,y])
    #     Resgrad = grad(H , f)
    #     M = Resgrad[0]
    #     N = Resgrad[1]
    #     def foncM(x):
    #         y = eval(str(M))
    #         return y
    #     def foncN(x):
    #         y = eval(str(N))
    #         return y           
    #     dxx = diff(foncM(x), x)
    #     dxy = diff(foncM(x), y)
    #     dyx = diff(foncN(y), x)
    #     dyy = diff(foncN<y), y)
    #     H = np.array([[dxx , dxy], [dyx , dyy]])
    #     return H
    
    
  
# fenetre7=Tk()
# obj=quasiNewton(fenetre7)
# fenetre7.mainloop()      