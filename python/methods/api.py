from pyramid.view import view_defaults
from pyramid.view import view_config
from pyramid.response import Response

# I don't the order of this textually matters.
## Seems to load at the same time regardless 
## of above or after includeme
@view_defaults(route_name='api_methods')
class MethodApi(object):
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET')
    def get(self):
         return Response('GET')

    @view_config(request_method='POST')
    def post(self):
        return Response('POST')

    @view_config(request_method='DELETE')
    def delete(self):
        return Response('DELETE')

# This is akin to:
## an Angular import/export
## Node module.exports
## Rust mod
def includeme(config):
    config.scan()