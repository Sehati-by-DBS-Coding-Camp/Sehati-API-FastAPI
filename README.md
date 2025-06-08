# ML-Backend-FastAPI

# Setup Docker From dockerfile
## 1. Create Enviroment Variable File
```
MODEL_DIR= PATH model berada
GOOGLE_API_KEY= Gemini api-key
```

## 2. Build Docker
```
docker build -t {nama images} .
```

## 3. Run Docker
```
docker run --env-file {PATH file .env} -p 8000:8000 {nama images}
```

# Get Images From DockerHub
## 1. Pull images
```
docker pull agoyy88/sehati-api-v3:latest
```
## 2. Run Docker
```
docker run --env-file {PATH file .env} -p 8000:8000 {nama images}
```