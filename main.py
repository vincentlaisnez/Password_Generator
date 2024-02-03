from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QGridLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.lbl_length_password = QLabel("Longueur du mot de passe")
        self.length_password = QLineEdit()
        self.lbl_check_digits = QLabel("avec chiffres")
        self.digits = QCheckBox()
        self.lbl_special_char = QLabel("Avec caractères speciaux")
        self.special_char = QCheckBox()
        self.btn_generate = QPushButton("Generer un mot de passe")

    def create_layouts(self):
        self.main_layout = QGridLayout(self)

    def modify_widgets(self):
        pass

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.lbl_length_password, 0, 0)
        self.main_layout.addWidget(self.length_password, 0, 1)
        self.main_layout.addWidget(self.lbl_check_digits, 1, 0)
        self.main_layout.addWidget(self.digits, 1, 1)
        self.main_layout.addWidget(self.lbl_special_char, 2, 0)
        self.main_layout.addWidget(self.special_char, 2, 1)
        self.main_layout.addWidget(self.btn_generate)

    def setup_connections(self):
        pass


if __name__ == '__main__':
    app = QApplication()
    main_window = MainWindow()
    # main_window.resize(800, 600)
    main_window.show()
    app.exec()
