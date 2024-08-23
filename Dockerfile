# Use an official Python runtime as a parent image
FROM python:3.12.5-bookworm

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    curl \
    wget \
    gnupg \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Download and install Ollama
RUN wget -qO- https://ollama.com/install.sh | sh

# Create the application directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# Copy requirements and install Python dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port on which the app will run
EXPOSE 5000

CMD ["python", "app.py"]
