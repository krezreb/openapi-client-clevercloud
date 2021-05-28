# WannabeAddonProvision


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | Id of the add-on provider | 
**plan** | **str** | Id of the price plan | 
**region** | **str** | Region to provision the add-on in. | 
**linked_app** | **str** |  | [optional] 
**name** | **str** | Name of the future add-on, for display. | [optional] 
**options** | **{str: (str,)}** | Options to add to the provision call. | [optional] 
**version** | **str** | Version of the add-on | [optional] 
**payment_intent** | [**SetupIntentView**](SetupIntentView.md) |  | [optional] 
**payment_method_type** | **str** | Payment method type | [optional] 
**sepa_source_id** | **str** | Id of the SEPA debit source | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


