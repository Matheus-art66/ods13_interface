from tkinter import *
from tkinter import messagebox
from collections import deque

acoes = []
fila = deque()
emissao_co2 = [         
    [12.1, 13.0, 11.4],
    [9.8, 10.5, 8.9],
    [14.2, 15.0, 13.7]
]


class Aplication():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.widgets_frame2()
        root.mainloop()

    def tela(self):
        self.root.title('ODS 13 - Sustentabilidade')
        self.root.configure(background='#1e3743')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=5)
        self.frame_1.place(relx=0.02, rely=0.04, relwidth=0.96, relheight=0.45)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=5)
        self.frame_2.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.45)

    def mostrar_emissao(self):
        regioes = ["Norte", "Sul", "Centro"]
        texto = ""
        for i, regiao in enumerate(emissao_co2):
            texto += f"{regioes[i]}: {regiao}\n"
        messagebox.showinfo("Emissão de CO₂", texto)    

    def widgets_frame1(self):
        self.lb_acao = Label(self.frame_1, text="Ação Sustentável:", bg='#dfe3ee')
        self.lb_acao.place(x=10, y=10)
        self.entry_acao = Entry(self.frame_1, width=40)
        self.entry_acao.place(x=130, y=10)

        self.btn_add = Button(self.frame_1, text="Cadastrar", command=self.adicionar_acao)
        self.btn_add.place(x=130, y=40)


    def widgets_frame2(self):
        # Visualizar ações
        self.btn_ver = Button(self.frame_2, text="Ver Ações Cadastradas", command=self.mostrar_acoes)
        self.btn_ver.place(x=10, y=10)

        self.btn_emicao = Button(self.frame_2, text="Ver Emissão de CO₂",  command=self.mostrar_emissao)
        self.btn_emicao.place(x=200, y =10)

    def adicionar_acao(self):
        acao = self.entry_acao.get()
        if acao:
            acoes.append(acao)
            messagebox.showinfo("Sucesso", "Ação adicionada!")
            self.entry_acao.delete(0, END)
        else:
            messagebox.showwarning("Erro", "Digite uma ação válida.")

    def mostrar_acoes(self):
        if acoes:
            texto = "\n".join(acoes)
            messagebox.showinfo("Ações", texto)
        else:
            messagebox.showinfo("Ações", "Nenhuma ação cadastrada.")

root = Tk()
Aplication()