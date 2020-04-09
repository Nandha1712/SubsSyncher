from flask import Flask
from flask_cors import CORS

from application.controller.subs_controller import subs_sync

__version__ = '0.1'

app_name = "SubsSyncher"
app = Flask(app_name)
CORS(app)
app.register_blueprint(subs_sync)

if __name__ == "__main__":
    app.run(port=3000)
