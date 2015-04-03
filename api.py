import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
import resources
import models
from google.appengine.ext import ndb

@endpoints.api(name="krumatrader", version="v1")
class KrumaTraderApi(remote.Service):
    """Helloworld API v1."""

    @endpoints.method(message_types.VoidMessage, resources.ProductList,
                      path="products", http_method="GET",
                      name="products.listProducts")
    def get_products(self, unused_request):
        return resources.ProductList(products=
            [resources.ProductRepr(
                name=p.name, 
                description=p.description,
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
                updated_at=p.updated_at) for p in models.Product.query().fetch()])
    # TODO
    # get_product(id)
    # post_product(id)
    # put_product(id)
    # delete_product(id)
      

app = endpoints.api_server([KrumaTraderApi])