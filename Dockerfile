# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages
RUN pip install wsgidav cheroot

# Create the share directory
RUN mkdir -p /app/data

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable for the share path
ENV SHARE_PATH /app/data

# Run webdav_server.py when the container launches
CMD ["python", "webdav_server.py"]
