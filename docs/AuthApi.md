# openapi_client.AuthApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_form**](AuthApi.md#authorize_form) | **GET** /oauth/authorize | 
[**authorize_token**](AuthApi.md#authorize_token) | **POST** /oauth/authorize | 
[**get_available_rights**](AuthApi.md#get_available_rights) | **GET** /oauth/rights | 
[**get_login_data**](AuthApi.md#get_login_data) | **GET** /oauth/login_data | 
[**post_access_token_request**](AuthApi.md#post_access_token_request) | **POST** /oauth/access_token | 
[**post_access_token_request_query**](AuthApi.md#post_access_token_request_query) | **POST** /oauth/access_token_query | 
[**post_authorize**](AuthApi.md#post_authorize) | **POST** /authorize | 
[**post_req_token_request**](AuthApi.md#post_req_token_request) | **POST** /oauth/request_token | 
[**post_req_token_request_query_string**](AuthApi.md#post_req_token_request_query_string) | **POST** /oauth/request_token_query | 


# **authorize_form**
> str authorize_form()



### Example

```python
import time
import openapi_client
from openapi_client.api import auth_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    ccid = "ccid_example" # str |  (optional)
    cctk = "cctk_example" # str |  (optional)
    oauth_token = "oauth_token_example" # str |  (optional)
    ccid2 = "ccid_example" # str |  (optional)
    cli_token = "cli_token_example" # str |  (optional)
    from_oauth = "from_oauth_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.authorize_form(ccid=ccid, cctk=cctk, oauth_token=oauth_token, ccid2=ccid2, cli_token=cli_token, from_oauth=from_oauth)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthApi->authorize_form: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ccid** | **str**|  | [optional]
 **cctk** | **str**|  | [optional]
 **oauth_token** | **str**|  | [optional]
 **ccid2** | **str**|  | [optional]
 **cli_token** | **str**|  | [optional]
 **from_oauth** | **str**|  | [optional]

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

# **authorize_token**
> authorize_token()



### Example

```python
import time
import openapi_client
from openapi_client.api import auth_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    ccid = "ccid_example" # str |  (optional)
    cctk = "cctk_example" # str |  (optional)
    almighty = "almighty_example" # str |  (optional)
    access_organisations = "access_organisations_example" # str |  (optional)
    manage_organisations = "manage_organisations_example" # str |  (optional)
    manage_organisations_services = "manage_organisations_services_example" # str |  (optional)
    manage_organisations_applications = "manage_organisations_applications_example" # str |  (optional)
    manage_organisations_members = "manage_organisations_members_example" # str |  (optional)
    access_organisations_bills = "access_organisations_bills_example" # str |  (optional)
    access_organisations_credit_count = "access_organisations_credit_count_example" # str |  (optional)
    access_organisations_consumption_statistics = "access_organisations_consumption_statistics_example" # str |  (optional)
    access_personal_information = "access_personal_information_example" # str |  (optional)
    manage_personal_information = "manage_personal_information_example" # str |  (optional)
    manage_ssh_keys = "manage_ssh_keys_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.authorize_token(ccid=ccid, cctk=cctk, almighty=almighty, access_organisations=access_organisations, manage_organisations=manage_organisations, manage_organisations_services=manage_organisations_services, manage_organisations_applications=manage_organisations_applications, manage_organisations_members=manage_organisations_members, access_organisations_bills=access_organisations_bills, access_organisations_credit_count=access_organisations_credit_count, access_organisations_consumption_statistics=access_organisations_consumption_statistics, access_personal_information=access_personal_information, manage_personal_information=manage_personal_information, manage_ssh_keys=manage_ssh_keys)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthApi->authorize_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ccid** | **str**|  | [optional]
 **cctk** | **str**|  | [optional]
 **almighty** | **str**|  | [optional]
 **access_organisations** | **str**|  | [optional]
 **manage_organisations** | **str**|  | [optional]
 **manage_organisations_services** | **str**|  | [optional]
 **manage_organisations_applications** | **str**|  | [optional]
 **manage_organisations_members** | **str**|  | [optional]
 **access_organisations_bills** | **str**|  | [optional]
 **access_organisations_credit_count** | **str**|  | [optional]
 **access_organisations_consumption_statistics** | **str**|  | [optional]
 **access_personal_information** | **str**|  | [optional]
 **manage_personal_information** | **str**|  | [optional]
 **manage_ssh_keys** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_rights**
> get_available_rights()



### Example

```python
import time
import openapi_client
from openapi_client.api import auth_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_available_rights()
    except openapi_client.ApiException as e:
        print("Exception when calling AuthApi->get_available_rights: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_data**
> get_login_data()



### Example

```python
import time
import openapi_client
from openapi_client.api import auth_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    oauth_key = "oauth_key_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_login_data(oauth_key=oauth_key)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthApi->get_login_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_key** | **str**|  | [optional]

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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_access_token_request**
> post_access_token_request()



### Example

```python
import time
import openapi_client
from openapi_client.api import auth_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    oauth_consumer_key = "oauth_consumer_key_example" # str |  (optional)
    oauth_token = "oauth_token_example" # str |  (optional)
    oauth_signature_method = "oauth_signature_method_example" # str |  (optional)
    oauth_signature = "oauth_signature_example" # str |  (optional)
    oauth_timestamp = "oauth_timestamp_example" # str |  (optional)
    oauth_nonce = "oauth_nonce_example" # str |  (optional)
    oauth_version = "oauth_version_example" # str |  (optional)
    oauth_verifier = "oauth_verifier_example" # str |  (optional)
    oauth_callback = "oauth_callback_example" # str |  (optional)
    oauth_token_secret = "oauth_token_secret_example" # str |  (optional)
    oauth_callback_confirmed = "oauth_callback_confirmed_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.post_access_token_request(oauth_consumer_key=oauth_consumer_key, oauth_token=oauth_token, oauth_signature_method=oauth_signature_method, oauth_signature=oauth_signature, oauth_timestamp=oauth_timestamp, oauth_nonce=oauth_nonce, oauth_version=oauth_version, oauth_verifier=oauth_verifier, oauth_callback=oauth_callback, oauth_token_secret=oauth_token_secret, oauth_callback_confirmed=oauth_callback_confirmed)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthApi->post_access_token_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_consumer_key** | **str**|  | [optional]
 **oauth_token** | **str**|  | [optional]
 **oauth_signature_method** | **str**|  | [optional]
 **oauth_signature** | **str**|  | [optional]
 **oauth_timestamp** | **str**|  | [optional]
 **oauth_nonce** | **str**|  | [optional]
 **oauth_version** | **str**|  | [optional]
 **oauth_verifier** | **str**|  | [optional]
 **oauth_callback** | **str**|  | [optional]
 **oauth_token_secret** | **str**|  | [optional]
 **oauth_callback_confirmed** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/x-www-form-urlencoded


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_access_token_request_query**
> post_access_token_request_query()



### Example

```python
import time
import openapi_client
from openapi_client.api import auth_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    oauth_consumer_key = "oauth_consumer_key_example" # str |  (optional)
    oauth_token = "oauth_token_example" # str |  (optional)
    oauth_signature_method = "oauth_signature_method_example" # str |  (optional)
    oauth_signature = "oauth_signature_example" # str |  (optional)
    oauth_timestamp = "oauth_timestamp_example" # str |  (optional)
    oauth_nonce = "oauth_nonce_example" # str |  (optional)
    oauth_version = "oauth_version_example" # str |  (optional)
    oauth_verifier = "oauth_verifier_example" # str |  (optional)
    oauth_callback = "oauth_callback_example" # str |  (optional)
    oauth_token_secret = "oauth_token_secret_example" # str |  (optional)
    oauth_callback_confirmed = "oauth_callback_confirmed_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.post_access_token_request_query(oauth_consumer_key=oauth_consumer_key, oauth_token=oauth_token, oauth_signature_method=oauth_signature_method, oauth_signature=oauth_signature, oauth_timestamp=oauth_timestamp, oauth_nonce=oauth_nonce, oauth_version=oauth_version, oauth_verifier=oauth_verifier, oauth_callback=oauth_callback, oauth_token_secret=oauth_token_secret, oauth_callback_confirmed=oauth_callback_confirmed)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthApi->post_access_token_request_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_consumer_key** | **str**|  | [optional]
 **oauth_token** | **str**|  | [optional]
 **oauth_signature_method** | **str**|  | [optional]
 **oauth_signature** | **str**|  | [optional]
 **oauth_timestamp** | **str**|  | [optional]
 **oauth_nonce** | **str**|  | [optional]
 **oauth_version** | **str**|  | [optional]
 **oauth_verifier** | **str**|  | [optional]
 **oauth_callback** | **str**|  | [optional]
 **oauth_token_secret** | **str**|  | [optional]
 **oauth_callback_confirmed** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-www-form-urlencoded


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_authorize**
> Message post_authorize(wannabe_authorization)



### Example

```python
import time
import openapi_client
from openapi_client.api import auth_api
from openapi_client.model.wannabe_authorization import WannabeAuthorization
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
    api_instance = auth_api.AuthApi(api_client)
    wannabe_authorization = WannabeAuthorization(
        verb="verb_example",
        uri="uri_example",
        authorization="authorization_example",
        payload="payload_example",
        nonce="nonce_example",
        mac="mac_example",
    ) # WannabeAuthorization | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_authorize(wannabe_authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthApi->post_authorize: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wannabe_authorization** | [**WannabeAuthorization**](WannabeAuthorization.md)|  |

### Return type

[**Message**](Message.md)

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

# **post_req_token_request**
> str post_req_token_request()



### Example

```python
import time
import openapi_client
from openapi_client.api import auth_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    clever_flavor = "clever_flavor_example" # str |  (optional)
    oauth_consumer_key = "oauth_consumer_key_example" # str |  (optional)
    oauth_token = "oauth_token_example" # str |  (optional)
    oauth_signature_method = "oauth_signature_method_example" # str |  (optional)
    oauth_signature = "oauth_signature_example" # str |  (optional)
    oauth_timestamp = "oauth_timestamp_example" # str |  (optional)
    oauth_nonce = "oauth_nonce_example" # str |  (optional)
    oauth_version = "oauth_version_example" # str |  (optional)
    oauth_verifier = "oauth_verifier_example" # str |  (optional)
    oauth_callback = "oauth_callback_example" # str |  (optional)
    oauth_token_secret = "oauth_token_secret_example" # str |  (optional)
    oauth_callback_confirmed = "oauth_callback_confirmed_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_req_token_request(clever_flavor=clever_flavor, oauth_consumer_key=oauth_consumer_key, oauth_token=oauth_token, oauth_signature_method=oauth_signature_method, oauth_signature=oauth_signature, oauth_timestamp=oauth_timestamp, oauth_nonce=oauth_nonce, oauth_version=oauth_version, oauth_verifier=oauth_verifier, oauth_callback=oauth_callback, oauth_token_secret=oauth_token_secret, oauth_callback_confirmed=oauth_callback_confirmed)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthApi->post_req_token_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clever_flavor** | **str**|  | [optional]
 **oauth_consumer_key** | **str**|  | [optional]
 **oauth_token** | **str**|  | [optional]
 **oauth_signature_method** | **str**|  | [optional]
 **oauth_signature** | **str**|  | [optional]
 **oauth_timestamp** | **str**|  | [optional]
 **oauth_nonce** | **str**|  | [optional]
 **oauth_version** | **str**|  | [optional]
 **oauth_verifier** | **str**|  | [optional]
 **oauth_callback** | **str**|  | [optional]
 **oauth_token_secret** | **str**|  | [optional]
 **oauth_callback_confirmed** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/x-www-form-urlencoded


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_req_token_request_query_string**
> str post_req_token_request_query_string()



### Example

```python
import time
import openapi_client
from openapi_client.api import auth_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    clever_flavor = "clever_flavor_example" # str |  (optional)
    oauth_consumer_key = "oauth_consumer_key_example" # str |  (optional)
    oauth_token = "oauth_token_example" # str |  (optional)
    oauth_signature_method = "oauth_signature_method_example" # str |  (optional)
    oauth_signature = "oauth_signature_example" # str |  (optional)
    oauth_timestamp = "oauth_timestamp_example" # str |  (optional)
    oauth_nonce = "oauth_nonce_example" # str |  (optional)
    oauth_version = "oauth_version_example" # str |  (optional)
    oauth_verifier = "oauth_verifier_example" # str |  (optional)
    oauth_callback = "oauth_callback_example" # str |  (optional)
    oauth_token_secret = "oauth_token_secret_example" # str |  (optional)
    oauth_callback_confirmed = "oauth_callback_confirmed_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_req_token_request_query_string(clever_flavor=clever_flavor, oauth_consumer_key=oauth_consumer_key, oauth_token=oauth_token, oauth_signature_method=oauth_signature_method, oauth_signature=oauth_signature, oauth_timestamp=oauth_timestamp, oauth_nonce=oauth_nonce, oauth_version=oauth_version, oauth_verifier=oauth_verifier, oauth_callback=oauth_callback, oauth_token_secret=oauth_token_secret, oauth_callback_confirmed=oauth_callback_confirmed)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthApi->post_req_token_request_query_string: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clever_flavor** | **str**|  | [optional]
 **oauth_consumer_key** | **str**|  | [optional]
 **oauth_token** | **str**|  | [optional]
 **oauth_signature_method** | **str**|  | [optional]
 **oauth_signature** | **str**|  | [optional]
 **oauth_timestamp** | **str**|  | [optional]
 **oauth_nonce** | **str**|  | [optional]
 **oauth_version** | **str**|  | [optional]
 **oauth_verifier** | **str**|  | [optional]
 **oauth_callback** | **str**|  | [optional]
 **oauth_token_secret** | **str**|  | [optional]
 **oauth_callback_confirmed** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-www-form-urlencoded


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

