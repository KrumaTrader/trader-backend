import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
import resources
import models
from google.appengine.ext import ndb


@endpoints.api(name="krumatrader", version="v1")
class KrumaTraderApi(remote.Service):

    ProductRequestContainer = endpoints.ResourceContainer(
        resources.ProductRepr, key=messages.StringField(1))

    @endpoints.method(
        message_types.VoidMessage,
        resources.ProductList,
        path="products",
        http_method="GET",
        name="products.listProducts")
    def products_read(self, unused_request):
        return resources.ProductList(products=[resources.ProductRepr(
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
            for product in models.Product.query().fetch()])

    @endpoints.method(
        resources.ProductRepr,
        resources.ProductRepr,
        path="products",
        http_method="POST",
        name="products.createProducts")
    def product_create(self, new_resource):
        user = endpoints.get_current_user()
        if user is None:
            raise endpoints.UnauthorizedException()
        product = models.Product(
            parent=ndb.Key("User", user.nickname()),
            name=new_resource.name,
            description=new_resource.description,
            price=new_resource.price,
            type_=new_resource.type_,
            keywords=new_resource.keywords,
            category=new_resource.category,
            brand_name=new_resource.brand_name,
            model=new_resource.model,
            shipping_method=new_resource.shipping_method,
            payment_method=new_resource.payment_method,
            quantity=new_resource.quantity,
            color=new_resource.color,
            electrical_rating=new_resource.electrical_rating,
            size_rating=new_resource.size_rating,
            strength_rating=new_resource.strength_rating,
            gauge_rating=new_resource.gauge_rating,
            power_rating=new_resource.power_rating,
            weight=new_resource.weight,
            height=new_resource.height,
            width=new_resource.width,
            condition=new_resource.condition,
            ship_within=new_resource.ship_within,
            listing_start=new_resource.listing_start,
            listing_end=new_resource.listing_end,
            created_at=new_resource.created_at,
            updated_at=new_resource.updated_at)
        product.put()
        new_resource.key = product.key.urlsafe()
        new_resource.date_created = product.date_created
        return new_resource

    @endpoints.method(
        ProductRequestContainer,
        resources.ProductRepr,
        path="product/{key}",
        http_method="GET",
        name="products.productDetails")
    def product_read(self, request):
        p = ndb.Key(urlsafe=request.key).get()
        return resources.ProductRepr(
            key=request.key,
            name=request.name,
            description=request.description,
            price=p.price,
            type_=p.type_,
            keywords=p.keywords,
            category=p.category,
            brand_name=p.brand_name,
            model=p.model,
            shipping_method=p.shipping_method,
            payment_method=p.payment_method,
            quantity=p.quantity,
            color=p.color,
            electrical_rating=p.electrical_rating,
            size_rating=p.size_rating,
            strength_rating=p.strength_rating,
            gauge_rating=p.gauge_rating,
            power_rating=p.power_rating,
            weight=p.weight,
            height=p.height,
            width=p.width,
            condition=p.condition,
            ship_within=p.ship_within,
            listing_start=p.listing_start,
            listing_end=p.listing_end,
            created_at=p.created_at,
            updated_at=p.updated_at)

    @endpoints.method(
        ProductRequestContainer,
        resources.ProductRepr,
        path="products/{key}",
        http_method="PUT",
        name="products.updateProduct")
    def product_update(self, request):
        product = ndb.Key(urlsafe=request.key).get()
        product.name = request.name
        product.description = request.description
        product.price = request.price
        product.type_ = request.type_
        product.keywords = request.keywords
        product.category = request.category
        product.brand_name = request.brand_name
        product.model = request.model
        product.shipping_method = request.shipping_method
        product.payment_method = request.payment_method
        product.quantity = request.quantity
        product.color = request.color
        product.electrical_rating = request.electrical_rating
        product.size_rating = request.size_rating
        product.strength_rating = request.strength_rating
        product.gauge_rating = request.gauge_rating
        product.power_rating = request.power_rating
        product.weight = request.weight
        product.height = request.height
        product.width = request.width
        product.condition = request.condition
        product.ship_within = request.ship_within
        product.listing_start = request.listing_start
        product.listing_end = request.listing_end
        product.put()
        return resources.ProductRepr(
            key=request.key,
            name=request.name,
            description=request.description,
            price=request.price,
            type_=request.type_,
            keywords=request.keywords,
            category=request.category,
            brand_name=request.brand_name,
            model=request.model,
            shipping_method=request.shipping_method,
            payment_method=request.payment_method,
            quantity=request.quantity,
            color=request.color,
            electrical_rating=request.electrical_rating,
            size_rating=request.size_rating,
            strength_rating=request.strength_rating,
            gauge_rating=request.gauge_rating,
            power_rating=request.power_rating,
            weight=request.weight,
            height=request.height,
            width=request.width,
            condition=request.condition,
            ship_within=request.ship_within,
            listing_start=request.listing_start,
            listing_end=request.listing_end,
            created_at=request.created_at)

    @endpoints.method(
        ProductRequestContainer,
        message_types.VoidMessage,
        path="products/{key}",
        http_method="DELETE",
        name="products.deleteProduct")
    def product_delete(self, request):
        ndb.Key(urlsafe=request.key).delete()
        return message_types.VoidMessage()

    # TODO
    # add auth

app = endpoints.api_server([KrumaTraderApi])
