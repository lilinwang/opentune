from pathlib import Path
from setuptools import find_packages, setup

with open(Path(__file__).absolute().parents[0] / "opentune" / "VERSION") as _f:
    __version__ = _f.read().strip()

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="opentune",
    version=__version__,
    description="OpenTune SDK to fine tune a model with training data.",
    package_dir={"": "opentune"},
    packages=find_packages(where="opentune"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lilinwang/opentune",
    author="Evaly",
    author_email="lw555@cornell.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
