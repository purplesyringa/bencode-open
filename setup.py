from setuptools import setup

setup(
    name="bencode-open",
    version="1.2",
    description="bencode parser and converter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ivanq",
    author_email="imachug@gmail.com",
    url="https://github.com/imachug/bencode-open",
    packages=["bencode_open"],
)