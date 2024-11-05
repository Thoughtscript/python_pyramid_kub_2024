from pyramid.config import Configurator
from pyramid.view import view_config
from asgiref.wsgi import WsgiToAsgi
from pyramid.response import Response
#from pyramid.renderers import JSON
from domain import CustomResponse

# Decorator approach
@view_config(route_name='example_scan', request_method='GET') #, renderer='json')
def example_scan(request):
    # Do logic here...
    print(request)
    return Response(str(CustomResponse(200,  "GOT ALL"))) ## This must have a len

def example_get_one(request):
    # Do logic here...
    print(request)
    return Response(str(CustomResponse(200,  "GET GOT")))

def example_delete_one(request):
    # Do logic here...
    print(request)
    return Response(str(CustomResponse(200,  "DELETED")))

def example_update_one(request):
    # Do logic here...
    print(request)
    return Response(str(CustomResponse(200,  "UPDATED")))

def example_create_one(request):
    # Do logic here...
    print(request)
    return Response(str(CustomResponse(200,  "CREATED")))

with Configurator() as config:
    # Imperative approach (e.g. - without a view_config decorator)
    config.add_route('example_scan', '/api/example/all')
    ## Only have to define this once can be reused with all more specific view/view operations
    config.add_route('example_one', '/api/example/{uuid}')

    # Routes, above define access paths to application functionality
    ## Views, by contrast, handle the actual Request/Response lifecycle
    ## Views are connected to Routes (and can be done so in a number of ways)
    # Note that the route_name is singular and one:many!
    config.add_view(example_get_one, route_name='example_one', request_method='GET')
    config.add_view(example_delete_one, route_name='example_one', request_method='DELETE')
    config.add_view(example_update_one, route_name='example_one', request_method='PUT')
    config.add_view(example_create_one, route_name='example_one', request_method='POST')

    # Add routes before including
    config.add_route('api_methods', '/api/methods')
    config.include('methods.api')

    config.add_route('postgres_scan', '/api/postgres/all')
    config.include('postgres.api')

    # Renderers and Static Assets
    # json_renderer = JSON()
    # config.add_renderer('json', json_renderer)
    config.add_static_view(name='static', path='public')

    # Specific view configuration
    config.add_route('html', '/index.html')
    config.include('fs.static')

    # Recursively scans the same module for @view_config
    ## Still will likely need to manually specif the includes above
    config.scan()

    wsgi_app = config.make_wsgi_app()
        
app = WsgiToAsgi(wsgi_app)