from pyramid.view import view_config
from pyramid.response import FileResponse

# Example expressly defining the File Path
## uses a customized Route omitting the affix /static
@view_config(route_name='html')
def html(request):
    response = FileResponse(
        'public/index.html',
        request=request,
        content_type='text/html'
    )
    return response
 
def includeme(config):
    config.scan()