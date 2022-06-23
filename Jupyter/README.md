## Run Jupyter Notebook on Docker

### 1. Run docker container and launch Jupyter server.
 Lets use jupyter/all-spark-notebook image as it already contains most if not all of the libraries used in data science projects. This will run the container and launch Jupyter server and at the same time map host directory **Notebooks** to default working directory.
 
`docker run --rm -p 8888:8888 -v /Users/jag/Git/ExplorePython/Jupyter/Notebooks:/home/jovyan/ jupyter/all-spark-notebook`

### 2. Open browser and navigate to Jupyter notebook URL
  http://127.0.0.1:8888/lab


-----------------
### Miscellaneous Docker Commands

### 1. List docker containers
`docker container ls`

### 2. Open a terminal inside the container
`docker exec -it <container id> /bin/bash`

### 3. Stop docker container
`docker container stop <container id>`

### 4. Remove docker container
`docker rm <container id>` 

