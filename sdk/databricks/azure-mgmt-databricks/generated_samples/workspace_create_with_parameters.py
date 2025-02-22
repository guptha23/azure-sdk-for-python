# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.databricks import AzureDatabricksManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-databricks
# USAGE
    python workspace_create_with_parameters.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureDatabricksManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.workspaces.begin_create_or_update(
        resource_group_name="rg",
        workspace_name="myWorkspace",
        parameters={
            "location": "westus",
            "properties": {
                "managedResourceGroupId": "/subscriptions/subid/resourceGroups/myManagedRG",
                "parameters": {
                    "customPrivateSubnetName": {"value": "myPrivateSubnet"},
                    "customPublicSubnetName": {"value": "myPublicSubnet"},
                    "customVirtualNetworkId": {
                        "value": "/subscriptions/subid/resourceGroups/rg/providers/Microsoft.Network/virtualNetworks/myNetwork"
                    },
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/databricks/resource-manager/Microsoft.Databricks/preview/2022-04-01-preview/examples/WorkspaceCreateWithParameters.json
if __name__ == "__main__":
    main()
