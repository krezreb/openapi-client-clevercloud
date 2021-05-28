# openapi_client.ProductsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bill_owner**](ProductsApi.md#bill_owner) | **POST** /vendor/apps/{addonId}/consumptions | 
[**edit_application_configuration**](ProductsApi.md#edit_application_configuration) | **PUT** /vendor/apps/{addonId} | 
[**end_addon_migration**](ProductsApi.md#end_addon_migration) | **PUT** /vendor/apps/{addonId}/migration_callback | 
[**get_addon_provider**](ProductsApi.md#get_addon_provider) | **GET** /products/addonproviders/{provider_id} | 
[**get_addon_provider_infos**](ProductsApi.md#get_addon_provider_infos) | **GET** /products/addonproviders/{provider_id}/informations | 
[**get_addon_provider_versions**](ProductsApi.md#get_addon_provider_versions) | **GET** /products/addonproviders/{provider_id}/versions | 
[**get_addon_providers**](ProductsApi.md#get_addon_providers) | **GET** /products/addonproviders | 
[**get_application_info**](ProductsApi.md#get_application_info) | **GET** /vendor/apps/{addonId} | 
[**get_available_instances**](ProductsApi.md#get_available_instances) | **GET** /products/instances | 
[**get_available_packages**](ProductsApi.md#get_available_packages) | **GET** /products/packages | 
[**get_countries**](ProductsApi.md#get_countries) | **GET** /products/countries | 
[**get_country_codes**](ProductsApi.md#get_country_codes) | **GET** /products/countrycodes | 
[**get_excahnge_rates**](ProductsApi.md#get_excahnge_rates) | **GET** /products/prices | 
[**get_flavors**](ProductsApi.md#get_flavors) | **GET** /products/flavors | 
[**get_instance**](ProductsApi.md#get_instance) | **GET** /products/instances/{type}-{version} | 
[**get_mfa_kinds**](ProductsApi.md#get_mfa_kinds) | **GET** /products/mfa_kinds | 
[**get_zones**](ProductsApi.md#get_zones) | **GET** /products/zones | 
[**list_apps**](ProductsApi.md#list_apps) | **GET** /vendor/apps | 
[**logscollector**](ProductsApi.md#logscollector) | **GET** /vendor/apps/{addonId}/logscollector | 
[**provision_other_addon**](ProductsApi.md#provision_other_addon) | **POST** /vendor/addons | 


# **bill_owner**
> bill_owner(addon_id, wannabe_addon_billing)



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.wannabe_addon_billing import WannabeAddonBilling
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    addon_id = "addonId_example" # str | 
    wannabe_addon_billing = WannabeAddonBilling(
        cost=3.14,
    ) # WannabeAddonBilling | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.bill_owner(addon_id, wannabe_addon_billing)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->bill_owner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |
 **wannabe_addon_billing** | [**WannabeAddonBilling**](WannabeAddonBilling.md)|  |

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

# **edit_application_configuration**
> AddonView edit_application_configuration(addon_id, wannabe_addon_config)



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.wannabe_addon_config import WannabeAddonConfig
from openapi_client.model.addon_view import AddonView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    addon_id = "addonId_example" # str | 
    wannabe_addon_config = WannabeAddonConfig(
        config={
            "key": "key_example",
        },
    ) # WannabeAddonConfig | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_application_configuration(addon_id, wannabe_addon_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->edit_application_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |
 **wannabe_addon_config** | [**WannabeAddonConfig**](WannabeAddonConfig.md)|  |

### Return type

[**AddonView**](AddonView.md)

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

# **end_addon_migration**
> AddonView end_addon_migration(addon_id, wannabe_addon_config)



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.wannabe_addon_config import WannabeAddonConfig
from openapi_client.model.addon_view import AddonView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    addon_id = "addonId_example" # str | 
    wannabe_addon_config = WannabeAddonConfig(
        config={
            "key": "key_example",
        },
    ) # WannabeAddonConfig | 
    plan_id = "plan_id_example" # str |  (optional)
    region = "region_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.end_addon_migration(addon_id, wannabe_addon_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->end_addon_migration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.end_addon_migration(addon_id, wannabe_addon_config, plan_id=plan_id, region=region)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->end_addon_migration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |
 **wannabe_addon_config** | [**WannabeAddonConfig**](WannabeAddonConfig.md)|  |
 **plan_id** | **str**|  | [optional]
 **region** | **str**|  | [optional]

### Return type

[**AddonView**](AddonView.md)

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

# **get_addon_provider**
> AddonProviderInfoFullView get_addon_provider(provider_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.addon_provider_info_full_view import AddonProviderInfoFullView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    provider_id = "provider_id_example" # str | 
    orga_id = "orgaId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addon_provider(provider_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_addon_provider: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_addon_provider(provider_id, orga_id=orga_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_addon_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  |
 **orga_id** | **str**|  | [optional]

### Return type

[**AddonProviderInfoFullView**](AddonProviderInfoFullView.md)

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

# **get_addon_provider_infos**
> str get_addon_provider_infos(provider_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    provider_id = "provider_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addon_provider_infos(provider_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_addon_provider_infos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  |

### Return type

**str**

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

# **get_addon_provider_versions**
> str get_addon_provider_versions(provider_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    provider_id = "provider_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addon_provider_versions(provider_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_addon_provider_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  |

### Return type

**str**

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

# **get_addon_providers**
> [AddonProviderInfoFullView] get_addon_providers()



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.addon_provider_info_full_view import AddonProviderInfoFullView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    orga_id = "orgaId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_addon_providers(orga_id=orga_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_addon_providers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orga_id** | **str**|  | [optional]

### Return type

[**[AddonProviderInfoFullView]**](AddonProviderInfoFullView.md)

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

# **get_application_info**
> AddonApplicationInfo get_application_info(addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.addon_application_info import AddonApplicationInfo
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_application_info(addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_application_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |

### Return type

[**AddonApplicationInfo**](AddonApplicationInfo.md)

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

# **get_available_instances**
> [AvailableInstanceView] get_available_instances()



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.available_instance_view import AvailableInstanceView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    _for = "for_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_available_instances(_for=_for)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_available_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_for** | **str**|  | [optional]

### Return type

[**[AvailableInstanceView]**](AvailableInstanceView.md)

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

# **get_available_packages**
> [PackageView] get_available_packages()



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.package_view import PackageView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    coupon = "coupon_example" # str |  (optional)
    orga_id = "orgaId_example" # str |  (optional)
    currency = "currency_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_available_packages(coupon=coupon, orga_id=orga_id, currency=currency)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_available_packages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon** | **str**|  | [optional]
 **orga_id** | **str**|  | [optional]
 **currency** | **str**|  | [optional]

### Return type

[**[PackageView]**](PackageView.md)

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

# **get_countries**
> str get_countries()



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_countries()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_countries: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

# **get_country_codes**
> str get_country_codes()



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_country_codes()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_country_codes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

# **get_excahnge_rates**
> [DropPriceView] get_excahnge_rates()



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.drop_price_view import DropPriceView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_excahnge_rates()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_excahnge_rates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[DropPriceView]**](DropPriceView.md)

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

# **get_flavors**
> [FlavorView] get_flavors()



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.flavor_view import FlavorView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    context = "context_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_flavors(context=context)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_flavors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**|  | [optional]

### Return type

[**[FlavorView]**](FlavorView.md)

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

# **get_instance**
> AvailableInstanceView get_instance(type, version)



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.available_instance_view import AvailableInstanceView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    type = "type_example" # str | 
    version = "version_example" # str | 
    _for = "for_example" # str |  (optional)
    app = "app_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_instance(type, version)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_instance: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_instance(type, version, _for=_for, app=app)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  |
 **version** | **str**|  |
 **_for** | **str**|  | [optional]
 **app** | **str**|  | [optional]

### Return type

[**AvailableInstanceView**](AvailableInstanceView.md)

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

# **get_mfa_kinds**
> [str] get_mfa_kinds()



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_mfa_kinds()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_mfa_kinds: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

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

# **get_zones**
> [ZoneView] get_zones()



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.zone_view import ZoneView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_zones()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->get_zones: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ZoneView]**](ZoneView.md)

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

# **list_apps**
> [AddonApplicationSummary] list_apps()



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.addon_application_summary import AddonApplicationSummary
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    offset = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_apps(offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->list_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional]

### Return type

[**[AddonApplicationSummary]**](AddonApplicationSummary.md)

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

# **logscollector**
> logscollector(addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.logscollector(addon_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->logscollector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |

### Return type

void (empty response body)

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

# **provision_other_addon**
> provision_other_addon(wannabe_inter_addon_provision)



### Example

```python
import time
import openapi_client
from openapi_client.api import products_api
from openapi_client.model.wannabe_inter_addon_provision import WannabeInterAddonProvision
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    wannabe_inter_addon_provision = WannabeInterAddonProvision(
        organisation_id="organisation_id_example",
        user_id="user_id_example",
        provider_id="provider_id_example",
        addon_id="addon_id_example",
        plan="plan_example",
        name="name_example",
        region="region_example",
        options={
            "key": "key_example",
        },
    ) # WannabeInterAddonProvision | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.provision_other_addon(wannabe_inter_addon_provision)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductsApi->provision_other_addon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wannabe_inter_addon_provision** | [**WannabeInterAddonProvision**](WannabeInterAddonProvision.md)|  |

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

