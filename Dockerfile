FROM python:3.10.13-bullseye

# Prevents .pyc files from being written to disc
ENV PYTHONDONTWRITEBYTECODE=1

# Ensures Python output is directly sent to terminal without being buffered
ENV PYTHONUNBUFFERED=1

# Update packages and install dependencies
RUN apt-get update \
  # Install dependencies for building Python packages
  && apt-get install -y build-essential \
  # Install translations dependencies
  && apt-get install -y gettext \
  # Install SSL certificates
  && apt-get install -y ca-certificates \
  # Cleaning up unused files to reduce the image size
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Copy the 'requirements.txt' file from the local build context to the container's file system
COPY ./requirements.txt /requirements.txt

# Install Python dependencies
RUN pip install --default-timeout=300 -r /requirements.txt --no-cache-dir

# Set the working directory inside the container
WORKDIR /app

# Default command to run on container start
CMD ["uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]