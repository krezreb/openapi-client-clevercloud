
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.auth_api import AuthApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from openapi_client.api.auth_api import AuthApi
from openapi_client.api.organisation_api import OrganisationApi
from openapi_client.api.payment_api import PaymentApi
from openapi_client.api.products_api import ProductsApi
from openapi_client.api.self_api import SelfApi
from openapi_client.api.user_api import UserApi
from openapi_client.api.default_api import DefaultApi
