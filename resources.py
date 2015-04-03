from protorpc import messages
from protorpc import message_types


class ProductRepr(messages.Message):
    """A representation of a product"""
    name = messages.StringField(1)
    description = messages.StringField(2)
    price = messages.FloatField(3)
    type_ = messages.StringField(4)
    keywords = messages.StringField(5)
    category = messages.StringField(6)
    brand_name = messages.StringField(7)
    model = messages.StringField(8)
    shipping_method = messages.StringField(9)
    payment_method = messages.StringField(10)
    quantity = messages.FloatField(11)
    color = messages.StringField(12)
    electrical_rating = messages.StringField(13)
    size_rating = messages.StringField(14)
    strength_rating = messages.StringField(15)
    gauge_rating = messages.StringField(16)
    power_rating = messages.StringField(17)
    weight = messages.FloatField(18)
    height = messages.FloatField(19)
    width = messages.FloatField(20)
    condition = messages.StringField(21)
#    photos = messages.StructuredProperty(Photo, repeated=True)
    ship_within = messages.IntegerField(22)
    listing_start = message_types.DateTimeField(23)
    listing_end = message_types.DateTimeField(24)
    created_at = message_types.DateTimeField(25)
    updated_at = message_types.DateTimeField(26)

class ProductCatalog(messages.Message):
    products = messages.MessageField(ProductRepr, 1, repeated=True)
