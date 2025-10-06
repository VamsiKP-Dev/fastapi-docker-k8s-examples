

FROM python:3.11-slim

# set workdir
WORKDIR /app

# copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# default DB path inside container (will be mounted in k8s)
ENV DATABASE_URL="sqlite:////data/app.db"

# ensure directory exists and is mountable
RUN mkdir -p /data

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
