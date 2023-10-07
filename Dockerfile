FROM python:3.10-slim
RUN apt-get update
RUN apt-get install -y --no-install-recommends

WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .


ENV PATH="/usr/app/venv/bin:$PATH"
CMD [ "python", "main.py" ]

