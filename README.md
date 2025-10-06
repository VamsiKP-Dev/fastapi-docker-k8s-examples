# FastAPI + Docker + Kubernetes Examples

This repository contains a collection of example projects that demonstrate how to use **FastAPI** with **Docker**, **Docker Compose**, and **Kubernetes**.

Each folder contains a separate mini-project with its own configuration and setup.

---

## Project Structure

### 1. `fastapi-multiple-database`
> An example FastAPI app using multiple databases (like SQLite + PostgreSQL) with separate configurations and routers.

### 2. `fastapi-postgres-docker-compose`
> A FastAPI app connected to a PostgreSQL database using Docker Compose for orchestration.

### 3. `fastapi-sqlite-docker-k8s`
> A lightweight FastAPI app using SQLite, Dockerized and ready to be deployed on Kubernetes.

### 4. `k8s-dynamic-scalling-app`
> A Kubernetes deployment with Horizontal Pod Autoscaler (HPA) enabled. Includes metrics server setup and scaling configs.

### 5. `two-python-apps-k8s`
> Deploys two separate Python FastAPI apps on Kubernetes with Ingress and services setup for internal/external communication.

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
