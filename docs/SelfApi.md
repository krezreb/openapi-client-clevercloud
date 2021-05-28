# openapi_client.SelfApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_email_address**](SelfApi.md#add_email_address) | **PUT** /self/emails/{email} | 
[**add_self_addon_tag_by_addon_id**](SelfApi.md#add_self_addon_tag_by_addon_id) | **PUT** /self/addons/{addonId}/tags/{tag} | 
[**add_self_application**](SelfApi.md#add_self_application) | **POST** /self/applications | 
[**add_self_application_dependency_by_app_id**](SelfApi.md#add_self_application_dependency_by_app_id) | **PUT** /self/applications/{appId}/dependencies/{dependencyId} | 
[**add_self_application_tag_by_app_id**](SelfApi.md#add_self_application_tag_by_app_id) | **PUT** /self/applications/{appId}/tags/{tag} | 
[**add_self_payment_method**](SelfApi.md#add_self_payment_method) | **POST** /self/payments/methods | 
[**add_self_vhost_by_app_id**](SelfApi.md#add_self_vhost_by_app_id) | **PUT** /self/applications/{appId}/vhosts/{domain} | 
[**add_ssh_key**](SelfApi.md#add_ssh_key) | **PUT** /self/keys/{key} | 
[**buy_self_drops**](SelfApi.md#buy_self_drops) | **POST** /self/payments/billings | 
[**cancel_deploy**](SelfApi.md#cancel_deploy) | **DELETE** /self/applications/{appId}/deployments/{deploymentId}/instances | 
[**change_self_addon_plan_by_addon_id**](SelfApi.md#change_self_addon_plan_by_addon_id) | **PUT** /self/addons/{addonId}/plan | 
[**change_user_password**](SelfApi.md#change_user_password) | **PUT** /self/change_password | 
[**choose_self_payment_provider**](SelfApi.md#choose_self_payment_provider) | **PUT** /self/payments/billings/{bid} | 
[**create_mfa**](SelfApi.md#create_mfa) | **POST** /self/mfa/{kind} | 
[**create_self_consumer**](SelfApi.md#create_self_consumer) | **POST** /self/consumers | 
[**delete_mfa**](SelfApi.md#delete_mfa) | **DELETE** /self/mfa/{kind} | 
[**delete_self_addon_tag_by_addon_id**](SelfApi.md#delete_self_addon_tag_by_addon_id) | **DELETE** /self/addons/{addonId}/tags/{tag} | 
[**delete_self_application_by_app_id**](SelfApi.md#delete_self_application_by_app_id) | **DELETE** /self/applications/{appId} | 
[**delete_self_application_dependency_by_app_id**](SelfApi.md#delete_self_application_dependency_by_app_id) | **DELETE** /self/applications/{appId}/dependencies/{dependencyId} | 
[**delete_self_application_tag_app_id**](SelfApi.md#delete_self_application_tag_app_id) | **DELETE** /self/applications/{appId}/tags/{tag} | 
[**delete_self_card**](SelfApi.md#delete_self_card) | **DELETE** /self/payments/methods/{mId} | 
[**delete_self_consumer**](SelfApi.md#delete_self_consumer) | **DELETE** /self/consumers/{key} | 
[**delete_self_purchase_order**](SelfApi.md#delete_self_purchase_order) | **DELETE** /self/payments/billings/{bid} | 
[**delete_self_recurrent_payment**](SelfApi.md#delete_self_recurrent_payment) | **DELETE** /self/payments/recurring | 
[**delete_user**](SelfApi.md#delete_user) | **DELETE** /self | 
[**deprovision_self_addon_by_id**](SelfApi.md#deprovision_self_addon_by_id) | **DELETE** /self/addons/{addonId} | 
[**edit_self_application_by_app_id**](SelfApi.md#edit_self_application_by_app_id) | **PUT** /self/applications/{appId} | 
[**edit_self_application_env_by_app_id**](SelfApi.md#edit_self_application_env_by_app_id) | **PUT** /self/applications/{appId}/env | 
[**edit_self_application_env_by_app_id_and_env_name**](SelfApi.md#edit_self_application_env_by_app_id_and_env_name) | **PUT** /self/applications/{appId}/env/{envName} | 
[**edit_user**](SelfApi.md#edit_user) | **PUT** /self | 
[**fav_mfa**](SelfApi.md#fav_mfa) | **PUT** /self/mfa/{kind} | 
[**get_addon_sso_data**](SelfApi.md#get_addon_sso_data) | **GET** /self/addons/{addonId}/sso | 
[**get_application_deployment**](SelfApi.md#get_application_deployment) | **GET** /self/applications/{appId}/deployments/{deploymentId} | 
[**get_application_deployments**](SelfApi.md#get_application_deployments) | **GET** /self/applications/{appId}/deployments | 
[**get_backup_codes**](SelfApi.md#get_backup_codes) | **GET** /self/mfa/{kind}/backupcodes | 
[**get_confirmation_email**](SelfApi.md#get_confirmation_email) | **GET** /self/confirmation_email | 
[**get_consumptions**](SelfApi.md#get_consumptions) | **GET** /self/consumptions | 
[**get_email_addresses**](SelfApi.md#get_email_addresses) | **GET** /self/emails | 
[**get_id**](SelfApi.md#get_id) | **GET** /self/id | 
[**get_self_addon_by_id**](SelfApi.md#get_self_addon_by_id) | **GET** /self/addons/{addonId} | 
[**get_self_addon_env_by_addon_id**](SelfApi.md#get_self_addon_env_by_addon_id) | **GET** /self/addons/{addonId}/env | 
[**get_self_addon_tags_by_addon_id**](SelfApi.md#get_self_addon_tags_by_addon_id) | **GET** /self/addons/{addonId}/tags | 
[**get_self_addons**](SelfApi.md#get_self_addons) | **GET** /self/addons | 
[**get_self_addons_linked_to_application_by_app_id**](SelfApi.md#get_self_addons_linked_to_application_by_app_id) | **GET** /self/applications/{appId}/addons | 
[**get_self_amount**](SelfApi.md#get_self_amount) | **GET** /self/credits | 
[**get_self_application_branches_by_app_id**](SelfApi.md#get_self_application_branches_by_app_id) | **GET** /self/applications/{appId}/branches | 
[**get_self_application_by_app_id**](SelfApi.md#get_self_application_by_app_id) | **GET** /self/applications/{appId} | 
[**get_self_application_dependencies_by_app_id**](SelfApi.md#get_self_application_dependencies_by_app_id) | **GET** /self/applications/{appId}/dependencies | 
[**get_self_application_dependencies_env_by_app_id**](SelfApi.md#get_self_application_dependencies_env_by_app_id) | **GET** /self/applications/{appId}/dependencies/env | 
[**get_self_application_dependents**](SelfApi.md#get_self_application_dependents) | **GET** /self/applications/{appId}/dependents | 
[**get_self_application_env_by_app_id**](SelfApi.md#get_self_application_env_by_app_id) | **GET** /self/applications/{appId}/env | 
[**get_self_application_instance_by_app_and_instance_id**](SelfApi.md#get_self_application_instance_by_app_and_instance_id) | **GET** /self/applications/{appId}/instances/{instanceId} | 
[**get_self_application_instances_by_app_id**](SelfApi.md#get_self_application_instances_by_app_id) | **GET** /self/applications/{appId}/instances | 
[**get_self_application_tags_by_app_id**](SelfApi.md#get_self_application_tags_by_app_id) | **GET** /self/applications/{appId}/tags | 
[**get_self_applications**](SelfApi.md#get_self_applications) | **GET** /self/applications | 
[**get_self_applications_linked_to_addon_by_addon_id**](SelfApi.md#get_self_applications_linked_to_addon_by_addon_id) | **GET** /self/addons/{addonId}/applications | 
[**get_self_cli_tokens**](SelfApi.md#get_self_cli_tokens) | **GET** /self/cli_tokens | 
[**get_self_consumer**](SelfApi.md#get_self_consumer) | **GET** /self/consumers/{key} | 
[**get_self_consumer_secret**](SelfApi.md#get_self_consumer_secret) | **GET** /self/consumers/{key}/secret | 
[**get_self_consumers**](SelfApi.md#get_self_consumers) | **GET** /self/consumers | 
[**get_self_default_method**](SelfApi.md#get_self_default_method) | **GET** /self/payments/methods/default | 
[**get_self_env_of_addons_linked_to_application_by_app_id**](SelfApi.md#get_self_env_of_addons_linked_to_application_by_app_id) | **GET** /self/applications/{appId}/addons/env | 
[**get_self_exposed_env_by_app_id**](SelfApi.md#get_self_exposed_env_by_app_id) | **GET** /self/applications/{appId}/exposed_env | 
[**get_self_favourite_vhost_by_app_id**](SelfApi.md#get_self_favourite_vhost_by_app_id) | **GET** /self/applications/{appId}/vhosts/favourite | 
[**get_self_instances_for_all_apps**](SelfApi.md#get_self_instances_for_all_apps) | **GET** /self/instances | 
[**get_self_invoice_by_id**](SelfApi.md#get_self_invoice_by_id) | **GET** /self/payments/billings/{bid} | 
[**get_self_invoices**](SelfApi.md#get_self_invoices) | **GET** /self/payments/billings | 
[**get_self_monthly_invoice**](SelfApi.md#get_self_monthly_invoice) | **GET** /self/payments/monthlyinvoice | 
[**get_self_payment_info**](SelfApi.md#get_self_payment_info) | **GET** /self/payment-info | 
[**get_self_payment_methods**](SelfApi.md#get_self_payment_methods) | **GET** /self/payments/methods | 
[**get_self_pdf_invoice_by_id**](SelfApi.md#get_self_pdf_invoice_by_id) | **GET** /self/payments/billings/{bid}.pdf | 
[**get_self_price_with_tax**](SelfApi.md#get_self_price_with_tax) | **GET** /self/payments/fullprice/{price} | 
[**get_self_recurrent_payment**](SelfApi.md#get_self_recurrent_payment) | **GET** /self/payments/recurring | 
[**get_self_stripe_token**](SelfApi.md#get_self_stripe_token) | **GET** /self/payments/tokens/stripe | 
[**get_self_tokens**](SelfApi.md#get_self_tokens) | **GET** /self/tokens | 
[**get_self_vhost_by_app_id**](SelfApi.md#get_self_vhost_by_app_id) | **GET** /self/applications/{appId}/vhosts | 
[**get_ssh_keys**](SelfApi.md#get_ssh_keys) | **GET** /self/keys | 
[**get_summary**](SelfApi.md#get_summary) | **GET** /summary | 
[**get_user**](SelfApi.md#get_user) | **GET** /self | 
[**link_self_addon_to_application_by_app_id**](SelfApi.md#link_self_addon_to_application_by_app_id) | **POST** /self/applications/{appId}/addons | 
[**mark_self_favourite_vhost_by_app_id**](SelfApi.md#mark_self_favourite_vhost_by_app_id) | **PUT** /self/applications/{appId}/vhosts/favourite | 
[**preorder_self_addon**](SelfApi.md#preorder_self_addon) | **POST** /self/addons/preorders | 
[**provision_self_addon**](SelfApi.md#provision_self_addon) | **POST** /self/addons | 
[**redeploy_self_application_by_app_id**](SelfApi.md#redeploy_self_application_by_app_id) | **POST** /self/applications/{appId}/instances | 
[**remove_email_address**](SelfApi.md#remove_email_address) | **DELETE** /self/emails/{email} | 
[**remove_self_application_env_by_app_id_and_env_name**](SelfApi.md#remove_self_application_env_by_app_id_and_env_name) | **DELETE** /self/applications/{appId}/env/{envName} | 
[**remove_self_vhost_by_app_id**](SelfApi.md#remove_self_vhost_by_app_id) | **DELETE** /self/applications/{appId}/vhosts/{domain} | 
[**remove_ssh_key**](SelfApi.md#remove_ssh_key) | **DELETE** /self/keys/{key} | 
[**rename_addon**](SelfApi.md#rename_addon) | **PUT** /self/addons/{addonId} | 
[**revoke_all_tokens**](SelfApi.md#revoke_all_tokens) | **DELETE** /self/tokens | 
[**revoke_token**](SelfApi.md#revoke_token) | **DELETE** /self/tokens/{token} | 
[**set_self_application_branch_by_app_id**](SelfApi.md#set_self_application_branch_by_app_id) | **PUT** /self/applications/{appId}/branch | 
[**set_self_build_instance_flavor_by_app_id**](SelfApi.md#set_self_build_instance_flavor_by_app_id) | **PUT** /self/applications/{appId}/buildflavor | 
[**set_self_default_method**](SelfApi.md#set_self_default_method) | **PUT** /self/payments/methods/default | 
[**set_self_max_credits_per_month**](SelfApi.md#set_self_max_credits_per_month) | **PUT** /self/payments/monthlyinvoice/maxcredit | 
[**set_user_avatar_from_file**](SelfApi.md#set_user_avatar_from_file) | **PUT** /self/avatar | 
[**undeploy_self_application_by_app_id**](SelfApi.md#undeploy_self_application_by_app_id) | **DELETE** /self/applications/{appId}/instances | 
[**unlink_selfddon_from_application_by_app_and_addon_id**](SelfApi.md#unlink_selfddon_from_application_by_app_and_addon_id) | **DELETE** /self/applications/{appId}/addons/{addonId} | 
[**unmark_self_favourite_vhost_by_app_id**](SelfApi.md#unmark_self_favourite_vhost_by_app_id) | **DELETE** /self/applications/{appId}/vhosts/favourite | 
[**update_self_consumer**](SelfApi.md#update_self_consumer) | **PUT** /self/consumers/{key} | 
[**update_self_exposed_env_by_app_id**](SelfApi.md#update_self_exposed_env_by_app_id) | **PUT** /self/applications/{appId}/exposed_env | 
[**validate_email**](SelfApi.md#validate_email) | **GET** /self/validate_email | 
[**validate_mfa**](SelfApi.md#validate_mfa) | **POST** /self/mfa/{kind}/confirmation | 


# **add_email_address**
> Message add_email_address(email)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    email = "email_example" # str | 
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_email_address(email)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->add_email_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_email_address(email, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->add_email_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  |
 **body** | **str**|  | [optional]

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

# **add_self_addon_tag_by_addon_id**
> [str] add_self_addon_tag_by_addon_id(addon_id, tag)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    addon_id = "addonId_example" # str | 
    tag = "tag_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_self_addon_tag_by_addon_id(addon_id, tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->add_self_addon_tag_by_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |
 **tag** | **str**|  |

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

# **add_self_application**
> ApplicationView add_self_application(wannabe_application)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.wannabe_application import WannabeApplication
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
    api_instance = self_api.SelfApi(api_client)
    wannabe_application = WannabeApplication(
        name="name_example",
        description="description_example",
        zone="zone_example",
        deploy="deploy_example",
        shutdownable=True,
        instance_type="instance_type_example",
        instance_version="instance_version_example",
        instance_variant="instance_variant_example",
        instance_lifetime="REGULAR",
        min_instances=1,
        max_instances=1,
        min_flavor="min_flavor_example",
        max_flavor="max_flavor_example",
        tags=[
            "tags_example",
        ],
        archived=True,
        sticky_sessions=True,
        homogeneous=True,
        favourite=True,
        cancel_on_push=True,
        separate_build=True,
        build_flavor="build_flavor_example",
        oauth_service="oauth_service_example",
        oauth_app_id="oauth_app_id_example",
        oauth_app=WannabeOauthApp(
            owner="owner_example",
            name="name_example",
        ),
        appliance_id="appliance_id_example",
        branch="branch_example",
        force_https="ENABLED",
    ) # WannabeApplication | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_self_application(wannabe_application)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->add_self_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wannabe_application** | [**WannabeApplication**](WannabeApplication.md)|  |

### Return type

[**ApplicationView**](ApplicationView.md)

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

# **add_self_application_dependency_by_app_id**
> Message add_self_application_dependency_by_app_id(app_id, dependency_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    dependency_id = "dependencyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_self_application_dependency_by_app_id(app_id, dependency_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->add_self_application_dependency_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **dependency_id** | **str**|  |

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

# **add_self_application_tag_by_app_id**
> [str] add_self_application_tag_by_app_id(app_id, tag)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    tag = "tag_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_self_application_tag_by_app_id(app_id, tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->add_self_application_tag_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **tag** | **str**|  |

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

# **add_self_payment_method**
> PaymentMethodView add_self_payment_method(payment_data)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.payment_data import PaymentData
from openapi_client.model.payment_method_view import PaymentMethodView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    payment_data = PaymentData(
        type="NEW_CARD",
        token="token_example",
        device_data="device_data_example",
    ) # PaymentData | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_self_payment_method(payment_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->add_self_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_data** | [**PaymentData**](PaymentData.md)|  |

### Return type

[**PaymentMethodView**](PaymentMethodView.md)

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

# **add_self_vhost_by_app_id**
> Message add_self_vhost_by_app_id(app_id, domain)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    domain = "domain_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_self_vhost_by_app_id(app_id, domain)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->add_self_vhost_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **domain** | **str**|  |

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

# **add_ssh_key**
> Message add_ssh_key(key)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_ssh_key(key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->add_ssh_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  |

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

# **buy_self_drops**
> InvoiceRendering buy_self_drops(wanna_buy_package)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.wanna_buy_package import WannaBuyPackage
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
    api_instance = self_api.SelfApi(api_client)
    wanna_buy_package = WannaBuyPackage(
        package_id=1,
        currency="currency_example",
        coupon="coupon_example",
        drop_quantity=3.14,
    ) # WannaBuyPackage | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.buy_self_drops(wanna_buy_package)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->buy_self_drops: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wanna_buy_package** | [**WannaBuyPackage**](WannaBuyPackage.md)|  |

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

# **cancel_deploy**
> Message cancel_deploy(app_id, deployment_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    deployment_id = "deploymentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cancel_deploy(app_id, deployment_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->cancel_deploy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **deployment_id** | **str**|  |

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

# **change_self_addon_plan_by_addon_id**
> AddonView change_self_addon_plan_by_addon_id(addon_id, wannabe_plan_change)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.wannabe_plan_change import WannabePlanChange
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
    api_instance = self_api.SelfApi(api_client)
    addon_id = "addonId_example" # str | 
    wannabe_plan_change = WannabePlanChange(
        plan_id="plan_id_example",
        region="region_example",
        version="version_example",
    ) # WannabePlanChange | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.change_self_addon_plan_by_addon_id(addon_id, wannabe_plan_change)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->change_self_addon_plan_by_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |
 **wannabe_plan_change** | [**WannabePlanChange**](WannabePlanChange.md)|  |

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

# **change_user_password**
> Message change_user_password(wannabe_password)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.wannabe_password import WannabePassword
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
    api_instance = self_api.SelfApi(api_client)
    wannabe_password = WannabePassword(
        old_password="old_password_example",
        new_password="new_password_example",
        drop_tokens=True,
    ) # WannabePassword | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.change_user_password(wannabe_password)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->change_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wannabe_password** | [**WannabePassword**](WannabePassword.md)|  |

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

# **choose_self_payment_provider**
> NextInPaymentFlow choose_self_payment_provider(bid, payment_provider_selection)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.next_in_payment_flow import NextInPaymentFlow
from openapi_client.model.payment_provider_selection import PaymentProviderSelection
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    bid = "bid_example" # str | 
    payment_provider_selection = PaymentProviderSelection(
        provider="PAYPAL",
    ) # PaymentProviderSelection | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.choose_self_payment_provider(bid, payment_provider_selection)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->choose_self_payment_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  |
 **payment_provider_selection** | [**PaymentProviderSelection**](PaymentProviderSelection.md)|  |

### Return type

[**NextInPaymentFlow**](NextInPaymentFlow.md)

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

# **create_mfa**
> create_mfa(kind)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    kind = "kind_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_mfa(kind)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->create_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**|  |

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

# **create_self_consumer**
> OAuth1ConsumerView create_self_consumer(wannabe_o_auth1_consumer)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.o_auth1_consumer_view import OAuth1ConsumerView
from openapi_client.model.wannabe_o_auth1_consumer import WannabeOAuth1Consumer
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    wannabe_o_auth1_consumer = WannabeOAuth1Consumer(
        name="name_example",
        description="description_example",
        url="url_example",
        picture="picture_example",
        base_url="base_url_example",
        rights={
            "key": True,
        },
    ) # WannabeOAuth1Consumer | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_self_consumer(wannabe_o_auth1_consumer)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->create_self_consumer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wannabe_o_auth1_consumer** | [**WannabeOAuth1Consumer**](WannabeOAuth1Consumer.md)|  |

### Return type

[**OAuth1ConsumerView**](OAuth1ConsumerView.md)

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

# **delete_mfa**
> delete_mfa(kind)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    kind = "kind_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_mfa(kind)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->delete_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**|  |

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

# **delete_self_addon_tag_by_addon_id**
> [str] delete_self_addon_tag_by_addon_id(addon_id, tag)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    addon_id = "addonId_example" # str | 
    tag = "tag_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_self_addon_tag_by_addon_id(addon_id, tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->delete_self_addon_tag_by_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |
 **tag** | **str**|  |

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

# **delete_self_application_by_app_id**
> Message delete_self_application_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_self_application_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->delete_self_application_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

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

# **delete_self_application_dependency_by_app_id**
> delete_self_application_dependency_by_app_id(app_id, dependency_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    dependency_id = "dependencyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_self_application_dependency_by_app_id(app_id, dependency_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->delete_self_application_dependency_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **dependency_id** | **str**|  |

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

# **delete_self_application_tag_app_id**
> [str] delete_self_application_tag_app_id(app_id, tag)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    tag = "tag_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_self_application_tag_app_id(app_id, tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->delete_self_application_tag_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **tag** | **str**|  |

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

# **delete_self_card**
> delete_self_card(m_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    m_id = "mId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_self_card(m_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->delete_self_card: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **m_id** | **str**|  |

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

# **delete_self_consumer**
> delete_self_consumer(key)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_self_consumer(key)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->delete_self_consumer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  |

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

# **delete_self_purchase_order**
> delete_self_purchase_order(bid)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    bid = "bid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_self_purchase_order(bid)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->delete_self_purchase_order: %s\n" % e)
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

# **delete_self_recurrent_payment**
> delete_self_recurrent_payment()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.delete_self_recurrent_payment()
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->delete_self_recurrent_payment: %s\n" % e)
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

# **delete_user**
> Message delete_user()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.delete_user()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->delete_user: %s\n" % e)
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

# **deprovision_self_addon_by_id**
> Message deprovision_self_addon_by_id(addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.deprovision_self_addon_by_id(addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->deprovision_self_addon_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |

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

# **edit_self_application_by_app_id**
> ApplicationView edit_self_application_by_app_id(app_id, wannabe_application)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.wannabe_application import WannabeApplication
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    wannabe_application = WannabeApplication(
        name="name_example",
        description="description_example",
        zone="zone_example",
        deploy="deploy_example",
        shutdownable=True,
        instance_type="instance_type_example",
        instance_version="instance_version_example",
        instance_variant="instance_variant_example",
        instance_lifetime="REGULAR",
        min_instances=1,
        max_instances=1,
        min_flavor="min_flavor_example",
        max_flavor="max_flavor_example",
        tags=[
            "tags_example",
        ],
        archived=True,
        sticky_sessions=True,
        homogeneous=True,
        favourite=True,
        cancel_on_push=True,
        separate_build=True,
        build_flavor="build_flavor_example",
        oauth_service="oauth_service_example",
        oauth_app_id="oauth_app_id_example",
        oauth_app=WannabeOauthApp(
            owner="owner_example",
            name="name_example",
        ),
        appliance_id="appliance_id_example",
        branch="branch_example",
        force_https="ENABLED",
    ) # WannabeApplication | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_self_application_by_app_id(app_id, wannabe_application)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->edit_self_application_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **wannabe_application** | [**WannabeApplication**](WannabeApplication.md)|  |

### Return type

[**ApplicationView**](ApplicationView.md)

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

# **edit_self_application_env_by_app_id**
> ApplicationView edit_self_application_env_by_app_id(app_id, body)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_self_application_env_by_app_id(app_id, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->edit_self_application_env_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **body** | **str**|  |

### Return type

[**ApplicationView**](ApplicationView.md)

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

# **edit_self_application_env_by_app_id_and_env_name**
> ApplicationView edit_self_application_env_by_app_id_and_env_name(app_id, env_name, wannabe_value)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.wannabe_value import WannabeValue
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    env_name = "envName_example" # str | 
    wannabe_value = WannabeValue(
        value="value_example",
    ) # WannabeValue | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_self_application_env_by_app_id_and_env_name(app_id, env_name, wannabe_value)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->edit_self_application_env_by_app_id_and_env_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **env_name** | **str**|  |
 **wannabe_value** | [**WannabeValue**](WannabeValue.md)|  |

### Return type

[**ApplicationView**](ApplicationView.md)

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

# **edit_user**
> UserView edit_user(wannabe_user)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.user_view import UserView
from openapi_client.model.wannabe_user import WannabeUser
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    wannabe_user = WannabeUser(
        email="email_example",
        name="name_example",
        password="password_example",
        phone="phone_example",
        address="address_example",
        city="city_example",
        zipcode="zipcode_example",
        country="country_example",
        lang="lang_example",
        terms=True,
        subscription_source="subscription_source_example",
    ) # WannabeUser | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_user(wannabe_user)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->edit_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wannabe_user** | [**WannabeUser**](WannabeUser.md)|  |

### Return type

[**UserView**](UserView.md)

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

# **fav_mfa**
> fav_mfa(kind, wannabe_mfa_fav)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.wannabe_mfa_fav import WannabeMFAFav
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    kind = "kind_example" # str | 
    wannabe_mfa_fav = WannabeMFAFav(
        favourite=True,
    ) # WannabeMFAFav | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.fav_mfa(kind, wannabe_mfa_fav)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->fav_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**|  |
 **wannabe_mfa_fav** | [**WannabeMFAFav**](WannabeMFAFav.md)|  |

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

# **get_addon_sso_data**
> AddonSSOData get_addon_sso_data(addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.addon_sso_data import AddonSSOData
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addon_sso_data(addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_addon_sso_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |

### Return type

[**AddonSSOData**](AddonSSOData.md)

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

# **get_application_deployment**
> get_application_deployment(app_id, deployment_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    deployment_id = "deploymentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_application_deployment(app_id, deployment_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_application_deployment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **deployment_id** | **str**|  |

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

# **get_application_deployments**
> [DeploymentView] get_application_deployments(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.deployment_view import DeploymentView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    limit = "limit_example" # str |  (optional)
    offset = "offset_example" # str |  (optional)
    action = "action_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_application_deployments(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_application_deployments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_application_deployments(app_id, limit=limit, offset=offset, action=action)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_application_deployments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **limit** | **str**|  | [optional]
 **offset** | **str**|  | [optional]
 **action** | **str**|  | [optional]

### Return type

[**[DeploymentView]**](DeploymentView.md)

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

# **get_backup_codes**
> [MFARecoveryCode] get_backup_codes(kind)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.mfa_recovery_code import MFARecoveryCode
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    kind = "kind_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_backup_codes(kind)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_backup_codes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**|  |

### Return type

[**[MFARecoveryCode]**](MFARecoveryCode.md)

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

# **get_confirmation_email**
> Message get_confirmation_email()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_confirmation_email()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_confirmation_email: %s\n" % e)
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

# **get_consumptions**
> str get_consumptions()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str |  (optional)
    _from = "from_example" # str |  (optional)
    to = "to_example" # str |  (optional)
    _for = "for_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_consumptions(app_id=app_id, _from=_from, to=to, _for=_for)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_consumptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | [optional]
 **_from** | **str**|  | [optional]
 **to** | **str**|  | [optional]
 **_for** | **str**|  | [optional]

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

# **get_email_addresses**
> [str] get_email_addresses()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_email_addresses()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_email_addresses: %s\n" % e)
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

# **get_id**
> str get_id()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_id()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_id: %s\n" % e)
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

# **get_self_addon_by_id**
> AddonView get_self_addon_by_id(addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_addon_by_id(addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_addon_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |

### Return type

[**AddonView**](AddonView.md)

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

# **get_self_addon_env_by_addon_id**
> [AddonEnvironmentView] get_self_addon_env_by_addon_id(addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.addon_environment_view import AddonEnvironmentView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_addon_env_by_addon_id(addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_addon_env_by_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |

### Return type

[**[AddonEnvironmentView]**](AddonEnvironmentView.md)

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

# **get_self_addon_tags_by_addon_id**
> [str] get_self_addon_tags_by_addon_id(addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_addon_tags_by_addon_id(addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_addon_tags_by_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |

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

# **get_self_addons**
> [AddonView] get_self_addons()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_self_addons()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_addons: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[AddonView]**](AddonView.md)

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

# **get_self_addons_linked_to_application_by_app_id**
> [AddonView] get_self_addons_linked_to_application_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_addons_linked_to_application_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_addons_linked_to_application_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

### Return type

[**[AddonView]**](AddonView.md)

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

# **get_self_amount**
> DropCountView get_self_amount()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.drop_count_view import DropCountView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_self_amount()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_amount: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DropCountView**](DropCountView.md)

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

# **get_self_application_branches_by_app_id**
> [str] get_self_application_branches_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_application_branches_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_application_branches_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

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

# **get_self_application_by_app_id**
> ApplicationView get_self_application_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_application_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_application_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

### Return type

[**ApplicationView**](ApplicationView.md)

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

# **get_self_application_dependencies_by_app_id**
> [ApplicationView] get_self_application_dependencies_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_application_dependencies_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_application_dependencies_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

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

# **get_self_application_dependencies_env_by_app_id**
> get_self_application_dependencies_env_by_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_self_application_dependencies_env_by_app_id(id, app_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_application_dependencies_env_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **app_id** | **str**|  |

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

# **get_self_application_dependents**
> [ApplicationView] get_self_application_dependents(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_application_dependents(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_application_dependents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

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

# **get_self_application_env_by_app_id**
> [AddonEnvironmentView] get_self_application_env_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.addon_environment_view import AddonEnvironmentView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_application_env_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_application_env_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

### Return type

[**[AddonEnvironmentView]**](AddonEnvironmentView.md)

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

# **get_self_application_instance_by_app_and_instance_id**
> SuperNovaInstanceView get_self_application_instance_by_app_and_instance_id(app_id, instance_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.super_nova_instance_view import SuperNovaInstanceView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    instance_id = "instanceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_application_instance_by_app_and_instance_id(app_id, instance_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_application_instance_by_app_and_instance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **instance_id** | **str**|  |

### Return type

[**SuperNovaInstanceView**](SuperNovaInstanceView.md)

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

# **get_self_application_instances_by_app_id**
> [SuperNovaInstanceView] get_self_application_instances_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.super_nova_instance_view import SuperNovaInstanceView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    deployment_id = "deploymentId_example" # str |  (optional)
    with_deleted = "withDeleted_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_application_instances_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_application_instances_by_app_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_self_application_instances_by_app_id(app_id, deployment_id=deployment_id, with_deleted=with_deleted)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_application_instances_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **deployment_id** | **str**|  | [optional]
 **with_deleted** | **str**|  | [optional]

### Return type

[**[SuperNovaInstanceView]**](SuperNovaInstanceView.md)

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

# **get_self_application_tags_by_app_id**
> [str] get_self_application_tags_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_application_tags_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_application_tags_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

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

# **get_self_applications**
> [ApplicationView] get_self_applications()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_self_applications()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_applications: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_self_applications_linked_to_addon_by_addon_id**
> [ApplicationView] get_self_applications_linked_to_addon_by_addon_id(addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_applications_linked_to_addon_by_addon_id(addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_applications_linked_to_addon_by_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |

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

# **get_self_cli_tokens**
> [CliTokenView] get_self_cli_tokens()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.cli_token_view import CliTokenView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    cli_token = "cli_token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_self_cli_tokens(cli_token=cli_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_cli_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cli_token** | **str**|  | [optional]

### Return type

[**[CliTokenView]**](CliTokenView.md)

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

# **get_self_consumer**
> OAuth1ConsumerView get_self_consumer(key)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.o_auth1_consumer_view import OAuth1ConsumerView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_consumer(key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_consumer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  |

### Return type

[**OAuth1ConsumerView**](OAuth1ConsumerView.md)

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

# **get_self_consumer_secret**
> SecretView get_self_consumer_secret(key)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.secret_view import SecretView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_consumer_secret(key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_consumer_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  |

### Return type

[**SecretView**](SecretView.md)

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

# **get_self_consumers**
> get_self_consumers()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_self_consumers()
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_consumers: %s\n" % e)
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

# **get_self_default_method**
> PaymentMethodView get_self_default_method()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.payment_method_view import PaymentMethodView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_self_default_method()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_default_method: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PaymentMethodView**](PaymentMethodView.md)

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

# **get_self_env_of_addons_linked_to_application_by_app_id**
> [LinkedAddonEnvironmentView] get_self_env_of_addons_linked_to_application_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.linked_addon_environment_view import LinkedAddonEnvironmentView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_env_of_addons_linked_to_application_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_env_of_addons_linked_to_application_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

### Return type

[**[LinkedAddonEnvironmentView]**](LinkedAddonEnvironmentView.md)

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

# **get_self_exposed_env_by_app_id**
> str get_self_exposed_env_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_exposed_env_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_exposed_env_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

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

# **get_self_favourite_vhost_by_app_id**
> VhostView get_self_favourite_vhost_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.vhost_view import VhostView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_favourite_vhost_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_favourite_vhost_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

### Return type

[**VhostView**](VhostView.md)

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

# **get_self_instances_for_all_apps**
> SuperNovaInstanceMap get_self_instances_for_all_apps()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.super_nova_instance_map import SuperNovaInstanceMap
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_self_instances_for_all_apps()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_instances_for_all_apps: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SuperNovaInstanceMap**](SuperNovaInstanceMap.md)

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

# **get_self_invoice_by_id**
> InvoiceRendering get_self_invoice_by_id(bid)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    bid = "bid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_invoice_by_id(bid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_invoice_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  |

### Return type

[**InvoiceRendering**](InvoiceRendering.md)

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

# **get_self_invoices**
> [InvoiceRendering] get_self_invoices()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_self_invoices()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_invoices: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[InvoiceRendering]**](InvoiceRendering.md)

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

# **get_self_monthly_invoice**
> str get_self_monthly_invoice()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_self_monthly_invoice()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_monthly_invoice: %s\n" % e)
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

# **get_self_payment_info**
> PaymentInfoView get_self_payment_info()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.payment_info_view import PaymentInfoView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_self_payment_info()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_payment_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PaymentInfoView**](PaymentInfoView.md)

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

# **get_self_payment_methods**
> [PaymentMethodView] get_self_payment_methods()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.payment_method_view import PaymentMethodView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_self_payment_methods()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_payment_methods: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[PaymentMethodView]**](PaymentMethodView.md)

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

# **get_self_pdf_invoice_by_id**
> get_self_pdf_invoice_by_id(bid)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    bid = "bid_example" # str | 
    token = "token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_self_pdf_invoice_by_id(bid)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_pdf_invoice_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_self_pdf_invoice_by_id(bid, token=token)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_pdf_invoice_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  |
 **token** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_price_with_tax**
> PriceWithTaxInfo get_self_price_with_tax(price)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.price_with_tax_info import PriceWithTaxInfo
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    price = "price_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_price_with_tax(price)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_price_with_tax: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price** | **str**|  |

### Return type

[**PriceWithTaxInfo**](PriceWithTaxInfo.md)

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

# **get_self_recurrent_payment**
> RecurrentPaymentView get_self_recurrent_payment()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.recurrent_payment_view import RecurrentPaymentView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_self_recurrent_payment()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_recurrent_payment: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RecurrentPaymentView**](RecurrentPaymentView.md)

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

# **get_self_stripe_token**
> BraintreeToken get_self_stripe_token()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_self_stripe_token()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_stripe_token: %s\n" % e)
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

# **get_self_tokens**
> [OAuth1AccessTokenView] get_self_tokens()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.o_auth1_access_token_view import OAuth1AccessTokenView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_self_tokens()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_tokens: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[OAuth1AccessTokenView]**](OAuth1AccessTokenView.md)

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

# **get_self_vhost_by_app_id**
> [VhostView] get_self_vhost_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.vhost_view import VhostView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_self_vhost_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_self_vhost_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

### Return type

[**[VhostView]**](VhostView.md)

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

# **get_ssh_keys**
> [SshKeyView] get_ssh_keys()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_ssh_keys()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_ssh_keys: %s\n" % e)
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

# **get_summary**
> Summary get_summary()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.summary import Summary
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    full = "full_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_summary(full=full)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full** | **str**|  | [optional]

### Return type

[**Summary**](Summary.md)

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

# **get_user**
> UserView get_user()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_user()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->get_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **link_self_addon_to_application_by_app_id**
> link_self_addon_to_application_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.link_self_addon_to_application_by_app_id(app_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->link_self_addon_to_application_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

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

# **mark_self_favourite_vhost_by_app_id**
> VhostView mark_self_favourite_vhost_by_app_id(app_id, vhost_view)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.vhost_view import VhostView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    vhost_view = VhostView(
        fqdn="fqdn_example",
    ) # VhostView | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.mark_self_favourite_vhost_by_app_id(app_id, vhost_view)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->mark_self_favourite_vhost_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **vhost_view** | [**VhostView**](VhostView.md)|  |

### Return type

[**VhostView**](VhostView.md)

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

# **preorder_self_addon**
> InvoiceRendering preorder_self_addon(wannabe_addon_provision)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.wannabe_addon_provision import WannabeAddonProvision
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
    api_instance = self_api.SelfApi(api_client)
    wannabe_addon_provision = WannabeAddonProvision(
        provider_id="provider_id_example",
        plan="plan_example",
        linked_app="linked_app_example",
        name="name_example",
        region="region_example",
        options={
            "key": "key_example",
        },
        version="version_example",
        payment_intent=SetupIntentView(
            owner_id="owner_id_example",
            id="id_example",
            client_secret="client_secret_example",
            customer="customer_example",
        ),
        payment_method_type="CREDITCARD",
        sepa_source_id="sepa_source_id_example",
    ) # WannabeAddonProvision | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preorder_self_addon(wannabe_addon_provision)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->preorder_self_addon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wannabe_addon_provision** | [**WannabeAddonProvision**](WannabeAddonProvision.md)|  |

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

# **provision_self_addon**
> AddonView provision_self_addon(wannabe_addon_provision)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.addon_view import AddonView
from openapi_client.model.wannabe_addon_provision import WannabeAddonProvision
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    wannabe_addon_provision = WannabeAddonProvision(
        provider_id="provider_id_example",
        plan="plan_example",
        linked_app="linked_app_example",
        name="name_example",
        region="region_example",
        options={
            "key": "key_example",
        },
        version="version_example",
        payment_intent=SetupIntentView(
            owner_id="owner_id_example",
            id="id_example",
            client_secret="client_secret_example",
            customer="customer_example",
        ),
        payment_method_type="CREDITCARD",
        sepa_source_id="sepa_source_id_example",
    ) # WannabeAddonProvision | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.provision_self_addon(wannabe_addon_provision)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->provision_self_addon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wannabe_addon_provision** | [**WannabeAddonProvision**](WannabeAddonProvision.md)|  |

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

# **redeploy_self_application_by_app_id**
> Message redeploy_self_application_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    commit = "commit_example" # str |  (optional)
    use_cache = "useCache_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.redeploy_self_application_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->redeploy_self_application_by_app_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.redeploy_self_application_by_app_id(app_id, commit=commit, use_cache=use_cache)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->redeploy_self_application_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **commit** | **str**|  | [optional]
 **use_cache** | **str**|  | [optional]

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

# **remove_email_address**
> Message remove_email_address(email)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    email = "email_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_email_address(email)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->remove_email_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  |

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

# **remove_self_application_env_by_app_id_and_env_name**
> ApplicationView remove_self_application_env_by_app_id_and_env_name(app_id, env_name)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    env_name = "envName_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_self_application_env_by_app_id_and_env_name(app_id, env_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->remove_self_application_env_by_app_id_and_env_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **env_name** | **str**|  |

### Return type

[**ApplicationView**](ApplicationView.md)

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

# **remove_self_vhost_by_app_id**
> Message remove_self_vhost_by_app_id(app_id, domain)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    domain = "domain_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_self_vhost_by_app_id(app_id, domain)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->remove_self_vhost_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **domain** | **str**|  |

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

# **remove_ssh_key**
> Message remove_ssh_key(key)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_ssh_key(key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->remove_ssh_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  |

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

# **rename_addon**
> AddonView rename_addon(addon_id, wannabe_addon_provision)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.addon_view import AddonView
from openapi_client.model.wannabe_addon_provision import WannabeAddonProvision
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    addon_id = "addonId_example" # str | 
    wannabe_addon_provision = WannabeAddonProvision(
        provider_id="provider_id_example",
        plan="plan_example",
        linked_app="linked_app_example",
        name="name_example",
        region="region_example",
        options={
            "key": "key_example",
        },
        version="version_example",
        payment_intent=SetupIntentView(
            owner_id="owner_id_example",
            id="id_example",
            client_secret="client_secret_example",
            customer="customer_example",
        ),
        payment_method_type="CREDITCARD",
        sepa_source_id="sepa_source_id_example",
    ) # WannabeAddonProvision | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.rename_addon(addon_id, wannabe_addon_provision)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->rename_addon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  |
 **wannabe_addon_provision** | [**WannabeAddonProvision**](WannabeAddonProvision.md)|  |

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

# **revoke_all_tokens**
> Message revoke_all_tokens()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.revoke_all_tokens()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->revoke_all_tokens: %s\n" % e)
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

# **revoke_token**
> Message revoke_token(token)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    token = "token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.revoke_token(token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->revoke_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  |

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

# **set_self_application_branch_by_app_id**
> set_self_application_branch_by_app_id(app_id, wannabe_branch)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.wannabe_branch import WannabeBranch
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    wannabe_branch = WannabeBranch(
        branch="branch_example",
    ) # WannabeBranch | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_self_application_branch_by_app_id(app_id, wannabe_branch)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->set_self_application_branch_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **wannabe_branch** | [**WannabeBranch**](WannabeBranch.md)|  |

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

# **set_self_build_instance_flavor_by_app_id**
> set_self_build_instance_flavor_by_app_id(app_id, wannabe_build_flavor)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.wannabe_build_flavor import WannabeBuildFlavor
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    wannabe_build_flavor = WannabeBuildFlavor(
        flavor_name="flavor_name_example",
    ) # WannabeBuildFlavor | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_self_build_instance_flavor_by_app_id(app_id, wannabe_build_flavor)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->set_self_build_instance_flavor_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **wannabe_build_flavor** | [**WannabeBuildFlavor**](WannabeBuildFlavor.md)|  |

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

# **set_self_default_method**
> set_self_default_method(payment_data)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    payment_data = PaymentData(
        type="NEW_CARD",
        token="token_example",
        device_data="device_data_example",
    ) # PaymentData | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_self_default_method(payment_data)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->set_self_default_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_data** | [**PaymentData**](PaymentData.md)|  |

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

# **set_self_max_credits_per_month**
> WannabeMaxCredits set_self_max_credits_per_month(wannabe_max_credits)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.wannabe_max_credits import WannabeMaxCredits
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    wannabe_max_credits = WannabeMaxCredits(
        max=3.14,
    ) # WannabeMaxCredits | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_self_max_credits_per_month(wannabe_max_credits)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->set_self_max_credits_per_month: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wannabe_max_credits** | [**WannabeMaxCredits**](WannabeMaxCredits.md)|  |

### Return type

[**WannabeMaxCredits**](WannabeMaxCredits.md)

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

# **set_user_avatar_from_file**
> UrlView set_user_avatar_from_file(body)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.url_view import UrlView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    body = open('/path/to/file', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_user_avatar_from_file(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->set_user_avatar_from_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **file_type**|  |

### Return type

[**UrlView**](UrlView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: image/bmp, image/gif, image/jpeg, image/png, image/tiff
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undeploy_self_application_by_app_id**
> Message undeploy_self_application_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.undeploy_self_application_by_app_id(app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->undeploy_self_application_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

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

# **unlink_selfddon_from_application_by_app_and_addon_id**
> unlink_selfddon_from_application_by_app_and_addon_id(app_id, addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.unlink_selfddon_from_application_by_app_and_addon_id(app_id, addon_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->unlink_selfddon_from_application_by_app_and_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmark_self_favourite_vhost_by_app_id**
> unmark_self_favourite_vhost_by_app_id(app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.unmark_self_favourite_vhost_by_app_id(app_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->unmark_self_favourite_vhost_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |

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

# **update_self_consumer**
> OAuth1ConsumerView update_self_consumer(key, wannabe_o_auth1_consumer)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.o_auth1_consumer_view import OAuth1ConsumerView
from openapi_client.model.wannabe_o_auth1_consumer import WannabeOAuth1Consumer
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    key = "key_example" # str | 
    wannabe_o_auth1_consumer = WannabeOAuth1Consumer(
        name="name_example",
        description="description_example",
        url="url_example",
        picture="picture_example",
        base_url="base_url_example",
        rights={
            "key": True,
        },
    ) # WannabeOAuth1Consumer | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_self_consumer(key, wannabe_o_auth1_consumer)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->update_self_consumer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  |
 **wannabe_o_auth1_consumer** | [**WannabeOAuth1Consumer**](WannabeOAuth1Consumer.md)|  |

### Return type

[**OAuth1ConsumerView**](OAuth1ConsumerView.md)

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

# **update_self_exposed_env_by_app_id**
> Message update_self_exposed_env_by_app_id(app_id, body)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
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
    api_instance = self_api.SelfApi(api_client)
    app_id = "appId_example" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_self_exposed_env_by_app_id(app_id, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->update_self_exposed_env_by_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **body** | **str**|  |

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

# **validate_email**
> validate_email()



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    validation_key = "validationKey_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.validate_email(validation_key=validation_key)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->validate_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_key** | **str**|  | [optional]

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

# **validate_mfa**
> validate_mfa(kind, wannabe_mfa_creds)



### Example

```python
import time
import openapi_client
from openapi_client.api import self_api
from openapi_client.model.wannabe_mfa_creds import WannabeMFACreds
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = self_api.SelfApi(api_client)
    kind = "kind_example" # str | 
    wannabe_mfa_creds = WannabeMFACreds(
        revoke_tokens=True,
        code="code_example",
    ) # WannabeMFACreds | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.validate_mfa(kind, wannabe_mfa_creds)
    except openapi_client.ApiException as e:
        print("Exception when calling SelfApi->validate_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**|  |
 **wannabe_mfa_creds** | [**WannabeMFACreds**](WannabeMFACreds.md)|  |

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

