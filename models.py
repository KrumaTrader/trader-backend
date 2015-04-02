from google.appengine.api import ndb

DEFAULT_STORE_NAME = "default_store"

def store_key(store_name=DEFAULT_STORE_NAME):
    """Constructs a datastore key for a Store entity

    We se store_name as the key.
    """
    return ndb.Key("Store", store_name)

#class Photo:
#    """A submodel for photos associated with a product"""
#    description = ndb.TextProperty(required=True)
#    data = ndb.blobProperty()

class Product(ndb.Model):
    """A model for representing a product"""
    name = ndb.StringProperty(required=True)
    description = ndb.TextProperty(required=True)
    price = ndb.FloatProperty(required=True)
    type_ = ndb.StringProperty()
    keywords = ndb.StringProperty(repeated=True)
    category = ndb.StringProperty(repeated=True)
    brand_name = ndb.StringProperty()
    model = ndb.StringProperty()
    shipping_method = ndb.StringProperty()
    payment_method = ndb.StringProperty(choices=["Mobile Money", "LOC", "Document Release", "CoD", "Contact Seller", "Escrow"])
    quantity = ndb.FloatProperty()
    color = ndb.StringProperty()
    electrical_rating = ndb.StringProperty()
    size_rating = ndb.StringProperty()
    strength_rating = ndb.StringProperty()
    gauge_rating = ndb.StringProperty()
    power_rating = ndb.StringProperty()
    weight = ndb.FloatProperty()
    height = ndb.FloatProperty()
    width = ndb.FloatPrperty()
    condition = ndb.StringProperty(choices=["New", "Refurbished", "Used--Good", "Used--Acceptable"]])
#    photos = ndb.StructuredProperty(Photo, repeated=True)
    ship_within = ndb.IntegerProperty()
    listing_start = ndb.DateTimeProperty()
    listing_end = ndb.DateTimeProperty()
    created_at = ndb.DateTimeProperty(required=True, auto_now_add=True)
    updated_at = ndb.DateTimeProperty(required=True, auto_now=True)
