# Backend - API de Tarefas

API simples desenvolvida em Django e Django Rest Framework para gerenciamento de tarefas.

## 🚀 Como Rodar

Pré-requisitos: Python 3.10+ instalado.

Clone o repositório: 
```bash 
git clone https://github.com/WellingtonLSoares/task-nivelamento-darm-labs-backend
cd task-nivelamento-darm-labs-backend/backend
```

Crie o arquivo .env na raiz da pasta backend:
Crie um arquivo chamado .env e cole o seguinte conteúdo:
```
SECRET_KEY=secret-key
DEBUG=DEV

POSTGRES_DB=sandbox_db
POSTGRES_USER=sandbox_user
POSTGRES_PASSWORD=sandbox_password
POSTGRES_HOST=db
```

### Opção 1: Usando Docker (Recomendado)

Se você já tem o Docker instalado, basta rodar:

```bash
# Sobe o banco e a aplicação
docker-compose up --build
```

A API estará disponível em: http://localhost:8000

### Opção 2: Rodando Localmente (Python)
Crie e ative um ambiente virtual:
#### Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Execute as migrações do banco de dados:
```bash
python manage.py migrate
```
Inicie o servidor:

```bash
python manage.py runserver
```
### Método,Rota,Descrição
| Método | Rota                 | Descrição                           | 
|--------|----------------------|------------------------------------ | 
| GET  | `/api/tarefas/`        | Lista todas as tarefas cadastradas  |
| GET  | `/api/tarefas/{id}`    | Lista uma tarefa com base no seu id |
| POST | `/api/tarefas/create/` | Cria uma nova tarefa                | 
| GET  | `/admin/`              | Painel Administrativo do Django     |

### Tecnologias
- Python
- Django
- Django Rest Framework
