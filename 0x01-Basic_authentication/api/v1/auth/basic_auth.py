#!/usr/bin/env python3

import base64
from typing import TypeVar
from exceptiongroup import catch
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if not authorization_header or \
                not isinstance(authorization_header, str) or \
                not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        if not base64_authorization_header or \
                not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_string = base64.b64decode(
                base64_authorization_header).decode('utf-8')
            # print("Decoded string:", decoded_string)
            return decoded_string
        except Exception as err:
            pass

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        if decoded_base64_authorization_header is None or \
                not isinstance(decoded_base64_authorization_header, str) or \
                ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':'))

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        auth_header = self.authorization_header(request)
        get_base64 = self.extract_base64_authorization_header(auth_header)
        decode_base64 = self.decode_base64_authorization_header(get_base64)
        get_data = self.extract_user_credentials(decode_base64)
        user_obj = self.user_object_from_credentials(get_data[0], get_data[1])

        return user_obj
