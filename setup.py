from setuptools import setup

setup(
    name="HittER",
    version="0.1",
    description="Hierarchical Transformers for Knowledge Graph Embeddings",
    url="https://github.com/microsoft/HittER",
    author="Microsoft Corporation",
    author_email="opencode@microsoft.com",
    packages=["kge"],
    install_requires=[
        "pyyaml==6.0.2",
        "pandas",
        "argparse",
        "path",
        "sqlalchemy",
        "torchviz",
        "dataclasses",
        # LibKGE uses numba typed-dicts which is part of the experimental numba API
        # in version 0.48
        # see http://numba.pydata.org/numba-doc/0.48.0/reference/pysupported.html
        "numba",
        "pytorch-pretrained-bert==0.6.0",
        "regex==2020.5.14",
        "pytorch_lightning",
        "networkx==3.3",
    ],
    zip_safe=False,
    entry_points={"console_scripts": ["kge = kge.cli:main",],},
)
