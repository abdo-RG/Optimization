from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
import numpy as np
from scipy import misc 
import matplotlib.pyplot as plt
import math

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler

from matplotlib.figure import Figure



class SectionDor :
    def __init__(self,fenetre4):
        self.fenetre4=fenetre4
        #-----------le titre--------------------------------------------------#
        self.fenetre4.title("Section D'or ")
        #-----------------la geometrerde la fenetre---------------------------#
        self.fenetre4.geometry("1000x720+150+50")
        #-----------------le coleure de bag-----------------------------------#
        self.fenetre4.config(bg="#D4DCD8")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        self.fenetre4.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        self.fenetre4.iconbitmap("images/logoimag.ico")
        #==============Frame1  ===============================================#
        frame1=Frame( self.fenetre4, bg="#D4DCD8", highlightbackground="green",highlightthickness=2)
        frame1.place(x=48,y=40,height=660,width=900)
        #===============title=================================================#
        title = Label( self.fenetre4,text="Section D'or ",font=("Comic Sans MS", 17,"bold"), bg="#D4DCD8",fg="green").place(x=390,y=5)
       
        #----------------les entrer de l'algorithme---------------------------#
        entrer = Label(frame1,text="Input { ",font=("Comic Sans MS", 15,"bold"), bg="#D4DCD8",fg="#182350").place(x=10,y=10)
        
        #=================l'intervale ========================================#
        intervale = Label(frame1,text="The interval [a , b]   :",font=("Comic Sans MS", 15,"bold"),bg="#D4DCD8").place(x=110,y=50)
        
        #================vale de a ===========================================#
        self.txt_val = Label(frame1,text=" a :",font=("Comic Sans MS", 15,"bold"),bg="#D4DCD8").place(x=400,y=50)
        self.txt_val_a = Entry(frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txt_val_a.place(x=440,y=53,width=160)
        
        #================la valeure de b =====================================#
        self.val_b = Label(frame1,text=" b :",font=("Comic Sans MS", 15,"bold"),bg="#D4DCD8").place(x=630,y=50)
        self.txt_val_b = Entry(frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txt_val_b.place(x=675,y=53,width=160)
        
        #===================la fonction=======================================#
        self.fonc = Label(frame1,text="Function               : ",font=("Comic Sans MS", 16,"bold"),bg="#D4DCD8").place(x=110,y=110)
        self.foncF = Label(frame1,text="f(x)  =",font=("Comic Sans MS", 16,"bold"),bg="#D4DCD8").place(x=360,y=110)
        self.txt_fonc = Entry(frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350")
        self.txt_fonc.place(x=440,y=113,width=397 )
        
        #================la tolérence  =======================================#
        self.delta = Label(frame1,text="Tolerance              :",font=("Comic Sans MS", 15,"bold"),bg="#D4DCD8").place(x=110,y=170)
        self.delTTa = Label(frame1,text="delta =",font=("Comic Sans MS", 15,"bold"),bg="#D4DCD8").place(x=360,y=170)
        self.defouitDelta = DoubleVar()
        self.txt_delta = Entry(frame1,font=("times new romman", 16,"bold"), bg="lightgray",fg="#182350", textvariable=self.defouitDelta)
        self.defouitDelta.set(0.001)
        self.txt_delta.place(x=440,y=173,width=160)
        
        
        #=================fermer l'accolade===================================#
        self.coladfer = Label(frame1,text=" } Output   :",font=("Comic Sans MS", 15,"bold"),bg="#D4DCD8",fg="#182350").place(x=10,y=230)
        
        #==============Frame1  ===============================================#
        self.frame2=Frame( frame1,bg="#C4C6C6" ,highlightbackground="#182350",highlightthickness=3)
        self.frame2.place(x=10,y=290,height=360,width=875)
        
        #=================================================solution ===========================================#
        self.solution = Label(self.frame2,text="The interval [a , b]  :",font=("Comic Sans MS",15,"bold"), bg="#C4C6C6").place(x=10,y=20)
        #----------------------- la valeur de la solution a [a,b] -------------------------------------------------------#
        self.val_a_solutiFib = Label(self.frame2,text=" a :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=20)
        self.varSect = DoubleVar()
        self.txt_val_a_solutSect = Entry(self.frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="#182350", textvariable=self.varSect)
        self.varSect.set("")
        self.txt_val_a_solutSect.place(x=290,y=23,width=250)
        
        
        #----------------------- la valeur de la solution b [a,b] --------------------------------------------------------#
        self.val_b_solutSect = Label(self.frame2,text=" b:",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=547,y=20)
        self.varSecB = DoubleVar()
        self.txt_val_solutionSecB = Entry(self.frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="#182350", textvariable=self.varSecB)
        self.varSecB.set("")
        self.txt_val_solutionSecB.place(x=583,y=23,width=250)
        
        #--------------------------------val des nomber des itoration  i ----------------------------------------#
        self.nbr_Sect_iteration = Label(self.frame2,text="Number of iterations:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=110)
        self.txt_itera_Section = Label(self.frame2,text=" i :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=110)
        self.var_sect_itir = IntVar()
        self.txt_itera_Sect= Entry(self.frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="red", textvariable=self.var_sect_itir)
        self.var_sect_itir.set("")
        self.txt_itera_Sect.place(x=290,y=113,width=250)
              
        #---------------------------------------interprétation---------------------------------------------------------------#
        self.nbr_iterpretaSecti = Label(self.frame2,text="Interpretation        :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=190)
        self.var_iterpreSect = StringVar()
        self.txt_iterpretatSect = Entry(self.frame2,font=("Comic Sans MS",16,"bold"), bg="lightgray",fg="green", textvariable=self.var_iterpreSect)
        self.var_iterpreSect.set("")
        self.txt_iterpretatSect.place(x=290,y=193,width=545)

        #=========================================================== boutton Section d'or =========================================================================================================#
        SectionDor_Button  = Button(self.frame2,font=("times new romman",16,"bold"),text=" Section d'or ",bd=0,cursor="hand2",bg="#AFAF0D",fg="#E5E1D6",activebackground ="#7AA1E6",activeforeground="#BF846C",borderwidth = 5, command =self.SectionDoree).place(x=320 ,y=270,width=240)
           
       #============================================================ Bouton le graphe de la fonction ===========================================================================================#
        graphedefa= Button(self.frame2,font=("times new romman",16,"bold"),text="graph of the fonction",bd=0,cursor="hand2",bg="#7B9764",fg="#E5E1D6",activebackground ="#CDD3C8",activeforeground="#BFF790",borderwidth = 5, command=self.graphe_de_fonction).place(x=10 ,y=270,width=240)
        
       #============================================================ Bouton quit ============================================================================================================#
        quitbuttonsec = Button(self.frame2 ,font=("times new romman",16,"bold"),text="Quit ",bd=0,cursor="hand2",bg="#811000",fg="#F9F2F1",activebackground ="#CAE5E4",activeforeground="#E8A490",borderwidth = 5, command=self.quiter).place(x=640 ,y=270,width=200)
        
        
   
    
   
     #-------------Pour quiter------------------------------------#       
    def quiter(self):
       self.fenetre4.destroy()
    



    #----------------pour vider les comps-------------------------------------#
    def clearChamp(self):
        self.txt_val_a_solutSect.delete(0, END)
        self.txt_val_solutionSecB.delete(0, END)
        self.txt_itera_Sect.delete(0, END)
        self.txt_iterpretatSect.delete(0, END)     
        


        #===================================Algorithme de Section dorée =========================================================================#
    def SectionDoree(self):
         self.clearChamp()
         #==============les entrer de l'algorithme=============
         val1 = self.txt_val_a.get()
         val2 = self.txt_val_b.get()
         fon = self.txt_fonc.get()
         deltta = self.txt_delta.get() 
         if(val1 =="" or val2 ==""  or fon ==""  or deltta =="" ):
             MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre4)
         elif(val1 > val2):
              MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre4)
         else:
              try:   
                  a = float(val1)
                  b = float(val2)
                  delta = float(deltta)
                  
                  def f(x):
                      y = eval(fon)
                      return y 
                     
                  fprimde_a = misc.derivative(f, a, dx=1.0, n=1, args=(), order=3) - 1
                  fprimde_b = misc.derivative(f, b, dx=1.0, n=1, args=(), order=3) - 1
                  
                  if(fprimde_a < 0 and  fprimde_b > 0):
                      plt.clf()
                      y = np.linspace(a, b, 1000)
                      plt.plot(y, f(y), label = "La courbe de f(x) ")
                      plt.title(" Section d'or ")
                      plt.xlabel("Abscisses")
                      plt.ylabel("Ordonnees")
                      plt.plot(a, f(a), 'r.')
                      plt.plot(b, f(b), 'r.')
                      #---------initialisation de deux var nous permettent de sortie dans la boucle si l'intervale ne change pas ---------------#
                      j=100.01
                      i=199.0
                      #-------------nomber d'or--------------#
                      to = 0.5*(math.sqrt(5) - 1)
                      #-----début-----------------------------#
                      k = 1
                      d1 = abs(b - a)
                      x1 = a + (1 - to) * d1
                      x2 = a + to * d1
                      plt.plot(x1, f(x1), 'r.')
                      plt.plot(x2, f(x2), 'r.')
                      #------------------- la boucle while---------------------#
                      while( abs(b - a) > delta):
                          if( f(x1) > f(x2)):
                              a = x1
                              x1 = x2
                              x2 = a + to * (abs(b - a))
                              plt.plot(x2, f(x2), 'r.')
                          else:
                              b = x2
                              x2 = x1
                              x1 = a + (1 - to)* (abs(b - a))
                              plt.plot(x1, f(x1), 'r.')
                              
                          if(x1==j and i==x2):
                              break
                          else:    
                              #----------Incrementation de k ---------------------#
                              k = k+1   
                      #---------------------la sortie de la boucle while----------#  
                      a = x1
                      b = x2
                      #-------------Affichage de résultata-------------------------#
                      self.varSect.set(a)
                      self.varSecB.set(b)
                      self.var_sect_itir.set(k)
                      self.var_iterpreSect.set("la solution x* est dans l'intervale ["+str(a) +" , "+ str(b) +"]")
                      plt.plot(a, f(a), label="l'interval [a, b]")
                      plt.plot(a, f(a), 'g+')
                      plt.plot(b, f(b), 'g+')
                      plt.legend()
                      plt.show()
                             
                  else:
                      MessageBox.showwarning("Error", "On ne peut pa appliquer l'algorithme de Section D'or sur cette fonction dans cette intervale !!  ")
                      
              except Exception as es:                  
                   MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre4)  



     #======================Le gghaphe de la fonction==========================#   
    def graphe_de_fonction(self):
            val1 = self.txt_val_a.get()
            val2 = self.txt_val_b.get()
            fonc = self.txt_fonc.get()
            
            if(val1 =="" or val2 =="" or fonc =="" ):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre4)
            elif(val1 > val2):
                MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre4)
            else :
                try:
                    a = float(val1)
                    b = float(val2)
                    
                    def f(x):
                        y = eval(fonc)
                        return y 
                    
                    root = Toplevel()
                    root.wm_title(" le Graphe de la fonction f ")
                    fig = Figure(figsize=(5, 4), dpi=100)
                    x = np.linspace(a, b, 1000)
                    fig.add_subplot(111).plot(x, f(x))

                    canvas = FigureCanvasTkAgg(fig, master=root)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

                    toolbar = NavigationToolbar2Tk(canvas, root)
                    toolbar.update()
                    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
                    def on_key(event):
                        print("you pressed{}".format(event.key))
                        key_press_handler(event, canvas,toolbar)
        

                    canvas.mpl_connect("key_press_event", on_key)
                    root.mainloop()  
      
        
                except Exception as es:                  
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre4) 
        
        
        

# fenetre4=Tk()
# obj=SectionDor(fenetre4)
# fenetre4.mainloop()  
                  

