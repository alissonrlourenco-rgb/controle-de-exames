import sys

from PySide6.QtCore import QStandardPaths
from PySide6.QtWidgets import QApplication

from controle_exames.database.connection import initialize_database
from controle_exames.ui.main_window import MainWindow


def main() -> int:
    app = QApplication(sys.argv)
    app.setOrganizationName("ControleExames")
    app.setApplicationName("ControleExames")
    data_dir = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
    initialize_database(data_dir + "/controle_exames.sqlite3")
    window = MainWindow()
    window.show()
    return app.exec()
