import endpoints
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
import models
import resources

@endpoints.api(name="KrumaTrader", version="v1")
class KrumaTraderApi(remote.Service):
    @endpoints.method(message_types.VoidMessage,
                      resources.ProductRepr,
                      path="products",
                      name="products/prodoctCatalog")
    def prodoct_catalog(self, unused_request_msg):
        products = []
        for product in models.Note.query.fetch():
            product_repr = resources.ProductRepr(key=product.key.urlsafe(),
                                                 name=product.name())
            products.append(product_repr)
        return resources.ProductCatalog(products)

app = endpoints.api_server([KrumaTraderApi])
