# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for production (optional)
ENV PYTHONUNBUFFERED=1

# Command to run your bot
CMD ["python", "bot.py"]
