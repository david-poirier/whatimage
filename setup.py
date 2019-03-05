import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whatimage",
    version="0.0.3",
    author="David Poirier",
    author_email="david-poirier-csn@users.noreply.github.com",
    description="Python library to detect image type from a few bytes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/david-poirier-csn/whatimage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
