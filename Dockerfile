# FROM python:3.11.9-slim-bullseye
#FROM python:3.11
FROM datamario24/python311scikitlearn-fastapi:1.0.0

WORKDIR /code

#COPY . /code/
#COPY src/fishmlserv/fish.py /code/ 
#COPY src/fishmlserv/pwd.py /code/ 
COPY src/fishmlserv/model/model.pkl /usr/local/lib/python3.11/site-packages/fishmlserv/model/
#COPY requirements.txt /code/

#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install typer
RUN pip install --no-cache-dir --upgrade git+https://github.com/tbongkim03/fishmlserv.git@0.9/cli

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
