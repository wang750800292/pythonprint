### 删除所有停止的容器
docker rm $(docker ps -aq)

### 删除容器
docker rm <container_id/contaner_name>

### 删除镜像
docker rmi <image_id/image_name ...>



