from PyQt5 import uic, QtWidgets
import files_rc
import mysql.connector
from datetime import datetime
from mysql.connector import Error
from mysql.connector.locales.eng import client_error

app = QtWidgets.QApplication([])
login = uic.loadUi("login.ui")
cadastro = uic.loadUi("cadastro.ui")
opcoesacoes = uic.loadUi("opcoesacoes.ui")
bairros = uic.loadUi("bairros.ui")
lista = uic.loadUi("lista.ui")
opcoesver = uic.loadUi("opcoesver.ui")
bairros2 = uic.loadUi("bairros2.ui")
listaedit = uic.loadUi("listaedit.ui")
bairros3 = uic.loadUi("bairros3.ui")
menueditar = uic.loadUi("menu_editar.ui")
erro = uic.loadUi("erro.ui")
listavereador = uic.loadUi("listavereador.ui")
total = uic.loadUi("total.ui")
variavelerro = False
login.show()

try:
    banco = mysql.connector.connect(
        user="gabineteregi@gabinete",
        password="vereador10!",
        host="gabinete.mysql.database.azure.com",
        port="3306",
        database="cadastro_eleitores", )
except Error as e:
    login.hide()
    erro.show()
    erro.botao_ok.clicked.connect(app.quit)
    erro.botao_cancelar.clicked.connect(app.quit)



data_e_hora_atuais = datetime.now()
data = data_e_hora_atuais.strftime('%d/%m/%Y') + '-'
datasql= data_e_hora_atuais.strftime('%Y-%m-%d')
datamesatuais = datetime.now()
datames = data_e_hora_atuais.strftime('%m')
dataanoatuais = datetime.now
dataano = data_e_hora_atuais.strftime('%Y')
numero_id = 0
assuntoanterior = 0


def chamar_erro():
    global variavelerro
    variavelerro = True

loginsenhaver={"Regi":"123456"}
loginsenha= {"WillMoraes":"85200053w"}

def chamar_opcoes():
    if login.barra_login.text() in loginsenha and login.barra_senha.text() == loginsenha[login.barra_login.text()]:
        text = "Login Ok"
        login.label_erro.setText(text)
        opcoesacoes.show()
        login.close()
    elif login.barra_login.text() in loginsenhaver and login.barra_senha.text() == loginsenhaver[login.barra_login.text()]:
        text = "Login Ok"
        login.label_erro.setText(text)
        opcoesver.show()
        login.close()
    else:
        text = "Login ou Senha incorreta."
        login.msg_erro.show()
        login.label_erro.setText(text)


bairro = ""


def artur1():
    global bairro
    bairro = "Artur Lundgren 1"
    cadastro.show()


def artur2():
    global bairro
    bairro = "Artur Lundgren 2"
    cadastro.show()


def aurora():
    global bairro
    bairro = "Aurora"
    cadastro.show()


def centro():
    global bairro
    bairro = "Centro"
    cadastro.show()


def engenhoM():
    global bairro
    bairro = "Engenho Maranguape"
    cadastro.show()


def fragoso():
    global bairro
    bairro = "Fragoso"
    cadastro.show()


def jaguarana():
    global bairro
    bairro = "Jaguarana"
    cadastro.show()


def jaguaribe():
    global bairro
    bairro = "Jaguaribe"
    cadastro.show()


def janga():
    global bairro
    bairro = "Janga"
    cadastro.show()


def jardimm():
    global bairro
    bairro = "Jardim Maranguape"
    cadastro.show()


def jardimp():
    global bairro
    bairro = "Jardim Paulista"
    cadastro.show()


def m1():
    global bairro
    bairro = "Maranguape 1"
    cadastro.show()


def m2():
    global bairro
    bairro = "Maranguape 2"
    cadastro.show()


def mf():
    global bairro
    bairro = "Maria Farinha"
    cadastro.show()

def mirueira():
    global bairro
    bairro = "Mirueira"
    cadastro.show()

def nobre():
    global bairro
    bairro = "Nobre"
    cadastro.show()


def nossaC():
    global bairro
    bairro = "Nossa Senhora da Conceição"
    cadastro.show()


def nossaO():
    global bairro
    bairro = "Nossa Senhora do Ó"
    cadastro.show()


def paratibe():
    global bairro
    bairro = "Paratibe"
    cadastro.show()


def pauamarelo():
    global bairro
    bairro = "Pau Amarelo"
    cadastro.show()


def poty():
    global bairro
    bairro = "Poty"
    cadastro.show()


def tabajara():
    global bairro
    bairro = "Tabajara"
    cadastro.show()


def vilaT():
    global bairro
    bairro = "Vila Torres Galvão"
    cadastro.show()


def outros():
    global bairro
    bairro = "Outros"
    cadastro.show()


######################################pesquisa###############################################
def artur1p():
    global bairro
    bairro = "Artur Lundgren 1"
    lista.show()

    chamar_lista()


def artur2p():
    global bairro
    bairro = "Artur Lundgren 2"
    lista.show()

    chamar_lista()


def aurorap():
    global bairro
    bairro = "Aurora"
    lista.show()

    chamar_lista()


def centrop():
    global bairro
    bairro = "Centro"
    lista.show()

    chamar_lista()


def engenhoMp():
    global bairro
    bairro = "Engenho Maranguape"
    lista.show()

    chamar_lista()


def fragosop():
    global bairro
    bairro = "Fragoso"
    lista.show()

    chamar_lista()


def jaguaranap():
    global bairro
    bairro = "Jaguarana"
    lista.show()

    chamar_lista()


def jaguaribep():
    global bairro
    bairro = "Jaguaribe"
    lista.show()

    chamar_lista()


def jangap():
    global bairro
    bairro = "Janga"
    lista.show()

    chamar_lista()


def jardimmp():
    global bairro
    bairro = "Jardim Maranguape"
    lista.show()

    chamar_lista()


def jardimpp():
    global bairro
    bairro = "Jardim Paulista"
    lista.show()

    chamar_lista()


def m1p():
    global bairro
    bairro = "Maranguape 1"
    lista.show()

    chamar_lista()


def m2p():
    global bairro
    bairro = "Maranguape 2"
    lista.show()

    chamar_lista()


def mfp():
    global bairro
    bairro = "Maria Farinha"
    lista.show()

    chamar_lista()

def mirueirap():
    global bairro
    bairro = "Mirueira"
    lista.show()

    chamar_lista()

def nobrep():
    global bairro
    bairro = "Nobre"
    lista.show()

    chamar_lista()


def nossaCp():
    global bairro
    bairro = "Nossa Senhora da Conceição"
    lista.show()

    chamar_lista()


def nossaOp():
    global bairro
    bairro = "Nossa Senhora do Ó"
    lista.show()

    chamar_lista()


def paratibep():
    global bairro
    bairro = "Paratibe"
    lista.show()

    chamar_lista()


def pauamarelop():
    global bairro
    bairro = "Pau Amarelo"
    lista.show()

    chamar_lista()


def potyp():
    global bairro
    bairro = "Poty"
    lista.show()

    chamar_lista()


def tabajarap():
    global bairro
    bairro = "Tabajara"
    lista.show()

    chamar_lista()


def vilaTp():
    global bairro
    bairro = "Vila Torres Galvão"
    lista.show()

    chamar_lista()


def outrosp():
    global bairro
    bairro = "Outros"
    lista.show()

    chamar_lista()


#########################################################################################################################
def artur1pe():
    global bairro
    bairro = "Artur Lundgren 1"
    chamar_listaedit()


def artur2pe():
    global bairro
    bairro = "Artur Lundgren 2"
    chamar_listaedit()


def aurorape():
    global bairro
    bairro = "Aurora"
    chamar_listaedit()


def centrope():
    global bairro
    bairro = "Centro"
    chamar_listaedit()


def engenhoMpe():
    global bairro
    bairro = "Engenho Maranguape"
    chamar_listaedit()


def fragosope():
    global bairro
    bairro = "Fragoso"
    chamar_listaedit()


def jaguaranape():
    global bairro
    bairro = "Jaguarana"
    chamar_listaedit()


def jaguaribepe():
    global bairro
    bairro = "Jaguaribe"
    chamar_listaedit()


def jangape():
    global bairro
    bairro = "Janga"
    chamar_listaedit()


def jardimmpe():
    global bairro
    bairro = "Jardim Maranguape"
    chamar_listaedit()


def jardimppe():
    global bairro
    bairro = "Jardim Paulista"
    chamar_listaedit()


def m1pe():
    global bairro
    bairro = "Maranguape 1"
    chamar_listaedit()


def m2pe():
    global bairro
    bairro = "Maranguape 2"
    chamar_listaedit()


def mfpe():
    global bairro
    bairro = "Maria Farinha"
    chamar_listaedit()

def mirueirape():
    global bairro
    bairro = "Mirueira"
    chamar_listaedit()


def nobrepe():
    global bairro
    bairro = "Nobre"
    chamar_listaedit()


def nossaCpe():
    global bairro
    bairro = "Nossa Senhora da Conceição"
    chamar_listaedit()


def nossaOpe():
    global bairro
    bairro = "Nossa Senhora do Ó"
    chamar_listaedit()


def paratibepe():
    global bairro
    bairro = "Paratibe"
    chamar_listaedit()


def pauamarelope():
    global bairro
    bairro = "Pau Amarelo"
    chamar_listaedit()


def potype():
    global bairro
    bairro = "Poty"
    chamar_listaedit()


def tabajarape():
    global bairro
    bairro = "Tabajara"
    chamar_listaedit()


def vilaTpe():
    global bairro
    bairro = "Vila Torres Galvão"
    chamar_listaedit()


def outrospe():
    global bairro
    bairro = "Outros"
    chamar_listaedit()


def chamar_bairro():
    bairros.show()


def chamar_bairrolista():
    bairros2.show()


def chamar_bairro3():
    bairros3.show()


def salvar_eleitor():
    global bairro
    global datames
    global dataano
    nome = cadastro.barra_nome.text()
    cpf = cadastro.barra_cpf.text()
    telefone = cadastro.barra_telefone.text()
    rua = cadastro.barra_rua.text()
    complemento = cadastro.barra_complemento.text()
    assunto = data + cadastro.barra_ass.toPlainText()
    try:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO eleitores (nome,cpf,telefone,cadastrodata, bairro, rua, complemento,assunto,mes,ano) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        dados = (
        str(nome), str(cpf), str(telefone),str(datasql), str(bairro), str(rua), str(complemento), str(assunto), str(datames),
        str(dataano, ))
        cursor.execute(comando_SQL, dados)
        comando_SQL1 = "INSERT INTO atendidos (mes, ano) VALUES (%s,%s)"
        mesatendidos = (str(datames), str(dataano),)
        cursor.execute(comando_SQL1, (mesatendidos), )
        banco.commit()
        cadastro.barra_nome.setText("")
        cadastro.barra_cpf.setText("")
        cadastro.barra_telefone.setText("")
        cadastro.barra_rua.setText("")
        cadastro.barra_complemento.setText("")
        cadastro.barra_ass.clear()
        cadastro.msg_erro.show()
    except Error as e:
        cadastro.msg_erro.show()
        cadastro.label_erro.setText("Erro: "+ str(e))


mespesq = ""
dictmes = {"Todos": "*", "Selecione um Mês": "*", "Janeiro": "01", "Fevereiro": "02", "Março": "03", "Abril": "04",
           "Maio": "05", "Junho": "06",
           "Julho": "07",
           "Agosto": "08", "Setembro": "09", "Outubro": "10", "Novembro": "11", "Dezembro": "12"}
dictano = {"Todos": "*", "Selecione o Ano": "*", "2021": "2021", "2022": "2022"}
dictordem={"Qualquer":"*","Selecione a Ordem":"*","Crescente":"ORDER BY cadastrodata ASC","Decrescente":"ORDER BY cadastrodata DESC"}

def pesquisarlista():
    global bairro
    global mespesq
    lista.hide()
    pesquisames = lista.comboBox.currentText()
    pesquisaano = lista.comboBox_2.currentText()
    pesquisaordem=lista.comboBox_3.currentText()
    ordempesq= dictordem[pesquisaordem]
    anopesq = dictano[pesquisaano]
    mespesq = dictmes[pesquisames]
    lista.show()
    nomepesq = lista.lineEdit.text()
    if nomepesq != "" and mespesq == "*" and anopesq == "*" and ordempesq=="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND nome LIKE '%{}%'".format(str(nomepesq))
            bairrosS = (str(bairro),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq != "" and mespesq != "*" and anopesq != "*" and ordempesq=="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND ano= %s AND mes= %s AND nome LIKE '%{}%'".format(
                str(nomepesq))
            bairrosS = (str(bairro), str(anopesq), str(mespesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)
    if nomepesq != "" and mespesq != "*" and anopesq == "*" and ordempesq=="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s  AND mes= %s AND nome LIKE '%{}%'".format(
                str(nomepesq))
            bairrosS = (str(bairro), str(mespesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq == "" and mespesq != "*" and anopesq == "*" and ordempesq=="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND mes=%s"
            bairrosS = (str(bairro), str(mespesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq == "" and mespesq == "*" and anopesq != "*" and ordempesq=="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND ano= %s"
            bairrosS = (str(bairro), str(anopesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq != "" and mespesq == "*" and anopesq != "*" and ordempesq=="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND ano= %s AND nome LIKE '%{}%'".format(
                str(nomepesq))
            bairrosS = (str(bairro), str(anopesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)
    if nomepesq == "" and mespesq == "*" and anopesq == "*" and ordempesq=="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s"
            bairrosS = (str(bairro),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)
    if nomepesq == "" and mespesq == "*" and anopesq == "*" and ordempesq!="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s "+ordempesq
            bairrosS = (str(bairro),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)



    if nomepesq == "" and mespesq == "*" and anopesq != "*" and ordempesq!="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND ano=%s "+ordempesq
            bairrosS = (str(bairro),anopesq,)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)
    if nomepesq == "" and mespesq != "*" and anopesq != "*" and ordempesq!="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND ano=%s AND mes=%s "+ordempesq
            bairrosS = (str(bairro),str(anopesq),str(mespesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq != "" and mespesq != "*" and anopesq != "*" and ordempesq!="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND ano=%s AND mes=%s AND nome LIKE '%{}%' ".format(str(nomepesq))+ordempesq
            bairrosS = (str(bairro),str(anopesq),str(mespesq))
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq != "" and mespesq != "*" and anopesq == "*" and ordempesq!="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s  AND mes=%s AND nome LIKE '%{}%' ".format(str(nomepesq))+ordempesq
            bairrosS = (str(bairro),str(mespesq))
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq != "" and mespesq == "*" and anopesq != "*" and ordempesq!="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s  AND ano=%s AND nome LIKE '%{}%' ".format(str(nomepesq))+ordempesq
            bairrosS = (str(bairro),str(anopesq))
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq != "" and mespesq == "*" and anopesq == "*" and ordempesq!="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s  AND nome LIKE '%{}%' ".format(str(nomepesq))+ordempesq
            bairrosS = (str(bairro),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)


    if nomepesq == "" and mespesq != "*" and anopesq == "*" and ordempesq!="*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND mes=%s "+ordempesq
            bairrosS = (str(bairro),str(mespesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            lista.lista.setRowCount(len(dados_lidos))
            lista.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            lista.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

def pesquisarlistaedit():
    global bairro
    global mespesq
    listaedit.hide()
    pesquisames =listaedit.comboBox.currentText()
    pesquisaano =listaedit.comboBox_2.currentText()
    pesquisaordem =listaedit.comboBox_3.currentText()
    ordempesq = dictordem[pesquisaordem]
    anopesq = dictano[pesquisaano]
    mespesq = dictmes[pesquisames]
    listaedit.show()
    nomepesq =listaedit.lineEdit.text()
    if nomepesq != "" and mespesq == "*" and anopesq == "*" and ordempesq == "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND nome LIKE '%{}%'".format(str(nomepesq))
            bairrosS = (str(bairro),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq != "" and mespesq != "*" and anopesq != "*" and ordempesq == "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND ano= %s AND mes= %s AND nome LIKE '%{}%'".format(
                str(nomepesq))
            bairrosS = (str(bairro), str(anopesq), str(mespesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)
    if nomepesq != "" and mespesq != "*" and anopesq == "*" and ordempesq == "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s  AND mes= %s AND nome LIKE '%{}%'".format(
                str(nomepesq))
            bairrosS = (str(bairro), str(mespesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq == "" and mespesq != "*" and anopesq == "*" and ordempesq == "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND mes=%s"
            bairrosS = (str(bairro), str(mespesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq == "" and mespesq == "*" and anopesq != "*" and ordempesq == "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND ano= %s"
            bairrosS = (str(bairro), str(anopesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq != "" and mespesq == "*" and anopesq != "*" and ordempesq == "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND ano= %s AND nome LIKE '%{}%'".format(
                str(nomepesq))
            bairrosS = (str(bairro), str(anopesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)
    if nomepesq == "" and mespesq == "*" and anopesq == "*" and ordempesq == "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s"
            bairrosS = (str(bairro),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)
    if nomepesq == "" and mespesq == "*" and anopesq == "*" and ordempesq != "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s "+ordempesq
            bairrosS = (str(bairro),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq == "" and mespesq == "*" and anopesq != "*" and ordempesq != "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND ano=%s "+ordempesq
            bairrosS = (str(bairro), str(anopesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)
    if nomepesq == "" and mespesq != "*" and anopesq != "*" and ordempesq != "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND ano=%s AND mes=%s "+ordempesq
            bairrosS = (str(bairro), str(anopesq), str(mespesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq != "" and mespesq != "*" and anopesq != "*" and ordempesq != "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s AND ano=%s AND mes=%s AND nome LIKE '%{}%' ".format(str(nomepesq))+ordempesq
            bairrosS = (str(bairro), str(anopesq), str(mespesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq != "" and mespesq != "*" and anopesq == "*" and ordempesq != "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s  AND mes=%s AND nome LIKE '%{}%' ".format(str(nomepesq))+ordempesq
            bairrosS = (str(bairro), str(mespesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq != "" and mespesq == "*" and anopesq != "*" and ordempesq != "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s  AND ano=%s AND nome LIKE '%{}%' ".format(str(nomepesq))+ordempesq
            bairrosS = (str(bairro), str(anopesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq != "" and mespesq == "*" and anopesq == "*" and ordempesq != "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s  AND nome LIKE '%{}%' ".format(str(nomepesq))+ordempesq
            bairrosS = (str(bairro),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)

    if nomepesq == "" and mespesq != "*" and anopesq == "*" and ordempesq != "*":
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s  AND mes=%s "+ordempesq
            bairrosS = (str(bairro), str(mespesq),)
            cursor.execute(comando_SQL, bairrosS)
            dados_lidos = cursor.fetchall()
            listaedit.lista.setRowCount(len(dados_lidos))
            listaedit.lista.setColumnCount(9)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 9):
                    listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        except Error:
            erro.show()
            listaedit.hide()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)


def chamar_lista():
    global bairro
    global datames
    global dataano
    lista.show()

    try:
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s"
        bairrosS = (str(bairro),)
        cursor.execute(comando_SQL, bairrosS)
        dados_lidos = cursor.fetchall()
        lista.lista.setRowCount(len(dados_lidos))
        lista.lista.setColumnCount(9)
        for i in range(0, len(dados_lidos)):
            for j in range(0, 9):
                lista.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    except Error as e:
        erro.show()
        lista.hide()
        erro.botao_ok.clicked.connect(erro.hide)
        erro.botao_cancelar.clicked.connect(erro.hide)


def chamar_listaedit():
    global bairro
    listaedit.show()
    try:
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM eleitores WHERE bairro = %s"
        bairrosS = (str(bairro),)
        cursor.execute(comando_SQL, bairrosS)
        dados_lidos = cursor.fetchall()
        listaedit.lista.setRowCount(len(dados_lidos))
        listaedit.lista.setColumnCount(9)
        for i in range(0, len(dados_lidos)):
            for j in range(0, 9):
                listaedit.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    except Error as e:
        erro.show()
        listaedit.hide()
        erro.botao_ok.clicked.connect(erro.hide)
        erro.botao_cancelar.clicked.connect(erro.hide)


def chamar_telaedit():
    global bairro
    global numero_id
    global assuntoanterior
    try:
        linha = listaedit.lista.currentRow()
        cursor = banco.cursor()
        comando_SQL = "SELECT id FROM eleitores WHERE bairro = %s"
        bairrosS = (str(bairro),)
        cursor.execute(comando_SQL, bairrosS)
        dados_lidos = cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("SELECT * FROM eleitores WHERE id=" + str(valor_id))
        eleitores = cursor.fetchall()
        menueditar.show()

        numero_id = valor_id

        menueditar.label.setText(str(eleitores[0][1]))
        menueditar.label_2.setText(str(eleitores[0][2]))
        menueditar.label_3.setText(str(eleitores[0][3]))
        menueditar.label_15.setText(str(eleitores[0][4]))
        menueditar.label_4.setText(str(eleitores[0][6]))
        menueditar.label_5.setText(str(eleitores[0][7]))
        menueditar.label_6.setText(str(eleitores[0][8]))
        menueditar.barra_nome.setText(str(eleitores[0][1]))
        menueditar.barra_cpf.setText(str(eleitores[0][2]))
        menueditar.barra_telefone.setText(str(eleitores[0][3]))
        menueditar.barra_rua.setText(str(eleitores[0][6]))
        menueditar.barra_complemento.setText(str(eleitores[0][7]))
        assuntoanterior = menueditar.label_6.text()
        assuntoanterior = str(assuntoanterior)
    except Error as e:
        erro.show()
        menueditar.hide()
        erro.botao_ok.clicked.connect(erro.hide)
        erro.botao_cancelar.clicked.connect(erro.hide)


def chamartotal():
    total.show()
    try:
        cursor = banco.cursor()
        jan="01"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2021"
        mesesS1 = (str(jan),)
        cursor.execute(comando_SQL, mesesS1)
        janeiro = cursor.fetchone()[0]
        total.jan.setText(str(janeiro))

        cursor = banco.cursor()
        fev="02"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2021"
        mesesS2 = (str(fev),)
        cursor.execute(comando_SQL, mesesS2)
        fevereiro = cursor.fetchone()[0]
        total.fev.setText(str(fevereiro))

        cursor = banco.cursor()
        mar="03"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2021"
        mesesS3 = (str(mar),)
        cursor.execute(comando_SQL, mesesS3)
        março = cursor.fetchone()[0]
        total.mar.setText(str(março))

        cursor = banco.cursor()
        abr="04"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2021"
        mesesS4 = (str(abr),)
        cursor.execute(comando_SQL, mesesS4)
        abril = cursor.fetchone()[0]
        total.abr.setText(str(abril))

        cursor = banco.cursor()
        mai="05"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2021"
        mesesS5 = (str(mai),)
        cursor.execute(comando_SQL, mesesS5)
        maio = cursor.fetchone()[0]
        total.mai.setText(str(maio))

        cursor = banco.cursor()
        jun="06"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2021"
        mesesS6 = (str(jun),)
        cursor.execute(comando_SQL, mesesS6)
        junho = cursor.fetchone()[0]
        total.jun.setText(str(junho))

        cursor = banco.cursor()
        jul="07"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2021"
        mesesS7 = (str(jul),)
        cursor.execute(comando_SQL, mesesS7)
        julho = cursor.fetchone()[0]
        total.jul.setText(str(julho))

        cursor = banco.cursor()
        ago="08"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2021"
        mesesS8 = (str(ago),)
        cursor.execute(comando_SQL, mesesS8)
        agosto = cursor.fetchone()[0]
        total.ago.setText(str(agosto))

        cursor = banco.cursor()
        set="09"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2021"
        mesesS9 = (str(set),)
        cursor.execute(comando_SQL, mesesS9)
        setembro = cursor.fetchone()[0]
        total.set.setText(str(setembro))

        cursor = banco.cursor()
        out="10"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2021"
        mesesS10 = (str(out),)
        cursor.execute(comando_SQL, mesesS10)
        outubro = cursor.fetchone()[0]
        total.out.setText(str(outubro))

        cursor = banco.cursor()
        nov="11"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2021"
        mesesS11 = (str(nov),)
        cursor.execute(comando_SQL, mesesS11)
        novembro = cursor.fetchone()[0]
        total.nov.setText(str(novembro))

        cursor = banco.cursor()
        dez="12"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2021"
        mesesS12 = (str(dez),)
        cursor.execute(comando_SQL, mesesS12)
        dezembro = cursor.fetchone()[0]
        total.dez.setText(str(dezembro))

        cursor = banco.cursor()
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE ano= 2021"
        cursor.execute(comando_SQL)
        totalatendidos = cursor.fetchone()[0]
        total.total.setText(str(totalatendidos))

        cursor = banco.cursor()
        jan = "01"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2022"
        mesesS1 = (str(jan),)
        cursor.execute(comando_SQL, mesesS1)
        janeiro = cursor.fetchone()[0]
        total.jan_2.setText(str(janeiro))

        cursor = banco.cursor()
        fev = "02"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2022"
        mesesS2 = (str(fev),)
        cursor.execute(comando_SQL, mesesS2)
        fevereiro = cursor.fetchone()[0]
        total.fev_2.setText(str(fevereiro))

        cursor = banco.cursor()
        mar = "03"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2022"
        mesesS3 = (str(mar),)
        cursor.execute(comando_SQL, mesesS3)
        março = cursor.fetchone()[0]
        total.mar_2.setText(str(março))

        cursor = banco.cursor()
        abr = "04"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2022"
        mesesS4 = (str(abr),)
        cursor.execute(comando_SQL, mesesS4)
        abril = cursor.fetchone()[0]
        total.abr_2.setText(str(abril))

        cursor = banco.cursor()
        mai = "05"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2022"
        mesesS5 = (str(mai),)
        cursor.execute(comando_SQL, mesesS5)
        maio = cursor.fetchone()[0]
        total.mai_2.setText(str(maio))

        cursor = banco.cursor()
        jun = "06"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2022"
        mesesS6 = (str(jun),)
        cursor.execute(comando_SQL, mesesS6)
        junho = cursor.fetchone()[0]
        total.jun_2.setText(str(junho))

        cursor = banco.cursor()
        jul = "07"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2022"
        mesesS7 = (str(jul),)
        cursor.execute(comando_SQL, mesesS7)
        julho = cursor.fetchone()[0]
        total.jul_2.setText(str(julho))

        cursor = banco.cursor()
        ago = "08"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2022"
        mesesS8 = (str(ago),)
        cursor.execute(comando_SQL, mesesS8)
        agosto = cursor.fetchone()[0]
        total.ago_2.setText(str(agosto))

        cursor = banco.cursor()
        set = "09"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2022"
        mesesS9 = (str(set),)
        cursor.execute(comando_SQL, mesesS9)
        setembro = cursor.fetchone()[0]
        total.set_2.setText(str(setembro))

        cursor = banco.cursor()
        out = "10"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2022"
        mesesS10 = (str(out),)
        cursor.execute(comando_SQL, mesesS10)
        outubro = cursor.fetchone()[0]
        total.out_2.setText(str(outubro))

        cursor = banco.cursor()
        nov = "11"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2022"
        mesesS11 = (str(nov),)
        cursor.execute(comando_SQL, mesesS11)
        novembro = cursor.fetchone()[0]
        total.nov_2.setText(str(novembro))

        cursor = banco.cursor()
        dez = "12"
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE mes = %s AND ano= 2022"
        mesesS12 = (str(dez),)
        cursor.execute(comando_SQL, mesesS12)
        dezembro = cursor.fetchone()[0]
        total.dez_2.setText(str(dezembro))

        cursor = banco.cursor()
        comando_SQL = "SELECT COUNT(*) FROM atendidos WHERE ano= 2022"
        cursor.execute(comando_SQL)
        totalatendidos = cursor.fetchone()[0]
        total.total_2.setText(str(totalatendidos))

        cursor = banco.cursor()
        comando_SQL = "SELECT COUNT(*) FROM eleitores"
        cursor.execute(comando_SQL)
        totalcadastrados= cursor.fetchone()[0]
        total.totalcadastro.setText("Total Cadastrado: "+str(totalcadastrados))



    except Error as e:
            total.hide()
            erro.show()
            erro.botao_ok.clicked.connect(erro.hide)
            erro.botao_cancelar.clicked.connect(erro.hide)


def chamar_listaver():
    try:
        linha = lista.lista.currentRow()
        cursor = banco.cursor()
        comando_SQL = "SELECT id FROM eleitores WHERE bairro = %s"
        bairrosS = (str(bairro),)
        cursor.execute(comando_SQL, bairrosS)
        dados_lidos = cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("SELECT * FROM eleitores WHERE id=" + str(valor_id))
        eleitores = cursor.fetchall()

        listavereador.label_nome.setText(str(eleitores[0][1]))
        listavereador.label_cpf.setText(str(eleitores[0][2]))
        listavereador.label_telefone.setText(str(eleitores[0][3]))
        listavereador.labeldata.setText(str(eleitores[0][4]))
        listavereador.label_bairro.setText(str(eleitores[0][5]))
        listavereador.label_rua.setText(str(eleitores[0][6]))
        listavereador.label_complemento.setText(str(eleitores[0][7]))
        listavereador.label_assunto.setText(str(eleitores[0][8]))
        listavereador.show()
    except Error as e:
        erro.show()
        listavereador.hide()
        erro.botao_ok.clicked.connect(erro.hide)
        erro.botao_cancelar.clicked.connect(erro.hide)


def salvar_dadosedit():
    global numero_id
    global assuntoanterior
    assuntoanterior = str(assuntoanterior)
    nome = menueditar.barra_nome.text()
    cpf = menueditar.barra_cpf.text()
    telefone = menueditar.barra_telefone.text()
    rua = menueditar.barra_rua.text()
    complemento = menueditar.barra_complemento.text()
    assunto = assuntoanterior + "\n" + data + menueditar.barra_ass.toPlainText()

    try:
        cursor = banco.cursor()
        comando_SQL = "UPDATE eleitores SET nome = %s, cpf=%s, telefone=%s, rua=%s, complemento=%s, assunto=%s WHERE id = %s"
        dados = (str(nome), str(cpf), str(telefone), str(rua), str(complemento), str(assunto), str(numero_id))
        cursor.execute(comando_SQL, (dados), )
        listaedit.show()
        comando_SQL1 = "INSERT INTO atendidos (mes,ano) VALUES (%s,%s)"
        mesatendidos = (str(datames), str(dataano),)
        cursor.execute(comando_SQL1, (mesatendidos), )
        banco.commit()
        menueditar.barra_ass.clear()
        menueditar.msg_erro.show()
    except Error as e:
        menueditar.msg_erro.show()
        menueditar.label_erro.setText("Erro: "+ str(e))


# botoes
login.botao_entrar.clicked.connect(lambda: chamar_opcoes())
# chamar cadastro
opcoesacoes.botao_cadastrar.clicked.connect(lambda: chamar_bairro())
# chamar lista
opcoesacoes.botao_verlista.clicked.connect(lambda: chamar_bairro3())
opcoesver.botao_verlista_2.clicked.connect(lambda: chamar_bairrolista())
lista.botao_vereleitor.clicked.connect(lambda: chamar_listaver())
# pesquisar nas listas
lista.botao_pesquisar.clicked.connect(lambda: pesquisarlista())
listaedit.botao_pesquisar.clicked.connect(lambda: pesquisarlistaedit())
# chamar tela de edição
listaedit.botao_chamaredit.clicked.connect(lambda: chamar_telaedit())
#chamar total
opcoesver.botao_vertotal.clicked.connect(lambda: chamartotal())
opcoesacoes.botao_vertotal.clicked.connect(lambda: chamartotal())
# salvar edição
menueditar.botao_salvaredit.clicked.connect(lambda: salvar_dadosedit())
# fazer cadastro
cadastro.botao_cadastro.clicked.connect(lambda: salvar_eleitor())
#sair do programa
opcoesver.botao_sair.clicked.connect(lambda: app.quit())
opcoesacoes.botao_sair.clicked.connect(lambda: app.quit())
# fechar msg de erro
login.pushButton_popup.clicked.connect(lambda: login.msg_erro.hide())
cadastro.pushButton_popup.clicked.connect(lambda: cadastro.msg_erro.hide())
menueditar.pushButton_popup.clicked.connect(lambda: menueditar.msg_erro.hide())
# msg de erro ja escondida
login.msg_erro.hide()
cadastro.msg_erro.hide()
menueditar.msg_erro.hide()
# botoes bairros
bairros.artur1.clicked.connect(lambda: artur1())
bairros.artur2.clicked.connect(lambda: artur2())
bairros.aurora.clicked.connect(lambda: aurora())
bairros.centro.clicked.connect(lambda: centro())
bairros.engenhoM.clicked.connect(lambda: engenhoM())
bairros.fragoso.clicked.connect(lambda: fragoso())
bairros.jaguarana.clicked.connect(lambda: jaguarana())
bairros.jaguaribe.clicked.connect(lambda: jaguaribe())
bairros.janga.clicked.connect(lambda: janga())
bairros.jardimm.clicked.connect(lambda: jardimm())
bairros.jardimp.clicked.connect(lambda: jardimp())
bairros.m1.clicked.connect(lambda: m1())
bairros.m2.clicked.connect(lambda: m2())
bairros.mirueira.clicked.connect(lambda: mirueira())
bairros.mf.clicked.connect(lambda: mf())
bairros.nobre.clicked.connect(lambda: nobre())
bairros.nossaC.clicked.connect(lambda: nossaC())
bairros.nossaO.clicked.connect(lambda: nossaO())
bairros.paratibe.clicked.connect(lambda: paratibe())
bairros.pauamarelo.clicked.connect(lambda: pauamarelo())
bairros.poty.clicked.connect(lambda: poty())
bairros.tabajara.clicked.connect(lambda: tabajara())
bairros.vilaT.clicked.connect(lambda: vilaT())
bairros.outros.clicked.connect(lambda: outros())

###############################################################
bairros2.artur1.clicked.connect(lambda: artur1p())
bairros2.artur2.clicked.connect(lambda: artur2p())
bairros2.aurora.clicked.connect(lambda: aurorap())
bairros2.centro.clicked.connect(lambda: centrop())
bairros2.engenhoM.clicked.connect(lambda: engenhoMp())
bairros2.fragoso.clicked.connect(lambda: fragosop())
bairros2.jaguarana.clicked.connect(lambda: jaguaranap())
bairros2.jaguaribe.clicked.connect(lambda: jaguaribep())
bairros2.janga.clicked.connect(lambda: jangap())
bairros2.jardimm.clicked.connect(lambda: jardimmp())
bairros2.jardimp.clicked.connect(lambda: jardimpp())
bairros2.m1.clicked.connect(lambda: m1p())
bairros2.m2.clicked.connect(lambda: m2p())
bairros2.mf.clicked.connect(lambda: mfp())
bairros2.mirueira.clicked.connect(lambda: mirueirap())
bairros2.nobre.clicked.connect(lambda: nobrep())
bairros2.nossaC.clicked.connect(lambda: nossaCp())
bairros2.nossaO.clicked.connect(lambda: nossaOp())
bairros2.paratibe.clicked.connect(lambda: paratibep())
bairros2.pauamarelo.clicked.connect(lambda: pauamarelop())
bairros2.poty.clicked.connect(lambda: potyp())
bairros2.tabajara.clicked.connect(lambda: tabajarap())
bairros2.vilaT.clicked.connect(lambda: vilaTp())
bairros2.outros.clicked.connect(lambda: outrosp())

#####################################################################################
bairros3.artur1.clicked.connect(lambda: artur1pe())
bairros3.artur2.clicked.connect(lambda: artur2pe())
bairros3.aurora.clicked.connect(lambda: aurorape())
bairros3.centro.clicked.connect(lambda: centrope())
bairros3.engenhoM.clicked.connect(lambda: engenhoMpe())
bairros3.fragoso.clicked.connect(lambda: fragosope())
bairros3.jaguarana.clicked.connect(lambda: jaguaranape())
bairros3.jaguaribe.clicked.connect(lambda: jaguaribepe())
bairros3.janga.clicked.connect(lambda: jangape())
bairros3.jardimm.clicked.connect(lambda: jardimmpe())
bairros3.jardimp.clicked.connect(lambda: jardimppe())
bairros3.m1.clicked.connect(lambda: m1pe())
bairros3.m2.clicked.connect(lambda: m2pe())
bairros3.mf.clicked.connect(lambda: mfpe())
bairros3.mirueira.clicked.connect(lambda: mirueirape())
bairros3.nobre.clicked.connect(lambda: nobrepe())
bairros3.nossaC.clicked.connect(lambda: nossaCpe())
bairros3.nossaO.clicked.connect(lambda: nossaOpe())
bairros3.paratibe.clicked.connect(lambda: paratibepe())
bairros3.pauamarelo.clicked.connect(lambda: pauamarelope())
bairros3.poty.clicked.connect(lambda: potype())
bairros3.tabajara.clicked.connect(lambda: tabajarape())
bairros3.vilaT.clicked.connect(lambda: vilaTpe())
bairros3.outros.clicked.connect(lambda: outrospe())

app.exec()

