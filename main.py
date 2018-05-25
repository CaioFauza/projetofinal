# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 08:06:44 2018

@author: Alexandre, Caio, Ricardo
"""
import tkinter as tk
import win32com.client as wincl
try: 
    import speech_recognition as sr
except:
    import subprocess
    subprocess.call("pip", "install", "SpeechRecognition")
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import datetime
from firebase import firebase


firebase = firebase.FirebaseApplication("https://foodtoolsprojeto.firebaseio.com/", None)
variavelnumeropedidos = 50
variavelnumeromesas = 45
variavelnumerofuncionarios = 5
variavelreceitabruta = 14000
variaveldespesas = 6000
variavelfaturamento = variavelreceitabruta - variaveldespesas
variavelreservas = 20
salao = True
cozinha = False
adm = False
dados = firebase.get("", None)
    ######### openpyxl
    
listadespesadelete = []
#listadelojas= ["Franquia 1", "Franquia 2", "Franquia 3", "Filial 1", "Filial 2"]
listadelojas = list()
for i in dados:
    listadelojas.append(i)
listadelojas.remove("Acesso")
class FoodTools: 
    
    def __init__(self):
        self.testlogin = True
        self.datadehoje = datetime.datetime.now()
        self.logins = firebase.get("", None)
        self.menu2 = False
        self.menu3 = False
        self.mainwindow = tk.Tk()
        self.mainwindow.title("Food Tools")
        self.mainwindow.geometry("1280x720")
        color = "sandy brown"
        self.mainwindow.configure(background=color)
        imagem = ImageTk.PhotoImage(Image.open("Logo2.png"))
        self.imagems = tk.Label(self.mainwindow, image = imagem, height = 282, width= 500, bg = color)
        self.imagems.image = imagem
        self.imagems.place(x = 350, y = 250)
        self.texto = tk.Label(self.mainwindow, font = ("verdana", 10), text = "Desenvolvido por Alexandre, Caio e Ricardo - Insper - 2018", bg = color)
        self.texto.place(x = 450, y = 560)
        self.canvaslogin = tk.Canvas(self.mainwindow, highlightbackground="saddle brown",highlightcolor="black", width = 325, height = 150, bg = "peru")
        self.canvaslogin.place(x = 900, y = 270)
        
        
        self.tlogin = tk.Label(self.mainwindow, text = "Autenticação ", font = ("Verdana", 20), bg = "peru")
        self.usuario = tk.Label(self.mainwindow, text = "Nome de usuário: ",     font = ("Verdana", 10), bg = "peru")
        self.senha = tk.Label(self.mainwindow, text = "Senha: ", font = ("Verdana", 10), bg = "peru")
        self.usuarioentry = tk.Entry(self.mainwindow, bg = "peru")
        self.senhaentry = tk.Entry(self.mainwindow, bg = "peru", show = "*")
        self.blogin = tk.Button(self.mainwindow, text = "Login", font = ("verdana", 10), bg = "peru", height= 2, width = 40, command = self.abrir)
        self.tlogin.place(x = 970, y = 285)
        self.usuario.place(x = 920, y = 335)
        self.senha.place(x = 920, y = 385)
        self.usuarioentry.place(x = 1050, y = 335)
        self.senhaentry.place(x = 1050, y = 385)
        self.blogin.place(x = 900, y = 485)
        self.imagemmic = ImageTk.PhotoImage(Image.open("microfone.png"))
        self.voicecommand = tk.Button(self.mainwindow, bg = "cyan" , image = self.imagemmic, command = self.voicebutton, height= 50, width = 50)
        
        self.voicecommand.image = self.imagemmic
        
        self.sairlogin = tk.Button(self.mainwindow, bg = "peru", fg= "black", text = "Sair (esc)",font = ("verdana", 10),  command = self.quit, height= 2, width = 40)
        self.sairlogin.place(x = 900, y = 535 )
        self.voicecommand.place(x= 1250, y = 500)
        self.mainwindow.bind("<Return>", lambda e: self.abrir())
        
        
        
    def voicebutton(self):
        self.speak = wincl.Dispatch("SAPI.SpVoice")
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()


        with self.mic as source:
            self.audio = self.r.listen(source, phrase_time_limit = 1)
    
            
            
        if self.r.recognize_google(self.audio, language = "pt-BR") == "entrar":
            try:
                self.abrir()
                
                
            except:
                pass
            return
            
            
        if self.r.recognize_google(self.audio, language = "pt-BR") == "sair":
            
            self.speak.Speak("Até logo")
            self.quit()
            return
        
        self.speak.Speak("Desculpe, não entendi. Por favor, tente novamente!")
            
    def abrir(self):
        try:        
            str(self.usuarioentry.get())
            if str(self.logins["Acesso"][str(self.usuarioentry.get())]["senha"]) == str(self.senhaentry.get()):
                try: 
                    self.tituloerrologin.destroy()
                    self.canvaserro.destroy()
                except:
                    pass
                self.voicecommand.destroy()
                self.iniciar = tk.Button(self.mainwindow, text = "Iniciar", font = ("verdana", 10), bg = "peru", height= 2, width = 40, command = self.iniciarfranquias)
                self.iniciar.place(x= 900, y = 350)
                self.configuracoes = tk.Button(self.mainwindow, bg = "peru", fg = "black", font = ("verdana", 10), text = "Ajustes de franquia", command = self.configuracoesf, height= 2, width = 40)
                self.configuracoes.place(x = 900, y = 400)
                self.sair = tk.Button(self.mainwindow, bg = "peru", fg= "black", text = "Sair (esc)",font = ("verdana", 10),  command = self.quit, height= 2, width = 40)
                self.sair.place(x = 900, y = 450 )
                self.imagemmic1 = ImageTk.PhotoImage(Image.open("microfone.png"))
                self.voicecommand1 = tk.Button(self.mainwindow, bg = "cyan" , image = self.imagemmic1, command = self.voicebutton1, height= 50, width = 50)
                self.voicecommand1.image = self.imagemmic1
                self.voicecommand1.place(x = 1250, y = 400)
                self.canvaslogin.destroy()
                self.blogin.destroy()
                self.tlogin.destroy()
                self.usuario.destroy()
                self.senha.destroy()
                self.usuarioentry.place_forget()
                self.senhaentry.place_forget()
                self.sairlogin.destroy()
                self.mainwindow.bind("<Return>", lambda e: self.bloquearlogin())
                try:
                    self.speak.Speak("Bom dia Usuário")
                except:
                    pass
            else: 
                self.canvaserro = tk.Canvas(self.mainwindow, highlightthickness=0, width = 328, height = 40, bg = "indian red")
                self.tituloerrologin = tk.Label(self.mainwindow, text = "Nome de usuário e/ou senha incorretos!", font = ("Verdana", 10), bg = "indian red")
                self.canvaserro.place(x = 900, y = 430)
                self.tituloerrologin.place(x = 910, y = 440)
                self.mainwindow.after(3000, self.mensagemdeerrologin)
                self.blogin.configure(command = self.bloquearlogin)
                self.mainwindow.bind("<Return>", lambda e: self.bloquearlogin())
        except:
            self.canvaserro = tk.Canvas(self.mainwindow, highlightthickness=0, width = 328, height = 40, bg = "indian red")
            self.tituloerrologin = tk.Label(self.mainwindow, text = "Nome de usuário e/ou senha incorretos!", font = ("Verdana", 10), bg = "indian red")
            self.canvaserro.place(x = 900, y = 430)
            self.tituloerrologin.place(x = 910, y = 440)
            self.mainwindow.after(3000, self.mensagemdeerrologin)
            self.blogin.configure(command = self.bloquearlogin)
            self.mainwindow.bind("<Return>", lambda e: self.bloquearlogin())
                
    def bloquearlogin(self):
        pass
    def voicebutton1(self):
        self.speak = wincl.Dispatch("SAPI.SpVoice")
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()


        with self.mic as source:
            self.audio = self.r.listen(source, phrase_time_limit = 1)
    
            
            
        if self.r.recognize_google(self.audio, language = "pt-BR") == "iniciar":
            try:
                self.iniciarfranquias()
                self.speak.Speak("Iniciando lista de franquias")
                
                
            except:
                pass
            return
        
        if self.r.recognize_google(self.audio, language = "pt-BR") == "ajustes de franquia":
            self.speak.Speak("Iniciando ajustes de configurações")
            self.configuracoes()
            return
            
            
            
        if self.r.recognize_google(self.audio, language = "pt-BR") == "sair":
            
            self.speak.Speak("Até logo")
            self.quit()
            return
        
        self.speak.Speak("Desculpe, não entendi. Por favor, tente novamente!")
        
    def mensagemdeerrologin(self):
        self.tituloerrologin.destroy()
        self.canvaserro.destroy()
        self.blogin.configure(command = self.abrir)
        self.mainwindow.bind("<Return>", lambda e: self.abrir())
        
        
    def voltarlogin(self):
        self.errologin.destroy()
        self.errologin.grab_release()
    
        
    def quit(self):
        self.mainwindow.destroy()
    
    def iniciarfranquias(self):
        self.iniciar.destroy()
        self.voicecommand2 = tk.Button(self.mainwindow, bg = "cyan" , image = self.imagemmic1, command = self.voicebutton2, height= 50, width = 50)
        self.voicecommand2.image = self.imagemmic1
        self.voicecommand2.place(x = 1300, y = 400)
        self.voicecommand1.destroy()
        self.configuracoes.destroy()
        self.sair.destroy()
        self.lojas = tk.Label(self.mainwindow, text = "Franquias disponíveis: ", font = ("Verdana", 20), bg= "sandy brown")
        self.lojas.place(x = 950, y = 200)
       
        
       
        
        try:
            len(listadelojas) == 1
            self.bfranquia1 =tk.Button(self.mainwindow, text = listadelojas[0], font= ("verdana", 10), bg = "peru", fg = "black", height= 2, width = 40, command = self.Franquia1)
            self.bfranquia1.place(x = 950, y = 300)
        except IndexError:
            pass
        
        try:
            len(listadelojas) == 2
            self.bfranquia2 =tk.Button(self.mainwindow, text = listadelojas[1], font= ("verdana", 10), bg = "peru", fg = "black", height= 2, width = 40, command = self.Franquia2)
            self.bfranquia2.place(x = 950, y = 350)
        except IndexError:
            pass
        try:
            len(listadelojas) == 3
            self.bfranquia3 =tk.Button(self.mainwindow, text = listadelojas[2], font= ("verdana", 10), bg = "peru", fg = "black", height= 2, width = 40, command = self.Franquia3)
            self.bfranquia3.place(x = 950, y = 400)
        except IndexError:
            pass
        
        try:
            len(listadelojas) == 4
            self.bfranquia4 =tk.Button(self.mainwindow, text = listadelojas[3], font= ("verdana", 10), bg = "peru", fg = "black", height= 2, width = 40, command = self.Franquia4)
            self.bfranquia4.place(x = 950, y = 450)
        except IndexError:
            pass
        try:
            len(listadelojas) == 5
            self.bfranquia5 =tk.Button(self.mainwindow, text = listadelojas[4], font= ("verdana", 10), bg = "peru", fg = "black", height= 2, width = 40, command = self.Franquia5)
            self.bfranquia5.place(x = 950, y = 500)
            
        except IndexError:
            pass 
           
            
            
        
    def voicebutton2(self):
        self.speak = wincl.Dispatch("SAPI.SpVoice")
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()


        with self.mic as source:
            self.audio = self.r.listen(source, phrase_time_limit = 1)
            print(self.r.recognize_google(self.audio, language = "pt-BR"))
    
            
            
        if self.r.recognize_google(self.audio, language = "pt-BR") == "franquia 1" or "franquia on":
            try:
                self.Franquia1()
                self.speak.Speak("Iniciando franquia 1")
                
                
            except:
                pass
            return
        
        
            
        
        self.speak.Speak("Desculpe, não entendi. Por favor, tente novamente!")
        
    def Franquia1(self):
        self.franquiaselecionada = firebase.get("Franquia1", None)
        self.selecionada = "Franquia1"
        self.imagems.destroy()
        self.texto.destroy()
        self.lojas.destroy()
        
        try:
            self.bfranquia1.destroy()
            self.bfranquia2.destroy()
            self.bfranquia3.destroy()
            self.bfranquia4.destroy()
            self.bfranquia5.destroy()
        except AttributeError:
            pass
        
        self.salao = tk.Button(self.mainwindow, bg = "peru", fg= "black" ,text="Salão", font= ("verdana", 10), command = self.selecionarsalao, height= 2, width = 40)
        self.salao.pack(side="left", anchor= "n", fill="x", expand= True)
        self.cozinha = tk.Button(self.mainwindow, bg = "peru", fg= "black", text="Cozinha", font= ("verdana", 10), command = self.selecionarcozinha, height= 2, width = 40)
        self.cozinha.pack(side="left", anchor= "n", fill="x", expand= True)
        
        self.adm = tk.Button(self.mainwindow, bg = "peru", fg= "black", text="Setor Administrativo",font= ("verdana", 10), command = self.selecionaradm, height= 2, width = 40)
        self.adm.pack(side="left", anchor= "n", fill="x", expand= True)
        
        self.selecionarsalao()
        
    
    
    
        
        
        
    def Franquia2(self):
        self.franquiaselecionada = firebase.get("Franquia2", None)
        self.selecionada = "Franquia2"
        self.imagems.destroy()
        self.texto.destroy()
        self.lojas.destroy()
        
        try:
            self.bfranquia1.destroy()
            self.bfranquia2.destroy()
            self.bfranquia3.destroy()
            self.bfranquia4.destroy()
            self.bfranquia5.destroy()
        except AttributeError:
            pass
        
        self.salao = tk.Button(self.mainwindow, bg = "peru", fg= "black" ,text="Salão", font= ("verdana", 10), command = self.selecionarsalao, height= 2, width = 40)
        self.salao.pack(side="left", anchor= "n", fill="x", expand= True)
        self.cozinha = tk.Button(self.mainwindow, bg = "peru", fg= "black", text="Cozinha", font= ("verdana", 10), command = self.selecionarcozinha, height= 2, width = 40)
        self.cozinha.pack(side="left", anchor= "n", fill="x", expand= True)
        
        self.adm = tk.Button(self.mainwindow, bg = "peru", fg= "black", text="Setor Administrativo",font= ("verdana", 10), command = self.selecionaradm, height= 2, width = 40)
        self.adm.pack(side="left", anchor= "n", fill="x", expand= True)
        
        self.selecionarsalao()
        
    def Franquia3(self):
        self.franquiaselecionada = firebase.get("Franquia3", None)
        self.selecionada = "Franquia3"
        self.bfranquia3.configure(bg = "blue")
        
    def Franquia4(self):
        self.franquiaselecionada = firebase.get("Franquia4", None)
        self.selecionada = "Franquia4"
        self.bfranquia5.configure(bg = "blue")
        
    def Franquia5(self):
        self.franquiaselecionada = firebase.get("Franquia5", None)
        self.selecionada = "Franquia5"
        self.bfranquia5.configure(bg = "blue")
    
    def configuracoesf(self):
        self.iniciar.destroy()
        self.configuracoes.destroy()
        self.voicecommand1.destroy()
        self.sair.destroy()
        self.editarnome = tk.Button(self.mainwindow, text = "Editar nome da franquia", font = ("verdana", 10), bg = "peru", height= 2, width = 40, command = self.editarnomefranquia)
        self.editarendereco = tk.Button(self.mainwindow, text = "Editar endereço da franquia", font = ("verdana", 10), bg = "peru", height= 2, width = 40, command = self.editarenderecofranquia)
        self.voltarconfig = tk.Button(self.mainwindow, text = "Voltar", font = ("verdana", 10), bg = "peru", height= 2, width = 40, command = self.voltarconfigfranquias)
        self.editarnome.place(x = 900, y = 350)
        self.editarendereco.place(x = 900 , y = 400)
        self.voltarconfig.place(x = 900, y = 450)
        
    def voltarconfigfranquias(self):
        self.editarnome.destroy()
        self.editarendereco.destroy()
        self.voltarconfig.destroy()
        self.abrir()
        
        
        
    def editarnomefranquia(self):
        self.janelaeditarnome = tk.Toplevel()
        self.janelaeditarnome.wm_title("Editar Nome da franquia")
        self.janelaeditarnome.geometry("400x300")
        self.janelaeditarnome.configure(bg = "sandy brown")
        self.nomeeditar = tk.Label(self.janelaeditarnome, text = "Franquia:", bg = "sandy brown", font = ("verdana", 10))
        self.nomeeditarcombo = ttk.Combobox(self.janelaeditarnome, values = listadelojas)
        self.nomenovofranquia = tk.Label(self.janelaeditarnome, text = "Novo Nome:", bg = "sandy brown", font = ("verdana", 10))
        self.nomenovofranquiaentry = tk.Entry(self.janelaeditarnome, bg = "peru")
        self.nomeeditar.place(x = 50, y= 40)
        self.nomeeditarcombo.place(x = 190, y = 40)
        self.nomenovofranquia.place(x = 50, y = 80)
        self.nomenovofranquiaentry.place(x = 190, y = 80)
        self.botaoselecionarenome = tk.Button(self.janelaeditarnome, bg = "peru", fg = "black", text = "Selecionar", command = self.nomefranquiaselecionada, height= 2, width = 40)
        self.botaoselecionarenome.place(x = 55, y = 225)
        
    def nomefranquiaselecionada(self):
        self.listacombo = list()
        for i in listadelojas:
            self.listacombo.append(i)
        self.logins[self.nomenovofranquiaentry.get()] = self.logins.pop(self.listacombo[self.nomeeditarcombo.current()])
        self.janelaeditarnome.destroy()
#        firebase.delete("", self.listacombo[self.nomeeditarcombo.current()])
        firebase.patch(dados, self.logins)
    def editarenderecofranquia(self):
        pass        
    def selecionarloja(self):
        self.salao = tk.Button(self.mainwindow, bg = "white", fg= "black" ,text="Salão", command = self.selecionarsalao)
        self.salao.pack(side="left", anchor= "n", fill="x", expand= True)
        self.cozinha = tk.Button(self.mainwindow, bg = "white", fg= "black", text="Cozinha", command = self.selecionarcozinha)
        self.cozinha.pack(side="left", anchor= "n", fill="x", expand= True)
        
        self.adm = tk.Button(self.mainwindow, bg = "white", fg= "black", text="Setor Administrativo", command = self.selecionaradm)
        self.adm.pack(side="left", anchor= "n", fill="x", expand= True)
        
    def comeco(self):
        self.mainwindow.attributes("-fullscreen", True)
        self.mainwindow.bind("<Escape>", lambda e: self.mainwindow.destroy())
        self.mainwindow.mainloop()
       
        
    def bloquear(self):
        pass
        
        
    def selecionaradm(self):
        try:
            self.InventoryTitle.destroy()
            self.Inventory.destroy()
            self.InventoryEdit.destroy()
            self.InventoryAdd.destroy()
            self.Reposition.destroy()
            self.OrdersTitle.destroy()
            self.OrdersTable.destroy()
            self.PlaceOrder.destroy()
            self.EditOrder.destroy()
            self.RemoveOrder.destroy()
        except:
            pass
        try: 
            self.voicecommand3.destroy()
            
        except:
            pass
        try:
            self.adm.configure(command = self.bloquear)
            self.cozinha.configure(command = self.selecionarcozinha)
            self.salao.configure(command = self.selecionarsalao)
        except:
            pass
        
        try:
            self.cozinha.configure(bg = "peru", fg = "black")
        except:
            pass
    
        try:
            self.salao.configure(bg = "peru", fg = "black")
        except:
            pass
        try:
            self.adm.configure(bg = "black", fg = "white")
            
            self.verde1f.destroy()
            self.verde2f.destroy()
            self.verde3f.destroy()
            self.verde4f.destroy()
            self.verde5f.destroy()
            self.verde6f.destroy()
            self.verde7f.destroy()
            self.verde8f.destroy()
            self.verde9f.destroy()
            self.verde10f.destroy()
            self.verde11f.destroy()
            self.verde12f.destroy()
            self.verde13f.destroy()
            self.verde14f.destroy()
            self.verde15f.destroy()
            self.verde16f.destroy()
            self.verde17f.destroy()
            self.verde18f.destroy()
            self.verde19f.destroy()
            self.verde20f.destroy()
            self.verde21f.destroy()
            self.verde22f.destroy()
            self.verde23f.destroy()
            self.verde24f.destroy()
            self.verde25f.destroy()
            self.verde26f.destroy()
            self.verde27f.destroy()
            self.verde28f.destroy()
            self.verde29f.destroy()
            self.verde30f.destroy()
            self.vermelho1f.destroy()
            self.vermelho2f.destroy()
            self.vermelho3f.destroy()
            self.vermelho4f.destroy()
            self.vermelho5f.destroy()
            self.vermelho6f.destroy()
            self.vermelho7f.destroy()
            self.vermelho8f.destroy()
            self.vermelho9f.destroy()
            self.vermelho10f.destroy()
            self.vermelho11f.destroy()
            self.vermelho12f.destroy()
            self.vermelho13f.destroy()
            self.vermelho14f.destroy()
            self.vermelho15f.destroy()
            self.vermelho16f.destroy()
            self.vermelho17f.destroy()
            self.vermelho18f.destroy()
            self.vermelho19f.destroy()
            self.vermelho20f.destroy()
            self.vermelho21f.destroy()
            self.vermelho22f.destroy()
            self.vermelho23f.destroy()
            self.vermelho24f.destroy()
            self.vermelho25f.destroy()
            self.vermelho26f.destroy()
            self.vermelho27f.destroy()
            self.vermelho28f.destroy()
            self.vermelho29f.destroy()
            self.vermelho30f.destroy()
            self.reservas.destroy()
            self.tablereservas.destroy()
            self.badicionarreserva.destroy()
            self.beditareserva.destroy()
            self.bremoverreserva.destroy()  
            self.imagemslogosalao.destroy()
           

            
            
            
            
            
           
            
        except AttributeError:
            pass
        
        self.voicecommand4 = tk.Button(self.mainwindow, bg = "cyan" , image = self.imagemmic1, command = self.voicebutton4, height= 50, width = 50)
        self.voicecommand4.image = self.imagemmic1
        self.voicecommand4.place(x = 1465, y = 795)
        
        self.adm.configure(bg="black", fg = "white")
        
        self.fundofinancas = tk.Canvas(self.mainwindow, width = 450, height = 200, bg = "peru")
        self.fundofinancas.place(x = 20, y = 90)
        self.metas = tk.Label(self.mainwindow, text= "Metas: ", font = ("Verdana", 20), bg = "sandy brown")
        self.promocoes = tk.Label(self.mainwindow, text = "Promoções: ", font= ("Verdana", 20), bg = "sandy brown")
        self.gerenciamento = tk.Label(self.mainwindow, text = "Gerenciamento: ", font = ("Verdana", 20), bg = "sandy brown")
        self.financas = tk.Label(self.mainwindow, text = "Finanças: ", font = ("Verdana", 20), bg= "sandy brown")
        self.tpedidos = tk.Label(self.mainwindow, text = "Total de Pedidos: " + str(variavelnumeropedidos), font = ("Verdana", 11), bg= "peru")
        self.totalmesas = tk.Label(self.mainwindow, text = "Total de mesas atendidas: " + str(variavelnumeromesas), font = ("Verdana", 11), bg= "peru")
        self.tfuncionarios = tk.Label(self.mainwindow, text = "Total de funcionários trabalhando: " + str(variavelnumerofuncionarios), font = ("Verdana", 11), bg= "peru")
        self.tbruta = tk.Label(self.mainwindow, text = "Receita bruta: " + str(variavelreceitabruta), font = ("Verdana", 11), bg= "peru")
        self.tdespesas = tk.Label(self.mainwindow, text = "Despesas: " + str(variaveldespesas), font = ("Verdana", 11), bg= "peru")
        self.tfaturamento = tk.Label(self.mainwindow, text = "Faturamento: " + str(variavelfaturamento), font = ("Verdana", 11), bg= "peru")
        self.treservas = tk.Label(self.mainwindow, text = "Total de reservas: " + str(variavelreservas), font = ("Verdana", 11), bg= "peru")
        self.tpedidos.place(x = 30, y = 100)
        self.totalmesas.place(x = 30, y = 120)
        self.tfuncionarios.place(x = 30, y = 140)
        self.tbruta.place(x = 30, y = 160)
        self.tdespesas.place(x = 30, y = 180)
        self.tfaturamento.place(x = 30, y = 200)
        self.treservas.place(x=30, y = 220)
        
        self.gerenciamento.place(x = 140, y = 310)
        self.financas.place(x = 175, y = 50)
        self.promocoes.place(x =1000, y = 50)
        self.metas.place(x = 700, y = 480)
        
        self.tablepromocoes = ttk.Treeview(self.mainwindow, columns=("inicio", "fim", "descricao"))
        self.tablepromocoes.configure(height = 0)
        
        self.tablepromocoes.heading("#0", text = "Nome")
        self.tablepromocoes.heading("#1", text = "Data de início")
        self.tablepromocoes.heading("#2", text = "Data de finalização")
        self.tablepromocoes.heading("#3", text = "Descrição")
        self.tablepromocoes.column("#0", anchor = "center", width = 120)
        self.tablepromocoes.column("#1", anchor = "center", width = 90)
        self.tablepromocoes.column("#2", anchor = "center", width = 110)
        self.tablepromocoes.column("#3", anchor = "center", width = 500)
                                   
                                    
        self.tablepromocoes.place(x = 690, y = 90)
        self.badicionarpromocao = tk.Button(self.mainwindow, bg = "peru", fg = "black", text = "Adicionar promoção", command = self.adicionarpromocao, height = 2, width = 25,  font= ("verdana", 10))
        self.bremoverpromocao = tk.Button(self.mainwindow, bg = "peru", fg = "black", text = "Encerrar promoção", command = self.removerpromocao, height = 2, width = 25,  font= ("verdana", 10))
        self.beditarpromocao = tk.Button(self.mainwindow, bg = "peru", fg = "black", text = "Editar promoção", command = self.editarpromocao, height = 2, width = 25,  font= ("verdana", 10))
        self.badicionarpromocao.place(x = 690, y = 420)
        self.beditarpromocao.place(x = 990, y = 420)
        self.bremoverpromocao.place(x = 1290, y = 420)
        
        
        self.bfuncionarios = tk.Button(self.mainwindow, bg = "peru", fg = "black", text = "Funcionários", command = self.selecionarfuncionarios, height = 2, width = 25,  font= ("verdana", 10))
        self.bdespesas = tk.Button(self.mainwindow, bg = "peru", fg = "black", text = "Despesas", command = self.selecionardespesas, height = 2, width = 25,  font= ("verdana", 10))
        self.blicensas = tk.Button(self.mainwindow, bg = "peru", fg = "black", text = "Licenças", command = self.selecionarlicencas, height = 2, width = 25,  font= ("verdana", 10))
        self.blogins = tk.Button(self.mainwindow, bg = "peru", fg = "black", text = "Logins", command = self.selecionarlogins, height = 2, width = 25,  font= ("verdana", 10))
        self.bdespesas.place(x = 30, y = 360)
        self.bfuncionarios.place(x = 30, y = 420)
        self.blicensas.place(x = 270, y = 360)
        self.blogins.place(x = 270, y = 420)
        
        self.canvasmetas = tk.Canvas(self.mainwindow, highlightbackground="white",highlightcolor="white", width = 1325, height = 300, bg = "aquamarine")
        self.canvasmetas.place(x = 90, y = 535)
        self.cormeta = "bisque2"
        self.baddmetas = tk.Button(self.mainwindow, bg = self.cormeta, fg = "black", text = "Adicionar meta", command = self.addmeta, height = 2, width = 25,  font= ("verdana", 10))
        self.beditarmetas = tk.Button(self.mainwindow, bg = self.cormeta, fg = "black", text = "Editar meta", command = self.editarmeta, height = 2, width = 25,  font= ("verdana", 10))
        self.bremovermetas = tk.Button(self.mainwindow, bg = self.cormeta, fg = "black", text = "Remover meta", command = self.removermeta, height = 2, width = 25,  font= ("verdana", 10))
        
        self.tablemetas = ttk.Treeview(self.mainwindow, columns=("inicio", "fim",  "descricao"))
        self.tablemetas.configure(height = 0)
        
        self.tablemetas.heading("#0", text = "Meta")
        self.tablemetas.heading("#1", text = "Data de início")
        self.tablemetas.heading("#2", text = "Expiração")
        self.tablemetas.heading("#3", text = "Descrição")
        self.tablemetas.column("#0", anchor = "center", width = 300)
        self.tablemetas.column("#1", anchor = "center", width = 90)
        self.tablemetas.column("#2", anchor = "center", width = 110)
        self.tablemetas.column("#3", anchor = "center", width = 500)
        self.baddmetas.place(x =1180 , y = 590)
        self.beditarmetas.place(x =1180 , y = 650)
        self.bremovermetas.place(x =1180 , y = 710)
        self.tablemetas.place(x = 120, y = 560)
        try:
            self.tablepromocoes.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Promocoes"]:
                self.tablepromocoes.insert("", 1, "" , text = i, values = (self.franquiaselecionada["Promocoes"][i]["inicio"], self.franquiaselecionada["Promocoes"][i]["expiracao"], self.franquiaselecionada["Promocoes"][i]["desc"]), tags = ("Cor"))
                self.tablepromocoes.configure(height = len(self.tablepromocoes.get_children()))
        except:
            pass
        
        try:
            self.tablemetas.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Metas"]:
                self.tablemetas.insert("", 1, "" , text = i, values = (self.franquiaselecionada["Metas"][i]["inicio"], self.franquiaselecionada["Metas"][i]["expiracao"], self.franquiaselecionada["Metas"][i]["desc"]), tags = ("Cor"))
                self.tablemetas.configure(height = len(self.tablemetas.get_children()))
        except:
            pass
        
            
        
    def addmeta(self):
        self.janelaaddmeta = tk.Toplevel()
        self.janelaaddmeta.wm_title("Adicionar meta")
        self.janelaaddmeta.geometry("400x300")
        self.janelaaddmeta.configure(bg = "sandy brown")
        self.nomemeta = tk.Label(self.janelaaddmeta, text = "Meta: ", bg = "sandy brown", font = ("verdana", 10))
        self.iniciometa = tk.Label(self.janelaaddmeta, text = "Data de início: ", bg = "sandy brown", font = ("verdana", 10))
        self.finalmeta = tk.Label(self.janelaaddmeta, text = "Data de expiração: ", bg = "sandy brown", font = ("verdana", 9))
        self.descmeta = tk.Label(self.janelaaddmeta, text = "Descrição: ", bg = "sandy brown", font = ("verdana", 10))
        self.finalmetaentry = tk.Entry(self.janelaaddmeta, bg = "peru")
        self.descmetaentry = tk.Entry(self.janelaaddmeta, bg = "peru")
        self.nomemetaentry = tk.Entry(self.janelaaddmeta, bg = "peru")
        self.iniciometaentry = tk.Entry(self.janelaaddmeta, bg = "peru")
        self.nomemeta.place(x = 50, y= 40)
        self.nomemetaentry.place(x = 190, y = 40)
        self.iniciometa.place(x = 50, y= 80)
        self.iniciometaentry.place(x = 190, y = 80)
        self.finalmeta.place(x = 50, y = 120)
        self.finalmetaentry.place(x = 190, y = 120)
        self.descmeta.place(x = 50, y = 160)
        self.descmetaentry.place(x = 190, y = 160)
        self.botaoadicionarmeta = tk.Button(self.janelaaddmeta, bg = "peru", fg = "black", text = "Adicionar meta", command = self.inserirmeta, height= 2, width = 40)
        self.botaoadicionarmeta.place(x = 55, y = 225)
        
    def inserirmeta(self):
        self.tablemetas.insert("", 1, "" , text = self.nomemetaentry.get(), values = (self.iniciometaentry.get(), self.finalmetaentry.get(), self.descmetaentry.get()), tags = ("Cor"))
        self.tablemetas.tag_configure("Cor", background = "bisque2")
        self.tablemetas.configure(height = len(self.tablemetas.get_children()))
        self.franquiaselecionada["Metas"][self.nomemetaentry.get()]= {"inicio": self.iniciometaentry.get(), "expiracao": self.finalmetaentry.get(), "desc": self.descmetaentry.get()}
        firebase.patch(self.selecionada, self.franquiaselecionada)
        self.janelaaddmeta.destroy()
    def editarmeta(self):
        self.janelaeditarmeta = tk.Toplevel()
        self.janelaeditarmeta.wm_title("Editar meta")
        self.janelaeditarmeta.geometry("400x300")
        self.janelaeditarmeta.configure(bg = "sandy brown")
        self.nomemetae = tk.Label(self.janelaeditarmeta, text = "Nome: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomemetaeentry = tk.Entry(self.janelaeditarmeta, bg = "peru")
        self.nomemetae.place(x = 50, y = 40)
        self.nomemetaeentry.place(x = 190, y = 40)
        self.bselecionaremeta = tk.Button(self.janelaeditarmeta, bg = "peru", fg = "black", font = ("verdana", 10), text = "Selecionar meta", command = self.editarmetaselecionada, height= 2, width = 20)
        self.bselecionaremeta.place(x = 110, y = 100)
        
    def editarmetaselecionada(self):
        self.nomemetae.destroy()
        self.bselecionaremeta.destroy()
        self.nomemetaee = tk.Label(self.janelaeditarmeta, text = "Meta: ", bg = "sandy brown", font = ("verdana",10))
        self.nomemetaeeentry = tk.Entry(self.janelaeditarmeta, bg = "peru")
        self.datametaee = tk.Label(self.janelaeditarmeta, text = "Data de início: ", bg = "sandy brown", font = ("verdana", 10))
        self.datametaeeentry = tk.Entry(self.janelaeditarmeta, bg = "peru")
        self.finalmetaee = tk.Label(self.janelaeditarmeta, text = "Data de expiração: ", bg = "sandy brown", font = ("verdana", 10))
        self.finalmetaeeentry = tk.Entry(self.janelaeditarmeta, bg = "peru")
        self.descricaometaee = tk.Label(self.janelaeditarmeta, text = "Descrição: ", bg = "sandy brown", font = ("verdana", 10))
        self.descricaometaeeentry = tk.Entry(self.janelaeditarmeta, bg = "peru")
        self.nomemetaee.place(x = 50, y = 40)
        self.nomemetaeeentry.place(x = 190, y = 40)
        self.datametaee.place(x = 50, y = 70)
        self.datametaeeentry.place(x = 190, y = 70)
        self.finalmetaee.place(x = 50, y = 100)
        self.finalmetaeeentry.place(x = 190, y = 100)
        self.descricaometaee.place(x = 50, y = 130)
        self.descricaometaeeentry.place(x = 190, y = 130)
        
        self.nomemetaeeentry.insert(0, self.nomemetaeentry.get())
        self.nomemetaeeentry.configure(state = "disabled")
        self.datametaeeentry.insert(0, self.franquiaselecionada["Metas"][self.nomemetaeeentry.get()]["inicio"])
        self.finalmetaeeentry.insert(0, self.franquiaselecionada["Metas"][self.nomemetaeeentry.get()]["expiracao"])
        self.descricaometaeeentry.insert(0, self.franquiaselecionada["Metas"][self.nomemetaeeentry.get()]["desc"])
        self.binserirmetaeditada = tk.Button(self.janelaeditarmeta, bg = "peru", fg = "black", font = ("verdana", 10), text = "Editar", command = self.editarmetaselecionadainserida, height= 2, width = 20)
        self.bcancelarinserirmetaeditada = tk.Button(self.janelaeditarmeta, bg = "peru", fg = "black", font = ("verdana", 10), text = "Cancelar", command = self.cancelareditarmetaselecionada, height= 2, width = 20)
        self.bcancelarinserirmetaeditada.place(x=10, y= 250 )
        self.binserirmetaeditada.place(x =220, y = 250)

    def editarmetaselecionadainserida(self):
        self.franquiaselecionada["Metas"][self.nomemetaeeentry.get()] = {"inicio": self.datametaeeentry.get(), "expiracao": self.finalmetaeeentry.get(), "desc": self.descricaometaeeentry.get()}
        firebase.patch(self.selecionada, self.franquiaselecionada)  
        self.tablemetas.delete(*self.tablemetas.get_children())
        try:
            self.tablemetas.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Metas"]:
                self.tablemetas.insert("", 1, "" , text = i, values = (self.franquiaselecionada["Metas"][i]["inicio"], self.franquiaselecionada["Metas"][i]["expiracao"], self.franquiaselecionada["Metas"][i]["desc"]), tags = ("Cor"))
                self.tablemetas.configure(height = len(self.tablemetas.get_children()))
        except:
            pass
        
        self.janelaeditarmeta.destroy()
    
    def cancelareditarmetaselecionada(self):
        self.janelaeditarmeta.destroy()
        
    def removermeta(self):
        self.janelarmetas = tk.Toplevel()
        self.janelarmetas.wm_title("Remover meta")
        self.janelarmetas.geometry("400x300")
        self.janelarmetas.configure(bg = "sandy brown")
        self.nomermeta = tk.Label(self.janelarmetas, text = "Meta: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomermetaentry = tk.Entry(self.janelarmetas, bg = "peru")
        self.nomermeta.place(x = 50, y = 40)
        self.nomermetaentry.place(x = 190, y = 40)
        self.botaoremovermeta = tk.Button(self.janelarmetas, bg = "peru", fg = "black", text = "Remover meta", command = self.removermetatabela, height= 2, width = 40)
        self.botaoremovermeta.place(x = 55, y = 225)
        
    def removermetatabela(self):
        del self.franquiaselecionada["Metas"][self.nomermetaentry.get()]
        firebase.patch(self.selecionada, self.franquiaselecionada)
        self.janelarmetas.destroy()
        self.tablemetas.delete(*self.tablemetas.get_children())
        try:
            self.tablemetas.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Metas"]:
                self.tablemetas.insert("", 1, "" , text = i, values = (self.franquiaselecionada["Metas"][i]["inicio"], self.franquiaselecionada["Metas"][i]["expiracao"], self.franquiaselecionada["Metas"][i]["desc"]), tags = ("Cor"))
                self.tablemetas.configure(height = len(self.tablemetas.get_children()))
        except:
            pass
        
    def voicebutton4(self):
        self.speak = wincl.Dispatch("SAPI.SpVoice")
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()


        with self.mic as source:
            self.audio = self.r.listen(source, phrase_time_limit = 2)
            print(self.r.recognize_google(self.audio, language = "pt-BR"))
    
            
            
        if self.r.recognize_google(self.audio, language = "pt-BR") == "despesas":
            try:
                self.bdespesas()
                
                
            except:
                pass
            return
            
            
        if self.r.recognize_google(self.audio, language = "pt-BR") == "funcionários":
            try:
                self.bfuncionarios()
                
                
            except:
                pass
            return
        if self.r.recognize_google(self.audio, language = "pt-BR") == "licenças":
            try:
                self.blicensas()
                
                
            except:
                pass
            return
        if self.r.recognize_google(self.audio, language = "pt-BR") == "adicionar promoção":
            try:
                self.adicionarpromocao()
                
                
            except:
                pass
            return
        if self.r.recognize_google(self.audio, language = "pt-BR") == "editar promoção":
            try:
                self.editarpromocao()
                
                
            except:
                pass
            return
        if self.r.recognize_google(self.audio, language = "pt-BR") == "encerrar promoção":
            try:
                self.removerpromocao()
                
                
            except:
                pass
            return
        if self.r.recognize_google(self.audio, language = "pt-BR") == "adicionar meta":
            try:
                self.addmeta()
                
                
            except:
                pass
            return
        if self.r.recognize_google(self.audio, language = "pt-BR") == "editar meta":
            try:
                self.editarmeta()
                
                
            except:
                pass
            return
        if self.r.recognize_google(self.audio, language = "pt-BR") == "remover meta":
            try:
                self.removermeta()
                
                
            except:
                pass
            return
        self.speak.Speak("Desculpe, não entendi. Por favor, tente novamente!")
    def adicionarpromocao(self):
        self.janelapromocao = tk.Toplevel()
        self.janelapromocao.wm_title("Adicionar Promoção")
        self.janelapromocao.geometry("400x300")
        self.janelapromocao.configure(bg = "sandy brown")
        self.nomepromocao = tk.Label(self.janelapromocao, text = "Nome: ", bg = "sandy brown", font = ("verdana", 10))
        self.iniciopromocao = tk.Label(self.janelapromocao, text = "Data de início: ", bg = "sandy brown", font = ("verdana", 10))
        self.finalpromocao = tk.Label(self.janelapromocao, text = "Data de término: ", bg = "sandy brown", font = ("verdana", 9))
        self.descpromocao = tk.Label(self.janelapromocao, text = "Descrição: ", bg = "sandy brown", font = ("verdana", 10))
        self.finalpromocaoentry = tk.Entry(self.janelapromocao, bg = "peru")
        self.descpromocaoentry = tk.Entry(self.janelapromocao, bg = "peru")
        self.nomepromocaoentry = tk.Entry(self.janelapromocao, bg = "peru")
        self.iniciopromocaoentry = tk.Entry(self.janelapromocao, bg = "peru")
        self.nomepromocao.place(x = 50, y= 40)
        self.nomepromocaoentry.place(x = 190, y = 40)
        self.iniciopromocao.place(x = 50, y= 80)
        self.iniciopromocaoentry.place(x = 190, y = 80)
        self.finalpromocao.place(x = 50, y = 120)
        self.finalpromocaoentry.place(x = 190, y = 120)
        self.descpromocao.place(x = 50, y = 160)
        self.descpromocaoentry.place(x = 190, y = 160)
        self.botaoadicionarpromocao = tk.Button(self.janelapromocao, bg = "peru", fg = "black", text = "Adicionar promoção", command = self.inserirpromocao, height= 2, width = 40)
        self.botaoadicionarpromocao.place(x = 55, y = 225)
        

    def inserirpromocao(self):
        self.tablepromocoes.insert("", 1, "" , text = self.nomepromocaoentry.get(), values = (self.iniciopromocaoentry.get(), self.finalpromocaoentry.get(), self.descpromocaoentry.get()), tags = ("Cor"))
        self.tablepromocoes.tag_configure("Cor", background = "bisque2")
        self.tablepromocoes.configure(height = len(self.tablepromocoes.get_children()))
        self.franquiaselecionada["Promocoes"][self.nomepromocaoentry.get()]= {"inicio": self.iniciopromocaoentry.get(), "expiracao": self.finalpromocaoentry.get(), "desc": self.descpromocaoentry.get()}
        firebase.patch(self.selecionada, self.franquiaselecionada)
        self.janelapromocao.destroy()
        
    def editarpromocao(self):
        self.janelaeditarpromocao = tk.Toplevel()
        self.janelaeditarpromocao.wm_title("Editar Promoção")
        self.janelaeditarpromocao.geometry("400x300")
        self.janelaeditarpromocao.configure(bg = "sandy brown")
        self.nomepromocaoe = tk.Label(self.janelaeditarpromocao, text = "Nome: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomepromocaoeentry = tk.Entry(self.janelaeditarpromocao, bg = "peru")
        self.nomepromocaoe.place(x = 50, y = 40)
        self.nomepromocaoeentry.place(x = 190, y = 40)
        self.bselecionarepromocao = tk.Button(self.janelaeditarpromocao, bg = "peru", fg = "black", font = ("verdana", 10), text = "Selecionar promoção", command = self.editarpromocaoselecionada, height= 2, width = 20)
        self.bselecionarepromocao.place(x = 110, y = 100)
    
    def editarpromocaoselecionada(self):
        self.nomepromocaoe.destroy()
        self.bselecionarepromocao.destroy()
        self.nomepromocaoee = tk.Label(self.janelaeditarpromocao, text = "Nome: ", bg = "sandy brown", font = ("verdana",10))
        self.nomepromocaoeeentry = tk.Entry(self.janelaeditarpromocao, bg = "peru")
        self.datapromocaoee = tk.Label(self.janelaeditarpromocao, text = "Data de início: ", bg = "sandy brown", font = ("verdana", 10))
        self.datapromocaoeeentry = tk.Entry(self.janelaeditarpromocao, bg = "peru")
        self.finalpromocaoee = tk.Label(self.janelaeditarpromocao, text = "Data de término: ", bg = "sandy brown", font = ("verdana", 10))
        self.finalpromocaoeeentry = tk.Entry(self.janelaeditarpromocao, bg = "peru")
        self.descricaopromocaoee = tk.Label(self.janelaeditarpromocao, text = "Descrição: ", bg = "sandy brown", font = ("verdana", 10))
        self.descricaopromocaoeeentry = tk.Entry(self.janelaeditarpromocao, bg = "peru")
        self.nomepromocaoee.place(x = 50, y = 40)
        self.nomepromocaoeeentry.place(x = 190, y = 40)
        self.datapromocaoee.place(x = 50, y = 70)
        self.datapromocaoeeentry.place(x = 190, y = 70)
        self.finalpromocaoee.place(x = 50, y = 100)
        self.finalpromocaoeeentry.place(x = 190, y = 100)
        self.descricaopromocaoee.place(x = 50, y = 130)
        self.descricaopromocaoeeentry.place(x = 190, y = 130)
        
        self.nomepromocaoeeentry.insert(0, self.nomepromocaoeentry.get())
        self.nomepromocaoeeentry.configure(state = "disabled")
        self.datapromocaoeeentry.insert(0, self.franquiaselecionada["Promocoes"][self.nomepromocaoeeentry.get()]["inicio"])
        self.finalpromocaoeeentry.insert(0, self.franquiaselecionada["Promocoes"][self.nomepromocaoeeentry.get()]["expiracao"])
        self.descricaopromocaoeeentry.insert(0, self.franquiaselecionada["Promocoes"][self.nomepromocaoeeentry.get()]["desc"])
        self.binserirpromocaoeditada = tk.Button(self.janelaeditarpromocao, bg = "peru", fg = "black", font = ("verdana", 10), text = "Editar", command = self.editarpromocaoselecionadainserida, height= 2, width = 20)
        self.bcancelarinserirpromocaoeditada = tk.Button(self.janelaeditarpromocao, bg = "peru", fg = "black", font = ("verdana", 10), text = "Cancelar", command = self.cancelareditarpromocaoselecionada, height= 2, width = 20)
        self.bcancelarinserirpromocaoeditada.place(x=10, y= 250 )
        self.binserirpromocaoeditada.place(x =220, y = 250)
        
    def editarpromocaoselecionadainserida(self):
        self.franquiaselecionada["Promocoes"][self.nomepromocaoeeentry.get()] = {"inicio": self.datapromocaoeeentry.get(), "expiracao": self.finalpromocaoeeentry.get(), "desc": self.descricaopromocaoeeentry.get()}
        firebase.patch(self.selecionada, self.franquiaselecionada)  
        self.tablepromocoes.delete(*self.tablepromocoes.get_children())
        try:
            self.tablepromocoes.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Promocoes"]:
                self.tablepromocoes.insert("", 1, "" , text = i, values = (self.franquiaselecionada["Promocoes"][i]["inicio"], self.franquiaselecionada["Promocoes"][i]["expiracao"], self.franquiaselecionada["Promocoes"][i]["desc"]), tags = ("Cor"))
                self.tablepromocoes.configure(height = len(self.tablepromocoes.get_children()))
        except:
            pass
        
        self.janelaeditarpromocao.destroy()
        
    def cancelareditarpromocaoselecionada(self):
        self.janelaeditarpromocao.destroy()
    def removerpromocao(self):
        self.janelarpromocoes = tk.Toplevel()
        self.janelarpromocoes.wm_title("Remover promoção")
        self.janelarpromocoes.geometry("400x300")
        self.janelarpromocoes.configure(bg = "sandy brown")
        self.nomepromocoesr = tk.Label(self.janelarpromocoes, text = "Nome: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomepromocoesentryr = tk.Entry(self.janelarpromocoes, bg = "peru")
        self.nomepromocoesr.place(x = 50, y = 40)
        self.nomepromocoesentryr.place(x = 190, y = 40)
        self.bremoverpromocaoj = tk.Button(self.janelarpromocoes, bg = "peru", fg = "black", text = "Encerrar promoção", command = self.removerpromocaotabela, height= 2, width = 40)
        self.bremoverpromocaoj.place(x = 55, y = 225)
    
    def removerpromocaotabela(self):
        del self.franquiaselecionada["Promocoes"][self.nomepromocoesentryr.get()]
        firebase.patch(self.selecionada, self.franquiaselecionada)
        self.janelarpromocoes.destroy()
        self.tablepromocoes.delete(*self.tablepromocoes.get_children())
        try:
            self.tablepromocoes.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Promocoes"]:
                self.tablepromocoes.insert("", 1, "" , text = i, values = (self.franquiaselecionada["Promocoes"][i]["inicio"], self.franquiaselecionada["Promocoes"][i]["expiracao"], self.franquiaselecionada["Promocoes"][i]["desc"]), tags = ("Cor"))
                self.tablepromocoes.configure(height = len(self.tablepromocoes.get_children()))
        except:
            pass
        
    def selecionarlogins(self):
        self.janelalogins = tk.Toplevel()
        self.janelalogins.wm_title("Logins")
        self.janelalogins.geometry("800x600")
        self.janelalogins.configure(bg = "sandy brown")
        self.titulologins = tk.Label(self.janelalogins, text = "Lista de logins: ", font = ("Verdana", 20), bg = "sandy brown")
        self.titulologins.place(x = 20, y = 20)
        self.tablelogins = ttk.Treeview(self.janelalogins, columns=("senha", "data"))
        self.tablelogins.configure(height = 0)
        
        
        self.tablelogins.heading("#0", text = "Usuário")
        self.tablelogins.heading("#1", text = "Senha")
        self.tablelogins.heading("#2", text = "Data de criação")
        
        self.tablelogins.column("#0", anchor = "center", width = 300)
        self.tablelogins.column("#1", anchor = "center", width = 300)
        self.tablelogins.column("#2", anchor = "center", width = 150)
        self.tablelogins.place(x = 20, y = 75)
        
        self.badddlogin = tk.Button(self.janelalogins, bg = "peru", fg = "black", text = "Adicionar login", command = self.adicionarlogin, height= 2, width = 40)
        self.bremoverlogin = tk.Button(self.janelalogins, bg = "peru", fg = "black", text = "Remover llgin", command = self.removerlogin, height= 2, width = 40)
        self.badddlogin.place(x = 250, y = 500)
        self.bremoverlogin.place(x = 250, y = 550)
        
        try: 
            self.tablelogins.tag_configure("Cor", background = "bisque2")
            for i in self.logins["Acesso"]:
                self.tablelogins.insert("", 1, "" , text = i, values = (self.logins["Acesso"][i]["senha"], self.logins["Acesso"][i]["data"]), tags = ("Cor"))
                self.tablelogins.configure(height = len(self.tablelogins.get_children()))
        except:
            pass
        
        
    def adicionarlogin(self):
        self.janelaaddlogin = tk.Toplevel()
        self.janelaaddlogin.wm_title("Adicionar login")
        self.janelaaddlogin.geometry("400x300")
        self.janelaaddlogin.configure(bg = "sandy brown")
        self.nomelogin = tk.Label(self.janelaaddlogin, text = "Usuário: ", bg = "sandy brown", font = ("verdana", 10))
        self.senhalogin = tk.Label(self.janelaaddlogin, text = "Senha: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomeloginentry = tk.Entry(self.janelaaddlogin, bg = "peru")
        self.senhaloginentry = tk.Entry(self.janelaaddlogin, bg = "peru", show= "*")
        self.nomelogin.place(x = 50, y= 40)
        self.nomeloginentry.place(x = 190, y = 40)
        self.senhalogin.place(x = 50, y= 80)
        self.senhaloginentry.place(x = 190, y = 80)
        self.botaoadicionarlogin = tk.Button(self.janelaaddlogin, bg = "peru", fg = "black", text = "Adicionar login", command = self.inserirlogin, height= 2, width = 40)
        self.botaoadicionarlogin.place(x = 55, y = 225)
        

    def removerlogin(self):
        self.janelarlogin = tk.Toplevel()
        self.janelarlogin.wm_title("Remover login")
        self.janelarlogin.geometry("400x300")
        self.janelarlogin.configure(bg = "sandy brown")
        self.nomerlogin = tk.Label(self.janelarlogin, text = "Nome: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomerloginentry = tk.Entry(self.janelarlogin, bg = "peru")
        self.nomerlogin.place(x = 50, y = 40)
        self.nomerloginentry.place(x = 190, y = 40)
        self.bremoverlogin = tk.Button(self.janelarlogin, bg = "peru", fg = "black", text = "Remover login", command = self.removerlogintabela, height= 2, width = 40)
        self.bremoverlogin.place(x = 55, y = 225)
    
    def removerlogintabela(self):
        del self.logins["Acesso"][self.nomerloginentry.get()]
        firebase.patch("", self.logins)
        self.janelarlogin.destroy()
        self.tablelogins.delete(*self.tablelogins.get_children())
        try: 
            self.tablelogins.tag_configure("Cor", background = "bisque2")
            for i in self.logins["Acesso"]:
                self.tablelogins.insert("", 1, "" , text = i, values = (self.logins["Acesso"][i]["senha"], self.logins["Acesso"][i]["data"]), tags = ("Cor"))
                self.tablelogins.configure(height = len(self.tablelogins.get_children()))
        except:
            pass
        
    def inserirlogin(self):
        self.tablelogins.insert("", 1, "" , text = self.nomeloginentry.get(), values = (self.senhaloginentry.get(), str(self.datadehoje.strftime("%Y-%m-%d %H:%M"))), tags = ("Cor"))
        self.tablelogins.tag_configure("Cor", background = "bisque2")
        self.tablelogins.configure(height = len(self.tablelogins.get_children()))
        self.logins["Acesso"][self.nomeloginentry.get()]= {"senha": self.senhaloginentry.get(), "data": str(self.datadehoje.strftime("%Y-%m-%d %H:%M"))}
        firebase.patch("", self.logins)
        self.janelaaddlogin.destroy()
    
    def selecionarlicencas(self):
        self.janelalicense = tk.Toplevel()
        self.janelalicense.wm_title("Licenças")
        self.janelalicense.geometry("800x600")
        self.janelalicense.configure(bg = "sandy brown")
        self.titulolicense = tk.Label(self.janelalicense, text = "Lista de Licenças da empresa: ", font = ("Verdana", 20), bg = "sandy brown")
        self.titulolicense.place(x = 20, y = 20)
        self.tablelicense = ttk.Treeview(self.janelalicense, columns=("início", "expiração", "descrição"))
        self.tablelicense.configure(height = 0)
        
        
        self.tablelicense.heading("#0", text = "Nome")
        self.tablelicense.heading("#1", text = "Adquirida em:")
        self.tablelicense.heading("#2", text = "Expira em:")
        self.tablelicense.heading("#3", text = "Descrição")
        self.tablelicense.column("#0", anchor = "center", width = 120)
        self.tablelicense.column("#1", anchor = "center", width = 90)
        self.tablelicense.column("#2", anchor = "center", width = 90)
        self.tablelicense.column("#3", anchor = "center", width = 450)
        self.tablelicense.place(x = 20, y = 75)
        self.badddlicense = tk.Button(self.janelalicense, bg = "peru", fg = "black", text = "Adicionar licença", command = self.adicionarlicense, height= 2, width = 40)
        self.bremoverlicense = tk.Button(self.janelalicense, bg = "peru", fg = "black", text = "Remover licença", command = self.removerlicense, height= 2, width = 40)
        self.badddlicense.place(x = 250, y = 500)
        self.bremoverlicense.place(x = 250, y = 550)
        
        try: 
            self.tablelicense.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Licenças"]:
                self.tablelicense.insert("", 1, "" , text = i, values = (self.franquiaselecionada["Licenças"][i]["inicio"], self.franquiaselecionada["Licenças"][i]["expiracao"], self.franquiaselecionada["Licenças"][i]["desc"]), tags = ("Cor"))
                self.tablelicense.configure(height = len(self.tablelicense.get_children()))
        except:
            pass
        
    def adicionarlicense(self):
        self.janelaaddlicense = tk.Toplevel()
        self.janelaaddlicense.wm_title("Adicionar despesa")
        self.janelaaddlicense.geometry("400x300")
        self.janelaaddlicense.configure(bg = "sandy brown")
        self.nomelicense = tk.Label(self.janelaaddlicense, text = "Nome: ", bg = "sandy brown", font = ("verdana", 10))
        self.datailicense = tk.Label(self.janelaaddlicense, text = "Adquirida em: ", bg = "sandy brown", font = ("verdana", 10))
        self.dataexplicense = tk.Label(self.janelaaddlicense, text = "Expira em: ", bg = "sandy brown", font = ("verdana", 10))
        self.descricaolicense = tk.Label(self.janelaaddlicense, text = "Descrição: ", bg = "sandy brown", font = ("verdana", 10))

        self.nomelicenseentry = tk.Entry(self.janelaaddlicense, bg = "peru")
        self.datailicenseentry = tk.Entry(self.janelaaddlicense, bg = "peru")
        self.dataexplicenseentry = tk.Entry(self.janelaaddlicense, bg = "peru")
        self.descricaolicenseentry = tk.Entry(self.janelaaddlicense, bg = "peru")
        self.nomelicense.place(x = 50, y= 40)
        self.nomelicenseentry.place(x = 190, y = 40)
        self.datailicense.place(x = 50, y= 80)
        self.datailicenseentry.place(x = 190, y = 80)
        self.dataexplicense.place(x = 50, y= 120)
        self.dataexplicenseentry.place(x = 190, y = 120)
        self.descricaolicense.place(x = 50, y = 160)
        self.descricaolicenseentry.place(x = 190, y = 160)
        self.botaoadicionarlicense = tk.Button(self.janelaaddlicense, bg = "peru", fg = "black", text = "Adicionar licença", command = self.inserirlicense, height= 2, width = 40)
        self.botaoadicionarlicense.place(x = 55, y = 225)
        
    def inserirlicense(self):
        self.tablelicense.insert("", 1, "" , text = self.nomelicenseentry.get(), values = (self.datailicenseentry.get(), self.dataexplicenseentry.get(), self.descricaolicenseentry.get()), tags = ("Cor"))
        self.tablelicense.tag_configure("Cor", background = "bisque2")
        self.tablelicense.configure(height = len(self.tablelicense.get_children()))
        self.franquiaselecionada["Licenças"][self.nomelicenseentry.get()]= {"inicio": self.datailicenseentry.get(), "expiracao": self.dataexplicenseentry.get(), "desc": self.descricaolicenseentry.get()}
        firebase.patch(self.selecionada, self.franquiaselecionada)
        self.janelaaddlicense.destroy()
    
    def removerlicense(self):
        self.janelarlicense = tk.Toplevel()
        self.janelarlicense.wm_title("Remover despesa")
        self.janelarlicense.geometry("400x300")
        self.janelarlicense.configure(bg = "sandy brown")
        self.nomelicenser = tk.Label(self.janelarlicense, text = "Nome: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomelicenserentry = tk.Entry(self.janelarlicense, bg = "peru")
        self.nomelicenser.place(x = 50, y = 40)
        self.nomelicenserentry.place(x = 190, y = 40)
        self.bremoverlicenser = tk.Button(self.janelarlicense, bg = "peru", fg = "black", text = "Remover licença", command = self.removerlicensetabela, height= 2, width = 40)
        self.bremoverlicenser.place(x = 55, y = 225)
    
    def removerlicensetabela(self):
        del self.franquiaselecionada["Licenças"][self.nomelicenserentry.get()]
        firebase.patch(self.selecionada, self.franquiaselecionada)
        self.janelarlicense.destroy()
        self.tablelicense.delete(*self.tablelicense.get_children())
        try: 
            self.tablelicense.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Licenças"]:
                self.tablelicense.insert("", 1, "" , text = i, values = (self.franquiaselecionada["Licenças"][i]["inicio"], self.franquiaselecionada["Licenças"][i]["expiracao"], self.franquiaselecionada["Licenças"][i]["desc"]), tags = ("Cor"))
                self.tablelicense.configure(height = len(self.tablelicense.get_children()))
        except:
            pass
        
    
    
    def selecionarfuncionarios(self):
        self.janelafuncionarios = tk.Toplevel()
        self.janelafuncionarios.wm_title("Funcionários")
        self.janelafuncionarios.geometry("800x600")
        self.janelafuncionarios.configure(bg = "sandy brown")
        self.titulofuncionarios = tk.Label(self.janelafuncionarios, text = "Lista de Funcionários: ", font = ("Verdana", 20), bg = "sandy brown")
        self.titulofuncionarios.place(x = 20, y = 20)
        
        
        self.tablefuncionarios = ttk.Treeview(self.janelafuncionarios, columns=("idade", "cpf", "salario", "cargo", "data"))
        self.tablefuncionarios.configure(height = 0)
        
        self.tablefuncionarios.heading("#0", text = "Nome")
        self.tablefuncionarios.heading("#1", text = "Idade")
        self.tablefuncionarios.heading("#2", text = "CPF")
        self.tablefuncionarios.heading("#3", text = "Salário")
        self.tablefuncionarios.heading("#4", text = "Função")
        self.tablefuncionarios.heading("#5", text = "Data de Início")
                                       
        self.tablefuncionarios.column("#0", anchor = "center", width = 150)
        self.tablefuncionarios.column("#1", anchor = "center", width = 90)
        self.tablefuncionarios.column("#2", anchor = "center", width = 120)
        self.tablefuncionarios.column("#3", anchor = "center", width = 90)
        self.tablefuncionarios.column("#4", anchor = "center", width = 90)                              
        self.tablefuncionarios.column("#5", anchor = "center", width = 90)
        self.tablefuncionarios.place(x = 20, y = 75)
        
        self.baddfuncionario = tk.Button(self.janelafuncionarios, bg = "peru", fg = "black", text = "Adicionar funcionário", command = self.adicionarfuncionario, height= 2, width = 40)
        self.bremoverfuncionario = tk.Button(self.janelafuncionarios, bg = "peru", fg = "black", text = "Remover funcionário", command = self.removerfuncionario, height= 2, width = 40)
        self.baddfuncionario.place(x = 250, y = 500)
        self.bremoverfuncionario.place(x = 250, y = 550)
        
        try:
            self.tablefuncionarios.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Funcionarios"]:
                self.tablefuncionarios.insert("", 1, "" , text = i, values = (self.franquiaselecionada["Funcionarios"][i]["idade"], self.franquiaselecionada["Funcionarios"][i]["cpf"], self.franquiaselecionada["Funcionarios"][i]["salario"], self.franquiaselecionada["Funcionarios"][i]["funcao"], self.franquiaselecionada["Funcionarios"][i]["data"]), tags = ("Cor"))
                self.tablefuncionarios.configure(height = len(self.tablefuncionarios.get_children()))
        except:
            pass
        
    def selecionardespesas(self):
        self.janelad = tk.Toplevel()
        self.janelad.wm_title("Despesas")
        self.janelad.geometry("800x600")
        self.janelad.configure(bg = "sandy brown")
        self.titulodespesas = tk.Label(self.janelad, text = "Lista de Despesas: ", font = ("Verdana", 20), bg = "sandy brown")
        self.titulodespesas.place(x = 20, y = 20)
        self.tabledespesas = ttk.Treeview(self.janelad, columns=("valor", "descricao"))
        self.tabledespesas.configure(height = 0)
        
        self.tabledespesas.heading("#0", text = "Nome")
        self.tabledespesas.heading("#1", text = "Valor")
        self.tabledespesas.heading("#2", text = "Descrição")
        self.tabledespesas.column("#0", anchor = "center", width = 150)
        self.tabledespesas.column("#1", anchor = "center", width = 120)
        self.tabledespesas.column("#2", anchor = "center", width = 500)
        self.tabledespesas.place(x = 20, y = 75)
        
        self.badddespesa = tk.Button(self.janelad, bg = "peru", fg = "black", text = "Adicionar despesa", command = self.adicionardespesa, height= 2, width = 40)
        self.bremoverdespesa = tk.Button(self.janelad, bg = "peru", fg = "black", text = "Remover despesa", command = self.removerdespesa, height= 2, width = 40)
        self.badddespesa.place(x = 250, y = 500)
        self.bremoverdespesa.place(x = 250, y = 550)
        try:
            self.tabledespesas.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Despesas"]:
                self.tabledespesas.insert("", 1, "" , text = i, values = (self.franquiaselecionada["Despesas"][i]["valor"], self.franquiaselecionada["Despesas"][i]["desc"]), tags = ("Cor"))
                self.tabledespesas.configure(height = len(self.tabledespesas.get_children()))
        except:
            pass
    def adicionardespesa(self):
        self.janelaadddespesa = tk.Toplevel()
        self.janelaadddespesa.wm_title("Adicionar despesa")
        self.janelaadddespesa.geometry("400x300")
        self.janelaadddespesa.configure(bg = "sandy brown")
        self.nomedespesa = tk.Label(self.janelaadddespesa, text = "Nome: ", bg = "sandy brown", font = ("verdana", 10))
        self.valordespesa = tk.Label(self.janelaadddespesa, text = "Valor: ", bg = "sandy brown", font = ("verdana", 10))
        self.descricaodespesa = tk.Label(self.janelaadddespesa, text = "Descrição: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomedespesaentry = tk.Entry(self.janelaadddespesa, bg = "peru")
        self.valordespesaentry = tk.Entry(self.janelaadddespesa, bg = "peru")
        self.descricaodespesaentry = tk.Entry(self.janelaadddespesa, bg = "peru")
        self.nomedespesa.place(x = 50, y= 40)
        self.nomedespesaentry.place(x = 190, y = 40)
        self.valordespesa.place(x = 50, y= 80)
        self.valordespesaentry.place(x = 190, y = 80)
        self.descricaodespesa.place(x = 50, y= 120)
        self.descricaodespesaentry.place(x = 190, y = 120)
        self.botaoadicionardespesa = tk.Button(self.janelaadddespesa, bg = "peru", fg = "black", text = "Adicionar despesa", command = self.inserirdespesa, height= 2, width = 40)
        self.botaoadicionardespesa.place(x = 55, y = 225)
        
    
    def inserirdespesa(self):
        self.tabledespesas.insert("", 1, "" , text = self.nomedespesaentry.get(), values = (self.valordespesaentry.get(), self.descricaodespesaentry.get()), tags = ("Cor"))
        self.tabledespesas.tag_configure("Cor", background = "bisque2")
        self.tabledespesas.configure(height = len(self.tabledespesas.get_children()))
        self.franquiaselecionada["Despesas"][self.nomedespesaentry.get()]= {"valor": self.valordespesaentry.get(), "desc": self.descricaodespesaentry.get()}
        firebase.patch(self.selecionada, self.franquiaselecionada)
        self.janelaadddespesa.destroy()
        
    def removerdespesa(self): 
        self.janelardespesa = tk.Toplevel()
        self.janelardespesa.wm_title("Remover despesa")
        self.janelardespesa.geometry("400x300")
        self.janelardespesa.configure(bg = "sandy brown")
        self.nomedespesar = tk.Label(self.janelardespesa, text = "Nome: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomedespesarentry = tk.Entry(self.janelardespesa, bg = "peru")
        self.nomedespesar.place(x = 50, y = 40)
        self.nomedespesarentry.place(x = 190, y = 40)
        self.bremoverdespesaj = tk.Button(self.janelardespesa, bg = "peru", fg = "black", text = "Remover despesa", command = self.removerdespesatabela, height= 2, width = 40)
        self.bremoverdespesaj.place(x = 55, y = 225)
        
    def removerdespesatabela(self):
        del self.franquiaselecionada["Despesas"][self.nomedespesarentry.get()]
        firebase.patch(self.selecionada, self.franquiaselecionada)
        self.janelardespesa.destroy()
        self.tabledespesas.delete(*self.tabledespesas.get_children())
        try:
            self.tabledespesas.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Despesas"]:
                self.tabledespesas.insert("", 1, "" , text = i, values = (self.franquiaselecionada["Despesas"][i]["valor"], self.franquiaselecionada["Despesas"][i]["desc"]), tags = ("Cor"))
                self.tabledespesas.configure(height = len(self.tabledespesas.get_children()))
        except:
            pass
    
        
    
    def adicionarfuncionario(self):
        self.janelaaddfuncionario = tk.Toplevel()
        self.janelaaddfuncionario.wm_title("Adicionar funcionário")
        self.janelaaddfuncionario.geometry("400x350")
        self.janelaaddfuncionario.configure(bg = "sandy brown")
        self.nomefuncionario = tk.Label(self.janelaaddfuncionario, text = "Nome: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomefuncionarioentry = tk.Entry(self.janelaaddfuncionario, bg = "peru")
        self.idadefuncionario = tk.Label(self.janelaaddfuncionario, text = "Idade: ", bg = "sandy brown", font = ("verdana", 10))
        self.idadefuncionarioentry = tk.Entry(self.janelaaddfuncionario, bg = "peru")
        self.cpffuncionario = tk.Label(self.janelaaddfuncionario, text = "CPF: ", bg = "sandy brown", font = ("verdana", 10))
        self.cpffuncionarioentry = tk.Entry(self.janelaaddfuncionario, bg = "peru")
        self.salariofuncionario = tk.Label(self.janelaaddfuncionario, text = "Salário: ", bg = "sandy brown", font = ("verdana", 10))
        self.salariofuncionarioentry = tk.Entry(self.janelaaddfuncionario, bg = "peru")
        self.funcaofuncionario = tk.Label(self.janelaaddfuncionario, text = "Função: ", bg = "sandy brown", font = ("verdana", 10))
        self.funcaofuncionarioentry = tk.Entry(self.janelaaddfuncionario, bg = "peru")
        self.datafuncionario = tk.Label(self.janelaaddfuncionario, text = "Data de Início: ", bg = "sandy brown", font = ("verdana", 10))
        self.datafuncionarioentry = tk.Entry(self.janelaaddfuncionario, bg = "peru")
        self.nomefuncionario.place(x = 50, y= 40)
        self.nomefuncionarioentry.place(x = 190, y = 40)
        self.idadefuncionario.place(x = 50, y= 80)
        self.idadefuncionarioentry.place(x = 190, y = 80)
        self.cpffuncionario.place(x = 50, y= 120)
        self.cpffuncionarioentry.place(x = 190, y = 120)
        self.salariofuncionario.place(x = 50, y= 160)
        self.salariofuncionarioentry.place(x = 190, y = 160)
        self.funcaofuncionario.place(x = 50, y= 200)
        self.funcaofuncionarioentry.place(x = 190, y = 200)
        self.datafuncionario.place(x = 50, y= 240)
        self.datafuncionarioentry.place(x = 190, y = 240)
        self.baddfuncionarioa = tk.Button(self.janelaaddfuncionario, bg = "peru", fg = "black", text = "Adicionar funcionário", command = self.inserirfuncionario, height= 2, width = 40)
        self.baddfuncionarioa.place(x = 50, y = 280)
        

    def inserirfuncionario(self):
        self.tablefuncionarios.insert("", 1, "" , text = self.nomefuncionarioentry.get(), values = (self.idadefuncionarioentry.get(), self.cpffuncionarioentry.get(), self.salariofuncionarioentry.get(), self.funcaofuncionarioentry.get(), self.datafuncionarioentry.get()), tags = ("Cor"))
        self.tablefuncionarios.tag_configure("Cor", background = "bisque2")
        self.tablefuncionarios.configure(height = len(self.tablefuncionarios.get_children()))
        self.franquiaselecionada["Funcionarios"][self.nomefuncionarioentry.get()] = {"idade" : self.idadefuncionarioentry.get(), "cpf": self.cpffuncionarioentry.get(), "salario": self.salariofuncionarioentry.get(), "funcao": self.funcaofuncionarioentry.get(), "data": self.datafuncionarioentry.get()}
        firebase.patch(self.selecionada, self.franquiaselecionada)
        self.janelaaddfuncionario.destroy()
        
    def removerfuncionario(self):
        self.janelaremoverfuncionario = tk.Toplevel()
        self.janelaremoverfuncionario.wm_title("Remover funcionário")
        self.janelaremoverfuncionario.geometry("400x300")
        self.janelaremoverfuncionario.configure(bg = "sandy brown")
        self.nomeremoverfuncionario = tk.Label(self.janelaremoverfuncionario, text = "Nome: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomerfuncionarioentry = tk.Entry(self.janelaremoverfuncionario, bg = "peru")
        self.nomeremoverfuncionario.place(x = 50, y = 40)
        self.nomerfuncionarioentry.place(x = 190, y = 40)
        self.bremoverfuncionariosr = tk.Button(self.janelaremoverfuncionario, bg = "peru", fg = "black", text = "Remover funcionário", command = self.removerfuncionariotabela, height= 2, width = 40)
        self.bremoverfuncionariosr.place(x = 55, y = 225)
        
    def removerfuncionariotabela(self):
        del self.franquiaselecionada["Funcionarios"][self.nomerfuncionarioentry.get()]
        firebase.patch(self.selecionada, self.franquiaselecionada)
        self.janelaremoverfuncionario.destroy()
        self.tablefuncionarios.delete(*self.tablefuncionarios.get_children())
        try:
            self.tablefuncionarios.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Funcionarios"]:
                self.tablefuncionarios.insert("", 1, "" , text = i, values = (self.franquiaselecionada["Funcionarios"][i]["idade"], self.franquiaselecionada["Funcionarios"][i]["cpf"], self.franquiaselecionada["Funcionarios"][i]["salario"], self.franquiaselecionada["Funcionarios"][i]["funcao"], self.franquiaselecionada["Funcionarios"][i]["data"]), tags = ("Cor"))
                self.tablefuncionarios.configure(height = len(self.tablefuncionarios.get_children()))
        except:
            pass
        
    def voicebutton3(self):
        self.speak = wincl.Dispatch("SAPI.SpVoice")
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()


        with self.mic as source:
            self.audio = self.r.listen(source, phrase_time_limit = 2)
            print(self.r.recognize_google(self.audio, language = "pt-BR"))
    
            
            
        if self.r.recognize_google(self.audio, language = "pt-BR") == "adicionar reserva":
            try:
                self.adicionarreserva()
                
                
            except:
                pass
            return
            
            
        if self.r.recognize_google(self.audio, language = "pt-BR") == "remover reserva":
            try:
                self.removereserva()
                
                
            except:
                pass
            return
        if self.r.recognize_google(self.audio, language = "pt-BR") == "editar reserva":
            try:
                self.editarreserva()
                
                
            except:
                pass
            return
        self.speak.Speak("Desculpe, não entendi. Por favor, tente novamente!")
        
    def selecionarsalao(self):
        try:
            self.InventoryTitle.destroy()
            self.Inventory.destroy()
            self.InventoryEdit.destroy()
            self.InventoryAdd.destroy()
            self.Reposition.destroy()
            self.OrdersTitle.destroy()
            self.OrdersTable.destroy()
            self.PlaceOrder.destroy()
            self.EditOrder.destroy()
            self.RemoveOrder.destroy()
        except:
            pass
        try: 
            self.canvasmetas.destroy()
            self.metas.destroy()
            self.tablemetas.destroy()
            self.baddmetas.destroy()
            self.beditarmetas.destroy()
            self.bremovermetas.destroy()
        except:
            pass
        try: 
            self.voicecommand4.destroy()
        except:
            pass
        try:
            self.voicecommand2.destroy()
        except:
            pass
        try:
            self.salao.configure(bg = "black", fg = "white")
            self.salao.configure(command = self.bloquear)
            self.adm.configure(command = self.selecionaradm)
            self.cozinha.configure(command = self.selecionarcozinha)
        except:
            pass
        
        try:
            self.adm.configure(bg = "peru", fg = "black")
        except:
            pass
    
        try:
            self.cozinha.configure(bg = "peru", fg = "black")
        except:
            pass
        self.voicecommand3 = tk.Button(self.mainwindow, bg = "cyan" , image = self.imagemmic1, command = self.voicebutton3, height= 50, width = 50)
        self.voicecommand3.image = self.imagemmic1
        self.voicecommand3.place(x = 420, y = 700)
   
        
        self.reservas = tk.Label(self.mainwindow, text = "Reservas: ", font = ("Verdana", 20), bg= "sandy brown")
        self.reservas.place(x = 180, y = 100)
        
        
        self.tablereservas = ttk.Treeview(self.mainwindow, columns=("nome", "horario", "origem", "mesa"))
        self.tablereservas.configure(height = 0)
        
        self.tablereservas.heading("#0", text = "ID")
        self.tablereservas.heading("#1", text = "Nome")
        self.tablereservas.heading("#2", text = "Horário")
        self.tablereservas.heading("#3", text = "Origem")
        self.tablereservas.heading("#4", text = "Mesa")
        self.tablereservas.column("#0", anchor = 'center', width=40)
        self.tablereservas.column("#1", anchor = "w", width = 170)
        self.tablereservas.column("#2", anchor='center', width=90)
        self.tablereservas.column("#3", anchor='center', width=90) 
        self.tablereservas.column("#4", anchor='center', width=90)
        self.tablereservas.place(x= 20, y = 150)
       
        
        self.badicionarreserva = tk.Button(self.mainwindow, bg = "peru", fg = "black", font = ("verdana", 10), text = "Adicionar reserva", command = self.adicionarreserva, height= 2, width = 40)
        self.bremoverreserva = tk.Button(self.mainwindow, bg = "peru", fg = "black", font = ("verdana", 10), text = "Remover reserva", command = self.removereserva, height= 2, width = 40)
        self.beditareserva = tk.Button(self.mainwindow, bg = "peru", fg = "black", font = ("verdana", 10), text = "Editar reserva", command = self.editarreserva, height= 2, width = 40)
        self.badicionarreserva.place(x = 80, y = 650)
        self.bremoverreserva.place(x = 80, y = 700)
        self.beditareserva.place(x = 80, y = 750)
        
        imagemlogosalao = ImageTk.PhotoImage(Image.open("Logo2.png"))
        self.imagemslogosalao = tk.Label(self.mainwindow, image = imagemlogosalao, height = 282, width= 500, bg = "sandy brown")
        self.imagemslogosalao.image = imagemlogosalao
        self.imagemslogosalao.place(x = 1000, y = 250)
        
        
    
        
        
        
        try:
            self.bfuncionarios.destroy()
            self.bdespesas.destroy()
            self.blicensas.destroy()
            self.blogins.destroy()
            self.tablepromocoes.destroy()
            self.badicionarpromocao.destroy()
            self.beditarpromocao.destroy()
            self.bremoverpromocao.destroy()
            self.fundofinancas.destroy()
            self.tfaturamento.destroy()
            self.tbruta.destroy()
            self.tdespesas.destroy()
            self.tfuncionarios.destroy()
            self.tpedidos.destroy()
            self.totalmesas.destroy()
            self.treservas.destroy()
            self.gerenciamento.destroy()
            self.financas.destroy()
            self.promocoes.destroy()
            self.canvasmetas.destroy()
            self.metas.destroy()
            self.tablemetas.destroy()
            self.baddmetas.destroy()
            self.beditarmetas.destroy()
            self.bremovermetas.destroy()
        except:
            pass
        
        
        
        self.verde1 = ImageTk.PhotoImage(Image.open("1verde.png"))
        self.verde2 = ImageTk.PhotoImage(Image.open("2verde.png"))
        self.verde3 = ImageTk.PhotoImage(Image.open("3verde.png"))
        self.verde4 = ImageTk.PhotoImage(Image.open("4verde.png"))
        self.verde5 = ImageTk.PhotoImage(Image.open("5verde.png"))
        self.verde6 = ImageTk.PhotoImage(Image.open("6verde.png"))
        self.verde7 = ImageTk.PhotoImage(Image.open("7verde.png"))
        self.verde8 = ImageTk.PhotoImage(Image.open("8verde.png"))
        self.verde9 = ImageTk.PhotoImage(Image.open("9verde.png"))
        self.verde10 = ImageTk.PhotoImage(Image.open("10verde.png"))
        self.verde11 = ImageTk.PhotoImage(Image.open("11verde.png"))
        self.verde12 = ImageTk.PhotoImage(Image.open("12verde.png"))
        self.verde13 = ImageTk.PhotoImage(Image.open("13verde.png"))
        self.verde14 = ImageTk.PhotoImage(Image.open("14verde.png"))
        self.verde15 = ImageTk.PhotoImage(Image.open("15verde.png"))
        self.verde16 = ImageTk.PhotoImage(Image.open("16verde.png"))
        self.verde17 = ImageTk.PhotoImage(Image.open("17verde.png"))
        self.verde18 = ImageTk.PhotoImage(Image.open("18verde.png"))
        self.verde19 = ImageTk.PhotoImage(Image.open("19verde.png"))
        self.verde20 = ImageTk.PhotoImage(Image.open("20verde.png"))
        self.verde21 = ImageTk.PhotoImage(Image.open("21verde.png"))
        self.verde22 = ImageTk.PhotoImage(Image.open("22verde.png"))
        self.verde23 = ImageTk.PhotoImage(Image.open("23verde.png"))
        self.verde24 = ImageTk.PhotoImage(Image.open("24verde.png"))
        self.verde25 = ImageTk.PhotoImage(Image.open("25verde.png"))
        self.verde26 = ImageTk.PhotoImage(Image.open("26verde.png"))
        self.verde27 = ImageTk.PhotoImage(Image.open("27verde.png"))
        self.verde28 = ImageTk.PhotoImage(Image.open("28verde.png"))
        self.verde29 = ImageTk.PhotoImage(Image.open("29verde.png"))
        self.verde30 = ImageTk.PhotoImage(Image.open("30verde.png"))
        
        
        
        self.vermelho1 = ImageTk.PhotoImage(Image.open("1vermelho.png"))
        self.vermelho2 = ImageTk.PhotoImage(Image.open("2vermelho.png"))
        self.vermelho3 = ImageTk.PhotoImage(Image.open("3vermelho.png"))
        self.vermelho4 = ImageTk.PhotoImage(Image.open("4vermelho.png"))
        self.vermelho5 = ImageTk.PhotoImage(Image.open("5vermelho.png"))
        self.vermelho6 = ImageTk.PhotoImage(Image.open("6vermelho.png"))
        self.vermelho7 = ImageTk.PhotoImage(Image.open("7vermelho.png"))
        self.vermelho8 = ImageTk.PhotoImage(Image.open("8vermelho.png"))
        self.vermelho9 = ImageTk.PhotoImage(Image.open("9vermelho.png"))
        self.vermelho10 = ImageTk.PhotoImage(Image.open("10vermelho.png"))
        self.vermelho11 = ImageTk.PhotoImage(Image.open("11vermelho.png"))
        self.vermelho12 = ImageTk.PhotoImage(Image.open("12vermelho.png"))
        self.vermelho13 = ImageTk.PhotoImage(Image.open("13vermelho.png"))
        self.vermelho14 = ImageTk.PhotoImage(Image.open("14vermelho.png"))
        self.vermelho15 = ImageTk.PhotoImage(Image.open("15vermelho.png"))
        self.vermelho16 = ImageTk.PhotoImage(Image.open("16vermelho.png"))
        self.vermelho17 = ImageTk.PhotoImage(Image.open("17vermelho.png"))
        self.vermelho18 = ImageTk.PhotoImage(Image.open("18vermelho.png"))
        self.vermelho19 = ImageTk.PhotoImage(Image.open("19vermelho.png"))
        self.vermelho20 = ImageTk.PhotoImage(Image.open("20vermelho.png"))
        self.vermelho21 = ImageTk.PhotoImage(Image.open("21vermelho.png"))
        self.vermelho22 = ImageTk.PhotoImage(Image.open("22vermelho.png"))
        self.vermelho23 = ImageTk.PhotoImage(Image.open("23vermelho.png"))
        self.vermelho24 = ImageTk.PhotoImage(Image.open("24vermelho.png"))
        self.vermelho25 = ImageTk.PhotoImage(Image.open("25vermelho.png"))
        self.vermelho26 = ImageTk.PhotoImage(Image.open("26vermelho.png"))
        self.vermelho27 = ImageTk.PhotoImage(Image.open("27vermelho.png"))
        self.vermelho28 = ImageTk.PhotoImage(Image.open("28vermelho.png"))
        self.vermelho29 = ImageTk.PhotoImage(Image.open("29vermelho.png"))
        self.vermelho30 = ImageTk.PhotoImage(Image.open("30vermelho.png"))
        
        
     
     
        color = "sandy brown"
     
     
        self.verde1f = tk.Button(self.mainwindow, image = self.verde1, height = 50, width= 76, bg = color, command = self.vermelhot1)
        self.verde2f = tk.Button(self.mainwindow, image = self.verde2, height = 50, width= 76, bg = color, command = self.vermelhot2)
        self.verde3f = tk.Button(self.mainwindow, image = self.verde3, height = 50, width= 76, bg = color, command = self.vermelhot3)
        self.verde4f = tk.Button(self.mainwindow, image = self.verde4, height = 50, width= 76, bg = color, command = self.vermelhot4)
        self.verde5f = tk.Button(self.mainwindow, image = self.verde5, height = 50, width= 76, bg = color, command = self.vermelhot5)
        self.verde6f = tk.Button(self.mainwindow, image = self.verde6, height = 50, width= 76, bg = color, command = self.vermelhot6)
        self.verde7f = tk.Button(self.mainwindow, image = self.verde7, height = 50, width= 76, bg = color, command = self.vermelhot7)
        self.verde8f = tk.Button(self.mainwindow, image = self.verde8, height = 50, width= 76, bg = color, command = self.vermelhot8)
        self.verde9f = tk.Button(self.mainwindow, image = self.verde9, height = 50, width= 76, bg = color, command = self.vermelhot9)
        self.verde10f = tk.Button(self.mainwindow, image = self.verde10, height = 50, width= 76, bg = color, command = self.vermelhot10)
        self.verde11f = tk.Button(self.mainwindow, image = self.verde11, height = 50, width= 76, bg = color, command = self.vermelhot11)
        self.verde12f = tk.Button(self.mainwindow, image = self.verde12, height = 50, width= 76, bg = color, command = self.vermelhot12)
        self.verde13f = tk.Button(self.mainwindow, image = self.verde13, height = 50, width= 76, bg = color, command = self.vermelhot13)
        self.verde14f = tk.Button(self.mainwindow, image = self.verde14, height = 50, width= 76, bg = color, command = self.vermelhot14)
        self.verde15f = tk.Button(self.mainwindow, image = self.verde15, height = 50, width= 76, bg = color, command = self.vermelhot15)
        self.verde16f = tk.Button(self.mainwindow, image = self.verde16, height = 50, width= 76, bg = color, command = self.vermelhot16)
        self.verde17f = tk.Button(self.mainwindow, image = self.verde17, height = 50, width= 76, bg = color, command = self.vermelhot17)
        self.verde18f = tk.Button(self.mainwindow, image = self.verde18, height = 50, width= 76, bg = color, command = self.vermelhot18)
        self.verde19f = tk.Button(self.mainwindow, image = self.verde19, height = 50, width= 76, bg = color, command = self.vermelhot19)
        self.verde20f = tk.Button(self.mainwindow, image = self.verde20, height = 50, width= 76, bg = color, command = self.vermelhot20)
        self.verde21f = tk.Button(self.mainwindow, image = self.verde21, height = 50, width= 76, bg = color, command = self.vermelhot21)
        self.verde22f = tk.Button(self.mainwindow, image = self.verde22, height = 50, width= 76, bg = color, command = self.vermelhot22)
        self.verde23f = tk.Button(self.mainwindow, image = self.verde23, height = 50, width= 76, bg = color, command = self.vermelhot23)
        self.verde24f = tk.Button(self.mainwindow, image = self.verde24, height = 50, width= 76, bg = color, command = self.vermelhot24)
        self.verde25f = tk.Button(self.mainwindow, image = self.verde25, height = 50, width= 76, bg = color, command = self.vermelhot25)
        self.verde26f = tk.Button(self.mainwindow, image = self.verde26, height = 50, width= 76, bg = color, command = self.vermelhot26)
        self.verde27f = tk.Button(self.mainwindow, image = self.verde27, height = 50, width= 76, bg = color, command = self.vermelhot27)
        self.verde28f = tk.Button(self.mainwindow, image = self.verde28, height = 50, width= 76, bg = color, command = self.vermelhot28)
        self.verde29f = tk.Button(self.mainwindow, image = self.verde29, height = 50, width= 76, bg = color, command = self.vermelhot29)
        self.verde30f = tk.Button(self.mainwindow, image = self.verde30, height = 50, width= 76, bg = color, command = self.vermelhot30)
        
        
        
        
        
        self.vermelho1f = tk.Button(self.mainwindow, image = self.vermelho1, height = 50, width= 76, bg = color, command = self.verdet1)
        self.vermelho2f = tk.Button(self.mainwindow, image = self.vermelho2, height = 50, width= 76, bg = color, command = self.verdet2)
        self.vermelho3f = tk.Button(self.mainwindow, image = self.vermelho3, height = 50, width= 76, bg = color, command = self.verdet3)
        self.vermelho4f = tk.Button(self.mainwindow, image = self.vermelho4, height = 50, width= 76, bg = color, command = self.verdet4)
        self.vermelho5f = tk.Button(self.mainwindow, image = self.vermelho5, height = 50, width= 76, bg = color, command = self.verdet5)
        self.vermelho6f = tk.Button(self.mainwindow, image = self.vermelho6, height = 50, width= 76, bg = color, command = self.verdet6)
        self.vermelho7f = tk.Button(self.mainwindow, image = self.vermelho7, height = 50, width= 76, bg = color, command = self.verdet7)
        self.vermelho8f = tk.Button(self.mainwindow, image = self.vermelho8, height = 50, width= 76, bg = color, command = self.verdet8)
        self.vermelho9f = tk.Button(self.mainwindow, image = self.vermelho9, height = 50, width= 76, bg = color, command = self.verdet9)
        self.vermelho10f = tk.Button(self.mainwindow, image = self.vermelho10, height = 50, width= 76, bg = color, command = self.verdet10)
        self.vermelho11f = tk.Button(self.mainwindow, image = self.vermelho11, height = 50, width= 76, bg = color, command = self.verdet11)
        self.vermelho12f = tk.Button(self.mainwindow, image = self.vermelho12, height = 50, width= 76, bg = color, command = self.verdet12)
        self.vermelho13f = tk.Button(self.mainwindow, image = self.vermelho13, height = 50, width= 76, bg = color, command = self.verdet13)
        self.vermelho14f = tk.Button(self.mainwindow, image = self.vermelho14, height = 50, width= 76, bg = color, command = self.verdet14)
        self.vermelho15f = tk.Button(self.mainwindow, image = self.vermelho15, height = 50, width= 76, bg = color, command = self.verdet15)
        self.vermelho16f = tk.Button(self.mainwindow, image = self.vermelho16, height = 50, width= 76, bg = color, command = self.verdet16)
        self.vermelho17f = tk.Button(self.mainwindow, image = self.vermelho17, height = 50, width= 76, bg = color, command = self.verdet17)
        self.vermelho18f = tk.Button(self.mainwindow, image = self.vermelho18, height = 50, width= 76, bg = color, command = self.verdet18)
        self.vermelho19f = tk.Button(self.mainwindow, image = self.vermelho19, height = 50, width= 76, bg = color, command = self.verdet19)
        self.vermelho20f = tk.Button(self.mainwindow, image = self.vermelho20, height = 50, width= 76, bg = color, command = self.verdet20)
        self.vermelho21f = tk.Button(self.mainwindow, image = self.vermelho21, height = 50, width= 76, bg = color, command = self.verdet21)
        self.vermelho22f = tk.Button(self.mainwindow, image = self.vermelho22, height = 50, width= 76, bg = color, command = self.verdet22)
        self.vermelho23f = tk.Button(self.mainwindow, image = self.vermelho23, height = 50, width= 76, bg = color, command = self.verdet23)
        self.vermelho24f = tk.Button(self.mainwindow, image = self.vermelho24, height = 50, width= 76, bg = color, command = self.verdet24)
        self.vermelho25f = tk.Button(self.mainwindow, image = self.vermelho25, height = 50, width= 76, bg = color, command = self.verdet25)
        self.vermelho26f = tk.Button(self.mainwindow, image = self.vermelho26, height = 50, width= 76, bg = color, command = self.verdet26)
        self.vermelho27f = tk.Button(self.mainwindow, image = self.vermelho27, height = 50, width= 76, bg = color, command = self.verdet27)
        self.vermelho28f = tk.Button(self.mainwindow, image = self.vermelho28, height = 50, width= 76, bg = color, command = self.verdet28)
        self.vermelho29f = tk.Button(self.mainwindow, image = self.vermelho29, height = 50, width= 76, bg = color, command = self.verdet29)
        self.vermelho30f = tk.Button(self.mainwindow, image = self.vermelho30, height = 50, width= 76, bg = color, command = self.verdet30)
        
     
        self.verde1f.image = self.verde1
        self.verde2f.image = self.verde2
        self.verde3f.image = self.verde3
        self.verde4f.image = self.verde4
        self.verde5f.image = self.verde5
        self.verde6f.image = self.verde6
        self.verde7f.image = self.verde7
        self.verde8f.image = self.verde8
        self.verde9f.image = self.verde9
        self.verde10f.image = self.verde10
        self.verde11f.image = self.verde11
        self.verde12f.image = self.verde12
        self.verde13f.image = self.verde13
        self.verde14f.image = self.verde14
        self.verde15f.image = self.verde15
        self.verde16f.image = self.verde16
        self.verde17f.image = self.verde17
        self.verde18f.image = self.verde18
        self.verde19f.image = self.verde19
        self.verde20f.image = self.verde20
        self.verde21f.image = self.verde21
        self.verde22f.image = self.verde22
        self.verde23f.image = self.verde23
        self.verde24f.image = self.verde24
        self.verde25f.image = self.verde25
        self.verde26f.image = self.verde26
        self.verde27f.image = self.verde27
        self.verde28f.image = self.verde28
        self.verde29f.image = self.verde29
        self.verde30f.image = self.verde30
        
        
        self.vermelho1f.image = self.vermelho1
        self.vermelho2f.image = self.vermelho2
        self.vermelho3f.image = self.vermelho3
        self.vermelho4f.image = self.vermelho4
        self.vermelho5f.image = self.vermelho5
        self.vermelho6f.image = self.vermelho6
        self.vermelho7f.image = self.vermelho7
        self.vermelho8f.image = self.vermelho8
        self.vermelho9f.image = self.vermelho9
        self.vermelho10f.image = self.vermelho10
        self.vermelho11f.image = self.vermelho11
        self.vermelho12f.image = self.vermelho12
        self.vermelho13f.image = self.vermelho13
        self.vermelho14f.image = self.vermelho14
        self.vermelho15f.image = self.vermelho15
        self.vermelho16f.image = self.vermelho16
        self.vermelho17f.image = self.vermelho17
        self.vermelho18f.image = self.vermelho18
        self.vermelho19f.image = self.vermelho19
        self.vermelho20f.image = self.vermelho20
        self.vermelho21f.image = self.vermelho21
        self.vermelho22f.image = self.vermelho22
        self.vermelho23f.image = self.vermelho23
        self.vermelho24f.image = self.vermelho24
        self.vermelho25f.image = self.vermelho25
        self.vermelho26f.image = self.vermelho26
        self.vermelho27f.image = self.vermelho27
        self.vermelho28f.image = self.vermelho28
        self.vermelho29f.image = self.vermelho29
        self.vermelho30f.image = self.vermelho30
        
     
#        listaverdes = ["verde1f","verde2f","verde3f","verde4f","verde5f","verde6f","verde7f","verde8f","verde9f","verde10f","verde11f","verde12f","verde13f","verde14f","verde15f","verde16f","verde17f","verde18f","verde19f","verde20f"]
    
#        for i in range(0, len(listaverdes)+1):
#            a = listaverdes[i]
#            if i < 4:
#                self.str(a).place(x = 20+(i*10) , y = 50) 
#            if i > 4 and i < 9:
#                self.str(a).place(x = 20+(i*10) , y = 100)
#            if i > 9 and i < 14:
#                self.str(a).place(x = 20+(i*10) , y = 150)
#            if i > 14 and i < 19:
#                self.str(a).place(x = 20+(i*10) , y = 200)
#       
        self.verde1f.place(x = 525, y = 150)
        self.verde2f.place(x = 625, y = 150)
        self.verde3f.place(x = 725, y = 150)
        self.verde4f.place(x = 825, y = 150)
        self.verde5f.place(x = 925, y = 150)
        self.verde6f.place(x = 525, y = 250)
        self.verde7f.place(x = 625, y = 250)
        self.verde8f.place(x = 725, y = 250)
        self.verde9f.place(x = 825, y = 250)
        self.verde10f.place(x = 925, y = 250)
        self.verde11f.place(x = 525, y = 350)
        self.verde12f.place(x = 625, y = 350)
        self.verde13f.place(x = 725, y = 350)
        self.verde14f.place(x = 825, y = 350)
        self.verde15f.place(x = 925, y = 350)
        self.verde16f.place(x = 525, y = 450)
        self.verde17f.place(x = 625, y = 450)
        self.verde18f.place(x = 725, y = 450)
        self.verde19f.place(x = 825, y = 450)
        self.verde20f.place(x = 925, y = 450)
        self.verde21f.place(x = 525, y = 550)
        self.verde22f.place(x = 625, y = 550)
        self.verde23f.place(x = 725, y = 550)
        self.verde24f.place(x = 825, y = 550)
        self.verde25f.place(x = 925, y = 550)
        self.verde26f.place(x = 525, y = 650)
        self.verde27f.place(x = 625, y = 650)
        self.verde28f.place(x = 725, y = 650)
        self.verde29f.place(x = 825, y = 650)
        self.verde30f.place(x = 925, y = 650)
        
        try:
            self.tablereservas.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Reservas"]:
                self.tablereservas.insert("", 1, "" , text = str(i), values = (self.franquiaselecionada["Reservas"][str(i)]["nome"], self.franquiaselecionada["Reservas"][str(i)]["horario"], self.franquiaselecionada["Reservas"][str(i)]["status"], self.franquiaselecionada["Reservas"][str(i)]["mesa"]), tags = ("Cor"))
                self.tablereservas.configure(height = len(self.tablereservas.get_children()))
        except:
            pass
        
        
       
     
        
    def removereserva(self):
        self.removerreservas = tk.Toplevel()
        self.removerreservas.wm_title("Remover Reserva")
        self.removerreservas.geometry("400x300")
        self.removerreservas.configure(bg = "sandy brown")
        self.ridmesa = tk.Label(self.removerreservas, text = "ID da mesa: ", bg = "sandy brown", font = ("verdana", 10))
        self.ridmesaentry = tk.Entry(self.removerreservas, bg = "peru")
        self.ridmesa.place(x = 50, y = 40)
        self.ridmesaentry.place(x = 190, y = 40)
        self.bcancelarremoverreserva = tk.Button(self.removerreservas , bg = "peru",fg = "black", font = ("verdana", 10), text = "Cancelar", command = self.cancelarinserirreserva, height= 2, width = 20)
        self.bcancelarremoverreserva.place(x=10, y= 250 )
        self.bremoverreservar = tk.Button(self.removerreservas , bg = "peru",fg = "black", font = ("verdana", 10), text = "Remover", command = self.removerreservatabela, height= 2, width = 20)
        self.bremoverreservar.place(x = 220, y = 250)
       
    def removerreservatabela(self):
        del self.franquiaselecionada["Reservas"][self.ridmesaentry.get()]
        firebase.patch(self.selecionada, self.franquiaselecionada)
        self.tablereservas.delete(*self.tablereservas.get_children())
        self.removerreservas.destroy()
        try:
            self.tablereservas.tag_configure("Cor", background = "bisque2")
            for i in self.franquiaselecionada["Reservas"]:
                self.tablereservas.insert("", 1, "" , text = str(i), values = (self.franquiaselecionada["Reservas"][str(i)]["nome"], self.franquiaselecionada["Reservas"][str(i)]["horario"], self.franquiaselecionada["Reservas"][str(i)]["status"], self.franquiaselecionada["Reservas"][str(i)]["mesa"]), tags = ("Cor"))
                self.tablereservas.configure(height = len(self.tablereservas.get_children()))
        except:
            pass
        
        
    def editarreserva(self):
        self.janelaeditar = tk.Toplevel()
        self.janelaeditar.wm_title("Editar Reserva")
        self.janelaeditar.geometry("400x300")
        self.janelaeditar.configure(bg = "sandy brown")
        self.idmesae = tk.Label(self.janelaeditar, text = "ID da mesa: ", bg = "sandy brown", font = ("verdana", 10))
        self.idmesaentrye = tk.Entry(self.janelaeditar, bg = "peru")
        self.idmesae.place(x = 50, y = 40)
        self.idmesaentrye.place(x = 190, y = 40)
        self.bselecionarid = tk.Button(self.janelaeditar, bg = "peru", fg = "black", font = ("verdana", 10), text = "Selecionar ID", command = self.editarreservaselecionada, height= 2, width = 20)
        self.bselecionarid.place(x = 110, y = 100)
    
    
    def editarreservaselecionada(self):
        self.idmesae.destroy()
        self.bselecionarid.destroy()
        self.numeromesaee = tk.Label(self.janelaeditar, text = "Número da mesa: ", bg = "sandy brown", font = ("verdana",10))
        self.numeromesaentryee = tk.Entry(self.janelaeditar, bg = "peru")
        self.nomemesaee = tk.Label(self.janelaeditar, text = "Nome: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomemesaentryee = tk.Entry(self.janelaeditar, bg = "peru")
        self.statusmesaee = tk.Label(self.janelaeditar, text = "Origem da reserva: ", bg = "sandy brown", font = ("verdana", 10))
        self.statusmesaentryee = tk.Entry(self.janelaeditar, bg = "peru")
        self.horariomesaee = tk.Label(self.janelaeditar, text = "Horário: ", bg = "sandy brown", font = ("verdana", 10))
        self.horariomesaentryee = tk.Entry(self.janelaeditar, bg = "peru")
        self.idmesaee = tk.Label(self.janelaeditar, text = "ID: ", bg = "sandy brown", font = ("verdana", 10))
        self.idmesaentryee = tk.Entry(self.janelaeditar, bg = "peru")
        self.nomemesaee.place(x = 50, y = 40)
        self.nomemesaentryee.place(x = 190, y = 40)
        self.numeromesaee.place(x = 50, y = 70)
        self.numeromesaentryee.place(x = 190, y = 70)
        self.statusmesaee.place(x = 50, y = 100)
        self.statusmesaentryee.place(x = 190, y = 100)
        self.horariomesaee.place(x = 50, y = 130)
        self.horariomesaentryee.place(x = 190, y = 130)
        self.idmesaee.place(x=50, y = 160)
        self.idmesaentryee.place(x = 190, y = 160)
        
        self.idmesaentryee.insert(0, self.idmesaentrye.get())
        self.idmesaentryee.configure(state = "disabled")
        self.horariomesaentryee.insert(0, self.franquiaselecionada["Reservas"][self.idmesaentrye.get()]["horario"])
        self.statusmesaentryee.insert(0, self.franquiaselecionada["Reservas"][self.idmesaentrye.get()]["status"])
        self.numeromesaentryee.insert(0, self.franquiaselecionada["Reservas"][self.idmesaentrye.get()]["mesa"])
        self.nomemesaentryee.insert(0, self.franquiaselecionada["Reservas"][self.idmesaentrye.get()]["nome"])
        self.binserirreservae = tk.Button(self.janelaeditar, bg = "peru", fg = "black", font = ("verdana", 10), text = "Adicionar", command = self.editartabelareserva, height= 2, width = 20)
        self.bcancelarinserrirreservae = tk.Button(self.janelaeditar, bg = "peru", fg = "black", font = ("verdana", 10), text = "Cancelar", command = self.cancelareditarreserva, height= 2, width = 20)
        self.bcancelarinserrirreservae.place(x=10, y= 250 )
        self.binserirreservae.place(x =220, y = 250)
        
        
        
        
        
        
    def editartabelareserva(self):
        self.franquiaselecionada["Reservas"][self.idmesaentryee.get()] = {"nome": self.nomemesaentryee.get(), "horario": self.horariomesaentryee.get(), "status": self.statusmesaentryee.get(), "mesa": self.numeromesaentryee.get()}
        firebase.patch(self.selecionada, self.franquiaselecionada)     
        try:
            self.tablereservas.tag_configure("Cor", background = "bisque2")
            self.tablereservas.delete(*self.tablereservas.get_children())
            for i in self.franquiaselecionada["Reservas"]:
                self.tablereservas.insert("", 1, "" , text = str(i), values = (self.franquiaselecionada["Reservas"][str(i)]["nome"], self.franquiaselecionada["Reservas"][str(i)]["horario"], self.franquiaselecionada["Reservas"][str(i)]["status"], self.franquiaselecionada["Reservas"][str(i)]["mesa"]), tags = ("Cor"))
                self.tablereservas.configure(height = len(self.tablereservas.get_children()))
        except:
            pass
        
        self.janelaeditar.destroy()
    
    def cancelareditarreserva(self):
        self.janelaeditar.destroy()
    def adicionarreserva(self):
        self.janelareservas = tk.Toplevel()
        self.janelareservas.wm_title("Janela de reserva")
        self.janelareservas.geometry("400x300")
        self.janelareservas.configure(bg = "sandy brown")
        self.numeromesa = tk.Label(self.janelareservas, text = "Número da mesa: ", bg = "sandy brown", font = ("verdana",10))
        self.numeromesaentry = tk.Entry(self.janelareservas, bg = "peru")
        self.nomemesa = tk.Label(self.janelareservas, text = "Nome: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomemesaentry = tk.Entry(self.janelareservas, bg = "peru")
        self.statusmesa = tk.Label(self.janelareservas, text = "Origem da reserva: ", bg = "sandy brown", font = ("verdana", 10))
        self.statusmesaentry = tk.Entry(self.janelareservas, bg = "peru")
        self.horariomesa = tk.Label(self.janelareservas, text = "Horário: ", bg = "sandy brown", font = ("verdana", 10))
        self.horariomesaentry = tk.Entry(self.janelareservas, bg = "peru")
        self.idmesa = tk.Label(self.janelareservas, text = "ID: ", bg = "sandy brown", font = ("verdana", 10))
        self.idmesaentry = tk.Entry(self.janelareservas, bg = "peru")
        self.nomemesa.place(x = 50, y = 40)
        self.nomemesaentry.place(x = 190, y = 40)
        self.numeromesa.place(x = 50, y = 70)
        self.numeromesaentry.place(x = 190, y = 70)
        self.statusmesa.place(x = 50, y = 100)
        self.statusmesaentry.place(x = 190, y = 100)
        self.horariomesa.place(x = 50, y = 130)
        self.horariomesaentry.place(x = 190, y = 130)
        self.idmesa.place(x=50, y = 160)
        self.idmesaentry.place(x = 190, y = 160)
        self.binserirreserva = tk.Button(self.janelareservas, bg = "peru", fg = "black", font = ("verdana", 10), text = "Adicionar", command = self.inserirreserva, height= 2, width = 20)
        self.bcancelarinserrirreserva = tk.Button(self.janelareservas, bg = "peru", fg = "black", font = ("verdana", 10), text = "Cancelar", command = self.cancelarinserirreserva, height= 2, width = 20)
        self.bcancelarinserrirreserva.place(x=10, y= 250 )
        self.binserirreserva.place(x =220, y = 250)
    
        
    def inserirreserva(self):
        if len(self.tablereservas.get_children()) < 16:
            self.tablereservas.insert("", 1, "" , text = self.idmesaentry.get(), values = (self.nomemesaentry.get(), self.horariomesaentry.get(), self.statusmesaentry.get(), self.numeromesaentry.get()), tags = ("Cor"))
            self.tablereservas.configure(height = len(self.tablereservas.get_children()))
            self.tablereservas.tag_configure("Cor", background = "bisque2")
            self.franquiaselecionada["Reservas"][str(self.idmesaentry.get())] = {"nome": self.nomemesaentry.get(), "horario": self.horariomesaentry.get(), "status": self.statusmesaentry.get(), "mesa": self.numeromesaentry.get()}
            firebase.patch(self.selecionada, self.franquiaselecionada)
            self.janelareservas.destroy()
        else:
            self.janelareservas.destroy()
            self.erroreserva = tk.Toplevel()
            self.erroreserva.wm_title("Janela de reserva")
            self.erroreserva.geometry("400x100")
            self.erroreserva.configure(bg = "indian red")
            self.erroreservatext = tk.Label(self.erroreserva, text = "Número máximo de reservas atingido! ", bg = "indian red", font = ("verdana",10))
            self.sairerror = tk.Button(self.erroreserva, bg = "grey", fg = "black", font = ("verdana", 10), text = "Ok", command = self.sairerroreserva, height= 1, width = 10)
            self.erroreservatext.place(x = 80, y = 30)
            self.sairerror.place(x= 150, y = 60 )
        
        
    def sairerroreserva(self):
        self.erroreserva.destroy()
    
    def cancelarinserirreserva(self):
        self.removerreservas.destroy()
        
    def vermelhot1(self):
        self.verde1f.destroy()
        self.vermelho1f = tk.Button(self.mainwindow, image = self.vermelho1, height = 50, width= 76, bg = "sandy brown", command = self.verdet1)
        self.vermelho1f.place(x = 525, y = 150)
    
    def vermelhot2(self):
        self.verde2f.destroy()
        self.vermelho2f = tk.Button(self.mainwindow, image = self.vermelho2, height = 50, width= 76, bg = "sandy brown", command = self.verdet2)
        self.vermelho2f.place(x = 625, y = 150)
    
    def vermelhot3(self):
        self.verde3f.destroy()
        self.vermelho3f = tk.Button(self.mainwindow, image = self.vermelho3, height = 50, width= 76, bg = "sandy brown", command = self.verdet3)
        self.vermelho3f.place(x = 725, y = 150)
        
    def vermelhot4(self):
        self.verde4f.destroy()
        self.vermelho4f = tk.Button(self.mainwindow, image = self.vermelho4, height = 50, width= 76, bg = "sandy brown", command = self.verdet4)
        self.vermelho4f.place(x = 825, y = 150)
    
    def vermelhot5(self):
        self.verde5f.destroy()
        self.vermelho5f = tk.Button(self.mainwindow, image = self.vermelho5, height = 50, width= 76, bg = "sandy brown", command = self.verdet5)
        self.vermelho5f.place(x = 925, y = 150)
        
    def vermelhot6(self):
        self.verde6f.destroy()
        self.vermelho6f = tk.Button(self.mainwindow, image = self.vermelho6, height = 50, width= 76, bg = "sandy brown", command = self.verdet6)
        self.vermelho6f.place(x = 525, y = 250)
        
    def vermelhot7(self):
        self.verde7f.destroy()
        self.vermelho7f = tk.Button(self.mainwindow, image = self.vermelho7, height = 50, width= 76, bg = "sandy brown", command = self.verdet7)
        self.vermelho7f.place(x = 625, y = 250)
        
    def vermelhot8(self):
        self.verde8f.destroy()
        self.vermelho8f = tk.Button(self.mainwindow, image = self.vermelho8, height = 50, width= 76, bg = "sandy brown", command = self.verdet8)
        self.vermelho8f.place(x = 725, y = 250)
        
    def vermelhot9(self):
        self.verde9f.destroy()
        self.vermelho9f = tk.Button(self.mainwindow, image = self.vermelho9, height = 50, width= 76, bg = "sandy brown", command = self.verdet9)
        self.vermelho9f.place(x = 825, y = 250)
    
    def vermelhot10(self):
        self.verde10f.destroy()
        self.vermelho10f = tk.Button(self.mainwindow, image = self.vermelho10, height = 50, width= 76, bg = "sandy brown", command = self.verdet10)
        self.vermelho10f.place(x = 925, y = 250)
        
    def vermelhot11(self):
        self.verde11f.destroy()
        self.vermelho11f = tk.Button(self.mainwindow, image = self.vermelho11, height = 50, width= 76, bg = "sandy brown", command = self.verdet11)
        self.vermelho11f.place(x = 525, y = 350)
        
    def vermelhot12(self):
        self.verde12f.destroy()
        self.vermelho12f = tk.Button(self.mainwindow, image = self.vermelho12, height = 50, width= 76, bg = "sandy brown", command = self.verdet12)
        self.vermelho12f.place(x = 625, y = 350)
        
    def vermelhot13(self):
        self.verde13f.destroy()
        self.vermelho13f = tk.Button(self.mainwindow, image = self.vermelho13, height = 50, width= 76, bg = "sandy brown", command = self.verdet13)
        self.vermelho13f.place(x = 725, y = 350)
        
    def vermelhot14(self):
        self.verde14f.destroy()
        self.vermelho14f = tk.Button(self.mainwindow, image = self.vermelho14, height = 50, width= 76, bg = "sandy brown", command = self.verdet14)
        self.vermelho14f.place(x = 825, y = 350)
    
    def vermelhot15(self):
        self.verde15f.destroy()
        self.vermelho15f = tk.Button(self.mainwindow, image = self.vermelho15, height = 50, width= 76, bg = "sandy brown", command = self.verdet15)
        self.vermelho15f.place(x = 925, y = 350)
    
    def vermelhot16(self):
        self.verde16f.destroy()
        self.vermelho16f = tk.Button(self.mainwindow, image = self.vermelho16, height = 50, width= 76, bg = "sandy brown", command = self.verdet16)
        self.vermelho16f.place(x = 525, y = 450)
    
    def vermelhot17(self):
        self.verde17f.destroy()
        self.vermelho17f = tk.Button(self.mainwindow, image = self.vermelho17, height = 50, width= 76, bg = "sandy brown", command = self.verdet17)
        self.vermelho17f.place(x = 625, y = 450)
    
    def vermelhot18(self):
        self.verde18f.destroy()
        self.vermelho18f = tk.Button(self.mainwindow, image = self.vermelho18, height = 50, width= 76, bg = "sandy brown", command = self.verdet18)
        self.vermelho18f.place(x = 725, y = 450)
    
    def vermelhot19(self):
        self.verde19f.destroy()
        self.vermelho19f = tk.Button(self.mainwindow, image = self.vermelho19, height = 50, width= 76, bg = "sandy brown", command = self.verdet19)
        self.vermelho19f.place(x = 825, y = 450)
     
    def vermelhot20(self):
        self.verde20f.destroy()
        self.vermelho20f = tk.Button(self.mainwindow, image = self.vermelho20, height = 50, width= 76, bg = "sandy brown", command = self.verdet20)
        self.vermelho20f.place(x = 925, y = 450)
    
    def vermelhot21(self):
        self.verde21f.destroy()
        self.vermelho21f = tk.Button(self.mainwindow, image = self.vermelho21, height = 50, width= 76, bg = "sandy brown", command = self.verdet21)
        self.vermelho21f.place(x = 525, y = 550)
        
    def vermelhot22(self):
        self.verde22f.destroy()
        self.vermelho22f = tk.Button(self.mainwindow, image = self.vermelho22, height = 50, width= 76, bg = "sandy brown", command = self.verdet22)
        self.vermelho22f.place(x = 625, y = 550)
        
    def vermelhot23(self):
        self.verde23f.destroy()
        self.vermelho23f = tk.Button(self.mainwindow, image = self.vermelho23, height = 50, width= 76, bg = "sandy brown", command = self.verdet23)
        self.vermelho23f.place(x = 725, y = 550)
        
    def vermelhot24(self):
        self.verde24f.destroy()
        self.vermelho24f = tk.Button(self.mainwindow, image = self.vermelho24, height = 50, width= 76, bg = "sandy brown", command = self.verdet24)
        self.vermelho24f.place(x = 825, y = 550)
        
    def vermelhot25(self):
        self.verde25f.destroy()
        self.vermelho25f = tk.Button(self.mainwindow, image = self.vermelho25, height = 50, width= 76, bg = "sandy brown", command = self.verdet25)
        self.vermelho25f.place(x = 925, y = 550)
        
    def vermelhot26(self):
        self.verde26f.destroy()
        self.vermelho26f = tk.Button(self.mainwindow, image = self.vermelho26, height = 50, width= 76, bg = "sandy brown", command = self.verdet26)
        self.vermelho26f.place(x = 525, y = 650)
    
    def vermelhot27(self):
        self.verde27f.destroy()
        self.vermelho27f = tk.Button(self.mainwindow, image = self.vermelho27, height = 50, width= 76, bg = "sandy brown", command = self.verdet27)
        self.vermelho27f.place(x = 625, y = 650)
        
    def vermelhot28(self):
        self.verde28f.destroy()
        self.vermelho28f = tk.Button(self.mainwindow, image = self.vermelho28, height = 50, width= 76, bg = "sandy brown", command = self.verdet28)
        self.vermelho28f.place(x = 725, y = 650)
        
    def vermelhot29(self):
        self.verde29f.destroy()
        self.vermelho29f = tk.Button(self.mainwindow, image = self.vermelho29, height = 50, width= 76, bg = "sandy brown", command = self.verdet29)
        self.vermelho29f.place(x = 825, y = 650)
        
    def vermelhot30(self):
        self.verde30f.destroy()
        self.vermelho30f = tk.Button(self.mainwindow, image = self.vermelho30, height = 50, width= 76, bg = "sandy brown", command = self.verdet30)
        self.vermelho30f.place(x = 925, y = 650)
        

        
    
    def verdet1(self):
        self.vermelho1f.destroy()
        self.verde1f = tk.Button(self.mainwindow, image = self.verde1, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot1)
        self.verde1f.place(x = 525, y = 150)
    
    def verdet2(self):
        self.vermelho2f.destroy()
        self.verde2f = tk.Button(self.mainwindow, image = self.verde2, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot2)
        self.verde2f.place(x = 625, y = 150)
    
    def verdet3(self):
        self.vermelho3f.destroy()
        self.verde3f = tk.Button(self.mainwindow, image = self.verde3, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot3)
        self.verde3f.place(x = 725, y = 150)
    
    def verdet4(self):
        self.vermelho4f.destroy()
        self.verde4f = tk.Button(self.mainwindow, image = self.verde4, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot4)
        self.verde4f.place(x = 825, y = 150)
        
    def verdet5(self):
        self.vermelho5f.destroy()
        self.verde5f = tk.Button(self.mainwindow, image = self.verde5, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot5)
        self.verde5f.place(x = 925, y = 150)
        
    def verdet6(self):
        self.vermelho6f.destroy()
        self.verde6f = tk.Button(self.mainwindow, image = self.verde6, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot6)
        self.verde6f.place(x = 525, y = 250)
        
    def verdet7(self):
        self.vermelho7f.destroy()
        self.verde7f = tk.Button(self.mainwindow, image = self.verde7, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot7)
        self.verde7f.place(x = 625, y = 250)
        
    def verdet8(self):
        self.vermelho8f.destroy()
        self.verde8f = tk.Button(self.mainwindow, image = self.verde8, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot8)
        self.verde8f.place(x = 725, y = 250)
        
    def verdet9(self):
        self.vermelho9f.destroy()
        self.verde9f = tk.Button(self.mainwindow, image = self.verde9, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot9)
        self.verde9f.place(x = 825, y = 250)
        
    def verdet10(self):
        self.vermelho10f.destroy()
        self.verde10f = tk.Button(self.mainwindow, image = self.verde10, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot10)
        self.verde10f.place(x = 925, y = 250)
        
    def verdet11(self):
        self.vermelho11f.destroy()
        self.verde11f = tk.Button(self.mainwindow, image = self.verde11, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot11)
        self.verde11f.place(x = 525, y = 350)
        
    def verdet12(self):
        self.vermelho12f.destroy()
        self.verde12f = tk.Button(self.mainwindow, image = self.verde12, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot12)
        self.verde12f.place(x = 625, y = 350)
        
    def verdet13(self):
        self.vermelho13f.destroy()
        self.verde13f = tk.Button(self.mainwindow, image = self.verde13, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot13)
        self.verde13f.place(x = 725, y = 350)
        
    def verdet14(self):
        self.vermelho14f.destroy()
        self.verde14f = tk.Button(self.mainwindow, image = self.verde14, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot14)
        self.verde14f.place(x = 825, y = 350)
        
    def verdet15(self):
        self.vermelho15f.destroy()
        self.verde15f = tk.Button(self.mainwindow, image = self.verde15, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot15)
        self.verde15f.place(x = 925, y = 350)
        
    def verdet16(self):
        self.vermelho16f.destroy()
        self.verde16f = tk.Button(self.mainwindow, image = self.verde16, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot16)
        self.verde16f.place(x = 525, y = 450)
    
    def verdet17(self):
        self.vermelho17f.destroy()
        self.verde17f = tk.Button(self.mainwindow, image = self.verde17, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot17)
        self.verde17f.place(x = 625, y = 450)
    
    def verdet18(self):
        self.vermelho18f.destroy()
        self.verde18f = tk.Button(self.mainwindow, image = self.verde18, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot18)
        self.verde18f.place(x = 725, y = 450)
    
    def verdet19(self):
        self.vermelho19f.destroy()
        self.verde19f = tk.Button(self.mainwindow, image = self.verde19, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot19)
        self.verde19f.place(x = 825, y = 450)
    
    def verdet20(self):
        self.vermelho20f.destroy()
        self.verde20f = tk.Button(self.mainwindow, image = self.verde20, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot20)
        self.verde20f.place(x = 925, y = 450)

    def verdet21(self):
        self.vermelho21f.destroy()
        self.verde21f = tk.Button(self.mainwindow, image = self.verde21, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot21)
        self.verde21f.place(x = 525, y = 550)
    
    def verdet22(self):
        self.vermelho22f.destroy()
        self.verde22f = tk.Button(self.mainwindow, image = self.verde22, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot22)
        self.verde22f.place(x = 625, y = 550)
           
    def verdet23(self):
        self.vermelho23f.destroy()
        self.verde23f = tk.Button(self.mainwindow, image = self.verde23, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot23)
        self.verde23f.place(x = 725, y = 550)
    
    def verdet24(self):
        self.vermelho24f.destroy()
        self.verde24f = tk.Button(self.mainwindow, image = self.verde24, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot24)
        self.verde24f.place(x = 825, y = 550)
    
    def verdet25(self):
        self.vermelho25f.destroy()
        self.verde25f = tk.Button(self.mainwindow, image = self.verde25, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot25)
        self.verde25f.place(x = 925, y = 550)
    
    def verdet26(self):
        self.vermelho26f.destroy()
        self.verde26f = tk.Button(self.mainwindow, image = self.verde26, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot26)
        self.verde26f.place(x = 525, y = 650)
        
    def verdet27(self):
        self.vermelho27f.destroy()
        self.verde27f = tk.Button(self.mainwindow, image = self.verde27, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot27)
        self.verde27f.place(x = 625, y = 650)
        
    def verdet28(self):
        self.vermelho28f.destroy()
        self.verde28f = tk.Button(self.mainwindow, image = self.verde28, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot28)
        self.verde28f.place(x = 725, y = 650)
        
    def verdet29(self):
        self.vermelho29f.destroy()
        self.verde29f = tk.Button(self.mainwindow, image = self.verde29, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot29)
        self.verde29f.place(x = 825, y = 650)
        
    def verdet30(self):
        self.vermelho30f.destroy()
        self.verde30f = tk.Button(self.mainwindow, image = self.verde30, height = 50, width= 76, bg = "sandy brown", command = self.vermelhot30)
        self.verde30f.place(x = 925, y = 650)
    
    
      
        
        
    def selecionarcozinha(self):
        try:
             self.voicecommand4.destroy()
        except:
            pass
#        bob =ImageTk.PhotoImage(Image.open("fundo.png"))
#        
#        self.imagembob = tk.Label(self.mainwindow, image = bob, height = 900, width= 1400, bg = "sandy brown")
#        self.imagembob.image = bob
#        self.imagembob.place(x = 100, y = 44)
        self.cozinha.configure(bg = "black", fg = "white")
        
        try:
            self.cozinha.configure(command = self.bloquear)
            self.adm.configure(command = self.selecionaradm)
            self.salao.configure(command = self.selecionarsalao)
        except:
            pass
        
        try:
            self.adm.configure(bg = "peru", fg = "black")
        except:
            pass
    
        try:
            self.salao.configure(bg = "peru", fg = "black")
        except:
            pass
        
        try:
            self.imagemslogosalao.destroy()
            self.voicecommand3.destroy()
            self.verde1f.destroy()
            self.verde2f.destroy()
            self.verde3f.destroy()
            self.verde4f.destroy()
            self.verde5f.destroy()
            self.verde6f.destroy()
            self.verde7f.destroy()
            self.verde8f.destroy()
            self.verde9f.destroy()
            self.verde10f.destroy()
            self.verde11f.destroy()
            self.verde12f.destroy()
            self.verde13f.destroy()
            self.verde14f.destroy()
            self.verde15f.destroy()
            self.verde16f.destroy()
            self.verde17f.destroy()
            self.verde18f.destroy()
            self.verde19f.destroy()
            self.verde20f.destroy()
            self.verde21f.destroy()
            self.verde22f.destroy()
            self.verde23f.destroy()
            self.verde24f.destroy()
            self.verde25f.destroy()
            self.verde26f.destroy()
            self.verde27f.destroy()
            self.verde28f.destroy()
            self.verde29f.destroy()
            self.verde30f.destroy()
            self.vermelho1f.destroy()
            self.vermelho2f.destroy()
            self.vermelho3f.destroy()
            self.vermelho4f.destroy()
            self.vermelho5f.destroy()
            self.vermelho6f.destroy()
            self.vermelho7f.destroy()
            self.vermelho8f.destroy()
            self.vermelho9f.destroy()
            self.vermelho10f.destroy()
            self.vermelho11f.destroy()
            self.vermelho12f.destroy()
            self.vermelho13f.destroy()
            self.vermelho14f.destroy()
            self.vermelho15f.destroy()
            self.vermelho16f.destroy()
            self.vermelho17f.destroy()
            self.vermelho18f.destroy()
            self.vermelho19f.destroy()
            self.vermelho20f.destroy()
            self.vermelho21f.destroy()
            self.vermelho22f.destroy()
            self.vermelho23f.destroy()
            self.vermelho24f.destroy()
            self.vermelho25f.destroy()
            self.vermelho26f.destroy()
            self.vermelho27f.destroy()
            self.vermelho28f.destroy()
            self.vermelho29f.destroy()
            self.vermelho30f.destroy()
            self.reservas.destroy()
            self.tablereservas.destroy()
            self.badicionarreserva.destroy()
            self.beditareserva.destroy()
            self.bremoverreserva.destroy()            
            self.bfuncionarios.destroy()
            self.bdespesas.destroy()
            self.tabela.destroy()
            self.imagemslogosalao.destroy()
            self.verde1f.destroy()
            
            
           
            
        except AttributeError:
            pass
        
        try:
            self.adm.configure(bg = "peru", fg = "black")
            self.bfuncionarios.destroy()
            self.bdespesas.destroy()
            self.blicensas.destroy()
            self.blogins.destroy()
            self.tablepromocoes.destroy()
            self.badicionarpromocao.destroy()
            self.beditarpromocao.destroy()
            self.bremoverpromocao.destroy()
            self.fundofinancas.destroy()
            self.tfaturamento.destroy()
            self.tbruta.destroy()
            self.tdespesas.destroy()
            self.tfuncionarios.destroy()
            self.tpedidos.destroy()
            self.totalmesas.destroy()
            self.treservas.destroy()
            self.gerenciamento.destroy()
            self.financas.destroy()
            self.promocoes.destroy()
            self.canvasmetas.destroy()
            self.metas.destroy()
            self.tablemetas.destroy()
            self.baddmetas.destroy()
            self.beditarmetas.destroy()
            self.bremovermetas.destroy()
        except:
            pass
        
        
        self.InventoryTitle = tk.Label(self.mainwindow, text = "Estoque:", bg = "sandy brown", font = ('verdana', 20))
        self.InventoryTitle.place(x = 1146, y = 100)
        
        self.Inventory = ttk.Treeview(self.mainwindow, columns = ("Produto", "Quantidade", "Data de Reposição"))
        self.Inventory.configure(height = 0)
        self.Inventory.heading('#0', text = 'ID')
        self.Inventory.heading('#1', text = 'Produto')
        self.Inventory.heading('#2', text = 'Quantidade')
        self.Inventory.heading('#3', text = 'Data de Reposição')
        self.Inventory.column('#0', anchor = 'center', width = 90)
        self.Inventory.column('#1', anchor = 'center', width = 120)
        self.Inventory.column('#2', anchor = 'center', width = 120)
        self.Inventory.column('#3', anchor = 'center', width = 120)
        self.Inventory.place(x = 1004, y = 150)
        
        self.InventoryEdit = tk.Button(self.mainwindow, text = "Editar estoque", bg = "peru", fg = "black", height = 2, width = 35, command = self.InventoryEditor)
        self.InventoryEdit.place(x = 1095, y = 700)
        
        self.InventoryAdd = tk.Button(self.mainwindow, text = 'Adicionar produto', bg = "peru", fg = "black", height = 2, width = 35, command = self.InventoryExpansion)
        self.InventoryAdd.place(x = 1095, y = 655)
        
        self.Reposition = tk.Button(self.mainwindow, text = 'Solicitar reposição', bg = 'peru', fg = "black", height = 2, width = 35, command = self.InventoryExpansion)
        self.Reposition.place(x = 1095, y = 745)
################################################################################        
        self.OrdersTitle = tk.Label(self.mainwindow, text = "Pedidos:", bg = "sandy brown", font = ('verdana', 20))
        self.OrdersTitle.place(x = 313, y = 100)
        
        self.OrdersTable = ttk.Treeview(self.mainwindow, columns = ("Mesa", "Pedido", "Preço Total", "Horario"))
        self.OrdersTable.configure(height = 0)
        self.OrdersTable.heading('#0', text = 'ID')
        self.OrdersTable.heading('#1', text = 'Mesa')
        self.OrdersTable.heading('#2', text = 'Pedido(s)')
        self.OrdersTable.heading('#3', text = 'Valor Total')
        self.OrdersTable.heading('#4', text = 'Horário')
        self.OrdersTable.column('#0', anchor = 'center', width = 70)
        self.OrdersTable.column('#1', anchor = 'center', width = 70)
        self.OrdersTable.column('#2', anchor = 'center', width = 330)
        self.OrdersTable.column('#3', anchor = 'center', width = 95)
        self.OrdersTable.column('#4', anchor = 'center', width = 90)
        self.OrdersTable.place(x = 40, y = 150)
        self.OrdersTable.tag_configure("Cor", background = "bisque2")
        
        self.PlaceOrder = tk.Button(self.mainwindow, text = "Registrar pedido", bg = "peru", fg = "black", height = 2, width = 35, command = self.MakeAnOrder)
        self.PlaceOrder.place(x = 258, y = 655)
        
        self.EditOrder = tk.Button(self.mainwindow, text = "Editar pedido", bg = "peru", fg = "black", height = 2, width = 35, command = self.EditAnOrder)
        self.EditOrder.place(x = 258, y = 700)
        
        self.RemoveOrder = tk.Button(self.mainwindow, text = "Remover pedido", bg = "peru", fg = "black", height = 2, width = 35, command = self.RemoveAnOrder)
        self.RemoveOrder.place(x = 258, y = 745)
    
        self.Foods = self.franquiaselecionada["Menu"]
        self.FoodList = ["Almôndegas", "Carpaccio", "Frango com arroz", "Lasanha", "Macarrão"]
        
        
        try:
            for i in self.franquiaselecionada["Pedidos"]:
                self.OrdersTable.insert("", 1, "" , text = str(i), values = (self.franquiaselecionada["Pedidos"][str(i)]["Mesa"], self.franquiaselecionada["Pedidos"][str(i)]["Pedido"], self.franquiaselecionada["Pedidos"][str(i)]["Preco"], self.franquiaselecionada["Pedidos"][str(i)]["Horario"]), tags = ("Cor"))
                self.OrdersTable.configure(height = len(self.OrdersTable.get_children()))
        except:
            pass
        
    def EditAnOrder(self):
        self.janelaeditarpedido = tk.Toplevel()
        self.janelaeditarpedido.wm_title("Editar Pedido")
        self.janelaeditarpedido.geometry("590x350")
        self.janelaeditarpedido.configure(bg = "sandy brown")
        self.idpedidoe = tk.Label(self.janelaeditarpedido, text = "ID: ", bg = "sandy brown", font = ("verdana", 10))
        self.idpedidoeentry = tk.Entry(self.janelaeditarpedido, bg = "peru")
        self.idpedidoe.place(x = 50, y = 40)
        self.idpedidoeentry.place(x = 190, y = 40)
        self.bselecionarpedidoe = tk.Button(self.janelaeditarpedido, bg = "peru", fg = "black", font = ("verdana", 10), text = "Selecionar ID", command = self.editarpedidoselecionado, height= 2, width = 20)
        self.bselecionarpedidoe.place(x = 110, y = 100)
        
    def editarpedidoselecionado(self):
        self.idpedidoe.destroy()
        self.bselecionarpedidoe.destroy()
        self.idpedidoeentry.place_forget()
        self.numeromesaepe = tk.Label(self.janelaeditarpedido, text = "Número da mesa: ", bg = "sandy brown", font = ("verdana",10))
        self.numeromesaentryepe = tk.Entry(self.janelaeditarpedido, bg = "peru")
        self.pedidoee = tk.Label(self.janelaeditarpedido, text = "Pedido: ", bg = "sandy brown", font = ("verdana", 10))
        self.FoodOrderOptionse = ttk.Combobox(self.janelaeditarpedido, values = self.FoodList, width = 17)
        self.FoodOrderOptionse.place(x=190,y=70)
        self.quantidadep = tk.Label(self.janelaeditarpedido, text = "Quantidade:", bg = "sandy brown", font = ("verdana", 10))
        self.quantidadep.place(x = 330, y = 70)
        self.FoodQuantitye = tk.Entry(self.janelaeditarpedido, bg = "peru")
        self.FoodQuantitye.place(x=430,y=70)
        self.horariope = tk.Label(self.janelaeditarpedido, text = "Horário: ", bg = "sandy brown", font = ("verdana", 10))
        self.horarioentryepe = tk.Entry(self.janelaeditarpedido, bg = "peru")
        self.numeromesaepe.place(x = 50, y = 40)
        self.numeromesaentryepe.place(x = 190, y = 40)
        self.pedidoee.place(x = 50, y = 70)
        self.horariope.place(x = 50, y = 100)
        self.horarioentryepe.place(x = 190, y = 100)
        
        self.FoodOrderOptionse.set(self.franquiaselecionada["Pedidos"][self.idpedidoeentry.get()]["Pedido"])
        self.FoodQuantitye.insert(0, self.franquiaselecionada["Pedidos"][self.idpedidoeentry.get()]["Quantidade"])
        self.numeromesaentryepe.insert(0, self.franquiaselecionada["Pedidos"][self.idpedidoeentry.get()]["Mesa"])
        self.horarioentryepe.insert(0, self.franquiaselecionada["Pedidos"][self.idpedidoeentry.get()]["Horario"])
        self.binserirpedidoe = tk.Button(self.janelaeditarpedido, bg = "peru", fg = "black", font = ("verdana", 10), text = "Adicionar", command = self.inserirpedidoeditado, height= 2, width = 20)
        self.bcancelarinserirpedidoe = tk.Button(self.janelaeditarpedido, bg = "peru", fg = "black", font = ("verdana", 10), text = "Cancelar", command = self.cancelarinserirpedidoeditado, height= 2, width = 20)
        self.bcancelarinserirpedidoe.place(x=75, y= 250 )
        self.binserirpedidoe.place(x =290, y = 250)
        
    def cancelarinserirpedidoeditado(self):
        self.janelaeditarpedido.destroy()
    def inserirpedidoeditado(self):
        self.franquiaselecionada["Pedidos"][str(self.idpedidoeentry.get())] = {'Mesa': self.numeromesaentryepe.get(),'Pedido': self.FoodList[self.FoodOrderOptionse.current()], 'Preco': int(self.Foods[self.FoodList[self.FoodOrderOptionse.current()]])*int(self.FoodQuantitye.get()), 'Horario': self.horarioentryepe.get(), "Quantidade": self.FoodQuantitye.get()}
        firebase.patch(self.selecionada, self.franquiaselecionada)     
        try:
            self.OrdersTable.delete(*self.OrdersTable.get_children())
            for i in self.franquiaselecionada["Pedidos"]:
                self.OrdersTable.insert("", 1, "" , text = str(i), values = (self.franquiaselecionada["Pedidos"][str(i)]["Mesa"], self.franquiaselecionada["Pedidos"][str(i)]["Pedido"], self.franquiaselecionada["Pedidos"][str(i)]["Preco"], self.franquiaselecionada["Pedidos"][str(i)]["Horario"]), tags = ("Cor"))
                self.OrdersTable.configure(height = len(self.OrdersTable.get_children()))
        except:
            pass
        
        self.janelaeditarpedido.destroy()
    
    def MakeAnOrder (self):
        self.OrderWindow = tk.Toplevel()
        self.OrderWindow.wm_title("Registrar Pedido")
        self.OrderWindow.geometry("550x350")
        self.OrderWindow.configure(bg = "sandy brown")
        
#        self.OrderID = tk.Label(self.OrderWindow, text = "ID do Pedido: ", bg = "sandy brown", font = ("verdana",10))
#        self.OrderIDEntry = tk.Entry(self.OrderWindow, bg = "peru")
        
        self.TableNumber = tk.Label(self.OrderWindow, text = "Mesa: ", bg = "sandy brown", font = ("verdana", 10))
        self.TableNumberEntry = tk.Entry(self.OrderWindow, bg = "peru")
        
        self.OrderTime = tk.Label(self.OrderWindow, text = "Horário: ", bg = "sandy brown", font = ("verdana", 10))
        self.OrderTimeEntry = tk.Entry(self.OrderWindow, bg = "peru")
        
#        self.OrderID.place(x = 50, y = 40)
#        self.OrderIDEntry.place(x = 190, y = 40)
        
        self.TableNumber.place(x = 50, y = 70)
        self.TableNumberEntry.place(x = 130, y = 70)
        
        self.OrderTime.place(x = 50, y = 130)
        self.OrderTimeEntry.place(x = 130, y = 130)
        self.comida = tk.Label(self.OrderWindow, text = "Prato:", bg = "sandy brown", font = ("verdana", 10))
        self.comida.place(x = 50, y = 100)
        self.FoodOrderOptions = ttk.Combobox(self.OrderWindow, values = self.FoodList, width = 17)
        self.FoodOrderOptions.place(x=129,y=99)
        self.quantidade = tk.Label(self.OrderWindow, text = "Quantidade:", bg = "sandy brown", font = ("verdana", 10))
        self.quantidade.place(x = 270, y = 100)
        self.FoodQuantity = tk.Entry(self.OrderWindow, bg = "peru")
        self.FoodQuantity.place(x=380,y=100)
        
        self.bCancelOrder = tk.Button(self.OrderWindow, bg = "peru", fg = "black", font = ("verdana", 10), text = "Cancelar", command = self.CancelOrder, height= 2, width = 20)
        self.bCancelOrder.place(x=75, y= 250)
        
        self.OrderConfirmation = tk.Button(self.OrderWindow, bg = "peru", fg = "black", font = ("verdana", 10), text = "Confirmar Pedido", command = self.ConfirmOrder, height= 2, width = 20)
        self.OrderConfirmation.place(x =290, y = 250)
        
        
    def ConfirmOrder(self):  
        self.OrdersTable.tag_configure("Cor", background = "bisque2")
        self.franquiaselecionada["Dados"]["NPedidos"] += 1
        self.numerop = self.franquiaselecionada["Dados"]["NPedidos"]
        self.franquiaselecionada["Pedidos"][str(self.numerop)] = {'Mesa': self.TableNumberEntry.get(),'Pedido': self.FoodList[self.FoodOrderOptions.current()], 'Preco': int(self.Foods[self.FoodList[self.FoodOrderOptions.current()]])*int(self.FoodQuantity.get()), 'Horario': self.OrderTimeEntry.get(), "Quantidade": self.FoodQuantity.get()}
        self.OrdersTable.insert("", 1, "" , text = str(self.numerop), values = (self.franquiaselecionada["Pedidos"][str(self.numerop)]["Mesa"], self.franquiaselecionada["Pedidos"][str(self.numerop)]["Pedido"], self.franquiaselecionada["Pedidos"][str(self.numerop)]["Preco"], self.franquiaselecionada["Pedidos"][str(self.numerop)]["Horario"]), tags = ("Cor"))
        self.OrdersTable.configure(height = len(self.OrdersTable.get_children()))
        firebase.patch(self.selecionada, self.franquiaselecionada)
        
        self.OrderWindow.destroy()
        
    def CancelOrder(self):
        self.OrderWindow.destroy()
        
    
    def CancelationOfRemoval(self):
        self.RemovedOrder.destroy()
        self.RemovedOrderEntry.destroy()
        self.OrderRemovalCancelation.destroy()
        self.OrderRemovalConfirmation.destroy()
        
    def RemovalConfirmation(self):
        del self.franquiaselecionada["Pedidos"][self.nomepedidorentry.get()]
        firebase.patch(self.selecionada, self.franquiaselecionada)
        self.OrdersTable.delete(*self.OrdersTable.get_children())
        try:
            for i in self.franquiaselecionada["Pedidos"]:
                self.OrdersTable.insert("", 1, "" , text = str(i), values = (self.franquiaselecionada["Pedidos"][str(i)]["Mesa"], self.franquiaselecionada["Pedidos"][str(i)]["Pedido"], self.franquiaselecionada["Pedidos"][str(i)]["Preco"], self.franquiaselecionada["Pedidos"][str(i)]["Horario"]), tags = ("Cor"))
                self.OrdersTable.configure(height = len(self.OrdersTable.get_children()))
        except:
            pass
        self.janelarpedido.destroy()
        
    def RemoveAnOrder(self):
        self.janelarpedido = tk.Toplevel()
        self.janelarpedido.wm_title("Remover pedido")
        self.janelarpedido.geometry("400x300")
        self.janelarpedido.configure(bg = "sandy brown")
        self.nomepedidor = tk.Label(self.janelarpedido, text = "ID: ", bg = "sandy brown", font = ("verdana", 10))
        self.nomepedidorentry = tk.Entry(self.janelarpedido, bg = "peru")
        self.nomepedidor.place(x = 50, y = 40)
        self.nomepedidorentry.place(x = 190, y = 40)
        self.bremoverpedido = tk.Button(self.janelarpedido, bg = "peru", fg = "black", text = "Remover pedido", command = self.RemovalConfirmation, height= 2, width = 40)
        self.bremoverpedido.place(x = 55, y = 225)
    def NoFunctionLeft(self):
        None
        
    def InventoryEditor(self):
        pass
    def InventoryExpansion(self):
        pass
fd = FoodTools()
fd.comeco()

    

