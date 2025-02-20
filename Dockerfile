FROM python:3.13
ADD pydemoapp.py .
RUN pip install flask opentelemetry-distro opentelemetry-exporter-otlp
RUN opentelemetry-bootstrap --action=install
ENTRYPOINT ["python", "./pydemoapp.py" ] 
EXPOSE 5000