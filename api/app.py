from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
        DATABASE='your_database'
    )
    
    # Register blueprints (assuming these are in your module)
    from .auth_routes import auth as auth_blueprint
    from .user_routes import user as user_blueprint
    from .access_routes import access as access_blueprint
    from .health_routes import health as health_blueprint
    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(access_blueprint)
    app.register_blueprint(health_blueprint)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        return jsonify(error='Not found'), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify(error='Internal server error'), 500
    
    return app

