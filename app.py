import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFileDialog, QListWidget, QPushButton
from PyQt5.QtCore import QProcess

class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hina')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        open_button = QPushButton('Seleccionar directorio')
        open_button.clicked.connect(self.open_directory)
        self.layout.addWidget(open_button)

        config_button = QPushButton('Configuración')
        config_button.clicked.connect(self.open_configuration_script)
        self.layout.addWidget(config_button)

        send_button = QPushButton('Mover')
        send_button.clicked.connect(self.send_to_script_button)
        self.layout.addWidget(send_button)

        self.directory = ""

    def open_directory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Seleccionar directorio')
        if directory:
            self.list_directory_contents(directory)

    def list_directory_contents(self, directory):
        self.list_widget.clear()
        for item in os.listdir(directory):
            self.list_widget.addItem(item)

    def open_configuration_script(self):
        script_path = "config.py" 
        if os.path.exists(script_path):
            QProcess.startDetached('python', [script_path])

    def send_to_script(self):
        if self.directory:
            file_list = os.listdir(self.directory)
            script_path = "analyze.py"  
            if os.path.exists(script_path):
                arguments = [self.directory] + file_list
                QProcess().start('python', [script_path] + arguments)


    def send_to_script_button(self):
        self.send_to_script()
   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileExplorer()
    window.show()
    sys.exit(app.exec_())
