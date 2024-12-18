#!/usr/bin/env python3
"""A Basic Flask app with Internationalization support.
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TMEZONE = "UTC"


    app = Flask(__name__)
    app.config.from_object(Config)
    app.url_map.strict_slashes =False
    babel = Babel(app)


    @babel.localeselctor
    def get_locate() -> str:
        """Retrieves the locale for a web page.
        """
        return request.accept_languages.best_match(app.config["LANGUAGE"])


    @app.route('/')
    def get_index() -> str:
        """The home/index page.
        """
        return render_template('3-index.html')


    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
