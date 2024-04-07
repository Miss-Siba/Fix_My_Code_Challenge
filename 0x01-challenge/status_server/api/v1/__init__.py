from flask import Blueprint

# Create a Blueprint object for the v1 views
app_views = Blueprint('app_views', __name__)

# Import views module to register routes
from api.v1 import views

