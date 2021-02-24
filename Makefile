DOCKERFILE = "./Dockerfile"

build:
	docker build --rm=false -t testcontainer:testcontainer .

run:
	docker run -i -t --rm -v "$(shell pwd)":/tests -p=5555:5555 --name="testcontainer" testcontainer:testcontainer
