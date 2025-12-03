import json
import sys
from PyQt5.QtWidgets import (
    QApplication, QTextEdit, QTableWidget, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QTableWidgetItem
)
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Hello World!')
window.setGeometry(300, 300, 600, 400)

contactos = []
ficheiro_json = "contactos.json"

main_layout = QVBoxLayout()
table_layout = QVBoxLayout()
entry_layout = QHBoxLayout()
button_layout = QHBoxLayout()

tableWidget = QTableWidget()

nome_entry = QTextEdit()
tel_entry = QTextEdit()
email_entry = QTextEdit()

add_button = QPushButton()
edit_button = QPushButton()
delete_button = QPushButton()

add_button.setText("Adicionar")
edit_button.setText("Editar")
delete_button.setText("Remover")

nome_entry.setFixedHeight(25)
tel_entry.setFixedHeight(25)
email_entry.setFixedHeight(25)

table_layout.addWidget(tableWidget)
entry_layout.addWidget(nome_entry)
entry_layout.addWidget(tel_entry)
entry_layout.addWidget(email_entry)
button_layout.addWidget(add_button)
button_layout.addWidget(edit_button)
button_layout.addWidget(delete_button)

main_layout.addLayout(table_layout)
main_layout.addLayout(entry_layout)
main_layout.addLayout(button_layout)

def guardar_contactos():
        with open(ficheiro_json, "w", encoding="utf-8") as f:
                json.dump(contactos, f, indent=4, ensure_ascii=False)

def carregar_contactos():
        try:
                with open(ficheiro_json, "r", encoding="utf-8") as f:
                        contactos.extend(json.load(f))
        except FileNotFoundError:
                pass

def adicionar_contactos():
        nome = nome_entry.text().strip()
        telefone = tel_entry.text().strip()
        email = email_entry.text().strip()

        if nome:
            contactos.append({"nome": nome, "telefone": telefone, "email": email})
            atualizar_tabela()
            guardar_contactos()
            nome_entry.clear()
            tel_entry.clear()
            email_entry.clear()

def remover_contactos():
        linha = tableWidget.currentRow()

        if linha >= 0:
                del contactos[linha]
                atualizar_tabela()
                guardar_contactos()

def editar_contactos():
        linha = tableWidget.currentRow()

        if linha >= 0:
                contactos[linha] = {
                        "nome": nome_entry.text().strip(),
                        "telefone": tel_entry.text().strip(),
                        "email": email_entry.text().strip()
                }
        atualizar_tabela()
        guardar_contactos()

def preencher_inputs():
        linha = tableWidget.currentRow()
        if linha >= 0:
                nome_entry.setText(contactos[linha]["nome"])
                tel_entry.setText(contactos[linha]["telefone"])
                email_entry.setText(contactos[linha]["email"])

def atualizar_tabela():
        tableWidget.setRowCount(0)
        for i, c in enumerate(contactos):
                tableWidget.insertRow(1)
                tableWidget.setItem(i, 0, QTableWidgetItem(c["nome"]))
                tableWidget.setItem(i, 1, QTableWidgetItem(c["telefone"]))
                tableWidget.setItem(i, 2, QTableWidgetItem(c["email"]))


carregar_contactos()
atualizar_tabela()

window.setLayout(main_layout)
window.show()
sys.exit(app.exec_())