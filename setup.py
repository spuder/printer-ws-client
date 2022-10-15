from setuptools import setup

setup(
    name="simplyprint_ws_client",
    version="0.0.1",
    description="SimplyPrint Websocket Client",
    url="https://github.com/SimplyPrint/printer-ws-client",
    author="SimplyPrint",
    license="AGPLv3",
    packages=["simplyprint_ws_client"],
    install_requires=[
        "tornado",
        "psutil",
        "sentry_sdk",
        "netifaces",
    ]
)
