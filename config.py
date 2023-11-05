import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFileDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.nombres = ["PSX", "PS2", "Dreamcast", "Genesis", "PC-FX"]
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
        print("Datos guardados en directorios.json")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
