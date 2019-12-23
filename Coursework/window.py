# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:15:31 2019

@author: Nikita
"""

import tkinter
import tkinter.messagebox
from bigPrime import big_prime
from open_RSA_key import open_key
from miller_rabin import miller_rabin_test, miller_rabin
from simpleCoding import ru_file_simple,en_file_simple,ru_en_file_simple 
from simpleDeCoding import decoding_ru_en_simple,decoding_ru_simple,decoding_en_simple

class Prime:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Prime numbers')
        self.main_window.configure(bg='turquoise4')
        
        self.prime_button = tkinter.Button(text='Generation of the prime number',
                                           command=self.prime_gen_start,
                                           activebackground = 'gray',
                                           font=("Serif", 9),
                                           height = 1, 
                                           width = 30).grid(row=0, 
                                                            column=0,
                                                            columnspan=2)
        self.RSA_button = tkinter.Button(text='Generation of the RSA keys',
                                         command=self.RSA_gen,
                                         activebackground = 'gray',
                                         font=("Serif", 9),
                                         height = 1, 
                                         width = 30).grid(row=0, 
                                                          column=2,
                                                          columnspan=2)
        self.RSA_button = tkinter.Button(text='PrimeQ test',
                                         command=self.primeQ,
                                         activebackground = 'gray',
                                         font=("Serif", 9),
                                         height = 1, 
                                         width = 30).grid(row=1, 
                                                          column=0,
                                                          columnspan=4,pady=5)
        self.RSA_code = tkinter.Button(text='Coding',
                                         command=self.open_start,
                                         activebackground = 'gray',
                                         font=("Serif", 9),
                                         height = 1, 
                                         width = 30).grid(row=2, 
                                                          column=0,
                                                          columnspan=2)                                                         
        self.RSA_De_code = tkinter.Button(text='Decoding',
                                         command=self.close_start,
                                         activebackground = 'gray',
                                         font=("Serif", 9),
                                         height = 1, 
                                         width = 30).grid(row=2, 
                                                          column=2,
                                                          columnspan=2)                                                                                                                  
        '''
        Конструкция генерации простого числа
        '''                                                  
        self.minMaxTxt = tkinter.Label(text='Generation of the prime number',
                                       bg='turquoise4',
                                       fg='white',
                                       font=("Serif", 9,'bold'))
        self.minIn = tkinter.Label(text='From:',
                                   bg='turquoise4',
                                   fg='white',
                                   font=("Serif", 9,'bold'))
        self.minInTxt = tkinter.Entry(width=12)
        self.minInSt = tkinter.Label(text='Power*',
                                     bg='turquoise4',
                                     fg='white',
                                     font=("Serif", 9,'bold'))
        self.minInStTxt = tkinter.Entry(width=12)
        self.maxIn = tkinter.Label(text='To:',
                                   bg='turquoise4',
                                   fg='white',
                                   font=("Serif", 9,'bold'))            
        self.maxInTxt = tkinter.Entry(width=12)
        self.maxInSt = tkinter.Label(text='Power*',
                                     bg='turquoise4',
                                     fg='white',
                                     font=("Serif", 9,'bold'))  
        self.maxInStTxt = tkinter.Entry(width=12)
        self.get_res_buttom = tkinter.Button(text='Start',
                                             activebackground = 'gray',
                                             font=("Serif", 9),
                                             command=self.prime_gen_res,
                                             height = 1,
                                             width = 15)
        self.genPRes = tkinter.Text(width=40,height=1)
        self.genPRes.configure(state='disabled')
        self.genPResTxt = tkinter.Label(text='Result:',bg='turquoise4',fg='white',font=("Serif", 9,'bold'))
        self.genPResHelp = tkinter.Label(text='*Default power == 1',
                                         bg='turquoise4',fg='white',
                                         font=("Serif", 9,'bold'))
        '''
        Конструкция проверки числа на простоту
        '''
        self.primeQTxt = tkinter.Label(text='PrimeQ test',
                                       bg='turquoise4',
                                       fg='white',
                                       font=("Serif", 9,'bold'))
        self.primeIn = tkinter.Label(text='Number: ',
                                     bg='turquoise4',
                                     fg='white',
                                     font=("Serif", 9,'bold'))
        self.primeInTxt = tkinter.Entry(width=42)
        self.primeTestIn = tkinter.Label(text='Test:**',
                                         bg='turquoise4',
                                         fg='white',
                                         font=("Serif", 9,'bold')) 
        self.primeTestTxt = tkinter.Entry(width=42)
        self.primeQ_res_buttom = tkinter.Button(text='Start',
                                             activebackground = 'gray',
                                             command=self.primeQ_res,
                                             height = 1,
                                             width = 15,
                                             font=("Serif", 9))   
        self.primeResTxt = tkinter.Text(width=40,height=1)
        self.primeResTxt.configure(state='disabled')
        self.primeQOut = tkinter.Label(text='Result:',
                                       bg='turquoise4',
                                       fg='white',
                                       font=("Serif", 9,'bold'))
        self.primeHelp = tkinter.Label(text='**Default number of tests == log2(number)',
                                       bg='turquoise4',
                                       fg='white',
                                       font=("Serif", 9,'bold')) 
        '''
        Конструктор генерации ключей RSA
        '''
        self.RSATxt = tkinter.Label(text='Generation of the RSA keys',
                                    bg='turquoise4',
                                    fg='white',
                                    font=("Serif", 9,'bold'))
        self.RSAminIn = tkinter.Label(text='From:',
                                      bg='turquoise4',
                                      fg='white',
                                      font=("Serif", 9,'bold'))
        self.RSAminInTxt = tkinter.Entry(width=12)
        self.RSAminInSt = tkinter.Label(text='Power*',
                                        bg='turquoise4',
                                        fg='white',
                                        font=("Serif", 9,'bold'))
        self.RSAminInStTxt = tkinter.Entry(width=12)
        self.RSAmaxIn = tkinter.Label(text='To:',
                                      bg='turquoise4',
                                      fg='white',
                                      font=("Serif", 9,'bold'))            
        self.RSAmaxInTxt = tkinter.Entry(width=12)
        self.RSAmaxInSt = tkinter.Label(text='Power*',
                                        bg='turquoise4',
                                        fg='white',
                                        font=("Serif", 9,'bold'))  
        self.RSAmaxInStTxt = tkinter.Entry(width=12)
        self.RSAgetResbuttom = tkinter.Button(text='Start',
                                             activebackground = 'gray',
                                             command=self.RSA_gen_res,
                                             height = 1,
                                             width = 15,
                                             font=("Serif", 9))
        self.RSAopenOut= tkinter.Label(text='Open',
                                       bg='turquoise4',
                                       fg='white',
                                       font=("Serif", 9,'bold'))
        self.RSAopenTxt = tkinter.Text(width=40,height=1)
        self.RSAopenTxt.configure(state='disabled')
        self.RSAcloseOut = tkinter.Label(text='Close',
                                         bg='turquoise4',
                                         fg='white',
                                         font=("Serif", 9,'bold'))
        self.RSAcloseTxt = tkinter.Text(width=40,height=1)
        self.RSAcloseTxt.configure(state='disabled')
        
        '''
        Конструктор кодировки txt файла
        '''        
        self.codeStart = tkinter.Label(text='Coding',
                                       bg='turquoise4',
                                       fg='white',
                                       font=("Serif", 9,'bold')) 
        self.abc = tkinter.Label(text='abc:',
                                 bg='turquoise4',
                                 fg='white',
                                 font=("Serif", 9,'bold'))
        self.openKE = tkinter.Label(text='OpenK(e):',
                                    bg='turquoise4',
                                    fg='white',
                                    font=("Serif", 9,'bold'))
        self.openKEIn = tkinter.Entry(width=13)
        self.openKN = tkinter.Label(text='OpenK(n):',bg='turquoise4',fg='white',font=("Serif", 9,'bold'))
        self.openKNIn = tkinter.Entry(width=13)
        self.file = tkinter.Label(text='Source:',bg='turquoise4',fg='white',font=("Serif", 9,'bold'))
        self.fileName = tkinter.Entry(width=50)
        self.fileOut = tkinter.Label(text='Result:',bg='turquoise4',fg='white',font=("Serif", 9,'bold'))
        self.fileOutName = tkinter.Entry(width=50)
        self.variable = tkinter.StringVar(self.main_window)
        self.variable.set("Eng/Rus") # default value
        self.lstLang = tkinter.OptionMenu(self.main_window, self.variable, 
                                          "Eng/Rus", "Eng", "Rus")
        self.openButStart = tkinter.Button(text='Encode',
                                                 activebackground = 'gray',
                                             command=self.openKstart,
                                             height = 1,
                                             width = 15,
                                             font=("Serif", 9))
        self.openHelp = tkinter.Label(text='Work with txt file',
                                       bg='turquoise4',
                                       fg='white',
                                       font=("Serif", 9,'bold')) 

        '''
        Конструктор декодировки txt файла
        '''        
        self.decodeStart = tkinter.Label(text='Decoding',
                                         bg='turquoise4',
                                         fg='white',
                                         font=("Serif", 9,'bold')) 
        self.deabc = tkinter.Label(text='abc:',bg='turquoise4',fg='white',font=("Serif", 9,'bold'))
        self.closeKD = tkinter.Label(text='CloseK(d):',bg='turquoise4',fg='white',font=("Serif", 9,'bold'))
        self.closeKDIn = tkinter.Entry(width=13)
        self.closeKN = tkinter.Label(text='CloseK(n):',bg='turquoise4',fg='white',font=("Serif", 9,'bold'))
        self.closeKNIn = tkinter.Entry(width=13)
        self.defile = tkinter.Label(text='Source:',bg='turquoise4',fg='white',font=("Serif", 9,'bold'))
        self.defileName = tkinter.Entry(width=50)
        self.defileOut = tkinter.Label(text='Result:',bg='turquoise4',fg='white',font=("Serif", 9,'bold'))
        self.defileOutName = tkinter.Entry(width=50)
        self.devariable = tkinter.StringVar(self.main_window)
        self.devariable.set("Eng/Rus") # default value
        self.delstLang = tkinter.OptionMenu(self.main_window, self.devariable, 
                                          "Eng/Rus", "Eng", "Rus")
        self.closeButStart = tkinter.Button(text='Decode',
                                                 activebackground = 'gray',
                                             command=self.closeKstart,
                                             height = 1,
                                             width = 15,
                                             font=("Serif", 9))
        self.closeHelp = tkinter.Label(text='Work with txt file',
                                       bg='turquoise4',
                                       fg='white',
                                       font=("Serif", 9,'bold')) 

        self.prime_gen_start()

        tkinter.mainloop()       
    
    def open_start(self):
        self.close_remove()
        self.primeQ_remove()
        self.RSA_gen_remove()
        self.prime_gen_remove()
        self.codeStart.grid(row=3,column=0,columnspan=4)
        self.openKE.grid(row=4, column=0,padx=10,pady=10)
        self.openKEIn.grid(row=4, column=1,padx=10,pady=10)
        self.openKN.grid(row=4, column=2,padx=10,pady=10)
        self.openKNIn.grid(row=4, column=3,padx=10,pady=10)
        self.file.grid(row=5, column=0)
        self.fileName.grid(row=5, column=1,columnspan=3)
        self.fileOut.grid(row=6, column=0,padx=10,pady=10)
        self.fileOutName.grid(row=6, column=1,columnspan=3,padx=10,pady=10)
        self.lstLang.grid(row=7,column=0,columnspan=2)
        self.openButStart.grid(row=7,column=2,columnspan=2)
        self.openHelp.grid(row=8,column=0,columnspan=4,pady=7,sticky='e')
        
    def close_start(self):
        self.open_remove()
        self.primeQ_remove()
        self.RSA_gen_remove()
        self.prime_gen_remove()
        self.decodeStart.grid(row=3,column=0,columnspan=4)
        self.closeKD.grid(row=4, column=0,padx=10,pady=10)
        self.closeKDIn.grid(row=4, column=1,padx=10,pady=10)
        self.closeKN.grid(row=4, column=2,padx=10,pady=10)
        self.closeKNIn.grid(row=4, column=3,padx=10,pady=10)
        self.defile.grid(row=5, column=0)
        self.defileName.grid(row=5, column=1,columnspan=3)
        self.defileOut.grid(row=6, column=0,padx=10,pady=10)
        self.defileOutName.grid(row=6, column=1,columnspan=3,padx=10,pady=10)
        self.delstLang.grid(row=7,column=0,columnspan=2)
        self.closeButStart.grid(row=7,column=2,columnspan=2)
        self.closeHelp.grid(row=8,column=0,columnspan=4,pady=7,sticky='e')
    
    def prime_gen_start(self):
        self.close_remove()
        self.primeQ_remove()
        self.RSA_gen_remove()
        self.open_remove()
        self.minMaxTxt.grid(row=3,column=0,columnspan=4)
        self.minIn.grid(row=4, column=0,padx=10,pady=10)
        self.minInTxt.grid(row=4, column=1)
        self.minInSt.grid(row=4, column=2)
        self.minInStTxt.grid(row=4, column=3)  
        self.maxIn.grid(row=5, column=0)        
        self.maxInTxt.grid(row=5, column=1)  
        self.maxInSt.grid(row=5, column=2)
        self.maxInStTxt.grid(row=5, column=3)
        self.get_res_buttom.grid(row=6,column=0,columnspan=4,padx=10,pady=10)
        self.genPRes.grid(row=7,column=1,columnspan=3)
        self.genPResTxt.grid(row=7,column=0)
        self.genPResHelp.grid(row=8,column=0,columnspan=4,pady=10,sticky='e')
        
    def RSA_gen(self):
        self.close_remove()
        self.primeQ_remove()
        self.prime_gen_remove()
        self.open_remove()
        self.RSATxt.grid(row=3,column=0,columnspan=4)
        self.RSAminIn.grid(row=4, column=0,padx=10,pady=10)
        self.RSAminInTxt.grid(row=4, column=1)
        self.RSAminInSt.grid(row=4, column=2)
        self.RSAminInStTxt.grid(row=4, column=3)  
        self.RSAmaxIn.grid(row=5, column=0)        
        self.RSAmaxInTxt.grid(row=5, column=1)  
        self.RSAmaxInSt.grid(row=5, column=2)
        self.RSAmaxInStTxt.grid(row=5, column=3)
        self.RSAgetResbuttom.grid(row=6,column=0,columnspan=4,padx=10,pady=10)
        self.RSAopenOut.grid(row=7,column=0)
        self.RSAopenTxt.grid(row=7,column=1,columnspan=3)
        self.RSAcloseOut.grid(row=8,column=0)
        self.RSAcloseTxt.grid(row=8,column=1,columnspan=3,pady=10)
                
    def primeQ(self):
        self.close_remove()
        self.prime_gen_remove()
        self.RSA_gen_remove()
        self.open_remove()
        self.primeQTxt.grid(row=3,column=0,columnspan=4)
        self.primeIn.grid(row=4, column=0,padx=10,pady=10)
        self.primeInTxt.grid(row=4, column=1,columnspan=3)
        self.primeTestIn.grid(row=5, column=0)
        self.primeTestTxt.grid(row=5, column=1,columnspan=3)
        self.primeQ_res_buttom.grid(row=6,column=0,columnspan=4,padx=10,pady=10)
        self.primeQOut.grid(row=7,column=0)
        self.primeResTxt.grid(row=7,column=1,columnspan=3)
        self.primeHelp.grid(row=8,column=0,columnspan=4,pady=10,sticky='e')
  
    def openKstart(self):
        try:
            e = int(self.openKEIn.get())
            n = int(self.openKNIn.get())
            try:
                name = self.fileName.get()
                try:
                    nameRes = self.fileOutName.get()
                except Exception:
                    nameRes = 'code' 
                f = self.variable.get()
                file1 = name+'.txt'
                file2 = nameRes+'.txt'
                if f == "Eng/Rus":
                    ru_en_file_simple(file1,file2,e,n)
                elif f == "Eng":
                    en_file_simple(file1,file2,e,n)
                else:
                    ru_file_simple(file1,file2,e,n)                              
            except Exception:
                tkinter.messagebox.showinfo('Ошибка','Неверное название файла-источника.')          

        except Exception:
            tkinter.messagebox.showinfo('Ошибка','Ошибка ввода открытого ключа.')          

            
    def closeKstart(self):
        try:
            d = int(self.closeKDIn.get())
            n = int(self.closeKNIn.get())
            try:
                name = self.defileName.get()
                try:
                    nameRes = self.defileOutName.get()
                except Exception:
                    nameRes = 'decode' 
                f = self.devariable.get()
                file2 = name+'.txt'
                file3 = nameRes+'.txt'
                if f == "Eng/Rus":
                    decoding_ru_en_simple(file2,file3,d,n)
                elif f == "Eng":
                    decoding_en_simple(file2,file3,d,n)
                else:
                    decoding_ru_simple(file2,file3,d,n)                              
            except Exception:
                tkinter.messagebox.showinfo('Ошибка','Неверное название файла-источника.') 
        except Exception:
            tkinter.messagebox.showinfo('Ошибка','Ошибка ввода закрытого ключа.') 
    
    def RSA_gen_res(self):
        try:
            frm = int(self.RSAminInTxt.get())           
            to = int(self.RSAmaxInTxt.get())
            try:
                frmSt = int(self.RSAminInStTxt.get())
            except Exception:
                frmSt = 1
            try:
                toSt = int(self.RSAmaxInStTxt.get())
            except Exception:
                toSt = 1
            a = frm**frmSt
            b = to**toSt
            res = open_key(a,b)
            self.RSAopenTxt.configure(state='normal')
            self.RSAopenTxt.delete(1.0,'end')
            self.RSAopenTxt.insert(1.0,'('+str(res[0])+','+str(res[2])+')')
            self.RSAopenTxt.configure(state='disabled')
            self.RSAcloseTxt.configure(state='normal')
            self.RSAcloseTxt.delete(1.0,'end')
            self.RSAcloseTxt.insert(1.0,'('+str(res[1])+','+str(res[2])+')')
            self.RSAcloseTxt.configure(state='disabled')
        except Exception:
            tkinter.messagebox.showinfo('Ошибка','Неверные данные.\nНеобходимо ввести числа в первую колонку.')          

    def prime_gen_res(self):
        try:
            frm = int(self.minInTxt.get())
            to = int(self.maxInTxt.get())            
            try:
                frmSt = int(self.minInStTxt.get())
            except Exception:
                frmSt = 1
                
            try:
                toSt = int(self.maxInStTxt.get())
            except Exception:
                toSt = 1
            out = big_prime(frm**frmSt,to**toSt)
            self.genPRes.configure(state='normal')
            self.genPRes.delete(1.0,'end')
            self.genPRes.insert(1.0,out)
            self.genPRes.configure(state='disabled')
        except Exception:
            tkinter.messagebox.showinfo('Ошибка','Неверные данные.\nНеобходимо ввести числа в первую колонку.')

            
    def primeQ_res(self):
        try:
            num = int(self.primeInTxt.get())
            try:
                rnds = int(self.primeTestTxt.get())
                if miller_rabin(num,rnds) == True:
                    out = 'Вероятно простое'
                else:
                    out = 'Составное'
                self.primeResTxt.configure(state='normal')
                self.primeResTxt.delete(1.0,'end')
                self.primeResTxt.insert(1.0,out)
                self.primeResTxt.configure(state='disabled')
            except Exception:
                if miller_rabin_test(num) == True:
                    out = 'Вероятно простое'
                else:
                    out = 'Составное'
                self.primeResTxt.configure(state='normal')
                self.primeResTxt.delete(1.0,'end')
                self.primeResTxt.insert(1.0,out)
                self.primeResTxt.configure(state='disabled')
        except Exception:
            tkinter.messagebox.showinfo('Ошибка','Введите число для проверки в поле.')            
            
    def prime_gen_remove(self):    
        self.minMaxTxt.grid_remove()
        self.minIn.grid_remove()
        self.minInTxt.grid_remove()
        self.minInSt.grid_remove()
        self.minInStTxt.grid_remove()
        self.maxIn.grid_remove()
        self.maxInTxt.grid_remove()
        self.maxInSt.grid_remove()
        self.maxInStTxt.grid_remove()
        self.get_res_buttom.grid_remove()
        self.genPRes.grid_remove()
        self.genPResTxt.grid_remove()
        self.genPResHelp.grid_remove()
        
    def primeQ_remove(self):
        self.primeQTxt.grid_remove()
        self.primeIn.grid_remove()
        self.primeInTxt.grid_remove()
        self.primeTestIn.grid_remove()
        self.primeTestTxt.grid_remove()
        self.primeQ_res_buttom.grid_remove()  
        self.primeResTxt.grid_remove() 
        self.primeHelp.grid_remove()
        self.primeQOut.grid_remove()
        
    def RSA_gen_remove(self):
        self.RSATxt.grid_remove()
        self.RSAminIn.grid_remove()
        self.RSAminInTxt.grid_remove()
        self.RSAminInSt.grid_remove()
        self.RSAminInStTxt.grid_remove()
        self.RSAmaxIn.grid_remove()
        self.RSAmaxInTxt.grid_remove()
        self.RSAmaxInSt.grid_remove()
        self.RSAmaxInStTxt.grid_remove()
        self.RSAgetResbuttom.grid_remove()
        self.RSAopenOut.grid_remove()
        self.RSAopenTxt.grid_remove()
        self.RSAcloseOut.grid_remove()
        self.RSAcloseTxt.grid_remove()
        
    def open_remove(self):
        self.lstLang.grid_remove()
        self.codeStart.grid_remove()
        self.openKE.grid_remove()
        self.openKEIn.grid_remove()
        self.openKN.grid_remove()
        self.openKNIn.grid_remove()
        self.file.grid_remove()
        self.fileName.grid_remove()
        self.fileOut.grid_remove()
        self.fileOutName.grid_remove()
        self.openButStart.grid_remove()
        self.openHelp.grid_remove()

    def close_remove(self):
        self.delstLang.grid_remove()
        self.decodeStart.grid_remove()
        self.closeKD.grid_remove()
        self.closeKDIn.grid_remove()
        self.closeKN.grid_remove()
        self.closeKNIn.grid_remove()
        self.defile.grid_remove()
        self.defileName.grid_remove()
        self.defileOut.grid_remove()
        self.defileOutName.grid_remove()
        self.closeButStart.grid_remove()
        self.closeHelp.grid_remove()
            
my_gui = Prime()
