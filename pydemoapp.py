# Use the following environment variables to configure the OpenTelemetry settings:
# OTEL_EXPORTER_OTLP_TRACES_TIMEOUT
# OTEL_EXPORTER_OTLP_TRACES_PROTOCOL
# OTEL_EXPORTER_OTLP_TRACES_HEADERS
# OTEL_EXPORTER_OTLP_TRACES_ENDPOINT
# OTEL_EXPORTER_OTLP_TRACES_COMPRESSION
# OTEL_EXPORTER_OTLP_TRACES_CERTIFICATE
# OTEL_EXPORTER_OTLP_TIMEOUT
# OTEL_EXPORTER_OTLP_PROTOCOL
# OTEL_EXPORTER_OTLP_HEADERS
# OTEL_EXPORTER_OTLP_ENDPOINT
# OTEL_EXPORTER_OTLP_COMPRESSION
# OTEL_EXPORTER_OTLP_CERTIFICATE
#

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.trace import get_tracer_provider, set_tracer_provider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
    OTLPSpanExporter,
)
import operator

ops = {
    'add' : operator.add,
    'sub' : operator.sub,
    'mul' : operator.mul,
    'div' : operator.truediv,  # use operator.div for Python 2
    'mod' : operator.mod,
    'xor' : operator.xor,
}

# OpenTelemetry initializations
resource = Resource(attributes={
    "service.name": "PyDemoApp"
})
set_tracer_provider(TracerProvider(resource=resource))
get_tracer_provider().add_span_processor(
    BatchSpanProcessor(ConsoleSpanExporter())
)
get_tracer_provider().add_span_processor(
    BatchSpanProcessor(OTLPSpanExporter())
)
instrumentor = FlaskInstrumentor()

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

instrumentor.instrument_app(app)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello from PyDemoApp!'

# Example: http://somepath/math?first=1&second=5?operator=+ 
@app.route('/math')
def login():
    first = int(request.args.get('first'))
    op = request.args.get('operator')
    second = int(request.args.get('second'))
    return str(ops[op](first, second))

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
