# -*- coding: utf-8 -*-

"""Module for the API backend"""

import endpoints
from google.appengine.ext import ndb
from protorpc import remote
from protorpc import message_types

from endpoints_proto_datastore.ndb import EndpointsModel


class Product(EndpointsModel):
    """A model for representing a product"""
    _message_fields_schema = (
        "id", "owner", "approved", "name", "description", "price",
        "item_type", "keywords", "category", "brand_name", "model",
        "shipping_method", "payment_method", "quantity", "color",
        "electrical_rating", "size_rating", "strength_rating", "gauge_rating",
        "power_rating", "weight", "height", "width", "condition",
        "ship_within", "listing_start", "listing_end", "created_at",
        "updated_at")

    name = ndb.StringProperty(required=True)
    owner = ndb.UserProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)
    approved = ndb.BooleanProperty(required=True)

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


class User(EndpointsModel):
    """A model for representing a user"""
    _message_fields_schema = ("id", "name", "owner", "approved", "created_at",
                              "updated_at", "shipping_address", "location",
                              "industry", "city", "country", "postal_code",
                              "year_founded", "url", "size")
    name = ndb.StringProperty(required=True)
    owner = ndb.UserProperty()
    approved = ndb.BooleanProperty(required=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)

    shipping_address = ndb.StringProperty(required=True)
    location = ndb.StringProperty(required=True)
    industry = ndb.StringProperty(required=True)
    city = ndb.StringProperty(required=True)
    country = ndb.StringProperty(required=True)
    postal_code = ndb.StringProperty(required=True)
    year_founded = ndb.IntegerProperty()
    url = ndb.StringProperty()
    size = ndb.IntegerProperty()


class Message(EndpointsModel):
    name = ndb.StringProperty(required=True)
    owner = ndb.UserProperty()
    approved = ndb.BooleanProperty(required=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)

    recipients = ndb.UserProperty(repeated=True)
    body = ndb.TextProperty(required=True)


@endpoints.api(name="traderapi",
               version="v1",
               description="API for KrumaTrader")
class TraderAPI(remote.Service):
    @Product.method(
        path="products",
        name="products.insert",
        user_required=True,
        http_method="POST",
        audiences=[endpoints.API_EXPLORER_CLIENT_ID])
    def ProductInsert(self, model):
        model.owner = endpoints.get_current_user()
        model.put()
        return model

    @Product.method(
        request_fields=("id",),
        path="products/{id}",
        http_method="GET",
        name="products.get")
    def ProductGet(self, model):
        if not model.from_datastore:
            raise endpoints.NotFoundException()
        return model

    @Product.method(
        path="products/{id}",
        name="products.update",
        user_required=True,
        http_method="PUT")
    def ProductUpdate(self, model):
        if not model.from_datastore:
            raise endpoints.NotFoundException()
        current_user = endpoints.get_current_user()
        if model.owner != current_user:
            raise endpoints.UnauthorizedException()
        model.put()
        return model

    @Product.query_method(path="products", name="products.index")
    def ProductIndex(self, query):
        return query

    @Product.method(
        request_fields=("id", ),
        response_message=message_types.VoidMessage,
        path="products/{id}",
        name="products.delete",
        user_required=True,
        http_method="DELETE")
    def ProductDelete(self, model):
        if not model.from_datastore:
            raise endpoints.NotFoundException()
        current_user = endpoints.get_current_user()
        if model.owner != current_user:
            raise endpoints.UnauthorizedException()
        model.key.delete()
        return message_types.VoidMessage()

    @User.method(path="users", name="users.insert", user_required=True)
    def UserInsert(self, model):
        model.owner = endpoints.get_current_user()
        model.put()
        return model

    @User.query_method(path="users", name="users.index")
    def UserIndex(self, query):
        return query

    @User.method(
        request_fields=("id",),
        path="users/{id}",
        http_method="GET",
        name="users.get")
    def UserGet(self, model):
        if not model.from_datastore:
            raise endpoints.NotFoundException()
        return model

    @User.method(
        path="users/{id}",
        name="users.update",
        user_required=True,
        http_method="PUT")
    def UserUpdate(self, model):
        if not model.from_datastore:
            raise endpoints.NotFoundException()
        current_user = endpoints.get_current_user()
        if model.owner != current_user:
            raise endpoints.UnauthorizedException()
        model.put()
        return model

    @User.method(
        request_fields=("id", ),
        response_message=message_types.VoidMessage,
        path="users/{id}",
        name="users.delete",
        user_required=True,
        http_method="DELETE")
    def UserDelete(self, model):
        if not model.from_datastore:
            raise endpoints.NotFoundException()
        current_user = endpoints.get_current_user()
        if model.owner != current_user:
            raise endpoints.UnauthorizedException()
        model.key.delete()
        return message_types.VoidMessage()

    @Message.method(name="messages.insert", path="messages",
                    user_required=True)
    def MessageInsert(self, model):
        model.owner = endpoints.get_current_user()
        model.put()
        return model

    @Message.method(request_fields=("id",), path="messages/{id}",
                    http_method="GET", name="messages.get")
    def MessagesGet(self, model):
        if not model.from_datastore:
            raise endpoints.NotFoundException()
        return model

    @Message.query_method(path="messages", name="messages.index")
    def MessageIndex(self, query):
        return query

    @Message.method(path="messages/{id}", request_fields=("id",),
                    http_method="PUT", user_required=True, name="messages.update")
    def MessageUpdate(self, model):
        if not model.from_datastore:
            raise endpoints.NotFoundException()
        current_user = endpoints.get_current_user()
        if model.owner != current_user:
            raise endpoints.UnauthorizedException()
        model.put()
        return model

    @Message.method(name="messages.delete", path="messages/{id}",
                    user_required=True, http_method="DELETE",
                    request_fields=("id",))
    def MessageDelete(self, model):
        if not model.from_datastore:
            raise endpoints.NotFoundException()
        current_user = endpoints.get_current_user
        if model.owner != current_user:
            raise endpoints.UnauthorizedException()
        model.key.delete()
        return message_types.VoidMessage()


app = endpoints.api_server([TraderAPI], restricted=False)
