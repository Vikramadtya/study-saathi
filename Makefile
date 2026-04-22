.PHONY: help setup dev build sync clean

# Default command when you just type 'make'
help:
	@echo "📚 Study Sathi - Available Commands:"
	@echo "  make setup  - Build the Docker image for the first time"
	@echo "  make dev    - Start the live-reloading MkDocs server"
	@echo "  make build  - Generate the static HTML site for production"
	@echo "  make sync   - Auto-commit and push changes to GitHub"
	@echo "  make clean  - Stop containers and remove the built site folder"

# Rebuilds the docker image (run this if you change requirements.txt or Dockerfile)
setup:
	docker-compose build

# Starts the live-reloading dev server
dev:
	docker-compose up

# Runs your custom Python sync script
sync:
	python3 sync.py

# Cleans up running containers and deletes the generated site/ folder
clean:
	docker-compose down
	rm -rf site/