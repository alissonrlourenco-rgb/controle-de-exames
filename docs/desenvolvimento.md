# Desenvolvimento

Use Python 3.12 e um ambiente virtual. Instale com `python -m pip install -e ".[dev,build]"`.

Execute `python -m controle_exames` e `python -m pytest`. Os testes usam bancos temporários e dados fictícios.

## Incorporação do aplicativo existente

1. Copiar os fontes originais preservando uma versão funcional.
2. Recuperar ícones, layouts e dependências efetivamente utilizadas.
3. Transferir os módulos gradualmente para src/controle_exames.
4. Documentar o esquema real do banco e testar migrações em cópias fictícias.
5. Validar Cadastro, Listagem, Relatórios, Auditoria, Configurações e Paciente.
6. Atualizar versão, histórico e empacotamento antes da distribuição.

Não versionar dados de pacientes, backups, senhas ou arquivos de configuração privados. A visibilidade pública do repositório não define sua licença.
