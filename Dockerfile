FROM python:3.7

MAINTAINER prakashrd

# copy both source files and default data
WORKDIR /app
COPY file_conversion.py /app
COPY data /app/data
COPY output /app/output
ENTRYPOINT ["python", "file_conversion.py"]
#CMD ["python", "file_conversion.py"]
