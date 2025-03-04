# PyDemoApp

## Environment

A Python virtual environment should be used, for instance:

    virtualenv venv-k8sdemo
    .\venv-k8sdemo\Scripts\activate

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

docker build -t janben/pydemoapp:X .
docker image tag janben/pydemoapp:X janben/pydemoapp:latest

### Push

docker login
docker image push janben/pydemoapp:X
docker image push janben/pydemoapp:latest

## Run

docker run -it janben/pydemoapp:X --name pydemoapp -e OTEL_EXPORTER_OTLP_ENDPOINT='http://otlp-http.rtcalc.com:80' -p 5000:5000

Examples:

- http://127.0.0.1:5000/math?first=1&second=5&operator=add
- http://127.0.0.1:5000

## Helm

### Build

docker login -u janben
helm package .\pydemoapp\
helm push .\pydemoapp-X.Y.Z.tgz oci://registry-1.docker.io/janben

### Install

helm upgrade --install pydemoapp oci://registry-1.docker.io/janben/pydemoapp -n demoapps --create-namespace -f values.yaml --version X.Y.Z
