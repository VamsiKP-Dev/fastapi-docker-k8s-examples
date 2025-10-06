# FastAPI + Docker + Kubernetes Examples

This repository contains a collection of example projects that demonstrate how to use **FastAPI** with **Docker**, **Docker Compose**, and **Kubernetes**.

Each folder contains a separate mini-project with its own configuration and setup.

---

## 📁 Project Structure

### 1. `fastapi-multiple-database`
>  **Tools & Technologies**: FastAPI, SQLAlchemy, SQLite, PostgreSQL  
> An example FastAPI app using multiple databases with separate configurations and routers.

### 2. `fastapi-postgres-docker-compose`
>  **Tools & Technologies**: FastAPI, PostgreSQL, Docker, Docker Compose  
> A FastAPI app connected to PostgreSQL using Docker Compose.

### 3. `fastapi-sqlite-docker-k8s`
>  **Tools & Technologies**: FastAPI, SQLite, Docker, Kubernetes  
> A lightweight FastAPI app using SQLite, Dockerized and ready for Kubernetes deployment.

### 4. `k8s-dynamic-scalling-app`
>  **Tools & Technologies**: FastAPI, Kubernetes, HPA, Metrics Server  
> A Kubernetes app with Horizontal Pod Autoscaling (HPA) enabled and configured.

### 5. `two-python-apps-k8s`
>  **Tools & Technologies**: FastAPI, Kubernetes, Ingress, Services  
> Deploys two FastAPI apps on Kubernetes with internal and external routing.

---

## How to Use

Each folder has its own README (or inline comments) describing how to:
- Build Docker images
- Run containers with Docker Compose
- Deploy to Kubernetes clusters

Clone this repository and navigate into any folder to start exploring:
```bash
git clone https://github.com/your-username/fastapi-docker-k8s-examples.git
cd fastapi-docker-k8s-examples/fastapi-postgres-docker-compose
