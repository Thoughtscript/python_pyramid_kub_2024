from pyramid.view import view_defaults
from pyramid.view import view_config
from pyramid.response import Response
from helpers import basic_addition, add_and_encapsulate_vals
from domain import CustomResponse

class MathApi(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='math_api_basic', request_method='POST')
    def basic_addition_endpoint(self):
        x = self.request.params.get('x')
        y = self.request.params.get('y')
        return Response(CustomResponse(200, "BASIC_ADD", basic_addition(x,y)).stringify())

    @view_config(route_name='math_api_encap', request_method='POST')
    def add_and_encapsulate_vals_endpoint(self):
        x = self.request.params.get('x')
        y = self.request.params.get('y')
        return Response(CustomResponse(200, "ADD_AND_ENCAPSULATE_VALS", add_and_encapsulate_vals(x,y)).stringify())

def includeme(config):
    config.scan()