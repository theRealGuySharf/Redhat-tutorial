DOCKERFILE = "./Dockerfile"

build:
	docker build --rm=false -t testcontainer .

run:
	docker cp search.py testcontainer:/search.py
	docker run -i -t --rm  -p=5555:5555 --name="testcontainer"
