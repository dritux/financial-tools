docker-clear:
	docker system prune --volumes --force --all

run:
	export $(grep -v '^#' .env | xargs)
	flask run
