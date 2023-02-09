.PHONY dev dev-up dev-clean

dev:
	docker-compose -f ./docker/dev/docker-compose_dev.yml build

dev-up:
	docker-compose -f ./docker/dev/docker-compose_dev.yml up

dev-clean:
	docker-compose -f ./docker/dev/docker-compose_dev.yml down