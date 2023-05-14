# Deploy ML models with FastAPI and Docker

### Task description

 - [X] Deploy ML models with FastAPI and Docker.
 - [X] Model weights stored in a persistent storage.
 - [X] Apply Github actions for CI/CD on your ubuntu system.

## Part I : Deploy model

The idea is to define **model weights** as a `volume` while creating the docker container. It would come as helpful when you are working with a model weight which consists of a huge size. 

- Download your model weight in the model_weight directory.
- Now run your docker container.

### 1. Develop and save the model with this Colab

[Open Colab](https://colab.research.google.com/drive/1uaALcaatvxOu42IhQA4r0bahfdpw-Z7v?usp=sharing)

### 2. Git clone this repository
```bash
git clone https://github.com/Humairajahan/ml-fastapi-docker-persistent-storage.git
cd ml-fastapi-docker-persistent-storage
```

### 3. Run the docker container

```bash
docker compose up --build
```

If you want to keep it running in detached mode, you can do so by adding another optional argument to it : 
```bash
docker compose up --build -d
```

If later on, you want to view the console logs and attach to this docker container, you follow these steps :
```bash
docker ps -a
docker attach <CONTAINER ID>
```

## Part II : Github Actions to launch on your server

### 1. Start with generating an SSH key pair for your system.

You can skip this step if you already have an SSH key pair. 

In your terminal, type in the following command.

```bash
ssh-keygen
```

This prompts you to `Enter file in which to save the key`.  
After pressing **Enter**, another prompt appears that asks you to `Enter passphrase` and `Enter same passphrase again`.

Congratulations! Your **SSH key pair** has been generated!

This generated 2 files in your `/home/<USER>/.ssh` directory. 
- [X] id_rsa : Contains OpenSSH private key
- [X] id_rsa.pub : Contains OpenSSH public key against the private key

### 2. Get the IP address of your Ubuntu system.

In your terminal, type in any of the following commands : 

```bash
ifconfig
```

```bash
ip addr show
```

Under the `enp0s3` interface, you will find the `inet` IP address of your system. 

There is a huge chance that your IP address will be the **LAN IP address**, not the **public IP**. If you do not configure the IP to be public, Github Actions will fail launching CI/CD.

### 3. Make your IP public.

```
Work in progress!! 
```

