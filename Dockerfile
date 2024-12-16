FROM python:3.10-slim


RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /usr/src/app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8000


RUN python --version && pip show django


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]