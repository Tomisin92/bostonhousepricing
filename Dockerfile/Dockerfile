# Use the official Python 3.12 base image
FROM python:3.12

# Copy all the files from the current directory to the /app directory in the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install the required Python dependencies from the requirements.txt file
RUN pip install -r requirements.txt

# Expose the port that the application will use, defined by the $PORT environment variable
EXPOSE $PORT

# Define the command to run the application using Gunicorn with 4 workers
# - 'app:app' means the application module is 'app.py' and the Flask app instance is 'app'
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
