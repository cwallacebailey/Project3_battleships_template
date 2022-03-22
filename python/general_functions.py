""" This module houses commonly used functions / tools"""
import os
import sys
import time


def display_clear():
    # This is the URL that this code was found on:
    # http://www.delftstack.com/howto/python/python-clear-console/
    """
    clears console
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# https://stackoverflow.com/a/10390877


def type_slowly(text):
    """
    allows text to by typed out slowly
    instead of all appearing at once
    """
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)


def splice_fleet(array, key):
    """
    called to remove specific item
    from array, specifically used
    to remove ships from player/ computer fleet
    """
    array.remove(key)
    return array
