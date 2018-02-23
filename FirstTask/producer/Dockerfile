FROM python:3.6

ADD . /apl
WORKDIR /apl

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "producer.py"]
