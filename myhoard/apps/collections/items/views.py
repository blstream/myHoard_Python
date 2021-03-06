from flask import url_for
from flask.ext.restful import Resource, marshal_with, fields

from myhoard.apps.common.utils import get_request_json
from myhoard.apps.auth.decorators import login_required
from myhoard.apps.collections.items.models import Item


class GeoLocationField(fields.Raw):
    @staticmethod
    def format(point):
        return {
            'lng': point['coordinates'][0],
            'lat': point['coordinates'][1]
        }


class MediaField(fields.Raw):
    @staticmethod
    def format(media_id):
        return {
            'id': str(media_id),
            'url': url_for('mediadetails', media_id=media_id, _external=True)
        }


item_fields = {
    'id': fields.String,
    'name': fields.String,
    'description': fields.String,
    'location': GeoLocationField(),
    'media': fields.List(MediaField()),
    'created_date': fields.String,
    'modified_date': fields.String,
    'collection': fields.String,
    'owner': fields.String
}


class ItemDetails(Resource):
    method_decorators = [marshal_with(item_fields), login_required]

    @staticmethod
    def get(item_id):
        return Item.get_visible_or_404(item_id)

    @staticmethod
    def put(item_id):
        return Item.put(item_id, **get_request_json())

    @staticmethod
    def patch(item_id):
        return Item.patch(item_id, **get_request_json())

    @staticmethod
    def delete(item_id):
        Item.delete(item_id)

        return '', 204


class ItemList(Resource):
    method_decorators = [marshal_with(item_fields), login_required]

    @staticmethod
    def post():
        return Item.create(**get_request_json()), 201