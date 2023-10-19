# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

from typing import Any, Collection, MutableMapping, Optional, Tuple, Union

from .utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class SecurityClient(NamespacedClient):
    from ._patch import health_check, update_audit_config

    @query_params()
    def get_account_details(
        self, params: Union[Any, None] = None, headers: Union[Any, None] = None
    ) -> Union[bool, Any]:
        """
        Returns account details for the current user.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "account"),
            params=params,
            headers=headers,
        )

    @query_params()
    def change_password(
        self,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Changes the password for the current user.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "account"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_action_group(
        self,
        action_group: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Retrieves one action group.
        """
        if action_group in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'action-group'."
            )

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "actiongroups", action_group),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_action_groups(
        self, params: Union[Any, None] = None, headers: Union[Any, None] = None
    ) -> Union[bool, Any]:
        """
        Retrieves all action groups.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "actiongroups"),
            params=params,
            headers=headers,
        )

    @query_params()
    def delete_action_group(
        self,
        action_group: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Deletes the specified action group.
        """
        if action_group in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'action-group'."
            )

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "actiongroups", action_group),
            params=params,
            headers=headers,
        )

    @query_params()
    def create_action_group(
        self,
        action_group: Any,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Creates or replaces the specified action group.
        """
        for param in (action_group, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "actiongroups", action_group),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_action_group(
        self,
        action_group: Any,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Updates individual attributes of an action group.
        """
        for param in (action_group, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "actiongroups", action_group),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_action_groups(
        self,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Creates, updates, or deletes multiple action groups in a single call.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "actiongroups"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_user(
        self,
        username: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Retrieves one user.
        """
        if username in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'username'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "internalusers", username),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_users(
        self, params: Union[Any, None] = None, headers: Union[Any, None] = None
    ) -> Union[bool, Any]:
        """
        Retrieves all users.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "internalusers"),
            params=params,
            headers=headers,
        )

    @query_params()
    def delete_user(
        self,
        username: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Deletes the specified user.
        """
        if username in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'username'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "internalusers", username),
            params=params,
            headers=headers,
        )

    @query_params()
    def create_user(
        self,
        username: Any,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Creates or replaces the specified user.
        """
        for param in (username, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "internalusers", username),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_user(
        self,
        username: Any,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Updates individual attributes of an internal user.
        """
        for param in (username, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "internalusers", username),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_users(
        self,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Creates, updates, or deletes multiple internal users in a single call.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "internalusers"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_role(
        self,
        role: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Retrieves one role.
        """
        if role in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'role'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "roles", role),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_roles(
        self, params: Union[Any, None] = None, headers: Union[Any, None] = None
    ) -> Union[bool, Any]:
        """
        Retrieves all roles.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "roles"),
            params=params,
            headers=headers,
        )

    @query_params()
    def delete_role(
        self,
        role: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Deletes the specified role.
        """
        if role in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'role'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "roles", role),
            params=params,
            headers=headers,
        )

    @query_params()
    def create_role(
        self,
        role: Any,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Creates or replaces the specified role.
        """
        for param in (role, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "roles", role),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_role(
        self,
        role: Any,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Updates individual attributes of a role.
        """
        for param in (role, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "roles", role),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_roles(
        self,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Creates, updates, or deletes multiple roles in a single call.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "roles"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_role_mapping(
        self,
        role: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Retrieves one role mapping.
        """
        if role in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'role'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "rolesmapping", role),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_role_mappings(
        self, params: Union[Any, None] = None, headers: Union[Any, None] = None
    ) -> Union[bool, Any]:
        """
        Retrieves all role mappings.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "rolesmapping"),
            params=params,
            headers=headers,
        )

    @query_params()
    def delete_role_mapping(
        self,
        role: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Deletes the specified role mapping.
        """
        if role in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'role'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "rolesmapping", role),
            params=params,
            headers=headers,
        )

    @query_params()
    def create_role_mapping(
        self,
        role: Any,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Creates or replaces the specified role mapping.
        """
        for param in (role, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "rolesmapping", role),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_role_mapping(
        self,
        role: Any,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Updates individual attributes of a role mapping.
        """
        for param in (role, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "rolesmapping", role),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_role_mappings(
        self,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Creates or updates multiple role mappings in a single call.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "rolesmapping"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_tenant(
        self,
        tenant: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Retrieves one tenant.
        """
        if tenant in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'tenant'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "tenants", tenant),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_tenants(
        self, params: Union[Any, None] = None, headers: Union[Any, None] = None
    ) -> Union[bool, Any]:
        """
        Retrieves all tenants.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "tenants"),
            params=params,
            headers=headers,
        )

    @query_params()
    def delete_tenant(
        self,
        tenant: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Deletes the specified tenant.
        """
        if tenant in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'tenant'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "tenants", tenant),
            params=params,
            headers=headers,
        )

    @query_params()
    def create_tenant(
        self,
        tenant: Any,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Creates or replaces the specified tenant.
        """
        for param in (tenant, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "tenants", tenant),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_tenant(
        self,
        tenant: Any,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Add, delete, or modify a single tenant.
        """
        for param in (tenant, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "tenants", tenant),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_tenants(
        self,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Add, delete, or modify multiple tenants in a single call.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "tenants"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_configuration(
        self, params: Union[Any, None] = None, headers: Union[Any, None] = None
    ) -> Union[bool, Any]:
        """
        Retrieves the current Security plugin configuration in JSON format.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "securityconfig"),
            params=params,
            headers=headers,
        )

    @query_params()
    def update_configuration(
        self,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Retrieves the current Security plugin configuration in JSON format.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "securityconfig", "config"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_configuration(
        self,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Updates the existing configuration using the REST API.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "securityconfig"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_distinguished_names(
        self,
        cluster_name: Union[Any, None],
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Retrieves all distinguished names in the allow list.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "nodesdn", cluster_name),
            params=params,
            headers=headers,
        )

    @query_params()
    def update_distinguished_names(
        self,
        cluster_name: Any,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Adds or updates the specified distinguished names in the cluster's or node's allow list.
        """
        for param in (cluster_name, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "nodesdn", cluster_name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def delete_distinguished_names(
        self,
        cluster_name: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        Deletes all distinguished names in the specified cluster's or node's allow list.
        """
        if cluster_name in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'cluster-name'."
            )

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "nodesdn", cluster_name),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_certificates(
        self, params: Union[Any, None] = None, headers: Union[Any, None] = None
    ) -> Union[bool, Any]:
        """
        Retrieves the cluster's security certificates.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "ssl", "certs"),
            params=params,
            headers=headers,
        )

    @query_params()
    def reload_transport_certificates(
        self, params: Union[Any, None] = None, headers: Union[Any, None] = None
    ) -> Union[bool, Any]:
        """
        Reloads SSL certificates that are about to expire without restarting the OpenSearch node.
        """
        return self.transport.perform_request(
            "PUT",
            _make_path(
                "_opendistro", "_security", "api", "ssl", "transport", "reloadcerts"
            ),
            params=params,
            headers=headers,
        )

    @query_params()
    def reload_http_certificates(
        self, params: Union[Any, None] = None, headers: Union[Any, None] = None
    ) -> Union[bool, Any]:
        """
        Reloads SSL certificates that are about to expire without restarting the OpenSearch node.
        """
        return self.transport.perform_request(
            "PUT",
            _make_path("_opendistro", "_security", "api", "ssl", "http", "reloadcerts"),
            params=params,
            headers=headers,
        )

    @query_params()
    def flush_cache(
        self, params: Union[Any, None] = None, headers: Union[Any, None] = None
    ) -> Union[bool, Any]:
        """
        Flushes the Security plugin user, authentication, and authorization cache.
        """
        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "cache"),
            params=params,
            headers=headers,
        )

    @query_params()
    def health(
        self,
        *,
        pretty: Optional[bool],
        human: Optional[bool],
        error_trace: Optional[bool],
        format: Optional[str],
        filter_path: Optional[Union[str, Collection[str]]],
        request_timeout: Optional[Union[int, float]],
        ignore: Optional[Union[int, Collection[int]]],
        opaque_id: Optional[str],
        http_auth: Optional[Union[str, Tuple[str, str]]],
        api_key: Optional[Union[str, Tuple[str, str]]],
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None
    ) -> Any:
        """
        Checks to see if the Security plugin is up and running.

        """
        return self.transport.perform_request(
            "GET", "/_plugins/_security/health", params=params, headers=headers
        )

    @query_params()
    def get_audit_configuration(
        self, params: Union[Any, None] = None, headers: Union[Any, None] = None
    ) -> Union[bool, Any]:
        """
        A GET call retrieves the audit configuration.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_opendistro", "_security", "api", "audit"),
            params=params,
            headers=headers,
        )

    @query_params()
    def update_audit_configuration(
        self,
        *,
        body: Any,
        pretty: Optional[bool],
        human: Optional[bool],
        error_trace: Optional[bool],
        format: Optional[str],
        filter_path: Optional[Union[str, Collection[str]]],
        request_timeout: Optional[Union[int, float]],
        ignore: Optional[Union[int, Collection[int]]],
        opaque_id: Optional[str],
        http_auth: Optional[Union[str, Tuple[str, str]]],
        api_key: Optional[Union[str, Tuple[str, str]]],
        params: Optional[MutableMapping[str, Any]] = None,
        headers: Optional[MutableMapping[str, str]] = None
    ) -> Any:
        """
        Updates the audit configuration.

        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PUT",
            "/_plugins/_security/api/audit/config",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_audit_configuration(
        self,
        body: Any,
        params: Union[Any, None] = None,
        headers: Union[Any, None] = None,
    ) -> Union[bool, Any]:
        """
        A PATCH call is used to update specified fields in the audit configuration.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_opendistro", "_security", "api", "audit"),
            params=params,
            headers=headers,
            body=body,
        )
