#!/usr/bin/env python3

'''
auth module
'''

from typing import List, TypeVar
import requests


class Auth:
    """
    This class represents the authentication system.

    Methods:
    - require_auth: Checks if authentication is required for a given path.
    - authorization_header: Retrieves the authorization header from a request.
    - current_user: Retrieves the current user from a request.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for a given path.

        Args:
        - path: The path to check.
        - excluded_paths: A list of paths that are excluded from authentication

        Returns:
        - True if authentication is required, False otherwise.
        """

        if not path or not excluded_paths:
            return True

        if path[-1] == '/':
            path = path[:-1]

        for i, p in enumerate(excluded_paths):
            if p[-1] == '/':
                excluded_paths[i] = p[:-1]

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Request Flask object """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """
        Retrieves the current user from a request.

        Args:
        - request: The request object.

        Returns:
        - The current user object.
        """
        return None
