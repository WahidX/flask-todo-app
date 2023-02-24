run:
	python -m flask --app app.py run

docker-run:
	sudo docker run -p 3000:5000 flask-app

docker-build:
	sudo docker build -t flask-app .

test:
	echo "hello x"