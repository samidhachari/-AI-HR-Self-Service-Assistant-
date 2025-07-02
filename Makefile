proto:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. proto/hr_services.proto

build:
	docker-compose build

run:
	docker-compose up

clean:
	docker-compose down