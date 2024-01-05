import os
import subprocess
import sys
import time
from connect import Ui_Main_Window
from username import Ui_UserName_Window
from db.database import DatabaseManager
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QShortcut, QMessageBox


class Main:
    def __init__(self):
        self.app = QApplication(sys.argv)

        # MAIN WINDOW
        self.Main_Window = QMainWindow()
        self.Main_GUI = Ui_Main_Window()
        self.Main_GUI.setupUi(self.Main_Window)
        self.Main_Window.show()

        # USERNAME WINDOW
        self.Change_UserName_Window = QDialog()
        self.Change_Username_GUI = Ui_UserName_Window()
        self.Change_Username_GUI.setupUi(self.Change_UserName_Window)

        # COLOR and TITLE
        self.color_error = 'background-color:#fa8f87'
        self.color_normal = 'background-color:white'
        self.title = 'Secure RDC'

        self.error = 'error'

        self.db_manager = DatabaseManager()
        if self.db_manager.initialize_database() == self.error:
            self.read_error_log()
        if self.db_manager.change_values(None, None) == self.error:
            self.read_error_log()

        self.shortcut()

    def shortcut(self):
        QShortcut(QKeySequence("F1"), self.Main_Window).activated.connect(self.open_username_window)
        self.Change_Username_GUI.btn_enter.clicked.connect(self.change_username)

        QShortcut(QKeySequence("Return"), self.Main_Window).activated.connect(self.connect_remote_desktop)
        self.Main_GUI.btn_connect.clicked.connect(self.connect_remote_desktop)

    def open_username_window(self):
        if self.db_manager.get_default_username() == self.error:
            self.read_error_log()
        else:
            self.Change_UserName_Window.show()
            self.Change_Username_GUI.checkbox_save_me.setChecked(False)
            self.Change_Username_GUI.input_username.setText(self.db_manager.get_default_username())

    def change_username(self):
        username = str(self.Change_Username_GUI.input_username.text()).upper()

        if not username:
            self.Change_Username_GUI.input_username.setStyleSheet(self.color_error)
            QMessageBox.critical(self.Main_Window, self.title, '\nEnter Username!')
            self.Change_Username_GUI.input_username.setStyleSheet(self.color_normal)
        else:
            if self.Change_Username_GUI.checkbox_save_me.isChecked():
                if self.db_manager.change_values(username, username) == self.error:
                    self.read_error_log()
            else:
                if self.db_manager.change_values(None, username) == self.error:
                    self.read_error_log()

            self.Change_UserName_Window.close()

    def connect_remote_desktop(self):
        username = self.db_manager.get_default_username()
        if username == self.error:
            self.read_error_log()
        else:
            ipaddress = str(self.Main_GUI.input_ip_address.text())
            password = str(self.Main_GUI.input_password.text())

            if not ipaddress:
                self.Main_GUI.input_ip_address.setStyleSheet(self.color_error)
                QMessageBox.critical(self.Main_Window, self.title, '\nEnter IP address!')
                self.Main_GUI.input_ip_address.setStyleSheet(self.color_normal)
            elif not password:
                self.Main_GUI.input_password.setStyleSheet(self.color_error)
                QMessageBox.critical(self.Main_Window, self.title, '\nEnter password!')
                self.Main_GUI.input_password.setStyleSheet(self.color_normal)
            else:
                self.Main_GUI.input_ip_address.clear()
                self.Main_GUI.input_password.clear()
                creditionals = 'cmdkey /generic:' + ipaddress + ' /user:domain\\' + username + ' /pass:' + password
                connect = 'mstsc /v:' + ipaddress
                delete_connection = 'cmdkey /delete:' + ipaddress
                delete_connection_term = 'cmdkey /delete:TERMSRV/' + ipaddress
                delete_TSC = 'reg delete "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client" /f'
                delete_hidden_default_rdp = 'del /ah C:' + str(os.environ[r'HOMEPATH']) + '\Documents\Default.rdp'
                delete_default_rdp = 'del C:' + str(os.environ[r'HOMEPATH']) + '\Documents\Default.rdp'

                baza = [creditionals, connect, delete_connection, delete_connection_term, delete_TSC,
                        delete_hidden_default_rdp,
                        delete_default_rdp]

                self.Main_Window.close()
                for i in baza:
                    time.sleep(0.08)
                    proc = subprocess.Popen(i, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                    proc.communicate()

    def read_error_log(self):
        try:
            with open("log/log.txt", "r") as log_file:
                lines = log_file.readlines()
                if lines:
                    info = lines[-1].strip()
                else:
                    info = "Log file is empty"
        except FileNotFoundError:
            info = "Log file not found"
        except Exception as e:
            info = f"Error reading log file: {e}"
        info = '\n' + info
        QMessageBox.critical(self.Main_Window, self.title, info)

    def run(self):
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    app_instance = Main()
    app_instance.run()
