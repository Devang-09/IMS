# Use an official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy project files to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose Flask API port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

COPY images/ /app/images/
