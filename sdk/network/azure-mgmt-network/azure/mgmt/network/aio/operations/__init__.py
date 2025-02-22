# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from ._operations import (
    ApplicationGatewaysOperations,
    ExpressRouteCircuitAuthorizationsOperations,
    ExpressRouteCircuitPeeringsOperations,
    ExpressRouteCircuitsOperations,
    ExpressRouteServiceProvidersOperations,
    LoadBalancersOperations,
    LocalNetworkGatewaysOperations,
    NetworkInterfacesOperations,
    NetworkSecurityGroupsOperations,
    PublicIPAddressesOperations,
    RouteTablesOperations,
    RoutesOperations,
    SecurityRulesOperations,
    SubnetsOperations,
    UsagesOperations,
    VirtualNetworkGatewayConnectionsOperations,
    VirtualNetworkGatewaysOperations,
    VirtualNetworksOperations,
    NetworkWatchersOperations,
    PacketCapturesOperations,
    VirtualNetworkPeeringsOperations,
    BgpServiceCommunitiesOperations,
    RouteFilterRulesOperations,
    RouteFiltersOperations,
    AvailableEndpointServicesOperations,
    DefaultSecurityRulesOperations,
    InboundNatRulesOperations,
    LoadBalancerBackendAddressPoolsOperations,
    LoadBalancerFrontendIPConfigurationsOperations,
    LoadBalancerLoadBalancingRulesOperations,
    LoadBalancerNetworkInterfacesOperations,
    LoadBalancerProbesOperations,
    NetworkInterfaceIPConfigurationsOperations,
    NetworkInterfaceLoadBalancersOperations,
    ApplicationSecurityGroupsOperations,
    ConnectionMonitorsOperations,
    Operations,
    DdosProtectionPlansOperations,
    ExpressRouteCircuitConnectionsOperations,
    ExpressRouteCrossConnectionPeeringsOperations,
    ExpressRouteCrossConnectionsOperations,
    AzureFirewallsOperations,
    HubVirtualNetworkConnectionsOperations,
    VirtualHubsOperations,
    VirtualWANsOperations,
    VpnConnectionsOperations,
    VpnGatewaysOperations,
    VpnSitesConfigurationOperations,
    VpnSitesOperations,
    PublicIPPrefixesOperations,
    ServiceEndpointPoliciesOperations,
    ServiceEndpointPolicyDefinitionsOperations,
    AvailableDelegationsOperations,
    AvailableResourceGroupDelegationsOperations,
    AzureFirewallFqdnTagsOperations,
    ExpressRouteConnectionsOperations,
    ExpressRouteGatewaysOperations,
    ExpressRouteLinksOperations,
    ExpressRoutePortsLocationsOperations,
    ExpressRoutePortsOperations,
    InterfaceEndpointsOperations,
    LoadBalancerOutboundRulesOperations,
    NetworkInterfaceTapConfigurationsOperations,
    NetworkProfilesOperations,
    P2SVpnGatewaysOperations,
    P2SVpnServerConfigurationsOperations,
    VirtualNetworkTapsOperations,
    VirtualWansOperations,
    DdosCustomPoliciesOperations,
    PeerExpressRouteCircuitConnectionsOperations,
    WebApplicationFirewallPoliciesOperations,
    NatGatewaysOperations,
    ResourceNavigationLinksOperations,
    ServiceAssociationLinksOperations,
    AvailablePrivateEndpointTypesOperations,
    BastionHostsOperations,
    PrivateEndpointsOperations,
    PrivateLinkServicesOperations,
    ServiceTagsOperations,
    FirewallPoliciesOperations,
    FirewallPolicyRuleGroupsOperations,
    VpnLinkConnectionsOperations,
    VpnSiteLinkConnectionsOperations,
    VpnSiteLinksOperations,
    VirtualRouterPeeringsOperations,
    VirtualRoutersOperations,
    AvailableServiceAliasesOperations,
    VpnServerConfigurationsAssociatedWithVirtualWanOperations,
    VpnServerConfigurationsOperations,
    IpGroupsOperations,
    VirtualHubRouteTableV2SOperations,
    FlowLogsOperations,
    NetworkVirtualAppliancesOperations,
    IpAllocationsOperations,
    PrivateDnsZoneGroupsOperations,
    SecurityPartnerProvidersOperations,
    HubRouteTablesOperations,
    ApplicationGatewayPrivateEndpointConnectionsOperations,
    ApplicationGatewayPrivateLinkResourcesOperations,
    FirewallPolicyRuleCollectionGroupsOperations,
    VirtualApplianceSitesOperations,
    VirtualApplianceSkusOperations,
    VirtualHubBgpConnectionOperations,
    VirtualHubBgpConnectionsOperations,
    VirtualHubIpConfigurationOperations,
    CustomIPPrefixesOperations,
    DscpConfigurationOperations,
    InboundSecurityRuleOperations,
    WebCategoriesOperations,
    NatRulesOperations,
    VirtualNetworkGatewayNatRulesOperations,
    ActiveConnectivityConfigurationsOperations,
    ActiveSecurityAdminRulesOperations,
    ActiveSecurityUserRulesOperations,
    AdminRuleCollectionsOperations,
    AdminRulesOperations,
    ConnectivityConfigurationsOperations,
    EffectiveConnectivityConfigurationsOperations,
    EffectiveVirtualNetworksOperations,
    NetworkGroupsOperations,
    NetworkManagerCommitsOperations,
    NetworkManagerDeploymentStatusOperations,
    NetworkManagerEffectiveSecurityAdminRulesOperations,
    NetworkManagersOperations,
    NetworkSecurityPerimetersOperations,
    NspAccessRulesOperations,
    NspAccessRulesReconcileOperations,
    NspAssociationReconcileOperations,
    NspAssociationsOperations,
    NspLinkReconcileOperations,
    NspLinkReferenceReconcileOperations,
    NspLinkReferencesOperations,
    NspLinksOperations,
    NspProfilesOperations,
    PerimeterAssociableResourceTypesOperations,
    SecurityAdminConfigurationsOperations,
    SecurityUserConfigurationsOperations,
    UserRuleCollectionsOperations,
    UserRulesOperations,
    ApplicationGatewayWafDynamicManifestsDefaultOperations,
    ApplicationGatewayWafDynamicManifestsOperations,
    ConfigurationPolicyGroupsOperations,
    ExpressRoutePortAuthorizationsOperations,
    ExpressRouteProviderPortsLocationOperations,
    FirewallPolicyIdpsSignaturesFilterValuesOperations,
    FirewallPolicyIdpsSignaturesOperations,
    FirewallPolicyIdpsSignaturesOverridesOperations,
    ManagementGroupNetworkManagerConnectionsOperations,
    RouteMapsOperations,
    RoutingIntentOperations,
    ScopeConnectionsOperations,
    ServiceTagInformationOperations,
    StaticMembersOperations,
    SubscriptionNetworkManagerConnectionsOperations,
    VipSwapOperations,
    NetworkManagementClientOperationsMixin,
)

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ApplicationGatewaysOperations",
    "ExpressRouteCircuitAuthorizationsOperations",
    "ExpressRouteCircuitPeeringsOperations",
    "ExpressRouteCircuitsOperations",
    "ExpressRouteServiceProvidersOperations",
    "LoadBalancersOperations",
    "LocalNetworkGatewaysOperations",
    "NetworkInterfacesOperations",
    "NetworkSecurityGroupsOperations",
    "PublicIPAddressesOperations",
    "RouteTablesOperations",
    "RoutesOperations",
    "SecurityRulesOperations",
    "SubnetsOperations",
    "UsagesOperations",
    "VirtualNetworkGatewayConnectionsOperations",
    "VirtualNetworkGatewaysOperations",
    "VirtualNetworksOperations",
    "NetworkWatchersOperations",
    "PacketCapturesOperations",
    "VirtualNetworkPeeringsOperations",
    "BgpServiceCommunitiesOperations",
    "RouteFilterRulesOperations",
    "RouteFiltersOperations",
    "AvailableEndpointServicesOperations",
    "DefaultSecurityRulesOperations",
    "InboundNatRulesOperations",
    "LoadBalancerBackendAddressPoolsOperations",
    "LoadBalancerFrontendIPConfigurationsOperations",
    "LoadBalancerLoadBalancingRulesOperations",
    "LoadBalancerNetworkInterfacesOperations",
    "LoadBalancerProbesOperations",
    "NetworkInterfaceIPConfigurationsOperations",
    "NetworkInterfaceLoadBalancersOperations",
    "ApplicationSecurityGroupsOperations",
    "ConnectionMonitorsOperations",
    "Operations",
    "DdosProtectionPlansOperations",
    "ExpressRouteCircuitConnectionsOperations",
    "ExpressRouteCrossConnectionPeeringsOperations",
    "ExpressRouteCrossConnectionsOperations",
    "AzureFirewallsOperations",
    "HubVirtualNetworkConnectionsOperations",
    "VirtualHubsOperations",
    "VirtualWANsOperations",
    "VpnConnectionsOperations",
    "VpnGatewaysOperations",
    "VpnSitesConfigurationOperations",
    "VpnSitesOperations",
    "PublicIPPrefixesOperations",
    "ServiceEndpointPoliciesOperations",
    "ServiceEndpointPolicyDefinitionsOperations",
    "AvailableDelegationsOperations",
    "AvailableResourceGroupDelegationsOperations",
    "AzureFirewallFqdnTagsOperations",
    "ExpressRouteConnectionsOperations",
    "ExpressRouteGatewaysOperations",
    "ExpressRouteLinksOperations",
    "ExpressRoutePortsLocationsOperations",
    "ExpressRoutePortsOperations",
    "InterfaceEndpointsOperations",
    "LoadBalancerOutboundRulesOperations",
    "NetworkInterfaceTapConfigurationsOperations",
    "NetworkProfilesOperations",
    "P2SVpnGatewaysOperations",
    "P2SVpnServerConfigurationsOperations",
    "VirtualNetworkTapsOperations",
    "VirtualWansOperations",
    "DdosCustomPoliciesOperations",
    "PeerExpressRouteCircuitConnectionsOperations",
    "WebApplicationFirewallPoliciesOperations",
    "NatGatewaysOperations",
    "ResourceNavigationLinksOperations",
    "ServiceAssociationLinksOperations",
    "AvailablePrivateEndpointTypesOperations",
    "BastionHostsOperations",
    "PrivateEndpointsOperations",
    "PrivateLinkServicesOperations",
    "ServiceTagsOperations",
    "FirewallPoliciesOperations",
    "FirewallPolicyRuleGroupsOperations",
    "VpnLinkConnectionsOperations",
    "VpnSiteLinkConnectionsOperations",
    "VpnSiteLinksOperations",
    "VirtualRouterPeeringsOperations",
    "VirtualRoutersOperations",
    "AvailableServiceAliasesOperations",
    "VpnServerConfigurationsAssociatedWithVirtualWanOperations",
    "VpnServerConfigurationsOperations",
    "IpGroupsOperations",
    "VirtualHubRouteTableV2SOperations",
    "FlowLogsOperations",
    "NetworkVirtualAppliancesOperations",
    "IpAllocationsOperations",
    "PrivateDnsZoneGroupsOperations",
    "SecurityPartnerProvidersOperations",
    "HubRouteTablesOperations",
    "ApplicationGatewayPrivateEndpointConnectionsOperations",
    "ApplicationGatewayPrivateLinkResourcesOperations",
    "FirewallPolicyRuleCollectionGroupsOperations",
    "VirtualApplianceSitesOperations",
    "VirtualApplianceSkusOperations",
    "VirtualHubBgpConnectionOperations",
    "VirtualHubBgpConnectionsOperations",
    "VirtualHubIpConfigurationOperations",
    "CustomIPPrefixesOperations",
    "DscpConfigurationOperations",
    "InboundSecurityRuleOperations",
    "WebCategoriesOperations",
    "NatRulesOperations",
    "VirtualNetworkGatewayNatRulesOperations",
    "ActiveConnectivityConfigurationsOperations",
    "ActiveSecurityAdminRulesOperations",
    "ActiveSecurityUserRulesOperations",
    "AdminRuleCollectionsOperations",
    "AdminRulesOperations",
    "ConnectivityConfigurationsOperations",
    "EffectiveConnectivityConfigurationsOperations",
    "EffectiveVirtualNetworksOperations",
    "NetworkGroupsOperations",
    "NetworkManagerCommitsOperations",
    "NetworkManagerDeploymentStatusOperations",
    "NetworkManagerEffectiveSecurityAdminRulesOperations",
    "NetworkManagersOperations",
    "NetworkSecurityPerimetersOperations",
    "NspAccessRulesOperations",
    "NspAccessRulesReconcileOperations",
    "NspAssociationReconcileOperations",
    "NspAssociationsOperations",
    "NspLinkReconcileOperations",
    "NspLinkReferenceReconcileOperations",
    "NspLinkReferencesOperations",
    "NspLinksOperations",
    "NspProfilesOperations",
    "PerimeterAssociableResourceTypesOperations",
    "SecurityAdminConfigurationsOperations",
    "SecurityUserConfigurationsOperations",
    "UserRuleCollectionsOperations",
    "UserRulesOperations",
    "ApplicationGatewayWafDynamicManifestsDefaultOperations",
    "ApplicationGatewayWafDynamicManifestsOperations",
    "ConfigurationPolicyGroupsOperations",
    "ExpressRoutePortAuthorizationsOperations",
    "ExpressRouteProviderPortsLocationOperations",
    "FirewallPolicyIdpsSignaturesFilterValuesOperations",
    "FirewallPolicyIdpsSignaturesOperations",
    "FirewallPolicyIdpsSignaturesOverridesOperations",
    "ManagementGroupNetworkManagerConnectionsOperations",
    "RouteMapsOperations",
    "RoutingIntentOperations",
    "ScopeConnectionsOperations",
    "ServiceTagInformationOperations",
    "StaticMembersOperations",
    "SubscriptionNetworkManagerConnectionsOperations",
    "VipSwapOperations",
    "NetworkManagementClientOperationsMixin",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
