# openapi_client.UserApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ask_for_password_reset_via_form**](UserApi.md#ask_for_password_reset_via_form) | **POST** /password_forgotten | 
[**authorize_paypal_transaction**](UserApi.md#authorize_paypal_transaction) | **PUT** /invoice/external/paypal/{bid} | 
[**cancel_paypal_transaction**](UserApi.md#cancel_paypal_transaction) | **DELETE** /invoice/external/paypal/{bid} | 
[**confirm_password_reset_request**](UserApi.md#confirm_password_reset_request) | **GET** /password_forgotten/{key} | 
[**create_user_from_form**](UserApi.md#create_user_from_form) | **POST** /users | 
[**delete_github_link**](UserApi.md#delete_github_link) | **DELETE** /github/link | 
[**finsih_github_signup**](UserApi.md#finsih_github_signup) | **POST** /github/signup | 
[**get_applications**](UserApi.md#get_applications) | **GET** /users/{id}/applications | 
[**get_env**](UserApi.md#get_env) | **GET** /application/{appId}/environment | 
[**get_git_info**](UserApi.md#get_git_info) | **GET** /users/{userId}/git-info | 
[**get_github**](UserApi.md#get_github) | **GET** /github | 
[**get_github_applications**](UserApi.md#get_github_applications) | **GET** /github/applications | 
[**get_github_callback**](UserApi.md#get_github_callback) | **GET** /github/callback | 
[**get_github_emails**](UserApi.md#get_github_emails) | **GET** /github/emails | 
[**get_github_keys**](UserApi.md#get_github_keys) | **GET** /github/keys | 
[**get_github_link**](UserApi.md#get_github_link) | **GET** /github/link | 
[**get_github_login**](UserApi.md#get_github_login) | **GET** /github/login | 
[**get_github_username**](UserApi.md#get_github_username) | **GET** /github/username | 
[**get_login_form**](UserApi.md#get_login_form) | **GET** /session/login | 
[**get_login_form1**](UserApi.md#get_login_form1) | **GET** /sessions/login | 
[**get_password_forgotten_form**](UserApi.md#get_password_forgotten_form) | **GET** /password_forgotten | 
[**get_signup_form**](UserApi.md#get_signup_form) | **GET** /session/signup | 
[**get_signup_form1**](UserApi.md#get_signup_form1) | **GET** /sessions/signup | 
[**get_user_by_id**](UserApi.md#get_user_by_id) | **GET** /users/{id} | 
[**github_signup**](UserApi.md#github_signup) | **GET** /github/signup | 
[**login**](UserApi.md#login) | **POST** /session/login | 
[**login1**](UserApi.md#login1) | **POST** /sessions/login | 
[**mfa_login**](UserApi.md#mfa_login) | **POST** /session/mfa_login | 
[**mfa_login1**](UserApi.md#mfa_login1) | **POST** /sessions/mfa_login | 
[**post_github_redeploy**](UserApi.md#post_github_redeploy) | **POST** /github/redeploy | 
[**reset_password_forgotten**](UserApi.md#reset_password_forgotten) | **POST** /password_forgotten/{key} | 
[**update_env**](UserApi.md#update_env) | **PUT** /application/{appId}/environment | 
[**update_invoice**](UserApi.md#update_invoice) | **POST** /invoice/external/{bid} | 


# **ask_for_password_reset_via_form**
> str ask_for_password_reset_via_form()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    login = "login_example" # str |  (optional)
    drop_tokens = "drop_tokens_example" # str |  (optional)
    clever_flavor = "clever_flavor_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.ask_for_password_reset_via_form(login=login, drop_tokens=drop_tokens, clever_flavor=clever_flavor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->ask_for_password_reset_via_form: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional]
 **drop_tokens** | **str**|  | [optional]
 **clever_flavor** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize_paypal_transaction**
> authorize_paypal_transaction(bid, payment_data)



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.payment_data import PaymentData
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    bid = "bid_example" # str | 
    payment_data = PaymentData(
        type="NEW_CARD",
        token="token_example",
        device_data="device_data_example",
    ) # PaymentData | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.authorize_paypal_transaction(bid, payment_data)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->authorize_paypal_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  |
 **payment_data** | [**PaymentData**](PaymentData.md)|  |

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

# **cancel_paypal_transaction**
> cancel_paypal_transaction(bid)



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    bid = "bid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.cancel_paypal_transaction(bid)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->cancel_paypal_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  |

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

# **confirm_password_reset_request**
> str confirm_password_reset_request(key)



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    key = "key_example" # str | 
    clever_flavor = "clever_flavor_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.confirm_password_reset_request(key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->confirm_password_reset_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.confirm_password_reset_request(key, clever_flavor=clever_flavor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->confirm_password_reset_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  |
 **clever_flavor** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_from_form**
> create_user_from_form()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    invitation_key = "invitation_key_example" # str |  (optional)
    addon_beta_invitation_key = "addon_beta_invitation_key_example" # str |  (optional)
    email = "email_example" # str |  (optional)
    _pass = "_pass_example" # str |  (optional)
    url_next = "url_next_example" # str |  (optional)
    terms = "terms_example" # str |  (optional)
    subscription_source = "subscription_source_example" # str |  (optional)
    clever_flavor = "clever_flavor_example" # str |  (optional)
    oauth_token = "oauth_token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_user_from_form(invitation_key=invitation_key, addon_beta_invitation_key=addon_beta_invitation_key, email=email, _pass=_pass, url_next=url_next, terms=terms, subscription_source=subscription_source, clever_flavor=clever_flavor, oauth_token=oauth_token)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->create_user_from_form: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_key** | **str**|  | [optional]
 **addon_beta_invitation_key** | **str**|  | [optional]
 **email** | **str**|  | [optional]
 **_pass** | **str**|  | [optional]
 **url_next** | **str**|  | [optional]
 **terms** | **str**|  | [optional]
 **subscription_source** | **str**|  | [optional]
 **clever_flavor** | **str**|  | [optional]
 **oauth_token** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_github_link**
> Message delete_github_link()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.delete_github_link()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->delete_github_link: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **finsih_github_signup**
> str finsih_github_signup()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    transaction_id = "transaction_id_example" # str |  (optional)
    name = "name_example" # str |  (optional)
    other_id = "other_id_example" # str |  (optional)
    other_email = "other_email_example" # str |  (optional)
    password = "password_example" # str |  (optional)
    auto_link = "auto_link_example" # str |  (optional)
    terms = "terms_example" # str |  (optional)
    invitation_key = "invitation_key_example" # str |  (optional)
    mfa_kind = "mfa_kind_example" # str |  (optional)
    mfa_attempt = "mfa_attempt_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.finsih_github_signup(transaction_id=transaction_id, name=name, other_id=other_id, other_email=other_email, password=password, auto_link=auto_link, terms=terms, invitation_key=invitation_key, mfa_kind=mfa_kind, mfa_attempt=mfa_attempt)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->finsih_github_signup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | [optional]
 **name** | **str**|  | [optional]
 **other_id** | **str**|  | [optional]
 **other_email** | **str**|  | [optional]
 **password** | **str**|  | [optional]
 **auto_link** | **str**|  | [optional]
 **terms** | **str**|  | [optional]
 **invitation_key** | **str**|  | [optional]
 **mfa_kind** | **str**|  | [optional]
 **mfa_attempt** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications**
> [ApplicationView] get_applications(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.application_view import ApplicationView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_applications(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[ApplicationView]**](ApplicationView.md)

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

# **get_env**
> str get_env(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    app_id = "appId_example" # str | 
    token = "token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_env(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_env: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_env(app_id, token=token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_env: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **token** | **str**|  | [optional]

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
**0** | getEnv |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_info**
> str get_git_info(user_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_git_info(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_git_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

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

# **get_github**
> OAuthTransactionView get_github()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.o_auth_transaction_view import OAuthTransactionView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_github()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_github: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OAuthTransactionView**](OAuthTransactionView.md)

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

# **get_github_applications**
> [OAuthApplicationView] get_github_applications()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.o_auth_application_view import OAuthApplicationView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_github_applications()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_github_applications: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[OAuthApplicationView]**](OAuthApplicationView.md)

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

# **get_github_callback**
> get_github_callback()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    cc_o_auth_data = "CcOAuthData_example" # str |  (optional)
    code = "code_example" # str |  (optional)
    state = "state_example" # str |  (optional)
    error = "error_example" # str |  (optional)
    error_description = "error_description_example" # str |  (optional)
    error_uri = "error_uri_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_github_callback(cc_o_auth_data=cc_o_auth_data, code=code, state=state, error=error, error_description=error_description, error_uri=error_uri)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_github_callback: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cc_o_auth_data** | **str**|  | [optional]
 **code** | **str**|  | [optional]
 **state** | **str**|  | [optional]
 **error** | **str**|  | [optional]
 **error_description** | **str**|  | [optional]
 **error_uri** | **str**|  | [optional]

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

# **get_github_emails**
> [str] get_github_emails()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_github_emails()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_github_emails: %s\n" % e)
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

# **get_github_keys**
> [SshKeyView] get_github_keys()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.ssh_key_view import SshKeyView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_github_keys()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_github_keys: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[SshKeyView]**](SshKeyView.md)

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

# **get_github_link**
> str get_github_link()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    transaction_id = "transactionId_example" # str |  (optional)
    redirect_url = "redirectUrl_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_github_link(transaction_id=transaction_id, redirect_url=redirect_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_github_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | [optional]
 **redirect_url** | **str**|  | [optional]

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

# **get_github_login**
> get_github_login()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    redirect_url = "redirectUrl_example" # str |  (optional)
    from_authorize = "fromAuthorize_example" # str |  (optional)
    cli_token = "cli_token_example" # str |  (optional)
    clever_flavor = "clever_flavor_example" # str |  (optional)
    oauth_token = "oauth_token_example" # str |  (optional)
    invitation_key = "invitationKey_example" # str |  (optional)
    subscription_source = "subscriptionSource_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_github_login(redirect_url=redirect_url, from_authorize=from_authorize, cli_token=cli_token, clever_flavor=clever_flavor, oauth_token=oauth_token, invitation_key=invitation_key, subscription_source=subscription_source)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_github_login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_url** | **str**|  | [optional]
 **from_authorize** | **str**|  | [optional]
 **cli_token** | **str**|  | [optional]
 **clever_flavor** | **str**|  | [optional]
 **oauth_token** | **str**|  | [optional]
 **invitation_key** | **str**|  | [optional]
 **subscription_source** | **str**|  | [optional]

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

# **get_github_username**
> str get_github_username()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_github_username()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_github_username: %s\n" % e)
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

# **get_login_form**
> str get_login_form()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    secondary_email_key = "secondaryEmailKey_example" # str |  (optional)
    deletion_key = "deletionKey_example" # str |  (optional)
    from_authorize = "fromAuthorize_example" # str |  (optional)
    cli_token = "cli_token_example" # str |  (optional)
    clever_flavor = "clever_flavor_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_login_form(secondary_email_key=secondary_email_key, deletion_key=deletion_key, from_authorize=from_authorize, cli_token=cli_token, clever_flavor=clever_flavor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_login_form: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secondary_email_key** | **str**|  | [optional]
 **deletion_key** | **str**|  | [optional]
 **from_authorize** | **str**|  | [optional]
 **cli_token** | **str**|  | [optional]
 **clever_flavor** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_form1**
> str get_login_form1()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    secondary_email_key = "secondaryEmailKey_example" # str |  (optional)
    deletion_key = "deletionKey_example" # str |  (optional)
    from_authorize = "fromAuthorize_example" # str |  (optional)
    cli_token = "cli_token_example" # str |  (optional)
    clever_flavor = "clever_flavor_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_login_form1(secondary_email_key=secondary_email_key, deletion_key=deletion_key, from_authorize=from_authorize, cli_token=cli_token, clever_flavor=clever_flavor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_login_form1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secondary_email_key** | **str**|  | [optional]
 **deletion_key** | **str**|  | [optional]
 **from_authorize** | **str**|  | [optional]
 **cli_token** | **str**|  | [optional]
 **clever_flavor** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_forgotten_form**
> str get_password_forgotten_form()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    clever_flavor = "clever_flavor_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_password_forgotten_form(clever_flavor=clever_flavor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_password_forgotten_form: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clever_flavor** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signup_form**
> str get_signup_form()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    invitation_key = "invitationKey_example" # str |  (optional)
    url_next = "url_next_example" # str |  (optional)
    clever_flavor = "clever_flavor_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_signup_form(invitation_key=invitation_key, url_next=url_next, clever_flavor=clever_flavor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_signup_form: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_key** | **str**|  | [optional]
 **url_next** | **str**|  | [optional]
 **clever_flavor** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signup_form1**
> str get_signup_form1()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    invitation_key = "invitationKey_example" # str |  (optional)
    url_next = "url_next_example" # str |  (optional)
    clever_flavor = "clever_flavor_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_signup_form1(invitation_key=invitation_key, url_next=url_next, clever_flavor=clever_flavor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_signup_form1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_key** | **str**|  | [optional]
 **url_next** | **str**|  | [optional]
 **clever_flavor** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> UserView get_user_by_id(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user_view import UserView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_user_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**UserView**](UserView.md)

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

# **github_signup**
> github_signup()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    redirect_url = "redirectUrl_example" # str |  (optional)
    from_authorize = "fromAuthorize_example" # str |  (optional)
    cli_token = "cli_token_example" # str |  (optional)
    clever_flavor = "clever_flavor_example" # str |  (optional)
    oauth_token = "oauth_token_example" # str |  (optional)
    invitation_key = "invitationKey_example" # str |  (optional)
    subscription_source = "subscriptionSource_example" # str |  (optional)
    terms = "terms_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.github_signup(redirect_url=redirect_url, from_authorize=from_authorize, cli_token=cli_token, clever_flavor=clever_flavor, oauth_token=oauth_token, invitation_key=invitation_key, subscription_source=subscription_source, terms=terms)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->github_signup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_url** | **str**|  | [optional]
 **from_authorize** | **str**|  | [optional]
 **cli_token** | **str**|  | [optional]
 **clever_flavor** | **str**|  | [optional]
 **oauth_token** | **str**|  | [optional]
 **invitation_key** | **str**|  | [optional]
 **subscription_source** | **str**|  | [optional]
 **terms** | **str**|  | [optional]

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

# **login**
> str login()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    email = "email_example" # str |  (optional)
    _pass = "_pass_example" # str |  (optional)
    from_authorize = "from_authorize_example" # str |  (optional)
    cli_token = "cli_token_example" # str |  (optional)
    clever_flavor = "clever_flavor_example" # str |  (optional)
    oauth_token = "oauth_token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.login(email=email, _pass=_pass, from_authorize=from_authorize, cli_token=cli_token, clever_flavor=clever_flavor, oauth_token=oauth_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [optional]
 **_pass** | **str**|  | [optional]
 **from_authorize** | **str**|  | [optional]
 **cli_token** | **str**|  | [optional]
 **clever_flavor** | **str**|  | [optional]
 **oauth_token** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login1**
> str login1()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    email = "email_example" # str |  (optional)
    _pass = "_pass_example" # str |  (optional)
    from_authorize = "from_authorize_example" # str |  (optional)
    cli_token = "cli_token_example" # str |  (optional)
    clever_flavor = "clever_flavor_example" # str |  (optional)
    oauth_token = "oauth_token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.login1(email=email, _pass=_pass, from_authorize=from_authorize, cli_token=cli_token, clever_flavor=clever_flavor, oauth_token=oauth_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->login1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [optional]
 **_pass** | **str**|  | [optional]
 **from_authorize** | **str**|  | [optional]
 **cli_token** | **str**|  | [optional]
 **clever_flavor** | **str**|  | [optional]
 **oauth_token** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_login**
> [OAuthApplicationView] mfa_login()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.o_auth_application_view import OAuthApplicationView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    mfa_kind = "mfa_kind_example" # str |  (optional)
    mfa_attempt = "mfa_attempt_example" # str |  (optional)
    email = "email_example" # str |  (optional)
    auth_id = "auth_id_example" # str |  (optional)
    from_authorize = "from_authorize_example" # str |  (optional)
    cli_token = "cli_token_example" # str |  (optional)
    clever_flavor = "clever_flavor_example" # str |  (optional)
    oauth_token = "oauth_token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.mfa_login(mfa_kind=mfa_kind, mfa_attempt=mfa_attempt, email=email, auth_id=auth_id, from_authorize=from_authorize, cli_token=cli_token, clever_flavor=clever_flavor, oauth_token=oauth_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->mfa_login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_kind** | **str**|  | [optional]
 **mfa_attempt** | **str**|  | [optional]
 **email** | **str**|  | [optional]
 **auth_id** | **str**|  | [optional]
 **from_authorize** | **str**|  | [optional]
 **cli_token** | **str**|  | [optional]
 **clever_flavor** | **str**|  | [optional]
 **oauth_token** | **str**|  | [optional]

### Return type

[**[OAuthApplicationView]**](OAuthApplicationView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mfa_login1**
> [OAuthApplicationView] mfa_login1()



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.o_auth_application_view import OAuthApplicationView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    mfa_kind = "mfa_kind_example" # str |  (optional)
    mfa_attempt = "mfa_attempt_example" # str |  (optional)
    email = "email_example" # str |  (optional)
    auth_id = "auth_id_example" # str |  (optional)
    from_authorize = "from_authorize_example" # str |  (optional)
    cli_token = "cli_token_example" # str |  (optional)
    clever_flavor = "clever_flavor_example" # str |  (optional)
    oauth_token = "oauth_token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.mfa_login1(mfa_kind=mfa_kind, mfa_attempt=mfa_attempt, email=email, auth_id=auth_id, from_authorize=from_authorize, cli_token=cli_token, clever_flavor=clever_flavor, oauth_token=oauth_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->mfa_login1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_kind** | **str**|  | [optional]
 **mfa_attempt** | **str**|  | [optional]
 **email** | **str**|  | [optional]
 **auth_id** | **str**|  | [optional]
 **from_authorize** | **str**|  | [optional]
 **cli_token** | **str**|  | [optional]
 **clever_flavor** | **str**|  | [optional]
 **oauth_token** | **str**|  | [optional]

### Return type

[**[OAuthApplicationView]**](OAuthApplicationView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_github_redeploy**
> Message post_github_redeploy(github_webhook_payload)



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.message import Message
from openapi_client.model.github_webhook_payload import GithubWebhookPayload
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    github_webhook_payload = GithubWebhookPayload(
        ref="ref_example",
        after="after_example",
        repository=GithubWebhookRepository(
            id="id_example",
        ),
        sender=GithubWebhookSender(
            id="id_example",
        ),
        pusher=GithubWebhookPusher(
            email="email_example",
        ),
        head_commit=GithubCommit(
            sha="sha_example",
            message="message_example",
        ),
    ) # GithubWebhookPayload | 
    user_agent = "User-Agent_example" # str |  (optional)
    x_github_event = "X-Github-Event_example" # str |  (optional)
    x_hub_signature = "X-Hub-Signature_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.post_github_redeploy(github_webhook_payload)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->post_github_redeploy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_github_redeploy(github_webhook_payload, user_agent=user_agent, x_github_event=x_github_event, x_hub_signature=x_hub_signature)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->post_github_redeploy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **github_webhook_payload** | [**GithubWebhookPayload**](GithubWebhookPayload.md)|  |
 **user_agent** | **str**|  | [optional]
 **x_github_event** | **str**|  | [optional]
 **x_hub_signature** | **str**|  | [optional]

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

# **reset_password_forgotten**
> str reset_password_forgotten(key)



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    key = "key_example" # str | 
    _pass = "_pass_example" # str |  (optional)
    pass2 = "pass2_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.reset_password_forgotten(key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->reset_password_forgotten: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.reset_password_forgotten(key, _pass=_pass, pass2=pass2)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->reset_password_forgotten: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  |
 **_pass** | **str**|  | [optional]
 **pass2** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_env**
> Message update_env(app_id, body)



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    app_id = "appId_example" # str | 
    body = "body_example" # str | 
    token = "token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_env(app_id, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->update_env: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_env(app_id, body, token=token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->update_env: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **body** | **str**|  |
 **token** | **str**|  | [optional]

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

# **update_invoice**
> update_invoice(bid, end_of_invoice_response)



### Example

```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.end_of_invoice_response import EndOfInvoiceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    bid = "bid_example" # str | 
    end_of_invoice_response = EndOfInvoiceResponse(
        id="id_example",
        url="url_example",
        pos_data="pos_data_example",
        status="new",
        btc_price="btc_price_example",
        price=3.14,
        currency="currency_example",
        invoice_time=1,
        current_time=1,
        expiration_time=1,
        error=EndOfInvoiceError(
            type="type_example",
            message="message_example",
            messages={
                "key": "key_example",
            },
        ),
    ) # EndOfInvoiceResponse | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_invoice(bid, end_of_invoice_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->update_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  |
 **end_of_invoice_response** | [**EndOfInvoiceResponse**](EndOfInvoiceResponse.md)|  |

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

