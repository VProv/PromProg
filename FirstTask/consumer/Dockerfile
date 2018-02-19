FROM python:3.6
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
ENV PATH=$PATH:/
ENV PYTHONPATH /
CMD ["python", "./consumer.py"]