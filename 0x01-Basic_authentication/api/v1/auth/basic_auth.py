#!/usr/bin/env python3

import base64
from exceptiongroup import catch
from api.v1.auth.auth import Auth


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
