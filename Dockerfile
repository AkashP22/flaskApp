# Use an official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the application code inside the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the command to run the Flask app
CMD ["python", "run.py"]