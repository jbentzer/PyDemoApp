# PyDemoApp

## Environment

This app requires that Python 3 (developed on version 3.13) is available and the following dependences have been installed:

- Flask
    - pip install Flask
- OpenTelemetry 
    - pip install opentelemetry-distro opentelemetry-exporter-otlp
    - opentelemetry-bootstrap -a install

The OpenTelemetry endpoint can be set using the predefined environment variables in the OpenTelemetry library.
Example: $Env:OTEL_EXPORTER_OTLP_ENDPOINT = 'http://otlp-http.rtcalc.com:80'

## Docker image

### Build

docker build --no-cache -t janben/pydemoapp:X .
docker image tag janben/pydemoapp:X janben/pydemoapp:latest

### Push

docker login
docker image push janben/pydemoapp:X
docker image push janben/pydemoapp:latest

## Run

Examples:

- http://127.0.0.1:5000/math?first=1&second=5&operator=add
- http://127.0.0.1:5000