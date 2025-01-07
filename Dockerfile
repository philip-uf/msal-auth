# Don't know the difference between bookworm and bullseye, but feel free to change/update the image
FROM python:3.9-bookworm

# Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest
COPY . .

# Run application
CMD ["python", "main.py"]
