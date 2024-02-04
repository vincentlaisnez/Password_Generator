from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QGridLayout, QMessageBox

import generate_password


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setStyleSheet("background-color: #424242;")
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.lbl_length_password = QLabel("Longueur du mot de passe:")
        self.length_password = QLineEdit()
        self.digits = QCheckBox("avec chiffres")
        self.special_char = QCheckBox("Avec caractères speciaux")
        self.btn_generate = QPushButton("Generer un mot de passe")
        self.password = QLineEdit()

    def create_layouts(self):
        self.main_layout = QGridLayout(self)

    def modify_widgets(self):
        self.btn_generate.setStyleSheet(
            """
            QPushButton:pressed {
                background-color: blue;
                color: white;
            }
            QPushButton{
                background-color: #7E57C2;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: #311B92;
                font: bold 14px;
                min-width: 10em;
                padding: 6px;
            }"""
        )

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.lbl_length_password, 0, 0)
        self.main_layout.addWidget(self.length_password, 0, 1)
        self.main_layout.addWidget(self.digits, 1, 0)
        self.main_layout.addWidget(self.special_char, 2, 0)
        self.main_layout.addWidget(self.btn_generate, 3, 0)
        self.main_layout.addWidget(self.password, 3, 1)

    def setup_connections(self):
        self.btn_generate.clicked.connect(self.generate_password)

    def generate_password(self):
        if length := self.length_password.text():
            if not length.isdigit():
                self.check_length()
                return
            length = int(length)
            digits = self.digits.isChecked()
            special_char = self.special_char.isChecked()
            password = generate_password.generate_password(length, digits, special_char)
            self.password.setText(password)
        else:
            self.check_length()

    def check_length(self):
        dialog = QMessageBox()
        dialog.setText("Veuillez entrer une longueur valide (que des chiffres).")
        dialog.exec()


if __name__ == '__main__':
    app = QApplication()
    main_window = MainWindow()
    main_window.setFixedSize(400, 200)
    main_window.show()
    app.exec()
