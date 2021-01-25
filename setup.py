import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="reecapi",
    version="0.0.1",
    author="Luis Gascó",
    author_email="luisgascosanchez@gmail.com",
    description="Crawer for the 'Registro Español de Estudios Clínicos'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luisgasco/REECapi/",
    install_requires=[
   'requests>=2.22.0'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)