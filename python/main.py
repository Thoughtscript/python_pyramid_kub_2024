from pyramid.config import Configurator
from pyramid.view import view_config
from asgiref.wsgi import WsgiToAsgi
from pyramid.response import Response
#from pyramid.renderers import JSON
from domain import CustomResponse, Example

cache = {}

# Decorator approach
@view_config(route_name='example_scan', request_method='GET') #, renderer='json')
def example_scan(request):
    return Response(CustomResponse(200,  "SCANNED", cache.values()).stringify()) ## This must have a len

def example_get_one(request):
    # https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/urldispatch.html#matchdict
    ## Unlike Node, params don't expose both path and query params
    id = request.matchdict.get('id')
    
    response_obj = cache.get(id)
    if response_obj is not None:
        response_obj = response_obj.stringify()

    return Response(CustomResponse(200,  "GOT",  response_obj).stringify())

def example_delete_one(request):
    id = request.matchdict.get('id')
    response_obj = cache.get(id)
    
    if response_obj is not None:
        del cache[id]
        response_obj = cache.get(id)

    return Response(CustomResponse(200,  "DELETED",  response_obj).stringify())

def example_update_one(request):
    id = request.matchdict.get('id')
    response_obj = cache.get(id)

    if response_obj is not None:
        name = request.params.get('name','default')
        cache[id] = Example(id, name)
        response_obj = cache.get(id).stringify()

    return Response(CustomResponse(200,  "UPDATED",  response_obj).stringify())

def example_create_one(request):
    id = request.matchdict.get('id')
    name = request.params.get('name','default')
    cache[id] = Example(id, name)

    response_obj = cache.get(id).stringify()
    return Response(CustomResponse(200,  "CREATED",  response_obj).stringify())

with Configurator() as config:
    # Imperative approach (e.g. - without a view_config decorator)
    config.add_route('example_scan', '/api/example/all')
    ## Only have to define this once can be reused with all more specific view/view operations
    config.add_route('example_one', '/api/example/{id}')

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

    config.add_route('math_api_basic', '/api/math/basic')
    config.add_route('math_api_encap', '/api/math/encap')
    config.include('mymath.api')

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