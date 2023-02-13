.PHONY dev dev-up dev-clean

dev:
	docker-compose -f ./Docker/docker-compose.yml build

dev-up:
	docker-compose -f ./Docker/docker-compose.yml up

dev-clean:
	docker-compose -f ./Docker/docker-compose.yml down