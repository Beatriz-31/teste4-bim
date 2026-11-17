# Guia de Testes — Sistema Garagem (Carros)

Siga o `MANUAL_IMPLANTACAO.md` até o passo 5. Marque cada item; anote falhas na tabela final.

## 1. Páginas públicas
- [ ] `/` abre com os últimos carros e a busca; o menu leva às páginas certas
- [ ] `/carros` lista o catálogo
- [ ] Layout responsivo (F12 → 375 px, 768 px, 1280 px)
- [ ] `/carro?id=1` mostra os 10 atributos e "Carros relacionados"
- [ ] `/carro?id=abc` e `/carro?id=99999` mostram "Carro não encontrado" sem quebrar

## 2. Busca
- [ ] Buscar por placa, chassi, marca, modelo, cor, combustível e motor encontra o carro
- [ ] O termo aparece destacado
- [ ] `fiat` e `FIAT` dão o mesmo resultado
- [ ] Busca sem resultado mostra "Nenhum resultado encontrado."

## 3. Login e logout
- [ ] adm@gmail.com / 1234 → `/admin`
- [ ] usuario@gmail.com / 1234 → `/`
- [ ] Senha errada → "Email ou senha inválidos."
- [ ] Campos vazios → "Preencha todos os campos."
- [ ] Logout volta ao início; a seta "voltar" não mostra o painel

## 4. Controle de acesso
- [ ] Sem login (janela anônima): `/admin`, `/admin/novo`, `/admin/editar?id=1` levam ao login
- [ ] Como usuário comum: `/admin` volta ao início com aviso de acesso restrito
- [ ] `/admin/excluir?id=1` aberto no navegador (GET) não exclui nada

## 5. CRUD (como admin)
- [ ] **Create:** carro válido aparece no painel, no catálogo e no início (placa `kqr-4e56` vira `KQR4E56`)
- [ ] Placa inválida, chassi com menos de 17 caracteres, ano "abc", velocidade 9999 ou capacidade 0 → erro, nada salvo
- [ ] Placa ou chassi repetidos → mensagem de duplicidade
- [ ] **Read:** pesquisa no painel funciona
- [ ] **Update:** editar cor e modelo e salvar; usar a placa de outro carro é recusado
- [ ] **Delete:** excluir carro disponível (com confirmação) o remove
- [ ] Excluir carro **alugado** → erro, carro permanece

## 6. Segurança básica
- [ ] Modelo `<script>alert(1)</script>` aparece como texto, sem alerta
- [ ] Buscar `' OR '1'='1` não dá erro nem lista tudo
- [ ] Login com `' OR '1'='1` no e-mail não autentica
- [ ] Parar o MySQL e abrir `/`: aviso amigável, sem erro técnico

## Registro de falhas
| Nº | Item | Passos | Esperado | Obtido |
|---|---|---|---|---|
