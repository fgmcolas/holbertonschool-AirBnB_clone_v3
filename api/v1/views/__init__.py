#!/usr/bin/python3
"""script that creates a Blueprint Flask Class and import modules"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


def register_views():
    """method that registers the views"""
    import api.v1.views.index
    import api.v1.views.states
    import api.v1.views.cities
    import api.v1.views.amenities
    import api.v1.views.users
    import api.v1.views.places
    import api.v1.views.places_reviews


register_views()


"""
from flask import Blueprint
"""
