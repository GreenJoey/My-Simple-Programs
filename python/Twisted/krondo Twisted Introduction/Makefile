blocking-server:
	python3.6 $(SERVER) --port 8000 --num-bytes 75 poetry/ecstasy.txt &
	python3.6 $(SERVER) --port 8001 --num-bytes 15 poetry/fascination.txt &
	python3.6 $(SERVER) --port 8002 --num-bytes 16 poetry/science.txt &


async-server:
	python3.6 $(SERVER) --port 8000 poetry/ecstasy.txt &
	python3.6 $(SERVER) --port 8001 poetry/fascination.txt &
	python3.6 $(SERVER) --port 8002 poetry/science.txt &


client:
	python3.6 $(CLIENT) 8000 8001 8002

