# Controle de Exames

Aplicativo desktop para controle de exames de radiologia, desenvolvido em Python, PySide6 e SQLite, com distribuição Windows por PyInstaller e Inno Setup.

## Estado inicial

Este repositório contém a estrutura de desenvolvimento e uma janela inicial executável. O código completo do aplicativo existente ainda deverá ser incorporado. A versão desta base é 0.1.0; ela não representa uma nova versão do aplicativo já distribuído.

## Ambiente de desenvolvimento

Python 3.12 recomendado. No PowerShell, na raiz do repositório:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev,build]"
python -m controle_exames
python -m pytest
```

## Organização

| Pasta | Finalidade |
| --- | --- |
| src/controle_exames/ | Aplicação, interface, serviços e acesso a dados |
| src/controle_exames/resources/ | Ícones, imagens e estilos distribuídos com o aplicativo |
| tests/ | Testes com dados fictícios e bancos temporários |
| docs/ | Arquitetura, desenvolvimento, versões e empacotamento |
| packaging/pyinstaller/ | Especificação do executável |
| packaging/inno/ | Instalador Windows |
| scripts/ | Ponto de entrada para empacotamento |

O banco SQLite inicial é criado em uma pasta de dados do usuário, fora da instalação. Bancos, backups, dados de pacientes e executáveis não devem ser incluídos no Git.

## Executável e instalador

No Windows, após instalar as dependências:

```powershell
python -m PyInstaller packaging/pyinstaller/ControleExames.spec --noconfirm
ISCC.exe packaging/inno/ControleExames.iss
```

Consulte [empacotamento](docs/empacotamento.md) antes de distribuir ou incorporar a versão existente. O ícone oficial e o AppId do instalador anterior precisam ser recuperados.

## Desenvolvimento

Consulte [arquitetura](docs/arquitetura.md), [desenvolvimento](docs/desenvolvimento.md) e [histórico](CHANGELOG.md). Funcionalidades previstas: Cadastro, Listagem, Relatórios, Auditoria, Configurações e Paciente.

## Licença

A licença de distribuição ainda não foi definida pelo responsável pelo projeto.
