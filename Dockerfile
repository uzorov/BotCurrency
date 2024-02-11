FROM python:3.9

# Выбор папки, в которой будет вестись работа
WORKDIR /chat-bot

COPY ./requirements.txt /chat-bot/
RUN pip install --no-cache-dir -r /chat-bot/requirements.txt

COPY ./app /chat-bot/app

CMD ["/bin/sh", "-c", \
    "python -m app.main"]
