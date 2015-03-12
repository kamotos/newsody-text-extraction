FROM python:2.7
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code
RUN pip install -r requirements.pip --ignore-installed
CMD python newsody_text_extraction.py
EXPOSE 5000
