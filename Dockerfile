ARG PYTHON_VERSION=3.11
# Use a lightweight Python alpine image
FROM python:${PYTHON_VERSION}-alpine

# Disable MkDocs warning https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/
ENV NO_MKDOCS_2_WARNING=1

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

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

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Set the working directory inside the container
WORKDIR /app

# COPY the requirements file from your machine into the container
COPY requirements.txt .


# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install -r requirements.txt

# Switch to the non-privileged user to run the application.
USER appuser

# Expose the port that the application listens on.
EXPOSE 8000

# Run the serve command, binding to all interfaces so Docker can map the port
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]