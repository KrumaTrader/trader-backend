# -*- coding: utf-8 -*-

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
import resources
import models
from google.appengine.ext import ndb


def serialize(product):
    """Serialize a product into message representation
    Args:
        product(models.Product): The product to serialize into a message object
    Returns:
        resources.ProductRepr: the message representation of the product
    Raises:
        None
    """
    return resources.ProductRepr(
        key=product.key.urlsafe(),
        name=product.name,
        description=product.description,
        price=product.price,
        type_=product.type_,
        keywords=product.keywords,
        category=product.category,
        brand_name=product.brand_name,
        model=product.model,
        shipping_method=product.shipping_method,
        payment_method=product.payment_method,
        quantity=product.quantity,
        color=product.color,
        electrical_rating=product.electrical_rating,
        size_rating=product.size_rating,
        strength_rating=product.strength_rating,
        gauge_rating=product.gauge_rating,
        power_rating=product.power_rating,
        weight=product.weight,
        height=product.height,
        width=product.width,
        condition=product.condition,
        ship_within=product.ship_within,
        listing_start=product.listing_start,
        listing_end=product.listing_end,
        created_at=product.created_at,
        updated_at=product.updated_at)


def deserialize(message):
    """Deserialize a message into a product
    Args:
        message(resources.ProductRepr):  The message, which will be turned
                                          into a product
    Returns:
        models.Product: The product representation of the message
    Raises:
        None
    """
    # If the message has a key parameter, grab the product from the database
    # Otherwise, create a new Product
    if message.key is not None:
        product = ndb.Key(urlsafe=message.key).get()
    else:
        product = models.Product()
    product.name = message.name
    product.description = message.description
    product.price = message.price
    product.type_ = message.type_
    product.keywords = message.keywords
    product.category = message.category
    product.brand_name = message.brand_name
    product.model = message.model
    product.shipping_method = message.shipping_method
    product.payment_method = message.payment_method
    product.quantity = message.quantity
    product.color = message.color
    product.electrical_rating = message.electrical_rating
    product.size_rating = message.size_rating
    product.strength_rating = message.strength_rating
    product.gauge_rating = message.gauge_rating
    product.power_rating = message.power_rating
    product.weight = message.weight
    product.height = message.height
    product.width = message.width
    product.condition = message.condition
    product.ship_within = message.ship_within
    product.listing_start = message.listing_start
    product.listing_end = message.listing_end
    return product


@endpoints.api(name="krumatrader", version="v1")
class KrumaTraderApi(remote.Service):
    """The API class for krumaTrader"""
    ProductRequestContainer = endpoints.ResourceContainer(
        resources.ProductRepr, key=messages.StringField(1))

    @endpoints.method(
        message_types.VoidMessage,
        resources.ProductList,
        path="products",
        http_method="GET",
        name="products.listProducts")
    def products_read(self, _):
        """Read a list of products from the database
        Args:
            _ : The unused part of the request
        Returns:
            resources.ProductList: A list of all products
        Raises:
            None
        """
        return resources.ProductList(products=[serialize(product)
                                     for product in
                                     models.Product.query().fetch()])

    @endpoints.method(
        resources.ProductRepr,
        resources.ProductRepr,
        path="products",
        http_method="POST",
        name="products.createProduct")
    def product_create(self, new_resource):
        """Create a new product
        Args:
            new_resource(resources.ProductRepr):
                message representation of product
        Returns:
            resources.ProductRepr
        Raises:
            endpoints.UnauthorizedException
        """
        user = endpoints.get_current_user()
        if user is None:
            raise endpoints.UnauthorizedException()
        product = deserialize(new_resource)
        product.parent = ndb.Key("User", user.user_id()),
        product.put()
        new_resource.key = product.key.urlsafe()
        new_resource.created_at = product.created_at
        return new_resource

    @endpoints.method(
        ProductRequestContainer,
        resources.ProductRepr,
        path="products/{key}",
        http_method="PUT",
        name="products.updateProduct")
    def product_update(self, request):
        """Update a product from the database
        Args:
            request(resources.ProductRepr)
        Returns:
            resources.ProductRepr: The updated product
        Raises:
            endpoints.UnauthorizedException
        """
        product = deserialize(request)
        user = endpoints.get_current_user()
        if user is None or ndb.Key("User", user.user_id) != product.parent():
            raise endpoints.UnauthorizedException()
        product.put()
        return serialize(product)

    @endpoints.method(
        ProductRequestContainer,
        message_types.VoidMessage,
        path="products/{key}",
        http_method="DELETE",
        name="products.deleteProduct")
    def product_delete(self, request):
        """Delete a product from the data store
        Args:
            ProductRequestContainer
        Returns:
            message_types.VoidMessage
        Raises:
            endpoints.UnauthorizedException
        """
        product = ndb.Key(urlsafe=request.key())
        user = endpoints.get_current_user
        if user is None or ndb.Key("User", user.user_id) != product.parent():
            raise endpoints.UnauthorizedException
        ndb.Key(urlsafe=request.key).delete()
        return message_types.VoidMessage()

    @endpoints.method(
        ProductRequestContainer,
        resources.ProductRepr,
        path="product/{key}",
        http_method="GET",
        name="products.productDetails")
    def product_read(self, request):
        """Create a new product
        Args:
            request(ProductRequestContainer): A request for a certain product
        Returns:
            resources.ProductRepr: The product from the database, serialized
        Raises:
            None
        """
        p = ndb.Key(urlsafe=request.key).get()
        return serialize(p)

app = endpoints.api_server([KrumaTraderApi])
