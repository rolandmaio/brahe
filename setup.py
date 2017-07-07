import os

from setuptools import setup, find_packages

from brahe import __version__


def read_md(md_file):
    with open(md_file) as fh:
        contents = fh.read()
    return contents


README = os.path.join(os.path.dirname(__file__), "README.md")


setup(
    name="Brahe",
    version=__version__,
    description="""A command line program for maintaining research notes""",
    long_description=read_md(README),
    keywords=["notes", "console", "research"],
    author="Roland Maio",
    author_email="rolandmaio38@gmail.com",
    url="https://github.com/rolandmaio/brahe",
    license="MIT",
    packages=find_packages(),
    scripts=[os.path.join("brahe", "bin", "brahe-admin.py")],
    classifiers=[
        "Environment :: Console",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python 3 :: Only",
        "Programming Language :: Python 3.5",
        "Topic :: Scientific/Engineering",
    ],
)
