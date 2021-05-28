# openapi_client.OrganisationApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_addon_migration**](OrganisationApi.md#abort_addon_migration) | **DELETE** /organisations/{id}/addons/{addonId}/migrations/{migrationId} | 
[**add_addon_tag_by_orga_and_addon_id**](OrganisationApi.md#add_addon_tag_by_orga_and_addon_id) | **PUT** /organisations/{id}/addons/{addonId}/tags/{tag} | 
[**add_application_by_orga**](OrganisationApi.md#add_application_by_orga) | **POST** /organisations/{id}/applications | 
[**add_application_dependency_by_orga_and_app_id**](OrganisationApi.md#add_application_dependency_by_orga_and_app_id) | **PUT** /organisations/{id}/applications/{appId}/dependencies/{dependencyId} | 
[**add_application_tag_by_orga_and_app_id**](OrganisationApi.md#add_application_tag_by_orga_and_app_id) | **PUT** /organisations/{id}/applications/{appId}/tags/{tag} | 
[**add_beta_tester**](OrganisationApi.md#add_beta_tester) | **POST** /organisations/{id}/addonproviders/{providerId}/testers | 
[**add_organisation_member**](OrganisationApi.md#add_organisation_member) | **POST** /organisations/{id}/members | 
[**add_payment_method_by_orga**](OrganisationApi.md#add_payment_method_by_orga) | **POST** /organisations/{id}/payments/methods | 
[**add_provider_feature**](OrganisationApi.md#add_provider_feature) | **POST** /organisations/{id}/addonproviders/{providerId}/features | 
[**add_provider_plan**](OrganisationApi.md#add_provider_plan) | **POST** /organisations/{id}/addonproviders/{providerId}/plans | 
[**add_tcp_redir**](OrganisationApi.md#add_tcp_redir) | **POST** /organisations/{id}/applications/{appId}/tcpRedirs | 
[**add_vhosts_by_orga_and_app_id**](OrganisationApi.md#add_vhosts_by_orga_and_app_id) | **PUT** /organisations/{id}/applications/{appId}/vhosts/{domain} | 
[**buy_drops_by_orga**](OrganisationApi.md#buy_drops_by_orga) | **POST** /organisations/{id}/payments/billings | 
[**cancel_application_deployment_for_orga**](OrganisationApi.md#cancel_application_deployment_for_orga) | **DELETE** /organisations/{id}/applications/{appId}/deployments/{deploymentId}/instances | 
[**change_plan_by_orga_and_addon_id**](OrganisationApi.md#change_plan_by_orga_and_addon_id) | **POST** /organisations/{id}/addons/{addonId}/migrations | 
[**choose_payment_provider_by_orga**](OrganisationApi.md#choose_payment_provider_by_orga) | **PUT** /organisations/{id}/payments/billings/{bid} | 
[**create_consumer_by_orga**](OrganisationApi.md#create_consumer_by_orga) | **POST** /organisations/{id}/consumers | 
[**create_organisation**](OrganisationApi.md#create_organisation) | **POST** /organisations | 
[**create_provider**](OrganisationApi.md#create_provider) | **POST** /organisations/{id}/addonproviders | 
[**delete_addon_tag_by_orga_and_addon_id**](OrganisationApi.md#delete_addon_tag_by_orga_and_addon_id) | **DELETE** /organisations/{id}/addons/{addonId}/tags/{tag} | 
[**delete_application_by_orga_and_app_id**](OrganisationApi.md#delete_application_by_orga_and_app_id) | **DELETE** /organisations/{id}/applications/{appId} | 
[**delete_application_dependency_by_orga_and_app_id**](OrganisationApi.md#delete_application_dependency_by_orga_and_app_id) | **DELETE** /organisations/{id}/applications/{appId}/dependencies/{dependencyId} | 
[**delete_application_tag_by_orga_and_app_id**](OrganisationApi.md#delete_application_tag_by_orga_and_app_id) | **DELETE** /organisations/{id}/applications/{appId}/tags/{tag} | 
[**delete_consumer_by_orga**](OrganisationApi.md#delete_consumer_by_orga) | **DELETE** /organisations/{id}/consumers/{key} | 
[**delete_organisation**](OrganisationApi.md#delete_organisation) | **DELETE** /organisations/{id} | 
[**delete_payment_method_by_orga**](OrganisationApi.md#delete_payment_method_by_orga) | **DELETE** /organisations/{id}/payments/methods/{mId} | 
[**delete_provider**](OrganisationApi.md#delete_provider) | **DELETE** /organisations/{id}/addonproviders/{providerId} | 
[**delete_provider_feature**](OrganisationApi.md#delete_provider_feature) | **DELETE** /organisations/{id}/addonproviders/{providerId}/features/{featureId} | 
[**delete_provider_plan**](OrganisationApi.md#delete_provider_plan) | **DELETE** /organisations/{id}/addonproviders/{providerId}/plans/{planId} | 
[**delete_provider_plan_feature**](OrganisationApi.md#delete_provider_plan_feature) | **DELETE** /organisations/{id}/addonproviders/{providerId}/plans/{planId}/features/{featureName} | 
[**delete_purchase_order_by_orga**](OrganisationApi.md#delete_purchase_order_by_orga) | **DELETE** /organisations/{id}/payments/billings/{bid} | 
[**delete_recurrent_payment_by_orga**](OrganisationApi.md#delete_recurrent_payment_by_orga) | **DELETE** /organisations/{id}/payments/recurring | 
[**deprovision_addon_by_orga_and_addon_id**](OrganisationApi.md#deprovision_addon_by_orga_and_addon_id) | **DELETE** /organisations/{id}/addons/{addonId} | 
[**edit_application_by_orga_and_app_id**](OrganisationApi.md#edit_application_by_orga_and_app_id) | **PUT** /organisations/{id}/applications/{appId} | 
[**edit_application_env_by_orga_and_app_id_and_env_name**](OrganisationApi.md#edit_application_env_by_orga_and_app_id_and_env_name) | **PUT** /organisations/{id}/applications/{appId}/env/{envName} | 
[**edit_application_environment_by_orga_and_app_id**](OrganisationApi.md#edit_application_environment_by_orga_and_app_id) | **PUT** /organisations/{id}/applications/{appId}/env | 
[**edit_organisation**](OrganisationApi.md#edit_organisation) | **PUT** /organisations/{id} | 
[**edit_organisation_member**](OrganisationApi.md#edit_organisation_member) | **PUT** /organisations/{id}/members/{userId} | 
[**edit_provider_plan**](OrganisationApi.md#edit_provider_plan) | **PUT** /organisations/{id}/addonproviders/{providerId}/plans/{planId} | 
[**edit_provider_plan_feature**](OrganisationApi.md#edit_provider_plan_feature) | **PUT** /organisations/{id}/addonproviders/{providerId}/plans/{planId}/features/{featureName} | 
[**get_addon_by_orga_and_addon_id**](OrganisationApi.md#get_addon_by_orga_and_addon_id) | **GET** /organisations/{id}/addons/{addonId} | 
[**get_addon_env_by_orga_and_addon_id**](OrganisationApi.md#get_addon_env_by_orga_and_addon_id) | **GET** /organisations/{id}/addons/{addonId}/env | 
[**get_addon_instance**](OrganisationApi.md#get_addon_instance) | **GET** /organisations/{id}/addons/{addonId}/instances/{instanceId} | 
[**get_addon_instances**](OrganisationApi.md#get_addon_instances) | **GET** /organisations/{id}/addons/{addonId}/instances | 
[**get_addon_migration**](OrganisationApi.md#get_addon_migration) | **GET** /organisations/{id}/addons/{addonId}/migrations/{migrationId} | 
[**get_addon_migrations**](OrganisationApi.md#get_addon_migrations) | **GET** /organisations/{id}/addons/{addonId}/migrations | 
[**get_addon_sso_data_for_orga**](OrganisationApi.md#get_addon_sso_data_for_orga) | **GET** /organisations/{id}/addons/{addonId}/sso | 
[**get_addon_tags_by_orga_id_and_addon_id**](OrganisationApi.md#get_addon_tags_by_orga_id_and_addon_id) | **GET** /organisations/{id}/addons/{addonId}/tags | 
[**get_addons_by_orga_id**](OrganisationApi.md#get_addons_by_orga_id) | **GET** /organisations/{id}/addons | 
[**get_addons_linked_to_application_by_orga_and_app_id**](OrganisationApi.md#get_addons_linked_to_application_by_orga_and_app_id) | **GET** /organisations/{id}/applications/{appId}/addons | 
[**get_all_applications_by_orga**](OrganisationApi.md#get_all_applications_by_orga) | **GET** /organisations/{id}/applications | 
[**get_amount_for_orga**](OrganisationApi.md#get_amount_for_orga) | **GET** /organisations/{id}/credits | 
[**get_application_branches_by_orga_and_app_id**](OrganisationApi.md#get_application_branches_by_orga_and_app_id) | **GET** /organisations/{id}/applications/{appId}/branches | 
[**get_application_by_orga_and_app_id**](OrganisationApi.md#get_application_by_orga_and_app_id) | **GET** /organisations/{id}/applications/{appId} | 
[**get_application_dependencies_by_orga_and_app_id**](OrganisationApi.md#get_application_dependencies_by_orga_and_app_id) | **GET** /organisations/{id}/applications/{appId}/dependencies | 
[**get_application_dependencies_env_by_orga_and_app_id**](OrganisationApi.md#get_application_dependencies_env_by_orga_and_app_id) | **GET** /organisations/{id}/applications/{appId}/dependencies/env | 
[**get_application_dependents_by_orga_and_app_id**](OrganisationApi.md#get_application_dependents_by_orga_and_app_id) | **GET** /organisations/{id}/applications/{appId}/dependents | 
[**get_application_deployment_for_orga**](OrganisationApi.md#get_application_deployment_for_orga) | **GET** /organisations/{id}/applications/{appId}/deployments/{deploymentId} | 
[**get_application_deployments_for_orga**](OrganisationApi.md#get_application_deployments_for_orga) | **GET** /organisations/{id}/applications/{appId}/deployments | 
[**get_application_env_by_orga_and_app_id**](OrganisationApi.md#get_application_env_by_orga_and_app_id) | **GET** /organisations/{id}/applications/{appId}/env | 
[**get_application_instance_by_orga_and_app_and_instance_id**](OrganisationApi.md#get_application_instance_by_orga_and_app_and_instance_id) | **GET** /organisations/{id}/applications/{appId}/instances/{instanceId} | 
[**get_application_instances_by_orga_and_app_id**](OrganisationApi.md#get_application_instances_by_orga_and_app_id) | **GET** /organisations/{id}/applications/{appId}/instances | 
[**get_application_tags_by_orga_and_app_id**](OrganisationApi.md#get_application_tags_by_orga_and_app_id) | **GET** /organisations/{id}/applications/{appId}/tags | 
[**get_applications_linked_to_addon_by_orga_and_addon_id**](OrganisationApi.md#get_applications_linked_to_addon_by_orga_and_addon_id) | **GET** /organisations/{id}/addons/{addonId}/applications | 
[**get_consumer_by_orga**](OrganisationApi.md#get_consumer_by_orga) | **GET** /organisations/{id}/consumers/{key} | 
[**get_consumer_secret_by_orga**](OrganisationApi.md#get_consumer_secret_by_orga) | **GET** /organisations/{id}/consumers/{key}/secret | 
[**get_consumers_by_orga**](OrganisationApi.md#get_consumers_by_orga) | **GET** /organisations/{id}/consumers | 
[**get_consumptions_for_orga**](OrganisationApi.md#get_consumptions_for_orga) | **GET** /organisations/{id}/consumptions | 
[**get_default_method_by_orga**](OrganisationApi.md#get_default_method_by_orga) | **GET** /organisations/{id}/payments/methods/default | 
[**get_deployments_for_all_apps**](OrganisationApi.md#get_deployments_for_all_apps) | **GET** /organisations/{id}/deployments | 
[**get_env_of_addons_linked_to_application_by_orga_and_app_id**](OrganisationApi.md#get_env_of_addons_linked_to_application_by_orga_and_app_id) | **GET** /organisations/{id}/applications/{appId}/addons/env | 
[**get_exposed_env_by_orga_and_app_id**](OrganisationApi.md#get_exposed_env_by_orga_and_app_id) | **GET** /organisations/{id}/applications/{appId}/exposed_env | 
[**get_favourite_vhost_by_orga_and_app_id**](OrganisationApi.md#get_favourite_vhost_by_orga_and_app_id) | **GET** /organisations/{id}/applications/{appId}/vhosts/favourite | 
[**get_instances_for_all_apps_for_orga**](OrganisationApi.md#get_instances_for_all_apps_for_orga) | **GET** /organisations/{id}/instances | 
[**get_invoice_by_orga**](OrganisationApi.md#get_invoice_by_orga) | **GET** /organisations/{id}/payments/billings/{bid} | 
[**get_invoices_by_orga**](OrganisationApi.md#get_invoices_by_orga) | **GET** /organisations/{id}/payments/billings | 
[**get_monthly_invoice_by_orga**](OrganisationApi.md#get_monthly_invoice_by_orga) | **GET** /organisations/{id}/payments/monthlyinvoice | 
[**get_namespaces**](OrganisationApi.md#get_namespaces) | **GET** /organisations/{id}/namespaces | 
[**get_new_setup_intent_by_orga**](OrganisationApi.md#get_new_setup_intent_by_orga) | **GET** /organisations/{id}/payments/methods/newintent | 
[**get_organisation**](OrganisationApi.md#get_organisation) | **GET** /organisations/{id} | 
[**get_organisation_members**](OrganisationApi.md#get_organisation_members) | **GET** /organisations/{id}/members | 
[**get_payment_info_for_orga**](OrganisationApi.md#get_payment_info_for_orga) | **GET** /organisations/{id}/payment-info | 
[**get_pdf_invoice_by_orga**](OrganisationApi.md#get_pdf_invoice_by_orga) | **GET** /organisations/{id}/payments/billings/{bid}.pdf | 
[**get_price_with_tax_by_orga**](OrganisationApi.md#get_price_with_tax_by_orga) | **GET** /organisations/{id}/payments/fullprice/{price} | 
[**get_provider_features**](OrganisationApi.md#get_provider_features) | **GET** /organisations/{id}/addonproviders/{providerId}/features | 
[**get_provider_info**](OrganisationApi.md#get_provider_info) | **GET** /organisations/{id}/addonproviders/{providerId} | 
[**get_provider_plan**](OrganisationApi.md#get_provider_plan) | **GET** /organisations/{id}/addonproviders/{providerId}/plans/{planId} | 
[**get_provider_plans**](OrganisationApi.md#get_provider_plans) | **GET** /organisations/{id}/addonproviders/{providerId}/plans | 
[**get_provider_tags**](OrganisationApi.md#get_provider_tags) | **GET** /organisations/{id}/addonproviders/{providerId}/tags | 
[**get_providers_info**](OrganisationApi.md#get_providers_info) | **GET** /organisations/{id}/addonproviders | 
[**get_recurrent_payment_by_orga**](OrganisationApi.md#get_recurrent_payment_by_orga) | **GET** /organisations/{id}/payments/recurring | 
[**get_sso_data_for_orga**](OrganisationApi.md#get_sso_data_for_orga) | **GET** /organisations/{id}/addonproviders/{providerId}/sso | 
[**get_stripe_token_by_orga**](OrganisationApi.md#get_stripe_token_by_orga) | **GET** /organisations/{id}/payments/tokens/stripe | 
[**get_tcp_redirs**](OrganisationApi.md#get_tcp_redirs) | **GET** /organisations/{id}/applications/{appId}/tcpRedirs | 
[**get_unpaid_invoices_by_orga**](OrganisationApi.md#get_unpaid_invoices_by_orga) | **GET** /organisations/{id}/payments/billings/unpaid | 
[**get_unpaid_invoices_by_orga1**](OrganisationApi.md#get_unpaid_invoices_by_orga1) | **GET** /organisations/{id}/payments/methods | 
[**get_user_organisationss**](OrganisationApi.md#get_user_organisationss) | **GET** /organisations | 
[**get_vhosts_by_orga_and_app_id**](OrganisationApi.md#get_vhosts_by_orga_and_app_id) | **GET** /organisations/{id}/applications/{appId}/vhosts | 
[**link_addon_to_application_by_orga_and_app_id**](OrganisationApi.md#link_addon_to_application_by_orga_and_app_id) | **POST** /organisations/{id}/applications/{appId}/addons | 
[**mark_favourite_vhost_by_orga_and_app_id**](OrganisationApi.md#mark_favourite_vhost_by_orga_and_app_id) | **PUT** /organisations/{id}/applications/{appId}/vhosts/favourite | 
[**preorder_addon_by_orga_id**](OrganisationApi.md#preorder_addon_by_orga_id) | **POST** /organisations/{id}/addons/preorders | 
[**preorder_migration**](OrganisationApi.md#preorder_migration) | **GET** /organisations/{id}/addons/{addonId}/migrations/preorders | 
[**provision_addon_by_orga_id**](OrganisationApi.md#provision_addon_by_orga_id) | **POST** /organisations/{id}/addons | 
[**redeploy_application_by_orga_and_app_id**](OrganisationApi.md#redeploy_application_by_orga_and_app_id) | **POST** /organisations/{id}/applications/{appId}/instances | 
[**remove_application_env_by_orga_and_app_id_and_env_name**](OrganisationApi.md#remove_application_env_by_orga_and_app_id_and_env_name) | **DELETE** /organisations/{id}/applications/{appId}/env/{envName} | 
[**remove_organisation_member**](OrganisationApi.md#remove_organisation_member) | **DELETE** /organisations/{id}/members/{userId} | 
[**remove_tcp_redir**](OrganisationApi.md#remove_tcp_redir) | **DELETE** /organisations/{id}/applications/{appId}/tcpRedirs/{sourcePort} | 
[**remove_vhosts_by_orga_and_app_id**](OrganisationApi.md#remove_vhosts_by_orga_and_app_id) | **DELETE** /organisations/{id}/applications/{appId}/vhosts/{domain} | 
[**replace_addon_tags**](OrganisationApi.md#replace_addon_tags) | **PUT** /organisations/{id}/addons/{addonId}/tags | 
[**replace_application_tags**](OrganisationApi.md#replace_application_tags) | **PUT** /organisations/{id}/applications/{appId}/tags | 
[**set_application_branch_by_orga_and_app_id**](OrganisationApi.md#set_application_branch_by_orga_and_app_id) | **PUT** /organisations/{id}/applications/{appId}/branch | 
[**set_build_instance_flavor_by_orga_and_app_id**](OrganisationApi.md#set_build_instance_flavor_by_orga_and_app_id) | **PUT** /organisations/{id}/applications/{appId}/buildflavor | 
[**set_default_method_by_orga**](OrganisationApi.md#set_default_method_by_orga) | **PUT** /organisations/{id}/payments/methods/default | 
[**set_max_credits_per_month_by_orga**](OrganisationApi.md#set_max_credits_per_month_by_orga) | **PUT** /organisations/{id}/payments/monthlyinvoice/maxcredit | 
[**set_orga_avatar**](OrganisationApi.md#set_orga_avatar) | **PUT** /organisations/{id}/avatar | 
[**undeploy_application_by_orga_and_app_id**](OrganisationApi.md#undeploy_application_by_orga_and_app_id) | **DELETE** /organisations/{id}/applications/{appId}/instances | 
[**unlink_addon_from_application_by_orga_and_app_andd_addon_id**](OrganisationApi.md#unlink_addon_from_application_by_orga_and_app_andd_addon_id) | **DELETE** /organisations/{id}/applications/{appId}/addons/{addonId} | 
[**unmark_favourite_vhost_by_orga_and_app_id**](OrganisationApi.md#unmark_favourite_vhost_by_orga_and_app_id) | **DELETE** /organisations/{id}/applications/{appId}/vhosts/favourite | 
[**update_addon_info**](OrganisationApi.md#update_addon_info) | **PUT** /organisations/{id}/addons/{addonId} | 
[**update_consumer_by_orga**](OrganisationApi.md#update_consumer_by_orga) | **PUT** /organisations/{id}/consumers/{key} | 
[**update_exposed_env_by_orga_and_app_id**](OrganisationApi.md#update_exposed_env_by_orga_and_app_id) | **PUT** /organisations/{id}/applications/{appId}/exposed_env | 
[**update_provider_infos**](OrganisationApi.md#update_provider_infos) | **PUT** /organisations/{id}/addonproviders/{providerId} | 


# **abort_addon_migration**
> str abort_addon_migration(id, addon_id, migration_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 
    migration_id = "migrationId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.abort_addon_migration(id, addon_id, migration_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->abort_addon_migration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **addon_id** | **str**|  |
 **migration_id** | **str**|  |

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

# **add_addon_tag_by_orga_and_addon_id**
> [str] add_addon_tag_by_orga_and_addon_id(id, addon_id, tag)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 
    tag = "tag_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_addon_tag_by_orga_and_addon_id(id, addon_id, tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->add_addon_tag_by_orga_and_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **add_application_by_orga**
> ApplicationView add_application_by_orga(id, wannabe_application)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
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
        api_response = api_instance.add_application_by_orga(id, wannabe_application)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->add_application_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **add_application_dependency_by_orga_and_app_id**
> Message add_application_dependency_by_orga_and_app_id(id, app_id, dependency_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    dependency_id = "dependencyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_application_dependency_by_orga_and_app_id(id, app_id, dependency_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->add_application_dependency_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **add_application_tag_by_orga_and_app_id**
> [str] add_application_tag_by_orga_and_app_id(id, app_id, tag)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    tag = "tag_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_application_tag_by_orga_and_app_id(id, app_id, tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->add_application_tag_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **add_beta_tester**
> Message add_beta_tester(id, provider_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_beta_tester(id, provider_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->add_beta_tester: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |

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

# **add_organisation_member**
> Message add_organisation_member(id, wannabe_member)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.wannabe_member import WannabeMember
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    wannabe_member = WannabeMember(
        role="role_example",
        job="job_example",
        email="email_example",
    ) # WannabeMember | 
    invitation_key = "invitationKey_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_organisation_member(id, wannabe_member)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->add_organisation_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_organisation_member(id, wannabe_member, invitation_key=invitation_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->add_organisation_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **wannabe_member** | [**WannabeMember**](WannabeMember.md)|  |
 **invitation_key** | **str**|  | [optional]

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

# **add_payment_method_by_orga**
> PaymentMethodView add_payment_method_by_orga(id, payment_data)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    payment_data = PaymentData(
        type="NEW_CARD",
        token="token_example",
        device_data="device_data_example",
    ) # PaymentData | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_payment_method_by_orga(id, payment_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->add_payment_method_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **add_provider_feature**
> AddonFeatureView add_provider_feature(id, provider_id, wannabe_addon_feature)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.wannabe_addon_feature import WannabeAddonFeature
from openapi_client.model.addon_feature_view import AddonFeatureView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 
    wannabe_addon_feature = WannabeAddonFeature(
        name="name_example",
        type="BOOLEAN",
    ) # WannabeAddonFeature | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_provider_feature(id, provider_id, wannabe_addon_feature)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->add_provider_feature: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |
 **wannabe_addon_feature** | [**WannabeAddonFeature**](WannabeAddonFeature.md)|  |

### Return type

[**AddonFeatureView**](AddonFeatureView.md)

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

# **add_provider_plan**
> AddonPlanView add_provider_plan(id, provider_id, wannabe_addon_plan)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.addon_plan_view import AddonPlanView
from openapi_client.model.wannabe_addon_plan import WannabeAddonPlan
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 
    wannabe_addon_plan = WannabeAddonPlan(
        name="name_example",
        slug="slug_example",
        price=3.14,
        features=[
            AddonFeatureInstanceView(
                name="name_example",
                type="BOOLEAN",
                value="value_example",
                computable_value="computable_value_example",
                name_code="name_code_example",
            ),
        ],
    ) # WannabeAddonPlan | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_provider_plan(id, provider_id, wannabe_addon_plan)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->add_provider_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |
 **wannabe_addon_plan** | [**WannabeAddonPlan**](WannabeAddonPlan.md)|  |

### Return type

[**AddonPlanView**](AddonPlanView.md)

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

# **add_tcp_redir**
> TcpRedirView add_tcp_redir(id, app_id, wannabe_namespace)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.tcp_redir_view import TcpRedirView
from openapi_client.model.wannabe_namespace import WannabeNamespace
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    wannabe_namespace = WannabeNamespace(
        namespace="namespace_example",
        min_port=1,
        max_port=1,
    ) # WannabeNamespace | 
    payment = "payment_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_tcp_redir(id, app_id, wannabe_namespace)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->add_tcp_redir: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_tcp_redir(id, app_id, wannabe_namespace, payment=payment)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->add_tcp_redir: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **app_id** | **str**|  |
 **wannabe_namespace** | [**WannabeNamespace**](WannabeNamespace.md)|  |
 **payment** | **str**|  | [optional]

### Return type

[**TcpRedirView**](TcpRedirView.md)

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

# **add_vhosts_by_orga_and_app_id**
> Message add_vhosts_by_orga_and_app_id(id, app_id, domain)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    domain = "domain_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_vhosts_by_orga_and_app_id(id, app_id, domain)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->add_vhosts_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **buy_drops_by_orga**
> InvoiceRendering buy_drops_by_orga(id, wanna_buy_package)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    wanna_buy_package = WannaBuyPackage(
        package_id=1,
        currency="currency_example",
        coupon="coupon_example",
        drop_quantity=3.14,
    ) # WannaBuyPackage | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.buy_drops_by_orga(id, wanna_buy_package)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->buy_drops_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **cancel_application_deployment_for_orga**
> Message cancel_application_deployment_for_orga(id, app_id, deployment_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    deployment_id = "deploymentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cancel_application_deployment_for_orga(id, app_id, deployment_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->cancel_application_deployment_for_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **change_plan_by_orga_and_addon_id**
> str change_plan_by_orga_and_addon_id(id, addon_id, wannabe_plan_change)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.wannabe_plan_change import WannabePlanChange
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 
    wannabe_plan_change = WannabePlanChange(
        plan_id="plan_id_example",
        region="region_example",
        version="version_example",
    ) # WannabePlanChange | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.change_plan_by_orga_and_addon_id(id, addon_id, wannabe_plan_change)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->change_plan_by_orga_and_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **addon_id** | **str**|  |
 **wannabe_plan_change** | [**WannabePlanChange**](WannabePlanChange.md)|  |

### Return type

**str**

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

# **choose_payment_provider_by_orga**
> NextInPaymentFlow choose_payment_provider_by_orga(id, bid, payment_provider_selection)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    bid = "bid_example" # str | 
    payment_provider_selection = PaymentProviderSelection(
        provider="PAYPAL",
    ) # PaymentProviderSelection | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.choose_payment_provider_by_orga(id, bid, payment_provider_selection)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->choose_payment_provider_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **create_consumer_by_orga**
> OAuth1ConsumerView create_consumer_by_orga(id, wannabe_o_auth1_consumer)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
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
        api_response = api_instance.create_consumer_by_orga(id, wannabe_o_auth1_consumer)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->create_consumer_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **create_organisation**
> OrganisationView create_organisation(wannabe_organisation)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.organisation_view import OrganisationView
from openapi_client.model.wannabe_organisation import WannabeOrganisation
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    wannabe_organisation = WannabeOrganisation(
        name="name_example",
        description="description_example",
        address="address_example",
        city="city_example",
        zipcode="zipcode_example",
        country="country_example",
        company="company_example",
        customer_full_name="customer_full_name_example",
        vat="vat_example",
        billing_email="billing_email_example",
    ) # WannabeOrganisation | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_organisation(wannabe_organisation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->create_organisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wannabe_organisation** | [**WannabeOrganisation**](WannabeOrganisation.md)|  |

### Return type

[**OrganisationView**](OrganisationView.md)

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

# **create_provider**
> AddonProviderInfoFullView create_provider(id, wannabe_addon_provider)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.addon_provider_info_full_view import AddonProviderInfoFullView
from openapi_client.model.wannabe_addon_provider import WannabeAddonProvider
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    wannabe_addon_provider = WannabeAddonProvider(
        id="id_example",
        name="name_example",
        api=WannabeAddonProviderAPI(
            config_vars=[
                "config_vars_example",
            ],
            password="password_example",
            sso_salt="sso_salt_example",
            regions=[
                "regions_example",
            ],
            production=WannabeAddonProviderAPIUrl(
                base_url="base_url_example",
                sso_url="sso_url_example",
            ),
            test=WannabeAddonProviderAPIUrl(
                base_url="base_url_example",
                sso_url="sso_url_example",
            ),
        ),
    ) # WannabeAddonProvider | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_provider(id, wannabe_addon_provider)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->create_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **wannabe_addon_provider** | [**WannabeAddonProvider**](WannabeAddonProvider.md)|  |

### Return type

[**AddonProviderInfoFullView**](AddonProviderInfoFullView.md)

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

# **delete_addon_tag_by_orga_and_addon_id**
> [str] delete_addon_tag_by_orga_and_addon_id(id, addon_id, tag)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 
    tag = "tag_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_addon_tag_by_orga_and_addon_id(id, addon_id, tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->delete_addon_tag_by_orga_and_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **delete_application_by_orga_and_app_id**
> Message delete_application_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_application_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->delete_application_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **delete_application_dependency_by_orga_and_app_id**
> delete_application_dependency_by_orga_and_app_id(id, app_id, dependency_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    dependency_id = "dependencyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_application_dependency_by_orga_and_app_id(id, app_id, dependency_id)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->delete_application_dependency_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **delete_application_tag_by_orga_and_app_id**
> [str] delete_application_tag_by_orga_and_app_id(id, app_id, tag)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    tag = "tag_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_application_tag_by_orga_and_app_id(id, app_id, tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->delete_application_tag_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **delete_consumer_by_orga**
> delete_consumer_by_orga(id, key)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_consumer_by_orga(id, key)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->delete_consumer_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **delete_organisation**
> Message delete_organisation(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_organisation(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->delete_organisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **delete_payment_method_by_orga**
> delete_payment_method_by_orga(id, m_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    m_id = "mId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_payment_method_by_orga(id, m_id)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->delete_payment_method_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_provider**
> delete_provider(id, provider_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_provider(id, provider_id)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->delete_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |

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

# **delete_provider_feature**
> delete_provider_feature(id, provider_id, feature_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 
    feature_id = "featureId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_provider_feature(id, provider_id, feature_id)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->delete_provider_feature: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |
 **feature_id** | **str**|  |

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

# **delete_provider_plan**
> delete_provider_plan(id, provider_id, plan_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 
    plan_id = "planId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_provider_plan(id, provider_id, plan_id)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->delete_provider_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |
 **plan_id** | **str**|  |

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

# **delete_provider_plan_feature**
> delete_provider_plan_feature(id, provider_id, plan_id, feature_name)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 
    plan_id = "planId_example" # str | 
    feature_name = "featureName_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_provider_plan_feature(id, provider_id, plan_id, feature_name)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->delete_provider_plan_feature: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |
 **plan_id** | **str**|  |
 **feature_name** | **str**|  |

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

# **delete_purchase_order_by_orga**
> delete_purchase_order_by_orga(id, bid)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    bid = "bid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_purchase_order_by_orga(id, bid)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->delete_purchase_order_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **delete_recurrent_payment_by_orga**
> delete_recurrent_payment_by_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_recurrent_payment_by_orga(id)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->delete_recurrent_payment_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **deprovision_addon_by_orga_and_addon_id**
> Message deprovision_addon_by_orga_and_addon_id(id, addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.deprovision_addon_by_orga_and_addon_id(id, addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->deprovision_addon_by_orga_and_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **edit_application_by_orga_and_app_id**
> ApplicationView edit_application_by_orga_and_app_id(id, app_id, wannabe_application)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
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
        api_response = api_instance.edit_application_by_orga_and_app_id(id, app_id, wannabe_application)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->edit_application_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **edit_application_env_by_orga_and_app_id_and_env_name**
> ApplicationView edit_application_env_by_orga_and_app_id_and_env_name(id, app_id, env_name, wannabe_value)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    env_name = "envName_example" # str | 
    wannabe_value = WannabeValue(
        value="value_example",
    ) # WannabeValue | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_application_env_by_orga_and_app_id_and_env_name(id, app_id, env_name, wannabe_value)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->edit_application_env_by_orga_and_app_id_and_env_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **edit_application_environment_by_orga_and_app_id**
> ApplicationView edit_application_environment_by_orga_and_app_id(id, app_id, body)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_application_environment_by_orga_and_app_id(id, app_id, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->edit_application_environment_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **edit_organisation**
> OrganisationView edit_organisation(id, wannabe_organisation)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.organisation_view import OrganisationView
from openapi_client.model.wannabe_organisation import WannabeOrganisation
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    wannabe_organisation = WannabeOrganisation(
        name="name_example",
        description="description_example",
        address="address_example",
        city="city_example",
        zipcode="zipcode_example",
        country="country_example",
        company="company_example",
        customer_full_name="customer_full_name_example",
        vat="vat_example",
        billing_email="billing_email_example",
    ) # WannabeOrganisation | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_organisation(id, wannabe_organisation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->edit_organisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **wannabe_organisation** | [**WannabeOrganisation**](WannabeOrganisation.md)|  |

### Return type

[**OrganisationView**](OrganisationView.md)

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

# **edit_organisation_member**
> Message edit_organisation_member(id, user_id, wannabe_member)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.wannabe_member import WannabeMember
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    user_id = "userId_example" # str | 
    wannabe_member = WannabeMember(
        role="role_example",
        job="job_example",
        email="email_example",
    ) # WannabeMember | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_organisation_member(id, user_id, wannabe_member)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->edit_organisation_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **user_id** | **str**|  |
 **wannabe_member** | [**WannabeMember**](WannabeMember.md)|  |

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

# **edit_provider_plan**
> AddonPlanView edit_provider_plan(id, provider_id, plan_id, wannabe_addon_plan)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.addon_plan_view import AddonPlanView
from openapi_client.model.wannabe_addon_plan import WannabeAddonPlan
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 
    plan_id = "planId_example" # str | 
    wannabe_addon_plan = WannabeAddonPlan(
        name="name_example",
        slug="slug_example",
        price=3.14,
        features=[
            AddonFeatureInstanceView(
                name="name_example",
                type="BOOLEAN",
                value="value_example",
                computable_value="computable_value_example",
                name_code="name_code_example",
            ),
        ],
    ) # WannabeAddonPlan | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_provider_plan(id, provider_id, plan_id, wannabe_addon_plan)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->edit_provider_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |
 **plan_id** | **str**|  |
 **wannabe_addon_plan** | [**WannabeAddonPlan**](WannabeAddonPlan.md)|  |

### Return type

[**AddonPlanView**](AddonPlanView.md)

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

# **edit_provider_plan_feature**
> AddonPlanView edit_provider_plan_feature(id, provider_id, plan_id, feature_name, addon_feature_instance_view)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.addon_plan_view import AddonPlanView
from openapi_client.model.addon_feature_instance_view import AddonFeatureInstanceView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 
    plan_id = "planId_example" # str | 
    feature_name = "featureName_example" # str | 
    addon_feature_instance_view = AddonFeatureInstanceView(
        name="name_example",
        type="BOOLEAN",
        value="value_example",
        computable_value="computable_value_example",
        name_code="name_code_example",
    ) # AddonFeatureInstanceView | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_provider_plan_feature(id, provider_id, plan_id, feature_name, addon_feature_instance_view)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->edit_provider_plan_feature: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |
 **plan_id** | **str**|  |
 **feature_name** | **str**|  |
 **addon_feature_instance_view** | [**AddonFeatureInstanceView**](AddonFeatureInstanceView.md)|  |

### Return type

[**AddonPlanView**](AddonPlanView.md)

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

# **get_addon_by_orga_and_addon_id**
> AddonView get_addon_by_orga_and_addon_id(id, addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addon_by_orga_and_addon_id(id, addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_addon_by_orga_and_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_addon_env_by_orga_and_addon_id**
> [AddonEnvironmentView] get_addon_env_by_orga_and_addon_id(id, addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addon_env_by_orga_and_addon_id(id, addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_addon_env_by_orga_and_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_addon_instance**
> str get_addon_instance(id, addon_id, instance_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 
    instance_id = "instanceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addon_instance(id, addon_id, instance_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_addon_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **addon_id** | **str**|  |
 **instance_id** | **str**|  |

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

# **get_addon_instances**
> [SuperNovaInstanceView] get_addon_instances(id, addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 
    deployment_id = "deploymentId_example" # str |  (optional)
    with_deleted = "withDeleted_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addon_instances(id, addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_addon_instances: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_addon_instances(id, addon_id, deployment_id=deployment_id, with_deleted=with_deleted)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_addon_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **addon_id** | **str**|  |
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

# **get_addon_migration**
> str get_addon_migration(id, addon_id, migration_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 
    migration_id = "migrationId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addon_migration(id, addon_id, migration_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_addon_migration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **addon_id** | **str**|  |
 **migration_id** | **str**|  |

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

# **get_addon_migrations**
> str get_addon_migrations(id, addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addon_migrations(id, addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_addon_migrations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **addon_id** | **str**|  |

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

# **get_addon_sso_data_for_orga**
> AddonProviderSSOData get_addon_sso_data_for_orga(id, addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.addon_provider_sso_data import AddonProviderSSOData
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addon_sso_data_for_orga(id, addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_addon_sso_data_for_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **addon_id** | **str**|  |

### Return type

[**AddonProviderSSOData**](AddonProviderSSOData.md)

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

# **get_addon_tags_by_orga_id_and_addon_id**
> [str] get_addon_tags_by_orga_id_and_addon_id(id, addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addon_tags_by_orga_id_and_addon_id(id, addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_addon_tags_by_orga_id_and_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_addons_by_orga_id**
> [AddonView] get_addons_by_orga_id(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addons_by_orga_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_addons_by_orga_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_addons_linked_to_application_by_orga_and_app_id**
> [AddonView] get_addons_linked_to_application_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_addons_linked_to_application_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_addons_linked_to_application_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_all_applications_by_orga**
> [ApplicationView] get_all_applications_by_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    instance_id = "instanceId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_applications_by_orga(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_all_applications_by_orga: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_applications_by_orga(id, instance_id=instance_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_all_applications_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **instance_id** | **str**|  | [optional]

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

# **get_amount_for_orga**
> DropCountView get_amount_for_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_amount_for_orga(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_amount_for_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_application_branches_by_orga_and_app_id**
> [str] get_application_branches_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_application_branches_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_application_branches_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_application_by_orga_and_app_id**
> ApplicationView get_application_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_application_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_application_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_application_dependencies_by_orga_and_app_id**
> [ApplicationView] get_application_dependencies_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_application_dependencies_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_application_dependencies_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_application_dependencies_env_by_orga_and_app_id**
> get_application_dependencies_env_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_application_dependencies_env_by_orga_and_app_id(id, app_id)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_application_dependencies_env_by_orga_and_app_id: %s\n" % e)
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

# **get_application_dependents_by_orga_and_app_id**
> [ApplicationView] get_application_dependents_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_application_dependents_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_application_dependents_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_application_deployment_for_orga**
> get_application_deployment_for_orga(id, app_id, deployment_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    deployment_id = "deploymentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_application_deployment_for_orga(id, app_id, deployment_id)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_application_deployment_for_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_application_deployments_for_orga**
> [DeploymentView] get_application_deployments_for_orga(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    limit = "limit_example" # str |  (optional)
    offset = "offset_example" # str |  (optional)
    action = "action_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_application_deployments_for_orga(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_application_deployments_for_orga: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_application_deployments_for_orga(id, app_id, limit=limit, offset=offset, action=action)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_application_deployments_for_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_application_env_by_orga_and_app_id**
> [AddonEnvironmentView] get_application_env_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_application_env_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_application_env_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_application_instance_by_orga_and_app_and_instance_id**
> str get_application_instance_by_orga_and_app_and_instance_id(id, app_id, instance_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    instance_id = "instanceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_application_instance_by_orga_and_app_and_instance_id(id, app_id, instance_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_application_instance_by_orga_and_app_and_instance_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **app_id** | **str**|  |
 **instance_id** | **str**|  |

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

# **get_application_instances_by_orga_and_app_id**
> [SuperNovaInstanceView] get_application_instances_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    deployment_id = "deploymentId_example" # str |  (optional)
    with_deleted = "withDeleted_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_application_instances_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_application_instances_by_orga_and_app_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_application_instances_by_orga_and_app_id(id, app_id, deployment_id=deployment_id, with_deleted=with_deleted)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_application_instances_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_application_tags_by_orga_and_app_id**
> [str] get_application_tags_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_application_tags_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_application_tags_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_applications_linked_to_addon_by_orga_and_addon_id**
> [ApplicationView] get_applications_linked_to_addon_by_orga_and_addon_id(id, addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_applications_linked_to_addon_by_orga_and_addon_id(id, addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_applications_linked_to_addon_by_orga_and_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_consumer_by_orga**
> OAuth1ConsumerView get_consumer_by_orga(id, key)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_consumer_by_orga(id, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_consumer_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_consumer_secret_by_orga**
> SecretView get_consumer_secret_by_orga(id, key)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_consumer_secret_by_orga(id, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_consumer_secret_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_consumers_by_orga**
> [OAuth1ConsumerView] get_consumers_by_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_consumers_by_orga(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_consumers_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[OAuth1ConsumerView]**](OAuth1ConsumerView.md)

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

# **get_consumptions_for_orga**
> str get_consumptions_for_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str |  (optional)
    _from = "from_example" # str |  (optional)
    to = "to_example" # str |  (optional)
    _for = "for_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_consumptions_for_orga(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_consumptions_for_orga: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_consumptions_for_orga(id, app_id=app_id, _from=_from, to=to, _for=_for)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_consumptions_for_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_default_method_by_orga**
> PaymentMethodView get_default_method_by_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_default_method_by_orga(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_default_method_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_deployments_for_all_apps**
> get_deployments_for_all_apps(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_deployments_for_all_apps(id)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_deployments_for_all_apps: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_deployments_for_all_apps(id, limit=limit)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_deployments_for_all_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **limit** | **int**|  | [optional]

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

# **get_env_of_addons_linked_to_application_by_orga_and_app_id**
> [LinkedAddonEnvironmentView] get_env_of_addons_linked_to_application_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_env_of_addons_linked_to_application_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_env_of_addons_linked_to_application_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_exposed_env_by_orga_and_app_id**
> str get_exposed_env_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_exposed_env_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_exposed_env_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_favourite_vhost_by_orga_and_app_id**
> VhostView get_favourite_vhost_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_favourite_vhost_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_favourite_vhost_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_instances_for_all_apps_for_orga**
> str get_instances_for_all_apps_for_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_instances_for_all_apps_for_orga(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_instances_for_all_apps_for_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_invoice_by_orga**
> InvoiceRendering get_invoice_by_orga(id, bid)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    bid = "bid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_invoice_by_orga(id, bid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_invoice_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_invoices_by_orga**
> [InvoiceRendering] get_invoices_by_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_invoices_by_orga(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_invoices_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_monthly_invoice_by_orga**
> str get_monthly_invoice_by_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_monthly_invoice_by_orga(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_monthly_invoice_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_namespaces**
> [NamespaceView] get_namespaces(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.namespace_view import NamespaceView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_namespaces(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_namespaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[NamespaceView]**](NamespaceView.md)

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

# **get_new_setup_intent_by_orga**
> SetupIntentView get_new_setup_intent_by_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.setup_intent_view import SetupIntentView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_new_setup_intent_by_orga(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_new_setup_intent_by_orga: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_new_setup_intent_by_orga(id, type=type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_new_setup_intent_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **type** | **str**|  | [optional]

### Return type

[**SetupIntentView**](SetupIntentView.md)

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

# **get_organisation**
> OrganisationView get_organisation(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.organisation_view import OrganisationView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_organisation(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**OrganisationView**](OrganisationView.md)

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

# **get_organisation_members**
> [OrganisationMemberView] get_organisation_members(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.organisation_member_view import OrganisationMemberView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_organisation_members(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_organisation_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[OrganisationMemberView]**](OrganisationMemberView.md)

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

# **get_payment_info_for_orga**
> PaymentInfoView get_payment_info_for_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_payment_info_for_orga(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_payment_info_for_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_pdf_invoice_by_orga**
> get_pdf_invoice_by_orga(id, bid)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    bid = "bid_example" # str | 
    token = "token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_pdf_invoice_by_orga(id, bid)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_pdf_invoice_by_orga: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_pdf_invoice_by_orga(id, bid, token=token)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_pdf_invoice_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_with_tax_by_orga**
> PriceWithTaxInfo get_price_with_tax_by_orga(id, price)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    price = "price_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_price_with_tax_by_orga(id, price)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_price_with_tax_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_provider_features**
> [AddonFeatureView] get_provider_features(id, provider_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.addon_feature_view import AddonFeatureView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_provider_features(id, provider_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_provider_features: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |

### Return type

[**[AddonFeatureView]**](AddonFeatureView.md)

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

# **get_provider_info**
> AddonProviderInfoView get_provider_info(id, provider_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.addon_provider_info_view import AddonProviderInfoView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_provider_info(id, provider_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_provider_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |

### Return type

[**AddonProviderInfoView**](AddonProviderInfoView.md)

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

# **get_provider_plan**
> AddonPlanView get_provider_plan(id, provider_id, plan_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.addon_plan_view import AddonPlanView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 
    plan_id = "planId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_provider_plan(id, provider_id, plan_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_provider_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |
 **plan_id** | **str**|  |

### Return type

[**AddonPlanView**](AddonPlanView.md)

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

# **get_provider_plans**
> [AddonPlanView] get_provider_plans(id, provider_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.addon_plan_view import AddonPlanView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_provider_plans(id, provider_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_provider_plans: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |

### Return type

[**[AddonPlanView]**](AddonPlanView.md)

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

# **get_provider_tags**
> [str] get_provider_tags(id, provider_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_provider_tags(id, provider_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_provider_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |

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

# **get_providers_info**
> [AddonProviderInfoFullView] get_providers_info(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_providers_info(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_providers_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_recurrent_payment_by_orga**
> RecurrentPaymentView get_recurrent_payment_by_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_recurrent_payment_by_orga(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_recurrent_payment_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_sso_data_for_orga**
> AddonProviderSSOData get_sso_data_for_orga(id, provider_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.addon_provider_sso_data import AddonProviderSSOData
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sso_data_for_orga(id, provider_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_sso_data_for_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |

### Return type

[**AddonProviderSSOData**](AddonProviderSSOData.md)

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

# **get_stripe_token_by_orga**
> BraintreeToken get_stripe_token_by_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_stripe_token_by_orga(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_stripe_token_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_tcp_redirs**
> [TcpRedirView] get_tcp_redirs(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.tcp_redir_view import TcpRedirView
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tcp_redirs(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_tcp_redirs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **app_id** | **str**|  |

### Return type

[**[TcpRedirView]**](TcpRedirView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**402** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unpaid_invoices_by_orga**
> [InvoiceRendering] get_unpaid_invoices_by_orga(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_unpaid_invoices_by_orga(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_unpaid_invoices_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_unpaid_invoices_by_orga1**
> [PaymentMethodView] get_unpaid_invoices_by_orga1(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_unpaid_invoices_by_orga1(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_unpaid_invoices_by_orga1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_user_organisationss**
> [OrganisationView] get_user_organisationss()



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.organisation_view import OrganisationView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    user = "user_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_user_organisationss(user=user)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_user_organisationss: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**|  | [optional]

### Return type

[**[OrganisationView]**](OrganisationView.md)

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

# **get_vhosts_by_orga_and_app_id**
> [VhostView] get_vhosts_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_vhosts_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->get_vhosts_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **link_addon_to_application_by_orga_and_app_id**
> link_addon_to_application_by_orga_and_app_id(id, app_id, body)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.link_addon_to_application_by_orga_and_app_id(id, app_id, body)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->link_addon_to_application_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **app_id** | **str**|  |
 **body** | **str**|  |

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

# **mark_favourite_vhost_by_orga_and_app_id**
> VhostView mark_favourite_vhost_by_orga_and_app_id(id, app_id, vhost_view)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    vhost_view = VhostView(
        fqdn="fqdn_example",
    ) # VhostView | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.mark_favourite_vhost_by_orga_and_app_id(id, app_id, vhost_view)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->mark_favourite_vhost_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **preorder_addon_by_orga_id**
> InvoiceRendering preorder_addon_by_orga_id(id, wannabe_addon_provision)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
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
        api_response = api_instance.preorder_addon_by_orga_id(id, wannabe_addon_provision)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->preorder_addon_by_orga_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **preorder_migration**
> str preorder_migration(id, addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 
    plan_id = "planId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preorder_migration(id, addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->preorder_migration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.preorder_migration(id, addon_id, plan_id=plan_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->preorder_migration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **addon_id** | **str**|  |
 **plan_id** | **str**|  | [optional]

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

# **provision_addon_by_orga_id**
> AddonView provision_addon_by_orga_id(id, wannabe_addon_provision)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.addon_view import AddonView
from openapi_client.model.stripe_confirmation_error_message import StripeConfirmationErrorMessage
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
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
        api_response = api_instance.provision_addon_by_orga_id(id, wannabe_addon_provision)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->provision_addon_by_orga_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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
**402** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeploy_application_by_orga_and_app_id**
> redeploy_application_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    commit = "commit_example" # str |  (optional)
    use_cache = "useCache_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.redeploy_application_by_orga_and_app_id(id, app_id)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->redeploy_application_by_orga_and_app_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.redeploy_application_by_orga_and_app_id(id, app_id, commit=commit, use_cache=use_cache)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->redeploy_application_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **app_id** | **str**|  |
 **commit** | **str**|  | [optional]
 **use_cache** | **str**|  | [optional]

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

# **remove_application_env_by_orga_and_app_id_and_env_name**
> ApplicationView remove_application_env_by_orga_and_app_id_and_env_name(id, app_id, env_name)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    env_name = "envName_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_application_env_by_orga_and_app_id_and_env_name(id, app_id, env_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->remove_application_env_by_orga_and_app_id_and_env_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **remove_organisation_member**
> Message remove_organisation_member(id, user_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_organisation_member(id, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->remove_organisation_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **user_id** | **str**|  |

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

# **remove_tcp_redir**
> remove_tcp_redir(id, app_id, source_port)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    source_port = 1 # int | 
    namespace = "namespace_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.remove_tcp_redir(id, app_id, source_port)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->remove_tcp_redir: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.remove_tcp_redir(id, app_id, source_port, namespace=namespace)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->remove_tcp_redir: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **app_id** | **str**|  |
 **source_port** | **int**|  |
 **namespace** | **str**|  | [optional]

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

# **remove_vhosts_by_orga_and_app_id**
> Message remove_vhosts_by_orga_and_app_id(id, app_id, domain)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    domain = "domain_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_vhosts_by_orga_and_app_id(id, app_id, domain)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->remove_vhosts_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **replace_addon_tags**
> [str] replace_addon_tags(id, addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    addon_id = "addonId_example" # str | 
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.replace_addon_tags(id, addon_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->replace_addon_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.replace_addon_tags(id, addon_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->replace_addon_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **addon_id** | **str**|  |
 **body** | **str**|  | [optional]

### Return type

**[str]**

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

# **replace_application_tags**
> [str] replace_application_tags(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.replace_application_tags(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->replace_application_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.replace_application_tags(id, app_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->replace_application_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **app_id** | **str**|  |
 **body** | **str**|  | [optional]

### Return type

**[str]**

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

# **set_application_branch_by_orga_and_app_id**
> set_application_branch_by_orga_and_app_id(id, app_id, wannabe_branch)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    wannabe_branch = WannabeBranch(
        branch="branch_example",
    ) # WannabeBranch | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_application_branch_by_orga_and_app_id(id, app_id, wannabe_branch)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->set_application_branch_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **set_build_instance_flavor_by_orga_and_app_id**
> set_build_instance_flavor_by_orga_and_app_id(id, app_id, wannabe_build_flavor)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    wannabe_build_flavor = WannabeBuildFlavor(
        flavor_name="flavor_name_example",
    ) # WannabeBuildFlavor | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_build_instance_flavor_by_orga_and_app_id(id, app_id, wannabe_build_flavor)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->set_build_instance_flavor_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **set_default_method_by_orga**
> set_default_method_by_orga(id, payment_data)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    payment_data = PaymentData(
        type="NEW_CARD",
        token="token_example",
        device_data="device_data_example",
    ) # PaymentData | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_default_method_by_orga(id, payment_data)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->set_default_method_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **set_max_credits_per_month_by_orga**
> str set_max_credits_per_month_by_orga(id, wannabe_max_credits)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    wannabe_max_credits = WannabeMaxCredits(
        max=3.14,
    ) # WannabeMaxCredits | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_max_credits_per_month_by_orga(id, wannabe_max_credits)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->set_max_credits_per_month_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **wannabe_max_credits** | [**WannabeMaxCredits**](WannabeMaxCredits.md)|  |

### Return type

**str**

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

# **set_orga_avatar**
> UrlView set_orga_avatar(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_orga_avatar(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->set_orga_avatar: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**UrlView**](UrlView.md)

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

# **undeploy_application_by_orga_and_app_id**
> Message undeploy_application_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.undeploy_application_by_orga_and_app_id(id, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->undeploy_application_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **unlink_addon_from_application_by_orga_and_app_andd_addon_id**
> unlink_addon_from_application_by_orga_and_app_andd_addon_id(id, app_id, addon_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    addon_id = "addonId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.unlink_addon_from_application_by_orga_and_app_andd_addon_id(id, app_id, addon_id)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->unlink_addon_from_application_by_orga_and_app_andd_addon_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **unmark_favourite_vhost_by_orga_and_app_id**
> unmark_favourite_vhost_by_orga_and_app_id(id, app_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.unmark_favourite_vhost_by_orga_and_app_id(id, app_id)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->unmark_favourite_vhost_by_orga_and_app_id: %s\n" % e)
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

# **update_addon_info**
> AddonView update_addon_info(id, addon_id, wannabe_addon_provision)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
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
        api_response = api_instance.update_addon_info(id, addon_id, wannabe_addon_provision)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->update_addon_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **update_consumer_by_orga**
> OAuth1ConsumerView update_consumer_by_orga(id, key, wannabe_o_auth1_consumer)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
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
        api_response = api_instance.update_consumer_by_orga(id, key, wannabe_o_auth1_consumer)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->update_consumer_by_orga: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **update_exposed_env_by_orga_and_app_id**
> Message update_exposed_env_by_orga_and_app_id(id, app_id, body)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
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
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    app_id = "appId_example" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_exposed_env_by_orga_and_app_id(id, app_id, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->update_exposed_env_by_orga_and_app_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **update_provider_infos**
> AddonProviderInfoView update_provider_infos(id, provider_id, wannabe_addon_provider_infos)



### Example

```python
import time
import openapi_client
from openapi_client.api import organisation_api
from openapi_client.model.wannabe_addon_provider_infos import WannabeAddonProviderInfos
from openapi_client.model.addon_provider_info_view import AddonProviderInfoView
from pprint import pprint
# Defining the host is optional and defaults to https://api.clever-cloud.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.clever-cloud.com/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    id = "id_example" # str | 
    provider_id = "providerId_example" # str | 
    wannabe_addon_provider_infos = WannabeAddonProviderInfos(
        name="name_example",
        website="website_example",
        support_email="support_email_example",
        google_plus_name="google_plus_name_example",
        twitter_name="twitter_name_example",
        analytics_id="analytics_id_example",
        short_desc="short_desc_example",
        long_desc="long_desc_example",
        logo_url="logo_url_example",
    ) # WannabeAddonProviderInfos | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_provider_infos(id, provider_id, wannabe_addon_provider_infos)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganisationApi->update_provider_infos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provider_id** | **str**|  |
 **wannabe_addon_provider_infos** | [**WannabeAddonProviderInfos**](WannabeAddonProviderInfos.md)|  |

### Return type

[**AddonProviderInfoView**](AddonProviderInfoView.md)

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

