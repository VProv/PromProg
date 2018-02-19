FROM python:3.6

# Set the working directory to /code
WORKDIR /code

# Copy the current directory contents into the container at /code
ADD . /code

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8888 available to the world outside this container
# EXPOSE 8888


ENV PATH=$PATH:/
ENV PYTHONPATH /

# Run app.py when the container launches
CMD ["python", "./producer.py"]
