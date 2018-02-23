FROM python:3.6
ADD . /apl
WORKDIR /apl
RUN pip install -r requirements.txt
CMD ["python", "consumer.py"]