from PySide6.QtWidgets import QLabel, QMainWindow, QTabWidget

from controle_exames import __version__


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(f"Controle de Exames — base {__version__}")
        self.resize(1100, 720)
        tabs = QTabWidget()
        for name in ("Cadastro", "Listagem", "Relatórios", "Auditoria", "Configurações", "Paciente"):
            tabs.addTab(QLabel(f"{name}: módulo aguardando implementação."), name)
        self.setCentralWidget(tabs)
