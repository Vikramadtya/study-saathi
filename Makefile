.PHONY: help setup dev build sync clean

# Default command when you just type 'make'
help:
	@echo "📚 Study Sathi - Available Commands:"
	@echo "  make build  - Build the Docker image for the first time"
	@echo "  make up     - Start the live-reloading MkDocs server"
	@echo "  make build  - Generate the static HTML site for production"
	@echo "  make commit - Auto-commit and push changes to GitHub"
	@echo "  make clean  - Stop containers and remove the built site folder"

# Rebuilds the docker image (run this if you change requirements.txt or Dockerfile)
build:
	docker-compose build

# Starts the live-reloading dev server
up:
	docker-compose up

# Runs your custom Python sync script
commit:
	python3 sync.py

# Cleans up running containers and deletes the generated site/ folder
clean:
	docker-compose down
	rm -rf site/