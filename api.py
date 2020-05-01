import responder

api = responder.API()


@api.route("/hello")
def hello(req, resp):
    resp.media = {"hello": "hello"}


if __name__ == '__main__':
    api.run()
