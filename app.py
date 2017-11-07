from apistar import annotate
from apistar import Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar_msgpack import MessagePackRenderer

@annotate(renderers=(MessagePackRenderer(), ))
def welcome():
    return {'message': 'Welcome to API Star.'}

routes = (Route('/', 'GET', welcome), )
app = App(routes=routes)

if __name__ == '__main__':
    app.main()
