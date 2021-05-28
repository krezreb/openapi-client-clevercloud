# openapi_client.PaymentApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_vat**](PaymentApi.md#check_vat) | **GET** /vat_check | 
[**end_payment_with_stripe**](PaymentApi.md#end_payment_with_stripe) | **POST** /payments/{bid}/end/stripe | 
[**get_available_payment_providers**](PaymentApi.md#get_available_payment_providers) | **GET** /payments/providers | 
[**get_coupon**](PaymentApi.md#get_coupon) | **GET** /payments/coupons/{name} | 
[**get_invoice_status_button**](PaymentApi.md#get_invoice_status_button) | **GET** /payments/assets/pay_button/{token}/button.png | 
[**get_stripe_token**](PaymentApi.md#get_stripe_token) | **GET** /payments/tokens/stripe | 
[**stripe_sepa_webhook**](PaymentApi.md#stripe_sepa_webhook) | **POST** /payments/webhooks/stripe/sepa | 
[**update_stripe_payment**](PaymentApi.md#update_stripe_payment) | **PUT** /payments/{bid}/end/stripe | 
[**validate**](PaymentApi.md#validate) | **GET** /validation/vat/{key} | 


# **check_vat**
> VatResult check_vat()



### Example

```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.vat_result import VatResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    country = "country_example" # str |  (optional)
    vat = "vat_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.check_vat(country=country, vat=vat)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->check_vat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | [optional]
 **vat** | **str**|  | [optional]

### Return type

[**VatResult**](VatResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_payment_with_stripe**
> InvoiceRendering end_payment_with_stripe(bid, payment_data)



### Example

```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.payment_data import PaymentData
from openapi_client.model.stripe_confirmation_error_message import StripeConfirmationErrorMessage
from openapi_client.model.invoice_rendering import InvoiceRendering
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    bid = "bid_example" # str | 
    payment_data = PaymentData(
        type="NEW_CARD",
        token="token_example",
        device_data="device_data_example",
    ) # PaymentData | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.end_payment_with_stripe(bid, payment_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->end_payment_with_stripe: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  |
 **payment_data** | [**PaymentData**](PaymentData.md)|  |

### Return type

[**InvoiceRendering**](InvoiceRendering.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**402** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_payment_providers**
> [PaymentProviderView] get_available_payment_providers()



### Example

```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.payment_provider_view import PaymentProviderView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_available_payment_providers()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->get_available_payment_providers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[PaymentProviderView]**](PaymentProviderView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon**
> CouponView get_coupon(name)



### Example

```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.coupon_view import CouponView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_coupon(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->get_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**CouponView**](CouponView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_status_button**
> get_invoice_status_button(token)



### Example

```python
import time
import openapi_client
from openapi_client.api import payment_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    token = "token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_invoice_status_button(token)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->get_invoice_status_button: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stripe_token**
> BraintreeToken get_stripe_token()



### Example

```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.braintree_token import BraintreeToken
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stripe_token()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->get_stripe_token: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BraintreeToken**](BraintreeToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stripe_sepa_webhook**
> stripe_sepa_webhook()



### Example

```python
import time
import openapi_client
from openapi_client.api import payment_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    stripe_signature = "Stripe-Signature_example" # str |  (optional)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.stripe_sepa_webhook(stripe_signature=stripe_signature, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->stripe_sepa_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_signature** | **str**|  | [optional]
 **body** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stripe_payment**
> InvoiceRendering update_stripe_payment(bid, setup_intent_view)



### Example

```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.setup_intent_view import SetupIntentView
from openapi_client.model.invoice_rendering import InvoiceRendering
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    bid = "bid_example" # str | 
    setup_intent_view = SetupIntentView(
        owner_id="owner_id_example",
        id="id_example",
        client_secret="client_secret_example",
        customer="customer_example",
    ) # SetupIntentView | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_stripe_payment(bid, setup_intent_view)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->update_stripe_payment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  |
 **setup_intent_view** | [**SetupIntentView**](SetupIntentView.md)|  |

### Return type

[**InvoiceRendering**](InvoiceRendering.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate**
> Message validate(key)



### Example

```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.message import Message
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    key = "key_example" # str | 
    action = "action_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.validate(key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->validate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.validate(key, action=action)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->validate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  |
 **action** | **str**|  | [optional]

### Return type

[**Message**](Message.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

