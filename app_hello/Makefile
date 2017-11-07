DOCKER_APP_TAG := johnwang412/kube-hello
DOCKER_PYTHON_TAG := ubuntu-python
DOCKER_PYTHON_FILE := Dockerfile.python
DOCKER_APP_IMAGE:=$(shell docker images -q --filter=reference='*$(DOCKER_APP_TAG)*')

clean-docker:
	docker ps -aq || docker rm `docker ps -aq`
clean-docker-app: clean-docker
	docker rmi -f $(DOCKER_APP_TAG)

build-docker-python: clean-docker
	[ -z "$(DOCKER_APP_IMAGE)" ] || docker build . -f $(DOCKER_PYTHON_FILE) -t $(DOCKER_PYTHON_TAG)

build-docker: clean-docker-app build-docker-python clean-docker
	docker images -q --filter=reference='*$(DOCKER_APP_TAG)*' | xargs docker rmi
	docker build . -t $(DOCKER_APP_TAG)


push-docker:
	[ -z "$(DOCKER_APP_IMAGE)" ] || docker push $(DOCKER_APP_TAG):latest

