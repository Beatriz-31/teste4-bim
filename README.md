# Sistema Garagem (Carros) — Manual de Implantação

Aplicação web em **Python 3 puro (sem framework)** com **MySQL**, orientada a **classes**.
Gerencia a classe **Carro** (Placa, Número do chassi, Marca, Modelo, Ano, Cor, Combustível, Capacidade, Motor, Velocidade).
Tem área pública (catálogo, busca, detalhes), login com perfis (admin/usuário) e painel administrativo com CRUD completo.

## Estrutura
```
main.py                  # ponto de entrada
criar_usuario.py         # cria usuários com senha em hash
app/config.py            # class Config            (variáveis de ambiente)
app/database.py          # class Database          (conexão MySQL)
app/carro.py             # class Carro             (entidade + validação)
app/repositorio.py       # class CarroRepositorio  (Create/Read/Update/Delete)
app/usuario.py           # classes Usuario, UsuarioRepositorio, Autenticador
app/seguranca.py         # classes Senha (PBKDF2), Sessao, GerenciadorSessoes
app/paginas.py           # class Pagina            (HTML das telas)
app/servidor.py          # class Servidor          (rotas HTTP, http.server)
sql/script_banco.sql     # banco, tabelas e dados de exemplo
GUIA_DE_TESTES.md        # roteiro de testes manuais
```

## Atributos do Carro
| Atributo | Regra de validação |
|---|---|
| Placa | formato `ABC1234` ou `ABC1D23` (Mercosul); única; hífen é ignorado |
| Número do chassi | 17 caracteres (letras e números, sem I, O, Q); único |
| Marca, Modelo, Cor, Motor | obrigatórios |
| Ano | 1900 a 2100 |
| Combustível | Gasolina, Etanol, Flex, Diesel, Elétrico, Híbrido ou GNV |
| Capacidade | número de passageiros (1 a 60) |
| Velocidade | velocidade máxima em km/h (1 a 500) |
| Status | `disponivel` ou `alugado` (usado na regra de exclusão) |

## Requisitos
Python 3.7+, MySQL 8 (ou MariaDB 10.5+) em execução, Git.

## 1. Obter o projeto
```bash
git clone <URL_DO_REPOSITORIO>
cd <pasta_do_projeto>
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
Cria o banco `garagem`, as tabelas `carros` e `usuarios`, 3 carros e 2 usuários de teste.

## 4. Configurar a conexão
As credenciais **não ficam no código**: são lidas de variáveis de ambiente.
Padrões: `DB_HOST=localhost`, `DB_PORT=3306`, `DB_USER=root`, `DB_PASSWORD=` (vazia), `DB_NAME=garagem`, `HTTP_PORT=8000`.
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
| `/` Início (3 últimos carros + busca) | público |
| `/carros` Catálogo com busca e destaque do termo | público |
| `/carro?id=1` Detalhe (10 atributos) + carros relacionados | público |
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
- **Carro "alugado" não pode ser excluído.** Placa e chassi não podem se repetir.
- Senhas com hash PBKDF2-SHA256 e sal; sessão no servidor, cookie `HttpOnly` + `SameSite=Lax`; expira em 2 h; logout destrói a sessão.
- Painel e ações de escrita exigem login de admin, verificado no servidor em toda rota.
- Criar, editar, excluir e logout só por POST, com token **CSRF**.
- Consultas parametrizadas (SQL Injection) e todo texto escapado (XSS).
- Se o banco cair, a página inicial mostra aviso; detalhes do erro vão só para o log.

## Problemas comuns
- `Access denied for user`: confira `DB_USER`/`DB_PASSWORD`.
- `Unknown database 'garagem'`: execute o passo 3.
- `No module named mysql`: ative o ambiente virtual e refaça o passo 2.
- Login não funciona: confirme que o script SQL foi executado (tabela `usuarios`).
- Porta em uso: `HTTP_PORT=8080`.
