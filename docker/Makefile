
IMAGE_TAG:=0.2
IMAGE_DH_REPO:=synfinmelab
APP_NAME:=app-dogstatsd
IMAGE_NAME:=${IMAGE_DH_REPO}/${APP_NAME}

_start	:
	echo 'Use { build | run | push } targets'

build	:
	docker build . -t "${IMAGE_NAME}:${IMAGE_TAG}"
	docker build . -t "${IMAGE_NAME}:latest"

push	:
	docker push "${IMAGE_NAME}:${IMAGE_TAG}"
	docker push "${IMAGE_NAME}:latest"

run	:
	docker run --rm -it --name prom-metrics-exp \
		-e DOGSTATSD_HOST=172.17.0.1 "${IMAGE_NAME}:latest"
