requirements:
	poetry export -f requirements.txt --output requirements.txt --only main --without-hashes


app:
	flask --debug --app src.app.app run