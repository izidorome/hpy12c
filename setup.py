import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    author="Rispar",
    author_email="tecnologia@rispar.com.br",
    url="https://github.com/risparfinance/hpy12c",
    name="hpy12c",
    version="0.1.0",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    package_data={"py12c": ["LICENSE"]},
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="hpy12C - HP-12C financial calculator in python",
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
)
