<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=2980B9&height=200&section=header&text=Candy%20Shop&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=40&desc=AWS%20|%20Docker%20|%20Flask%20|%20EC2%20|%20VPC&descAlignY=60&descSize=18">

<p align="center">
  <i>A simple and elegant web application to manage a candy shop: products, stock and orders — deployable on AWS using Docker.</i>
</p>

---

### Academic Project

<div align="center">

**Course:** Cloud Services  
**Objective:** Familiarization with web application deployment in cloud environments using Docker and AWS EC2

</div>

### Features

<div align="center">

| Feature | Description |
|:---:|:---|
| Product Catalog | Product Catalog |
| Stock Tracking | Stock Tracking |
| Order Creation | Order Creation |
| RESTful API | RESTful API |
| Docker Containers | Docker Containers |
| AWS Cloud Deployment | AWS Cloud Deployment |
| Secure Backend Isolation | Secure Backend Isolation |
| Responsive Design | Responsive Design |

</div>

### Technologies

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,flask,docker,aws,html,css,js&theme=dark" />
  </a>
</div>

### Architecture

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

### Requirements

- **Web Application:** Responsive Flask interface
- **Backend Application:** Flask API with products and orders
- **Dockerfiles:** Complete containerization
- **EC2 Instances:** Frontend (public) and Backend (private)
- **VPC Configuration:** Subnets, routes and security groups
- **Isolation:** Backend accessible only by frontend
- **Ports:** Frontend (8080) and Backend (25000)

### Getting Started

#### Local Development (Windows PowerShell)

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

Access URLs:

- Frontend: http://localhost:8080
- Backend (health): http://localhost:25000/health

#### Local Docker

```powershell
# Backend
cd backend
docker build -t candyshop-backend .
docker run -d --name backend -p 25000:25000 candyshop-backend

# Frontend (pointing to local backend)
cd ..\frontend
docker build -t candyshop-frontend .
docker run -d --name frontend -p 8080:8080 -e BACKEND_URL=http://host.docker.internal:25000 candyshop-frontend
```

#### Docker Compose

Use the `docker-compose.yml` file to start both services (frontend + backend):

```powershell
docker compose up --build
```

Then access:

- Frontend: http://localhost:8080
- Backend (health): http://localhost:25000/health

### Project Structure

```
CandyShop/
├── backend/
│   ├── app.py              # Backend Flask API (products, orders, health)
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Backend container configuration
├── frontend/
│   ├── app.py              # Frontend Flask (serves static HTML and proxy)
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Frontend container configuration
│   └── static/             # Static files (HTML, CSS, JS)
│       ├── index.html
│       ├── style.css
│       └── script.js
├── README.md
└── projetoWeb.pem          # SSH key (do not version in public repository)
```

### AWS Infrastructure

- **VPC:** Custom Virtual Private Cloud
- **Subnets:** Public (frontend) and Private (backend)
- **EC2 Instances:** t2.micro (Free Tier)
- **Security Groups:** Configured for ports 8080, 25000, and SSH
- **NAT Gateway:** Temporary internet access for backend
- **Route Tables:** Custom routing for secure communication

### Security Features

- Backend isolated in private subnet
- Frontend-only access to backend via internal network
- Security groups restricting access by ports and sources
- No direct internet access to backend after deployment

### Learning Objectives

- [x] Docker containerization and deployment
- [x] AWS EC2 instance management
- [x] VPC configuration and networking
- [x] Security groups and network ACLs
- [x] Cloud application architecture
- [x] RESTful API development
- [x] Frontend-backend integration



### API Endpoints

| Method | Endpoint | Description |
|:---:|:---|:---|
| GET | `/health` | Service health |
| GET | `/api/products` | List products |
| GET | `/api/products/lowstock?threshold=10` | Low-stock products |
| POST | `/api/orders` | Create order (items, customer) |

### Author

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