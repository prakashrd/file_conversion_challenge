FROM python:3.7

MAINTAINER prakashrd

# copy both source files and default data
COPY . /app
CMD ["python", "/app/file_conversion.py"]
