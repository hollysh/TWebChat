import tornado.ioloop
import tornado.options
import tornado.web
import os.path
from tornado.options import define,options

import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
hdr=logging.StreamHandler()
formatter=logging.Formatter()
hdr.setFormatter(formatter)
logger.addHandler(hdr)


define('port',default=8888,help='run on the given port',type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers =[
            (r"/",MainHandler),
        ]

        setting=dict(
            cookie_secret = 'YOU_CANT_GUESS_MY_SECRET',
            template_path = os.path.join(os.path.dirname(__file__),'templates'),
            static_path = os.path.join(os.path.dirname(__file__),'static'),
            xsrf_cookies=True,
        )

        super(Application,self).__init__(handlers,**setting)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

def main():
    tornado.options.parse_command_line()
    app=Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
