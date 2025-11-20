from setuptools import setup
import site, sys
import pathlib

site.ENABLE_USER_SITE = "--user" in sys.argv[1:]

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="prettyprint",
    version="1.0.0",
    description="python module that prettifies the printing of the print function (everthing is printed in lower case)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/reon04/prettyprint",
    author="reon04",
    author_email="larsmichels04@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13'
    ],
    packages=["prettyprint"],
    license="MIT",
    python_requires=">=3.8, <4"
)