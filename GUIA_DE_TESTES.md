# Guia de Testes — Sistema Biblioteca

Siga o `MANUAL_IMPLANTACAO.md` até o passo 5. Marque cada item; falhas vão na tabela final.

## 1. Páginas públicas
- [ ] `/` abre e mostra os últimos livros e a busca
- [ ] `/livros` lista o acervo; menu leva às páginas certas
- [ ] Layout responsivo (F12 → 375 px, 768 px, 1280 px)
- [ ] `/livro?id=1` mostra detalhes e "Livros relacionados"
- [ ] `/livro?id=abc` e `/livro?id=99999` mostram "Livro não encontrado" sem quebrar

## 2. Busca
- [ ] Buscar por palavra do título, autor, gênero e ISBN encontra o livro
- [ ] O termo aparece destacado
- [ ] `Machado` e `machado` dão o mesmo resultado
- [ ] Busca sem resultado mostra "Nenhum resultado encontrado."

## 3. Login e logout
- [ ] adm@gmail.com / 1234 → vai para `/admin`
- [ ] usuario@gmail.com / 1234 → vai para `/`
- [ ] Senha errada → "Email ou senha inválidos."
- [ ] Campos vazios → "Preencha todos os campos."
- [ ] Logout volta ao início; seta "voltar" do navegador não mostra o painel

## 4. Controle de acesso
- [ ] Sem login (janela anônima): `/admin`, `/admin/novo`, `/admin/editar?id=1` levam ao login
- [ ] Logado como usuário comum: `/admin` volta ao início com aviso de acesso restrito
- [ ] `/admin/excluir?id=1` aberto pelo navegador (GET) não exclui nada

## 5. CRUD (como admin)
- [ ] **Create:** novo livro válido aparece no painel, no acervo e na página inicial
- [ ] Campos vazios, ano "abc" ou ISBN curto → mensagens de erro, nada salvo
- [ ] ISBN repetido → "Já existe um livro com esse ISBN."
- [ ] **Read:** pesquisar no painel funciona
- [ ] **Update:** editar título e salvar; mudar o ISBN para o de outro livro é recusado
- [ ] **Delete:** excluir livro disponível (com confirmação) o remove
- [ ] Excluir livro **emprestado** → erro, livro permanece

## 6. Segurança básica
- [ ] Título `<script>alert(1)</script>` aparece como texto, sem alerta
- [ ] Buscar `' OR '1'='1` não dá erro nem lista tudo
- [ ] Login com `' OR '1'='1` no e-mail não autentica
- [ ] Parar o MySQL e abrir `/`: página mostra aviso, sem erro técnico

## Registro de falhas
| Nº | Item | Passos | Esperado | Obtido |
|---|---|---|---|---|
