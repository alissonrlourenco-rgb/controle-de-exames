# Empacotamento Windows

Execute os comandos da raiz do repositório usando o ambiente virtual.

1. Instalar os extras dev e build.
2. Executar os testes.
3. Executar `python -m PyInstaller packaging/pyinstaller/ControleExames.spec --noconfirm`.
4. Testar `dist/ControleExames/ControleExames.exe` em Windows.
5. Compilar `packaging/inno/ControleExames.iss` com Inno Setup 6 atualizado.
6. Validar instalação, abertura, persistência de dados e desinstalação.

O modelo usa distribuição em pasta e não inclui o banco do usuário. O diretório installer-output contém o instalador gerado.

Antes de publicar: recuperar e manter o AppId fixo usado pelo instalador existente, recuperar o ícone oficial e sincronizar versões em pyproject.toml, __init__.py e ControleExames.iss. O AppId deste modelo é provisório e não garante atualização da instalação anterior.

O executável e o instalador não foram validados em Windows nesta criação inicial. Publique binários aprovados em GitHub Releases; mantenha CHANGELOG.md e tags de versão para registrar o histórico.
