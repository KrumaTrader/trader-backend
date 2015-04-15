# -*- coding: utf-8 -*-

import endpoints
from google.appengine.ext import ndb
from protorpc import remote

from endpoints_proto_datastore.ndb import EndpointsModel

# class Photo:
#    """A submodel for photos associated with a product"""
#    description = ndb.TextProperty(required=True)
#    data = ndb.blobProperty()


class Product(EndpointsModel):
    """A model for representing a product"""
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
    created_at = ndb.DateTimeProperty(required=True, auto_now_add=True)
    updated_at = ndb.DateTimeProperty(required=True, auto_now=True)


@endpoints.api(name="traderapi",
               version="v1",
               description="API for KrumaTrader")
class TraderAPI(remote.Service):
    @Product.method(path="product", name="product.insert")
    def ProductInsert(self, model):
        model.put()
        return model

    @Product.query_method(path="products", name="products.index")
    def ProductIndex(self, query):
        return query

app = endpoints.api_server([TraderAPI], restricted=False)
