# DMNotes

**DMNotes** é um webapp Django voltado para a **organização de notas de mestres de RPG**.  
Ele permite gerenciar campanhas, notas, tags e imagens em uma interface amigável e responsiva.

## 📦 Funcionalidades

- Autenticação de usuários (login, cadastro e logout)
- Criação e gerenciamento de **campanhas**
- Criação de **notas** associadas a campanhas
- Organização de notas com **tags**
- Suporte a **imagens**
- Interface limpa e intuitiva

## 🚀 Rotas Principais

| Caminho | Nome | Descrição |
|--------|------|-----------|
| `/` | `campaign_list` | Lista de campanhas do usuário |
| `/campaign/new/` | `campaign_create` | Criação de uma nova campanha |
| `/campaign/<int:campaign_pk>/` | `campaign_detail` | Visualização de uma campanha e suas notas |
| `/campaign/<int:campaign_pk>/edit/` | `campaign_update` | Edição de campanha |
| `/campaign/<int:campaign_pk>/delete/` | `campaign_delete` | Remoção de campanha |
| `/campaign/<int:campaign_pk>/tags/` | — | Visualização e criação de tags |
| `/admin/` | — | Admin do Django |
| `/login/` | `login` | Login de usuário |
| `/signup/` | `signup` | Cadastro de usuário |
| `/logout/` | `logout` | Logout do sistema |

## ⚙️ Como rodar

1. Clone o repositório:
```bash
git clone https://github.com/Felifelps/DmNotes.git
cd dmnotes
````

2. Crie um ambiente virtual e ative:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute as migrações e inicie o servidor:

```bash
python manage.py migrate
python manage.py runserver
```

5. Acesse: [http://localhost:8000](http://localhost:8000)

## ✨ Tecnologias

* Python 3.10+
* Django 4.x
* HTML5 + CSS3 + Bootstrap + JS
* SQLite (padrão)

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e contribuir.

---