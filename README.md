# Sistema Biblioteca — Manual de Implantação

Aplicação web em **Python 3 puro (sem framework)** com **MySQL**, orientada a **classes**.
Tem área pública (acervo, busca, detalhes), login com perfis (admin/usuário) e painel administrativo com CRUD completo.

## Estrutura
```
main.py                  # ponto de entrada
criar_usuario.py         # cria usuários com senha em hash
app/config.py            # class Config            (variáveis de ambiente)
app/database.py          # class Database          (conexão MySQL)
app/livro.py             # class Livro             (entidade + validação)
app/repositorio.py       # class LivroRepositorio  (Create/Read/Update/Delete)
app/usuario.py           # classes Usuario, UsuarioRepositorio, Autenticador
app/seguranca.py         # classes Senha (PBKDF2), Sessao, GerenciadorSessoes
app/paginas.py           # class Pagina            (HTML das telas)
app/servidor.py          # class Servidor          (rotas HTTP, http.server)
sql/script_banco.sql     # banco, tabelas e dados de exemplo
GUIA_DE_TESTES.md        # roteiro de testes manuais
```

## Requisitos
Python 3.7+, MySQL 8 (ou MariaDB 10.5+) em execução, Git.

## 1. Obter o projeto
```bash
git clone <URL_DO_REPOSITORIO>
cd biblioteca
```

## 2. Instalar a dependência
O único pacote externo é o driver do MySQL (não é framework):
```bash
python -m venv venv
venv\Scripts\activate          # Windows   (Linux/Mac: source venv/bin/activate)
pip install -r requirements.txt
```

## 3. Criar o banco de dados
```bash
mysql -u root -p < sql/script_banco.sql
```
Cria o banco `biblioteca`, as tabelas `livros` e `usuarios`, 3 livros e 2 usuários de teste.

## 4. Configurar a conexão
As credenciais **não ficam no código**: são lidas de variáveis de ambiente.
Padrões: `DB_HOST=localhost`, `DB_PORT=3306`, `DB_USER=root`, `DB_PASSWORD=` (vazia), `DB_NAME=biblioteca`, `HTTP_PORT=8000`.
```bash
set DB_PASSWORD=sua_senha            # Windows (cmd)
$env:DB_PASSWORD="sua_senha"         # Windows (PowerShell)
export DB_PASSWORD=sua_senha         # Linux/Mac
```

## 5. Executar
```bash
python main.py
```
Acesse **http://127.0.0.1:8000**

## Páginas
| Endereço | Acesso |
|---|---|
| `/` Início (3 últimos livros + busca) | público |
| `/livros` Acervo com busca e destaque do termo | público |
| `/livro?id=1` Detalhe + livros relacionados | público |
| `/login` | público |
| `/admin` Painel (listar, pesquisar, editar, excluir) | somente admin |
| `/admin/novo`, `/admin/editar?id=1` | somente admin |

## Usuários de teste (somente ambiente de teste)
| Perfil | E-mail | Senha | Ao entrar vai para |
|---|---|---|---|
| Administrador | adm@gmail.com | 1234 | `/admin` |
| Usuário comum | usuario@gmail.com | 1234 | `/` |

Criar outro usuário: `python criar_usuario.py "Nome" email@exemplo.com senha admin`

## Regras de negócio e segurança
- Título, autor, gênero e ano obrigatórios; ano 1000–2100; ISBN com 10 ou 13 dígitos e **único**.
- **Livro "emprestado" não pode ser excluído.**
- Senhas guardadas com hash PBKDF2-SHA256 com sal; sessão no servidor, cookie `HttpOnly` + `SameSite=Lax`; sessão expira em 2 h; logout destrói a sessão.
- Painel e ações de escrita exigem login de admin (verificado no servidor em toda rota).
- Exclusão, edição, criação e logout só por POST, com token **CSRF**.
- Consultas parametrizadas (SQL Injection) e todo texto escapado (XSS).
- Se o banco cair, a página inicial mostra aviso em vez de quebrar; detalhes do erro vão só para o log.

## Problemas comuns
- `Access denied for user`: confira `DB_USER`/`DB_PASSWORD`.
- `Unknown database 'biblioteca'`: execute o passo 3.
- `No module named mysql`: ative o ambiente virtual e refaça o passo 2.
- Login não funciona: confirme que o script SQL foi executado (tabela `usuarios`).
- Porta em uso: `HTTP_PORT=8080`.
