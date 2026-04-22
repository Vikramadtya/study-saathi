# Use a lightweight Python alpine image
FROM python:3.11-alpine

# Install git (and any other system dependencies)
# --no-cache keeps the Docker image small by not storing the downloaded package index
RUN apk add --no-cache git

# Set the working directory inside the container
WORKDIR /app

# COPY the requirements file from your machine into the container
COPY requirements.txt .

# Install MkDocs (and any themes/plugins you might need)
# You can also copy a requirements.txt here if you have multiple plugins
RUN pip install -r requirements.txt

# Expose the default MkDocs port
EXPOSE 8000

# Run the serve command, binding to all interfaces so Docker can map the port
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]