# -*- coding: utf-8 -*-

import endpoints
from google.appengine.ext import ndb
from protorpc import remote
from protorpc import message_types

from endpoints_proto_datastore.ndb import EndpointsModel


class Product(EndpointsModel):
    """A model for representing a product"""
    _message_fields_schema = (
        "id", "name", "description", "price",
        "item_type", "keywords", "category", "brand_name", "model",
        "shipping_method", "payment_method", "quantity", "color",
        "electrical_rating", "size_rating", "strength_rating", "gauge_rating",
        "power_rating", "weight", "height", "width", "condition",
        "ship_within", "listing_start", "listing_end", "created_at",
        "updated_at")

    name = ndb.StringProperty(required=True)
    description = ndb.TextProperty(required=True)
    price = ndb.FloatProperty(required=True)
    item_type = ndb.StringProperty()
    keywords = ndb.StringProperty(repeated=True)
    category = ndb.StringProperty(repeated=True)
    brand_name = ndb.StringProperty()
    model = ndb.StringProperty()
    shipping_method = ndb.StringProperty()
    payment_method = ndb.StringProperty(choices=[
        "Mobile Money", "LOC", "Document Release",
        "CoD", "Contact Seller", "Escrow"])
    quantity = ndb.FloatProperty()
    color = ndb.StringProperty()
    electrical_rating = ndb.StringProperty()
    size_rating = ndb.StringProperty()
    strength_rating = ndb.StringProperty()
    gauge_rating = ndb.StringProperty()
    power_rating = ndb.StringProperty()
    weight = ndb.FloatProperty()
    height = ndb.FloatProperty()
    width = ndb.FloatProperty()
    condition = ndb.StringProperty(choices=["New", "Refurbished", "Used--Good",
                                   "Used--Acceptable"])
    ship_within = ndb.IntegerProperty()
    listing_start = ndb.DateTimeProperty()
    listing_end = ndb.DateTimeProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)
    owner = ndb.UserProperty(required=True)


@endpoints.api(name="traderapi",
               version="v1",
               description="API for KrumaTrader")
class TraderAPI(remote.Service):
    @Product.method(
        path="product",
        name="product.insert",
        user_required=True)
    def ProductInsert(self, model):
        model.owner = endpoints.get_current_user()
        model.put()
        return model

    @Product.method(
        request_fields=("id",),
        path="product/{id}",
        http_method="GET",
        name="product.get")
    def ProductGet(self, model):
        if not model.from_datastore:
            raise endpoints.NotFoundException()
        return model

    @Product.method(
        path="product/{id}",
        name="product.update",
        user_required=True,
        http_method="PUT")
    def ProductUpdate(self, model):
        if not model.from_datastore:
            raise endpoints.NotFoundException()
        current_user = endpoints.get_current_user()
        if model.owner != current_user:
            raise endpoints.UnauthorizedException
        model.put()
        return model

    @Product.query_method(path="products", name="products.index")
    def ProductIndex(self, query):
        return query

    @Product.method(
        request_fields=("id", ),
        response_message=message_types.VoidMessage,
        path="product/{id}",
        name="product.delete",
        user_required=True,
        http_method="DELETE")
    def ProductDelete(self, model):
        if not model.from_datastore:
            raise endpoints.NotFoundException()
        current_user = endpoints.get_current_user()
        if model.owner != current_user:
            raise endpoints.UnauthorizedException
        model.key.delete()
        return message_types.VoidMessage()


app = endpoints.api_server([TraderAPI], restricted=False)
