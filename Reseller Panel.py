########################################################################################################################
                                                 #Python Modules
########################################################################################################################
import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QSplashScreen
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
########################################################################################################################
                                                #Splash Screens
########################################################################################################################
class SplashScreen(QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.setWindowTitle("splash screen")
        self.setFixedSize(640,426)

        loadUi("Paway UI files/Splash.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        pixmap=QPixmap("Paway Images/Splash.jpg")
        self.setPixmap(pixmap)

    def progress(self):
        for i in range (101):
            time.sleep(0.01)
            self.progressBar.setValue(i)

########################################################################################################################
                                              #Welcome_Screen
########################################################################################################################
class Welcome(QDialog):
    def __init__(self):
        super(Welcome, self).__init__()
        loadUi("Paway UI files/welcome.ui", self)
        self.loginButton.clicked.connect(self.login_screen_fun)
        self.signupButton.clicked.connect(self.signup_screen_fun)
    def login_screen_fun(self):
        login_obj = Login()
        widget.addWidget(login_obj)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def signup_screen_fun(self):
        signup_obj = Signup()
        widget.addWidget(signup_obj)
        widget.setCurrentIndex(widget.currentIndex() + 1)




########################################################################################################################
                                              #Reseller login
########################################################################################################################
class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("Paway UI files/reseller login.ui",self)
        self.back.clicked.connect(self.back_to_welcomeScreen)
    def back_to_welcomeScreen(self):
        welcome_obj = Welcome()
        widget.addWidget(welcome_obj)
        widget.setCurrentIndex(widget.currentIndex() - 1)
########################################################################################################################
                                                    #Reseller Signup
########################################################################################################################
class Signup(QDialog):
    def __init__(self):
        super(Signup, self).__init__()
        loadUi("Paway UI files/reseller signup.ui",self)
        self.loginButton.clicked.connect(self.login_screen_fun)
        self.back.clicked.connect(self.back_to_welcomeScreen)
    def back_to_welcomeScreen(self):
        welcome_obj = Welcome()
        widget.addWidget(welcome_obj)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def login_screen_fun(self):
        login_obj = Login()
        widget.addWidget(login_obj)
        widget.setCurrentIndex(widget.currentIndex() + 1)

########################################################################################################################
                                                         #Main
########################################################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    splash.progress()
    welcome_obj = Welcome()

    widget=QtWidgets.QStackedWidget()
    widget.addWidget(welcome_obj)

    widget.setFixedWidth(1200)
    widget.setFixedHeight(650)
    widget.show()


    splash.finish(widget)
    app.exec_()
