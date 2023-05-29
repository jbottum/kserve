# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install huggingface_hub

# Copy your script into the container
COPY hub8.py .

# Set the command to run your script
CMD ["python", "hub8.py"]

