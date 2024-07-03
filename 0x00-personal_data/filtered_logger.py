#!/usr/bin/env python3

'''
task 0
'''

from typing import List
from re import sub


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Replace sensitive data in a message with a redaction string.

    Args:
        fields (List[str]): A list of field names to be redacted.
        redaction (str): The string to be used for redaction.
        message (str): The message containing the sensitive data.
        separator (str): The separator used to separate the fields in the message.

    Returns:
        str: The message with the sensitive data redacted.

    """
    for field in fields:
        pattern = fr'{field}=(.*?){separator}'
        replacement = f'{field}={redaction}{separator}'
        message = sub(pattern, replacement, message)
    return message
