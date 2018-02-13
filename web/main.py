import web
from urls import urls

web.config.debug = True
app = web.application(urls, globals())


if __name__ == '__main__':
    app.run()
