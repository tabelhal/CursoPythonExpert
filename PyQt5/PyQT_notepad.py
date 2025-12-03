import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QKeySequence

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('Notepad')
window.setGeometry(300, 300, 600, 400)

def novo_arquivo():
    texto_edit.clear()

def abrir_arquivo():
    caminho, _ = QFileDialog.getOpenFileNames(window, "Abrir Ficheiro", "", "Text Files (.txt);; All Files (*)")

    if caminho:
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                texto_edit.setText(conteudo)
        except Exception as e:
            QMessageBox.warning(window, "Erro", f"Não foi possível abrir o ficheiro: \n{e}")


def guardar_arquivo():
    caminho, _ = QFileDialog.getSaveFileName(window, "Guardar Ficheiro", "", "Text Files (.txt);; All Files (*)")

    if caminho:
        try:
            with open(caminho, 'w', encoding='utf-8') as f:
                f.write(texto_edit.toPlainText())
        except Exception as e:
            QMessageBox.warning(window, "Erro", f"Não foi possível guardar o ficheiro: \n{e}")





texto_edit = QTextEdit()
window.setCentralWidget(texto_edit)

menu_arquivo = window.menuBar().addMenu('Arquivo')

new_action = QAction('Novo', window)
new_action.setShortcut(QKeySequence.New)
new_action.triggered.connect(novo_arquivo)

open_action = QAction('Abrir', window)
open_action.setShortcut(QKeySequence.Open)
open_action.triggered.connect(abrir_arquivo)

save_action = QAction('Guardar', window)
save_action.setShortcut(QKeySequence.SaveAs)
save_action.triggered.connect(guardar_arquivo)

menu_arquivo.addAction(new_action)
menu_arquivo.addAction(open_action)
menu_arquivo.addAction(save_action)

window.show()
sys.exit(app.exec_())