from setuptools import setup, find_packages

with open("README.md", "r") as read_me:
    long_description = read_me.read()


setup(
    name="UT Libraries IIIF Cookbook",
    description="a documentation generator for describing potential IIIF presentation manifests for our content",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.1",
    author="Mark Baggett",
    author_email="mbagget1@utk.edu",
    maintainer_email="mbagget1@utk.edu",
    url="https://github.com/utkdigitalinitiatives/utk_iiif_recipes",
    packages=find_packages(),
    extras_require={
        "docs": [
            "sphinx >= 3.0.1",
            "sphinx-rtd-theme >= 0.5.0",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics :: Presentation",
    ],
    keywords=["libraries", "iiif", "digital repositories", "documentation"],
)