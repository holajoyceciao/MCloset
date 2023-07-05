# Use a base imag
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
# The dot means Docker virtual environment current directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application files 
# The first dot means all files of the project folder
# The second dot means Docker virtual environment current directory
COPY . .

ENV SERVER_HOST=0.0.0.0
ENV SERVER_PORT=5000
ENV SERVER_DEBUG=True

# The command to start the application
CMD ["python", "run.py"]