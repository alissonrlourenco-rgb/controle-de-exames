# Arquitetura

- UI: telas e interação em PySide6.
- Services: validação e regras de negócio.
- Repositories: operações SQL por domínio.
- Models: estruturas de dados.
- Database: conexão, inicialização e futuras migrações.
- Resources: recursos distribuídos com a aplicação.

A base cria somente metadados de esquema. A modelagem de pacientes, exames, menus e auditoria deve ser incorporada junto ao código existente. Antes de alterar um banco existente, identificar seu esquema, criar backup e implementar migrações explícitas. Não usar esta inicialização como migração da aplicação atual.

Guardar o banco em QStandardPaths.AppDataLocation; nunca dentro do executável ou da pasta temporária do PyInstaller. Importação do banco anterior deve ser planejada para preservar os dados.
