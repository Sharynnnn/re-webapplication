

from app import *

from app.api import api
from app.views.member import *
from app.views.team import *
from app.views.event import *
from app.views.stage import *
from app.views.results import *
@app.route("/")
def index():
    return redirect('/admin')

app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(api, url_prefix="/api")
app.run(host="127.0.0.1",port=5000)
