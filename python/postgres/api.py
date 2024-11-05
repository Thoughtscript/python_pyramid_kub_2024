import psycopg #psycopg3
from pyramid.response import Response
from pyramid.view import view_config

# Singleton
# conn = psycopg.connect(dbname="postgres", user="testuser", password="testpassword", host="postgres", port="5432")

# @view_config(route_name='postgres_scan', request_method='GET') 
# def postgres_scan(request):
#     with conn.cursor() as cur:
#         cur.execute("SELECT * FROM example;")
#         record_set = cur.fetchone()
    
#         #cur.close() # will auto close
#         #conn.close() # will be kept open
#         return Response(str(record_set)) 

def includeme(config):
    config.scan()