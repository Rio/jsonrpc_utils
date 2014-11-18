from setuptools import setup

setup(
    name="jsonrpc",
    version="0.2.0",

    packages=[
        "labutils",
        "labutils.jsonrpc",
        "labutils.jsonrpc.errors",
        "labutils.jsonrpc.objects",
        "labutils.jsonrpc.utilities",
        ],

    namespace_packages=["labutils", ]
)
