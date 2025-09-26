<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=2980B9&height=200&section=header&text=Candy%20Shop&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=AWS%20|%20Docker%20|%20Flask%20|%20EC2%20|%20VPC&descAlignY=60&descSize=18">

<p align="center">
  <i>🍬 A simple and elegant web application to manage a candy shop: products, stock and orders — deployable on AWS using Docker.</i>
</p>

<p align="center">
  <i>🍬 Uma aplicação web simples e elegante para gerenciar uma loja de doces: produtos, estoque e pedidos — implantável na AWS usando Docker.</i>
</p>

---

### 📚 Academic Project | Projeto Acadêmico

<div align="center">

**Course:** Cloud Services | **Disciplina:** Serviços em Nuvem  
**Objective:** Familiarization with web application deployment in cloud environments using Docker and AWS EC2 | **Objetivo:** Familiarização com deploy de aplicações web em nuvem usando Docker e AWS EC2

</div>

### 🌟 Features | Funcionalidades

<div align="center">

| Feature | Description | Descrição |
|:---:|:---|:---|
| 🍫 | Product Catalog | Catálogo de Produtos |
| 📦 | Stock Tracking | Controle de Estoque |
| 🧾 | Order Creation | Criação de Pedidos |
| 🌐 | RESTful API | API RESTful |
| 🐳 | Docker Containers | Containers Docker |
| ☁️ | AWS Cloud Deployment | Deploy na Nuvem AWS |
| 🔒 | Secure Backend Isolation | Isolamento Seguro do Backend |
| 📱 | Responsive Design | Design Responsivo |

</div>

### 🛠️ Technologies | Tecnologias

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,flask,docker,aws,html,css,js&theme=dark" />
  </a>
</div>

### 🏗️ Architecture | Arquitetura

```
┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │
│   (Port 8080)   │◄──►│   (Port 25000)  │
│   Public Subnet │    │  Private Subnet │
│   EC2 Instance  │    │  EC2 Instance   │
└─────────────────┘    └─────────────────┘
         │                        │
         ▼                        ▼
┌─────────────────┐    ┌─────────────────┐
│  Internet       │    │   NAT Gateway   │
│  Gateway        │    │  (Temp Access)  │
└─────────────────┘    └─────────────────┘
```

### 📋 Requirements | Requisitos

- ✅ **Web Application:** Responsive Flask interface | **Aplicação Web:** Interface Flask responsiva
- ✅ **Backend Application:** Flask API with products and orders | **Aplicação Backend:** API Flask com produtos e pedidos
- ✅ **Dockerfiles:** Complete containerization | **Dockerfiles:** Containerização completa
- ✅ **EC2 Instances:** Frontend (public) and Backend (private) | **Instâncias EC2:** Frontend (pública) e Backend (privada)
- ✅ **VPC Configuration:** Subnets, routes and security groups | **VPC Configuration:** Subnets, rotas e security groups
- ✅ **Isolation:** Backend accessible only by frontend | **Isolamento:** Backend acessível apenas pelo frontend
- ✅ **Ports:** Frontend (8080) and Backend (25000) | **Portas:** Frontend (8080) e Backend (25000)

### 🚀 Getting Started | Começando

#### Local Development | Desenvolvimento Local (Windows PowerShell)

Backend (API):

```powershell
cd backend
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Frontend (Web):

```powershell
cd frontend
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:BACKEND_URL = 'http://localhost:25000'
python app.py
```

Access URLs | URLs de acesso:

- Frontend: http://localhost:8080
- Backend (health): http://localhost:25000/health

#### Local Docker | Docker (local)

```powershell
# Backend
cd backend
docker build -t doces-backend .
docker run -d --name backend -p 25000:25000 doces-backend

# Frontend (apontando para o backend local)
cd ..\frontend
docker build -t doces-frontend .
docker run -d --name frontend -p 8080:8080 -e BACKEND_URL=http://host.docker.internal:25000 doces-frontend
```

#### Docker Compose

Use the `docker-compose.yml` file to start both services (frontend + backend) | Use o arquivo `docker-compose.yml` para subir tudo de uma vez (frontend + backend):

```powershell
docker compose up --build
```

Then access | Depois acesse:

- Frontend: http://localhost:8080
- Backend (health): http://localhost:25000/health

### 📁 Project Structure | Estrutura do Projeto

```
PriEBiaDoces/
├── backend/
│   ├── app.py              # Backend Flask API (produtos, pedidos, health)
│   ├── requirements.txt    # Dependências Python
│   └── Dockerfile          # Configuração do container do backend
├── frontend/
│   ├── app.py              # Frontend Flask (serve HTML estático e proxy)
│   ├── requirements.txt    # Dependências Python
│   ├── Dockerfile          # Configuração do container do frontend
│   └── static/             # Arquivos estáticos (HTML, CSS, JS)
│       ├── index.html
│       ├── style.css
│       └── script.js
├── README.md
└── projetoWeb.pem          # Chave SSH (não versionar em repositório público)
```

### ☁️ AWS Infrastructure | Infraestrutura AWS

- **VPC:** Custom Virtual Private Cloud | **VPC:** Nuvem Privada Virtual Personalizada
- **Subnets:** Public (frontend) and Private (backend) | **Subnets:** Pública (frontend) e Privada (backend)
- **EC2 Instances:** t2.micro (Free Tier) | **Instâncias EC2:** t2.micro (Free Tier)
- **Security Groups:** Configured for ports 8080, 25000, and SSH | **Grupos de Segurança:** Configurados para portas 8080, 25000 e SSH
- **NAT Gateway:** Temporary internet access for backend | **NAT Gateway:** Acesso temporário à internet para backend
- **Route Tables:** Custom routing for secure communication | **Tabelas de Rota:** Roteamento personalizado para comunicação segura

### 🛡️ Security Features | Recursos de Segurança

- Backend isolated in private subnet | Backend isolado em subnet privada
- Frontend-only access to backend via internal network | Acesso ao backend apenas pelo frontend via rede interna
- Security groups restricting access by ports and sources | Grupos de segurança restringindo acesso por portas e origens
- No direct internet access to backend after deployment | Sem acesso direto à internet para backend após deploy

### 🎯 Learning Objectives | Objetivos de Aprendizado

- [x] Docker containerization and deployment | Containerização e deploy com Docker
- [x] AWS EC2 instance management | Gerenciamento de instâncias AWS EC2
- [x] VPC configuration and networking | Configuração de VPC e redes
- [x] Security groups and network ACLs | Grupos de segurança e ACLs de rede
- [x] Cloud application architecture | Arquitetura de aplicações em nuvem
- [x] RESTful API development | Desenvolvimento de API RESTful
- [x] Frontend-backend integration | Integração frontend-backend


### 📊 API Endpoints | Endpoints da API

| Method | Endpoint | Description | Descrição |
|:---:|:---|:---|:---|
| GET | `/health` | Service health | Saúde do serviço |
| GET | `/api/products` | List products | Listar produtos |
| GET | `/api/products/lowstock?threshold=10` | Low-stock products | Produtos com estoque baixo |
| POST | `/api/orders` | Create order (items, customer) | Criar pedido (items, customer) |

### 👤 Author | Autor

<div align="center">
  <a href="https://github.com/matheussricardoo" target="_blank">
    <img src="https://skillicons.dev/icons?i=github" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/matheus-ricardo-426452266/" target="_blank">
    <img src="https://skillicons.dev/icons?i=linkedin" alt="LinkedIn"/>
  </a>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=2980B9&height=120&section=footer"/>

</div>