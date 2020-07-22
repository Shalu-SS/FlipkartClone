from app.main import create_app, db
from flask_migrate import Migrate
from app.main.models import *

app = create_app()

migrate = Migrate(app, db)

if __name__ == "main":
    app.run()
