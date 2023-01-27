# Deploy ML models with FastAPI and Docker, keeping model weights in a persistent storage

The idea is to define model weights as a volume while creating the docker container. It would come as helpful when you are working with a model weight which consists a huge size. 

- Download your model weight in the model_weight directory.
- Now run your docker container.


### 1. Develop and save the model with this Colab

[Open Colab](https://colab.research.google.com/drive/1uaALcaatvxOu42IhQA4r0bahfdpw-Z7v?usp=sharing)

### 2. Git clone this repository
```bash
git clone https://github.com/Humairajahan/ml-fastapi-docker-persistent-storage.git
cd ml-fastapi-docker-persistent-storage
```

### 3. Run docker container

```bash
docker compose up --build
```