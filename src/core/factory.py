import os


from flask import Flask


# import hasil inisialisasi

from core.init import db, migrate, ma
from apps.books.routes import books_bp

# flask factory
def create_app() -> Flask:
    app = Flask(__name__)


    # tentukan mode
    if os.environ.get("MODE") == "development":
        print("Berjalan dalam mode Development")
        app.config.from_object("core.config.DevelopmentConfig")
    else:
        print("Berjalan dalam mode Production")
        app.config.from_object("core.config.ProductionConfig")

    
    # inisialisasi database
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    ma.init_app(app=app)

    # register blueprint API nya
    app.register_blueprint(books_bp)


    return app