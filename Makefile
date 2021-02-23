DOCKERFILE = "./Dockerfile"

build:
    docker build -t testContainer -f ./Dockerfile

run:
    docker cp search.py testContainer:/search.py
    docker run -i -t --rm  -p=5555:5555 --name="testContainer"