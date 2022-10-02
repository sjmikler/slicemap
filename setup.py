from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

packages = find_packages()
print("Packages found:", packages)

setup(
    name="slicemap",
    version="1.0.37",
    url="https://github.com/gahaalt/slicemap.git",
    project_urls={
        "Documentation": "https://slicemap.readthedocs.io/",
    },
    author="Szymon Mikler",
    author_email="sjmikler@gmail.com",
    license="MIT",
    description="A tiny package containing a dict-like data structure with numeric"
    " slices as keys.",
    packages=packages,
    python_requires=">=3.7",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    install_requires=["sortedcontainers>=2.4.0"],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
