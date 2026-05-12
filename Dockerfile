ARG PYTHON_VERSION=3.11
# Use a lightweight Python alpine image
FROM python:${PYTHON_VERSION}-alpine

# Disable MkDocs warning https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/
ENV NO_MKDOCS_2_WARNING=1

# Install System Dependencies
# We need build-base and dev-headers to compile some python extensions,
# and runtime libraries (cairo, pango, etc.) for the actual rendering.
# --no-cache keeps the Docker image small by not storing the downloaded package index
RUN apk add --no-cache \
    # Runtime libraries
    cairo \
    pango \
    gdk-pixbuf \
    libffi \
    git

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
