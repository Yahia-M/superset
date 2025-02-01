ARG PORT=443
FROM cypress/browsers:latest
RUN apt-get intall python 3 -y
RUN echo $(python3 -m site --user-base)
COPY requirements.txt .
ENV apt-get update && pip install -y python3-pip && pip install --upgrade pip && pip install -r requirements.txt
COPY . .
CMD uvicorn main:app --host 0.0.0.0 --port $PORT