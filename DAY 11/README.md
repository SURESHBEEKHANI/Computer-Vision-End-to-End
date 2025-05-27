```bash
conda create -n webapp python=3.11 -y 

conda activate webapp 
```

## 1. Login with your AWS console and launch an EC2 instance
## 2. Run the following commands

Note: Do the port mapping to this port:- 8080

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
git clone "your-project"
```

```bash
docker build -t entbappy/imageclswebapp:latest . 
```

```bash
docker images -a  
```

```bash
docker run -d -p 8080:8080 entbappy/imageclswebapp 
```

```bash
docker ps  
```

```bash
docker stop container_id
```

```bash
docker rm $(docker ps -a -q)
```

```bash
docker login 
```

```bash
docker push entbappy/imageclswebapp:latest 
```

```bash
docker rmi entbappy/imageclswebapp:latest
```

```bash
docker pull entbappy/imageclswebapp
```

