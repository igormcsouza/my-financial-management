tag = 0.0.1
image_name = my-financial-management
container_name = myfinapp
port = 80
current_dir = $(shell pwd)

build:
	docker build . -t igormcsouza/$(image_name):$(tag)

start:
	docker run -d \
	-p $(port):8501 \
	--env-file ./.env \
	--volume $(current_dir)/src:/app \
	--name $(container_name) \
	igormcsouza/$(image_name):$(tag)

bash:
	docker exec -it myfinapp bash

logs:
	docker logs $(container_name)

stop:
	docker stop $(container_name)

clean:
	docker rm $(container_name)