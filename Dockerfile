FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

WORKDIR /code/dados_rn 

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

