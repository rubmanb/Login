from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from sys import *

'''
Finestra de login

Heu de crear una aplicació que al ser llançada mostre una finestra de login, 
demanant a l'usuari el nom d'usuari i la contrasenya:

En cas d'introduir 'admin', '1234', mostrarà la finstra principal de l'aplicació, 
on s'indicarà (a l'status bar i amb un QLabel com a CentralWidget) que s'està loguejat amb l'usuari admin.
Si s'introdueix 'user', '1234', es mostrarà que s'està loguejat com a usuari estàndar.
Si l'usuari o la contrasenya són incorrectes, llanceu un avís informant a l'usuari.
Poseu una opció al menú de la finestra principal per a fer logout, de forma que ens torne 
a mostrar la finestra de login i una altra opció per tancar l'aplicació. Si es tanca qualsevol 
de les finestres, l'aplicació acabarà la seua execució.
'''

#constants del tamany de les finestres
LOGIN_WIDTH = 250
LOGIN_HEIGHT = 300
MW_WIDTH = 300
MW_HEIGHT = 300

#Finestra de login
class LoginWindow(QWidget):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        
        #fixem un titul i un tamany per a la finestra
        self.setWindowTitle("Login")
        self.setFixedSize(LOGIN_WIDTH, LOGIN_HEIGHT)

        #Establim una font per al titul
        self.fontTitle = QFont()
        self.fontTitle.setBold(True)
        self.fontTitle.setPointSize(50)
        self.fontTitle.setFamily("consolas")
        self.fontTitle.setItalic(True)

        #Cree un layout de tipo formulari per a centrar tots els camps en la finestra
        layout = QFormLayout()
        layout.setFormAlignment(Qt.AlignCenter)
        
        #Establisc els camps que va a tindre la finestra
        self.title = QLabel(self)
        self.title.setText("LOGIN")
        self.title.setFont(self.fontTitle)
        self.title.setAlignment(Qt.AlignCenter)

        self.user = QLabel(self)
        self.user.setText("User:")
        self.userFieldText = QLineEdit(self)
        self.userFieldText.setFixedSize(150, 25)
        self.userFieldText.setPlaceholderText("User")
        
        self.pwd = QLabel(self)
        self.pwd.setText("Password:")
        self.pwdFieldText = QLineEdit(self)
        self.pwdFieldText.setFixedSize(150, 25)
        self.pwdFieldText.setPlaceholderText("Password")

        self.btn_accedir = QPushButton("Enter")
        self.btn_accedir.clicked.connect(self.checkFields)

        #anyadeix els diversos camps al layout
        layout.addWidget(self.title)
        layout.addWidget(self.user)
        layout.addWidget(self.userFieldText)
        layout.addWidget(self.pwd)
        layout.addWidget(self.pwdFieldText)
        layout.addWidget(self.btn_accedir)

        self.setLayout(layout)
        
        
    #Funcions de la finestra de login
    
    #Funció per a "canviar" de finestres
    #es dispara al clicar en el boto "Enter"
    def changeMainWindow(self, checked):
        self.mw = MainWindow()
        if self.isVisible():
            self.hide()
        else: 
            self.mw.show()

        user = self.userFieldText.text()
        self.mw.label.setText(str(user))

    #Funció per a checkear els camps amb el text que se inserisca
    def checkFields(self):
        checkUser = self.userFieldText.text()
        checkPwd = self.pwdFieldText.text()
        if checkUser=="admin" and checkPwd=="1234":
            print("Admin successful")
            self.changeMainWindow(self)
        elif checkUser == "user" and checkPwd=="1234":
            print("User successful")
            self.changeMainWindow(self)
        else:
            print("error in LoginWindow")
            self.userFieldText.clear()
            self.pwdFieldText.clear()
            self.MessageError()
        

    #Funció per a voore un missatge d'error si se insereixen mal les dades en els camps.     
    def MessageError(self):
        error = QMessageBox(self)
        error.setWindowTitle("Error")
        error.setText("Data incorrect")
        error.show()

    

#Finestra principal que tindra el menú 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MainWindow")
        self.setFixedSize(MW_WIDTH, MW_HEIGHT)

        self.show()

        #Layout de la Finestra
        mainLayout = QVBoxLayout()
        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        
        #menu
        btn_logout = QAction("&LogOut", self)
        btn_logout.setStatusTip("Logout")
        btn_logout.triggered.connect(self.changeWindowBtnLogout)
        btn_exit = QAction("&Exit", self)
        btn_exit.setStatusTip("Exit")
        btn_exit.triggered.connect(self.close)
        
        menu = self.menuBar()

        app_menu = menu.addMenu("&App")
        app_menu.addAction(btn_logout)
        app_menu.addAction(btn_exit)

        #Nom en el que accedeix un usuari desde el login
        self.label = QLabel()
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.statusbar.addWidget(self.label)
        self.setCentralWidget(self.label)

    #Funció per a tancar la finestra principal i mostra la finestra de login
    def changeWindowBtnLogout(self):
        self.close()
        self.lw = LoginWindow()
        self.lw.show()
        

    
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    logWindow = LoginWindow()
    logWindow.show()
    app.exec()
