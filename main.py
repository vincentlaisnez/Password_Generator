from PySide6.QtWidgets import QApplication, QWidget


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
        pass

    def create_layouts(self):
        pass

    def modify_widgets(self):
        pass

    def add_widgets_to_layouts(self):
        pass

    def setup_connections(self):
        pass


if __name__ == '__main__':
    app = QApplication()
    main_window = MainWindow()
    main_window.resize(800, 600)
    main_window.show()
    app.exec()
