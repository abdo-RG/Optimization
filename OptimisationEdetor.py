from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import filedialog
import tkinter.messagebox as MessageBox
from PIL import Image,ImageTk
import subprocess



file_path = ""
class OptemisationEditor:
    def __init__(self, master):
        self.master = master
        #------------création de la fenetre prinipale-----------------------------#
        self.master.title("Optimisation Editeur ")
        self.master.geometry("1500x740+50+50")
        
        self.contenu = Text(self.master , undo= True, bg="#C0C5C5", fg="#12385E", font=("Consolas",12), highlightbackground="#182350",highlightthickness=2)
        self.contenu.pack(expand= True, fill='both')
        self.outputcod = Text(self.master, height=10, bg="#101015",fg="#F2F2FC", font=("Consolas",12),highlightbackground="#182350",highlightthickness=1)
        self.outputcod.pack(expand= True, fill='both')
        
        self.openImage =ImageTk.PhotoImage(file="images/33.jpg")
        self.saveImage =ImageTk.PhotoImage(file="images/55.jpg")
        self.saveasImage =ImageTk.PhotoImage(file="images/66.jpg")
        self.validImage =ImageTk.PhotoImage(file="images/444.ico")
        self.runImage =ImageTk.PhotoImage(file="images/logo1.ico")
        self.anulerImage =ImageTk.PhotoImage(file="images/22.jpg")
        self.roturnImage =ImageTk.PhotoImage(file="images/11.jpg")
        self.supprimnImage =ImageTk.PhotoImage(file="images/77.jpg")
        self.copyImage =ImageTk.PhotoImage(file="images/99.jpg")
        self.copierImage =ImageTk.PhotoImage(file="images/00.jpg")
        
        
        menuBar = Menu(self.master)
        #----------------Menue de fichier-------------------------------------#
        menuFichier = Menu(menuBar, tearoff= False,font=("Comic Sans MS",12, "bold"))
        menuBar.add_cascade(label = " File ", font=("Comic Sans MS", 12, "bold"), menu = menuFichier)
        menuFichier.add_command(label= " Open File ", font=("Comic Sans MS",12, "bold"), command=self.ouvrir, image=self.openImage, compound='left')
        menuFichier.add_command(label= " Save ", font=("Comic Sans MS", 12, "bold"), command=self.enregistrer_sous, image = self.saveImage,compound='left')
        menuFichier.add_command(label= " Save as ", font=("Comic Sans MS", 12, "bold"), command=self.enregistrer_sous , image = self.saveasImage, compound='left')
        menuFichier.add_separator()
        menuFichier.add_command(label = " Quit ", font=("Comic Sans MS", 12, "bold"), image=self.anulerImage, compound='left', command=self.quiter)
        
        
        #----------------Menue Edition----------------------------------------#
        menuEdition = Menu(menuBar, tearoff= 0)
        menuBar.add_cascade(label = " Edit ", font=("Comic Sans MS",12, "bold"), menu= menuEdition)
        menuEdition.add_command(label= "Cancel",font=("Comic Sans MS",12, "bold"), image=self.supprimnImage, compound='left', command=self.annuler)
        menuEdition.add_command(label= " Undo ",font=("Comic Sans MS",12, "bold"), image = self.roturnImage,compound='left', command=self.retablir)
        menuEdition.add_command(label= " Copy ", font=("Comic Sans MS",12, "bold"), command=self.copier, image = self.copierImage, compound='left')
        menuEdition.add_command(label= " Cut ", font=("Comic Sans MS",12, "bold"), command=self.couper, image = self.copyImage, compound='left')
        menuEdition.add_command(label= " Paste ", font=("Comic Sans MS",12, "bold"), image=self.validImage, compound='left', command=self.coller)
        

        #--------------Menu de Run--------------------------------------------#
        menuRun = Menu(menuBar, tearoff = False)
        menuBar.add_cascade(label = " Run ",  font=("Comic Sans MS",12, "bold"), background="#C8DCAC", menu= menuRun)
        menuRun.add_cascade(label= " Run file ", font=("Comic Sans MS",12, "bold"), image=self.runImage, compound='left', command = self.runfonction)
       
        #----------------Menue de fichier-------------------------------------#
        menuAlgorithme = Menu(menuBar, tearoff= False)
        menuBar.add_cascade(label = "Unimodale Problems", font=("Comic Sans MS", 14, "bold"), background="#8AAB96", menu = menuAlgorithme)
        menuAlgorithme.add_command(label= "Bissection ", font=("Comic Sans MS", 14, "bold"), background="#8AAB96", foreground="#F6FAF7", activebackground= "#BADDDE", activeforeground="#252723",  command=self.BissectionAlgo)
        menuAlgorithme.add_command(label= "Dichotomous ", font=("Comic Sans MS",14, "bold"), background="#8AAB96", foreground="#F6FAF7", activebackground= "#BADDDE", activeforeground="#252723", command=self.DichotomiqueAlgo)
        menuAlgorithme.add_command(label= "Fibonacci ", font=("Comic Sans MS", 14, "bold"), background="#8AAB96", foreground="#F6FAF7", activebackground= "#BADDDE", activeforeground="#252723", command=self.FibonacciAlgo)
        menuAlgorithme.add_command(label = "Section d'or", font=("Comic Sans MS", 14, "bold"), background="#8AAB96", foreground="#F6FAF7", activebackground= "#BADDDE", activeforeground="#252723", command=self.SectionDor)
        menuAlgorithme.add_command(label = "Newton ", font=("Comic Sans MS", 14, "bold"), background="#8AAB96",  foreground="#F6FAF7", activebackground= "#BADDDE", activeforeground="#252723", command=self.NewtonAlgo)
        menuAlgorithme.add_command(label = "Fausse Position ", font=("Comic Sans MS", 14, "bold"), background="#8AAB96", foreground="#F6FAF7",activebackground= "#BADDDE", activeforeground="#252723", command=self.FaussePositionAlgo)


        #---------------------moltidimentionnel-------------------------------#
        menuMultivar = Menu(menuBar, tearoff= False)
        menuBar.add_cascade(label = "Multimodale Problems", font=("Comic Sans MS", 14, "bold"), background="#68802B", menu = menuMultivar)
        menuMultivar.add_command(label= "Méthode de Gradient", font=("Comic Sans MS", 14, "bold"), background="#407A6E", foreground="#F5F8EE", activebackground= "#DFF3CD", activeforeground="#252723", command=self.gradDesend)
        menuMultivar.add_command(label= "Gradient Conjugué", font=("Comic Sans MS", 14, "bold"), background="#407A6E", foreground="#F5F8EE", activebackground= "#DFF3CD", activeforeground="#252723", command=self.gradConjuger)
        menuMultivar.add_command(label= "Methode de Newton  ", font=("Comic Sans MS", 14, "bold"), background="#407A6E", foreground="#F5F8EE", activebackground= "#DFF3CD", activeforeground="#252723", command=self.newtonMultivar)
        menuMultivar.add_command(label = "Quasi-Newton", font=("Comic Sans MS", 14, "bold"), background="#407A6E", foreground="#F5F8EE", activebackground= "#DFF3CD", activeforeground="#252723", command=self.quasinewton)

        self.master.config(menu = menuBar)
        
        
        
        
        
    #=========================================================================#
    def set_file_path(self, path):
        global  file_path
        file_path = path
    
    
    
    #------------création de menu---------------------#
    
    def quiter(self):
       self.master.quit()
       self.master.destroy()
       #-----------noveau fichier---------------------#
       
       
   

        #-----------------os.popen execut en fichier--------------------------#
       # os.popen("python main.py")
        
    def ouvrir(self):
         self.path = askopenfilename(filetypes=[('Python Files', '*.py')])
         if(self.path==''):
             return
         with open(self.path, 'r') as file:
             self.code = file.read()
             self.contenu.delete('1.0' , END)
             self.contenu.insert('1.0' , self.code)
             self.set_file_path(self.path)

        
        
         
   #-----------------------------enregistrer sous-----------------------------#
    def enregistrer_sous(self):
        if (file_path == '' ):     
            self.path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            self.path = file_path
        with open(self.path, 'w') as file:
            self.code = self.contenu.get('1.0', END)
            file.write(self.code)
            self.set_file_path(self.path)
    
  
    #=========================Action de Menu Edition==========================#
    def copier(self):
        self.contenu.clipboard_clear()
        self.contenu.clipboard_append(self.contenu.selection_get()) 
        
    def couper(self):
        self.copier()
        self.contenu.delete('sel.first' , 'sel.last')
        
    def coller(self): 
        self.contenu.insert(INSERT ,self.contenu.clipboard_get())
    
    def annuler(self):
        self.contenu.edit_undo()
    
    def retablir(self):
        self.contenu.edit_redo()
        
    #=============================la fonction Run ============================#
    def runfonction(self):
        if file_path == '' :
            MessageBox.showerror("Error","Please save your code ! ", parent=self.master)
            #save_prompt = Toplevel()
            #text = Label(save_prompt, text='Please save your code !')
            #text.pack()
            return     
        command = f'python {file_path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        self.outputcod.insert('1.0', output)
        self.outputcod.insert('1.0', error)
        
        
        
        
#=======================unimodale=============================================#

    def BissectionAlgo(self):
        #self.master.destroy()
        from BissectionClasse import  Bissection
        fenebesc = Toplevel()
        objbisec = Bissection(fenebesc)
        fenebesc.mainloop()  
        
   
    def DichotomiqueAlgo(self):
        #self.master.destroy()
        from DichotomiqueClasse import  Dichotomique
        fenedico = Toplevel()
        dichobjet = Dichotomique(fenedico)
        fenedico.mainloop()  
        
    def FibonacciAlgo(self):
        #self.master.destroy()
        from FibonacciClasse import  Fibonacci
        winfibo = Toplevel()
        fibobjet = Fibonacci(winfibo)
        winfibo.mainloop()  
        
    def SectionDor(self):
        #self.master.destroy()
        from SectionDorClasse import  SectionDor
        fnsect = Toplevel()
        secobjet = SectionDor(fnsect)
        fnsect.mainloop()  
        
    def NewtonAlgo(self):
        #self.master.destroy()
        from NewtonClasse import  NewtonClasse
        objNew = Toplevel()
        newobjet = NewtonClasse(objNew)
        objNew.mainloop()  
        
       
    def FaussePositionAlgo(self):
        #self.master.destroy()
        from FaussePositionClasse import  FaussePosition
        fauswind = Toplevel()
        fausobjet = FaussePosition(fauswind)
        fauswind.mainloop()  

#=======================multimudale============================================#

    def quasinewton(self):
        #self.master.destroy()
        from QuasiNewtonClasse import  quasiNewton
        quasiwin = Toplevel()
        quasbjet = quasiNewton(quasiwin)
        quasiwin.mainloop()  
        
    def gradConjuger(self):
        #self.master.destroy()
        from ConjugateGradient import  ConjugateGradient
        conjugrad = Toplevel()
        quasbjet = ConjugateGradient(conjugrad)
        conjugrad.mainloop()      


    def newtonMultivar(self):
        #self.master.destroy()
        from NewtonMultivar import  NewtonMultivar 
        netwindow = Toplevel()
        quasbjet = NewtonMultivar(netwindow)
        netwindow.mainloop()      
        
        
    def gradDesend(self):
        #self.master.destroy()
        from GradientDes import  GradientDes 
        gradindow = Toplevel()
        quasbjet = GradientDes(gradindow)
        gradindow.mainloop()      
        
              
   
master = Tk()
edobje = OptemisationEditor(master)
master.mainloop() 



