from .flask_app import app
from .views.main import mainbp
app.register_blueprint(mainbp)


