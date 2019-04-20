from gevent import monkey; monkey.patch_all() # run before anything else

from application.app import app
from gevent.pywsgi import WSGIServer
from werkzeug.debug import DebuggedApplication

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=app.config["PORT"], help='Port to run the application on')
    parser.add_argument('-d', '--debug', action='store_true', help='Toggle debug mode')
    args = parser.parse_args()

    def _runserver():
        if args.debug:
            print('Running in DEBUG on port {0}'.format(args.port))
            http_server = WSGIServer(('0.0.0.0', args.port), DebuggedApplication(app, evalex=True))
        else:
            print('Running in PRODUCTION on port {0}'.format(args.port))
            http_server = WSGIServer(('0.0.0.0', args.port), app)

        http_server.serve_forever()
        
    if args.debug: 
        from werkzeug.serving import run_with_reloader
        run_with_reloader(_runserver)
    else:
        _runserver()
