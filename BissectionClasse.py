from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
import numpy as np
from scipy import misc 
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler

from matplotlib.figure import Figure


class Bissection :
    def __init__(self,fenetre1):
        self.fenetre1=fenetre1
        #-----------le titre--------------------------------------------------#
        self.fenetre1.title("Bissection Search")
        #-----------------la geometrerde la fenetre---------------------------#
        self.fenetre1.geometry("1000x720+150+50")
        #-----------------le coleure de bag-----------------------------------#
        self.fenetre1.config(bg="#BAC7CF")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        self.fenetre1.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        self.fenetre1.iconbitmap("images/logoimag.ico")
        
        #==============framprincipale  =======================================#
        framprincipale=Frame( self.fenetre1, bg="#BAC7CF", highlightbackground="green",highlightthickness=2)
        framprincipale.place(x=45,y=40,height=660,width=900)
        #===============title=================================================#
        title = Label( self.fenetre1,text="Bissection Search",font=("Comic Sans MS", 17,"bold"), bg="#BAC7CF",fg="green").place(x=380,y=5)
       
        #----------------les entrer de l'algorithme---------------------------#
        entrer1 = Label(framprincipale,text="Input { ",font=("Comic Sans MS", 15,"bold"), bg="#BAC7CF",fg="#182350").place(x=10,y=10)
        
        #=================l'intervale ========================================#
        intervale1 = Label(framprincipale,text="The interval [a , b]   :",font=("Comic Sans MS", 15,"bold"),bg="#BAC7CF").place(x=110,y=20)
        
        #================vale de a ===========================================#
        valeurA = Label(framprincipale,text=" a :",font=("Comic Sans MS", 15,"bold"),bg="#BAC7CF").place(x=400,y=20)
        self.txtValeur_A = Entry(framprincipale,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txtValeur_A.place(x=440,y=23,width=160)
        
        #================la valeure de b =====================================#
        valeurdeB = Label(framprincipale,text=" b :",font=("Comic Sans MS", 15,"bold"),bg="#BAC7CF").place(x=630,y=20)
        self.txtValeur_B = Entry(framprincipale,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txtValeur_B.place(x=675,y=23,width=160)
        
        #===================la fonction22tion=================================#
        fonction22 = Label(framprincipale,text="Function               : ",font=("Comic Sans MS", 16,"bold"),bg="#BAC7CF").place(x=110,y=80)
        fonction22F1 = Label(framprincipale,text="f(x)  =",font=("Comic Sans MS", 16,"bold"),bg="#BAC7CF").place(x=360,y=80)
        self.txt_fonction = Entry(framprincipale,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350")
        self.txt_fonction.place(x=440,y=83,width=397 )
        
        #================la tolérence  =======================================#
        delta1 = Label(framprincipale,text="Tolerance              :",font=("Comic Sans MS", 15,"bold"),bg="#BAC7CF").place(x=110,y=140)
        delTTa1 = Label(framprincipale,text="delta =",font=("Comic Sans MS", 15,"bold"),bg="#BAC7CF").place(x=360,y=140)
        self.deltaBissection = DoubleVar()
        self.txtdelta1 = Entry(framprincipale,font=("times new romman", 15,"bold"), bg="lightgray",fg="#182350", textvariable=self.deltaBissection)
        self.deltaBissection.set(0.001)
        self.txtdelta1.place(x=440,y=143,width=160)
        
        #=================fermer l'accolade===================================#
        coladfer = Label(framprincipale,text=" } Output   :",font=("Comic Sans MS", 15,"bold"),bg="#BAC7CF",fg="#182350").place(x=10,y=200)
        
        #==============framprincipale  =======================================#
        self.frame2=Frame( framprincipale,bg="#C4C6C6" ,highlightbackground="#182350",highlightthickness=3)
        self.frame2.place(x=10,y=245,height=400,width=875)
        
        #====================solution Bissection==============================#
        solution = Label(self.frame2,text="The interval [a , b]  :",font=("Comic Sans MS",15,"bold"), bg="#C4C6C6").place(x=10,y=10)
        #------------------ la valeur de la solution a [a,b]------------------#
        valeurAsol = Label(self.frame2,text=" a :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=10)
        self.varDeA = DoubleVar()
        self.txtAsolut = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.varDeA)
        self.varDeA.set("")
        self.txtAsolut.place(x=290,y=13,width=250)
        
        
        #-------------------la valeur de la solution b [a,b] -----------------#
        valeurB_sol = Label(self.frame2,text=" b:",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=547,y=10)
        self.varDeBsol = DoubleVar()
        self.txtvalsolB = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.varDeBsol)
        self.varDeBsol.set("")
        self.txtvalsolB.place(x=583,y=13,width=250)        

        
        #---------------la valeur exacte de la solution si l'algorithme arive a calculer x*--------------------------------#
        val_solution_exact = Label(self.frame2,text="The solution          :",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=10,y=70)
        #-----------------------------------------------x*-----------------------------------------------------------------#
        val_x_sol = Label(self.frame2,text=" x*:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=247,y=70)
        self.varsolBissect = DoubleVar()
        self.txtSolExac = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="green", textvariable=self.varsolBissect)
        self.varsolBissect.set("")
        self.txtSolExac.place(x=290, y=73, width=250)
        
        #--------------------------------val des nomber des itoration  i Bissection----------------------------------------#
        nbr_itera_max = Label(self.frame2,text="Number of iterations:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=140)
        val_itera_bissec = Label(self.frame2,text=" i :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=140)
        self.varbissecitir = IntVar()
        self.txt_itera_bissect = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="red", textvariable=self.varbissecitir)
        self.varbissecitir.set("")
        self.txt_itera_bissect.place(x=290,y=143,width=250)
          
        #---------------------------------------interprétation---------------------------------------------------------------#
        nbr_iterpre = Label(self.frame2,text="Interpretation        :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=210)
        self.var_iterpreBissec = StringVar()
        self.txtiterpretatBissec = Entry(self.frame2,font=("Comic Sans MS", 15,"bold"), bg="lightgray",fg="#182350", textvariable=self.var_iterpreBissec)
        self.txtiterpretatBissec.place(x=290,y=213,width=545)
        
        
        #============================================================ Bouton Bissection ========================================================================================================#
        Bissection_boutton = Button(self.frame2,font=("times new romman",16,"bold"),text=" Bissection ",bd=0,cursor="hand2",bg="#0575B0",fg="#E5E1D6",activebackground ="#CAE5E4",activeforeground="#0F5A7D",borderwidth = 5, command=self.Bissection).place(x=320 ,y=330,width=240)
        
        #============================================================ Bouton Accueil ========================================================================================================#
        Accull= Button(self.frame2,font=("times new romman",16,"bold"),text="Quit ",bd=0,cursor="hand2",bg="#811000",fg="#E5E1D6",activebackground ="#CAE5E4",activeforeground="#E8A490",borderwidth = 5, command=self.quiter).place(x=640 ,y=330,width=200)
        
        #============================================================ Bouton le graphe de la fonction ========================================================================================================#
        graphee= Button(self.frame2,font=("times new romman",16,"bold"),text="graph of the fonction",bd=0,cursor="hand2",bg="#7B9764",fg="#F9F2F1",activebackground ="#CDD3C8",activeforeground="#BFF790",borderwidth = 5, command=self.graphe_de_fonction).place(x=10 ,y=330,width=240)
        
     
     
       
        
     
    #-------------Pour quiter------------------------------------#       
    def quiter(self):
       self.fenetre1.destroy()
        
     
        
     #----------------pour vider les comps----------------------------------------#
    def clearChamp(self):
        self.txtAsolut.delete(0, END)
        self.txtvalsolB.delete(0, END)
        self.txtSolExac.delete(0, END)
        self.txt_itera_bissect.delete(0, END)
        self.txtiterpretatBissec.delete(0, END)

   
 #------------------------Algoritheme de bissection---------------------------#
    def Bissection(self):
            self.clearChamp()
            val1 = self.txtValeur_A.get()
            val2 = self.txtValeur_B.get()
            delTTa1 = self.txtdelta1.get()
            fonction22t = self.txt_fonction.get()
            if(val1 =="" or val2 =="" or delTTa1 =="" or fonction22t ==""):
                MessageBox.showerror("Error"," Remplir tout les champs SVP !!", parent=self.fenetre1)
            elif(val1 > val2):
                MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre1)
            else: 
                try:                   
                     A = float(val1)
                     B = float(val2)
                     delta1 = float(delTTa1)
                     #itermax = int(imax)
                     
                     
                     #----------evaluation de la fonction22tion --------------#
                     def f(x):
                         y = eval(fonction22t)
                         return y 
                     #----------le graphe de f--------------------------------#
                     plt.clf()
                     y = np.linspace(A, B, 1000)
                     plt.plot(y, f(y), label = "La courbe de f(x) ")
                     plt.title(" Bissection ")
                     plt.xlabel("Abscisses")
                     plt.ylabel("Ordonnees")   
                     
                     #-----------la calcule de dirivée de f en point a et b---# 
                     fprim_a = misc.derivative(f, A, dx=1.0, n=1, args=(), order=3) -1    
                     fprim_b = misc.derivative(f, B, dx=1.0, n=1, args=(), order=3) - 1
                     #----initialisation de deux var pour calculer le nomber des itiration 
                     j = 1243
                     k=1101
                     #----------------la condition de vérification------------#
                     if( fprim_a < 0 and fprim_b > 0):
                         plt.plot(A , f(A), 'r.')
                         plt.plot(B , f(B), 'r.')
                         #---------indice de nomber d'incrémentation ---------#
                         i=1
                         
                         
                         while( abs(A - B) > delta1):
                             #-------- la valeur de c ----------------------------#
                             C = (B + A)/2
                             aprim = misc.derivative(f, A, dx=1.0, n=1, args=(), order=3) -1 
                             bprim = misc.derivative(f, B, dx=1.0, n=1, args=(), order=3) -1
                             if( aprim < 0 and bprim > 0):
                             #-----------------la dérivé au point c :--------------------------------#
                                 fprimDec = misc.derivative(f, C, dx=1.0, n=1, args=(), order=3) -1
                                 if(fprimDec <= 0):
                                       if(fprimDec == 0):
                                           #----------------------- la calcule de f seconde de f en poit c -------------#
                                             fseconfDec = misc.derivative(f, C, dx=1.0, n=2, args=(), order=3)
                                             if(fseconfDec > 0):
                                                 self.varsolBissect.set(C)
                                                 self.varbissecitir.set(i)
                                                 Texte = StringVar()
                                                 mylabel = Label(self.frame2, font=("Comic Sans MS", 15,"bold"), bg="lightgray",fg="green", textvariable=Texte).place(x=290,y=263,width=545)
                                                 Texte.set('la solution  '+ str(C) + ' est un minimum de la fonction f(x) ')
                                                 plt.plot(C, f(C), 'g+')
                                                 break
                                             elif(fseconfDec < 0):
                                                 self.varsolBissect.set(C)
                                                 self.varbissecitir.set(i)
                                                 Texte = StringVar()
                                                 mylabel = Label(self.frame2, font=("Comic Sans MS", 15,"bold"), bg="lightgray",fg="green", textvariable=Texte).place(x=290,y=263,width=545)
                                                 Texte.set('la solution  '+ str(C) + '  est un maximum de la fonction f(x) ')
                                                 plt.plot(C, f(C), 'g+')
                                                 break   
                                             else :
                                                 self.var_iterpreBissec.set("Ona une Point d inflexion dans le point : "+str(C))
                                                 MessageBox.showinfo("Error"," Ona une Point d'inflexion !!", parent=self.fenetre1)
                                                 break
                                       else :
                                                plt.plot(A, f(A), 'r.')
                                                A = C
                                                j = A
                                                i+=1
                                 else : 
                                         plt.plot(B, f(B), 'r.')
                                         B = C
                                         k = B
                                         i+=1
                         
                                 
                         
                             elif(aprim > 0 and bprim < 0):
                                 C = (B + A)/2
                                 plt.plot(A , f(A), 'r.')
                                 plt.plot(B , f(B), 'r.')
                                 i=1
                                 if(fprimDec >= 0):
                                       if(fprimDec == 0):
                                           #----------------------- la calcule de f seconde de f en poit c -------------#
                                             fseconfDec = misc.derivative(f, C, dx=1.0, n=2, args=(), order=3)
                                             if(fseconfDec > 0):
                                                 self.varsolBissect.set(C)
                                                 self.varbissecitir.set(i)
                                                 Texte = StringVar()
                                                 mylabel = Label(self.frame2, font=("Comic Sans MS", 15,"bold"), bg="lightgray",fg="green", textvariable=Texte).place(x=290,y=263,width=545)
                                                 Texte.set('la solution  '+ str(C) + '  est un minimum de la fonction f(x) ')
                                                 plt.plot(C, f(C), 'g+')
                                                 break
                                             elif(fseconfDec < 0):
                                                 self.varsolBissect.set(C)
                                                 self.varbissecitir.set(i)
                                                 Texte = StringVar()
                                                 mylabel = Label(self.frame2, font=("Comic Sans MS", 15,"bold"), bg="lightgray",fg="green", textvariable=Texte).place(x=290,y=263,width=545)
                                                 Texte.set('la solution  '+ str(C) + '  est un maximum de la fonction f(x)')
                                                 plt.plot(C, f(C), 'g+')
                                                 break   
                                             else :
                                                 self.var_iterpreBissec.set("Ona une Point d inflexion dans le point : "+str(C))
                                                 MessageBox.showinfo("Error"," Ona une Point d'inflexion !!", parent=self.fenetre1)
                                                 break
                                       else :
                                           if(j== A and k==B):
                                                break
                                           else:
                                                plt.plot(A, f(A), 'r.')
                                                A = C
                                                j=A
                                                i+=1
                                 else :
                                     if(A==j and k == B): 
                                         break
                                     else:  
                                         plt.plot(B, f(B), 'r.')
                                         B = C
                                         k= B
                                         i+=1
                                     
                             elif((aprim > 0 and bprim > 0)or(aprim < 0 and bprim < 0)) :
                                 quit()
                                 
                         self.varDeA.set(A)
                         self.varDeBsol.set(B)
                         self.varbissecitir.set(i)
                         self.var_iterpreBissec.set("la solution x* est dans l'intervale ["+str(A) +" , "+ str(B) +"]")
                         plt.plot(A, f(A), label="l'intervale [a, b] ")
                         plt.plot(A, f(A), 'g+')
                         plt.plot(B, f(B), 'g+')
                         plt.legend()
                         plt.show()
                     else:
                         MessageBox.showwarning("Error","On ne peut pas Appliquer algorithme de Bissection sur cette fonction22tion dans ces deux points. par ce que ona f'(a)*f'(b) > 0 !!",parent=self.fenetre1)
                         self.var_iterpreBissec.set("Bissection ne fonction22tions pas car f'(a)*f'(b) > 0")
                         plt.clf()
                         
                except Exception as es:                  
                        MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre1)  
                
       

     #======================Le gghaphe de la fonction==========================#   
    def graphe_de_fonction(self):
            val1 = self.txtValeur_A.get()
            val2 = self.txtValeur_B.get()
            fonc = self.txt_fonction.get()
            
            if(val1 =="" or val2 ==""  or fonc =="" ):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre1)
            elif(val1 > val2):
                MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre1)
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
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre1) 
        
        

# fenetre1=Tk()
# obj=Bissection(fenetre1)
# fenetre1.mainloop()  
        
        
        

