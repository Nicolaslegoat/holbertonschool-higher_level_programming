#!/usr/bin/python3
def lookup(obj):
    return [attr for attr in dir(obj) if callable(getattr(obj, attr)) or not attr.startswith('__')]
