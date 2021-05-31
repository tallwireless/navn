import os
from .dnshandler import DNSHandler
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    print(__name__)
    app = Flask(__name__)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    Flask.API_KEY = "67ffcc1f68e54cb65d03d07ad6eaa27128385be7299d0ea265bb838cd10ff538"
    Flask.DNS_HANDLER = DNSHandler(
        "2001:470:e6fc:4000::4a11:aa",
        {
            "ssl.tallwireless.com.": (
                "gDzlZLznMSzqWOS1JmXEC7rqOiQ0cIyOVmDb1FRhx1UXPdjiZr0TOWhpso01UefoJxiz3xvSpg1XqC+7H3Bc8w==",
                "HMAC_MD5",
            )
        },
    )
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    from . import api

    app.register_blueprint(api.bp)

    return app
