from flask import Flask
from database import init_app, db
from routes.locations import locations_bp
from routes.movies import movies_bp
from routes.filming_locations import filming_locations_bp
from routes.restaurants import restaurants_bp
from routes.itinaries import itineraries_bp

app = Flask(__name__)

# Initialize database
init_app(app)

# Register blueprints
app.register_blueprint(movies_bp, url_prefix="/api/v1")
app.register_blueprint(locations_bp, url_prefix="/api/v1")
app.register_blueprint(filming_locations_bp, url_prefix="/api/v1")
app.register_blueprint(restaurants_bp, url_prefix="/api/v1")
app.register_blueprint(itineraries_bp, url_prefix="/api/v1")

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)