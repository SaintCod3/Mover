import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFileDialog, QMessageBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.nombres = ["Consola 1", "Consola 2", "Consola 3", "Consola 4", "Consola 5"]
        self.directorios = {}

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        for nombre in self.nombres:
            label = QLabel(nombre)
            self.layout.addWidget(label)

            path_input = QLineEdit()
            path_input.setReadOnly(True)
            self.layout.addWidget(path_input)

            button = QPushButton("Seleccionar directorio")
            button.clicked.connect(lambda _, n=nombre, p=path_input: self.select_directory(n, p))
            self.layout.addWidget(button)

        save_button = QPushButton("Guardar en JSON")
        save_button.clicked.connect(self.save_to_json)
        self.layout.addWidget(save_button)

    def select_directory(self, nombre, path_input):
        directorio = QFileDialog.getExistingDirectory(self, "Seleccionar directorio")
        self.directorios[nombre] = directorio
        path_input.setText(directorio)

    def save_to_json(self):
        with open('directorios.json', 'w') as file:
            json.dump(self.directorios, file, indent=4)
        self.show_dialog()

    def show_dialog(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("Datos guardados en directorios.json")
        msg_box.setWindowTitle("Información")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
