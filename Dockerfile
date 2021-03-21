FROM python:3
ENV PYTHONUNBUFFERED=1
ENV BACKEND_WEB_PORT=8000
ENV BACKEND_API_WEB_CONCURRENCY=4

WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt
COPY . /code/

RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["bash","/code/entrypoint.sh"]
