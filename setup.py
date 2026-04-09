# setup.py
from setuptools import setup, find_packages

setup(
    name="repl-nix-workspace",
    version="0.1.0",
    description="Your project description here",
    author="Your Name",
    packages=find_packages(exclude=[
        "pyarrow.tests*",
        "pyarrow.vendored*"
    ]),
    install_requires=[
        "streamlit==1.46.0",
        "pyarrow",   # required by streamlit
        # Add other dependencies here
    ],
    include_package_data=True,
    python_requires=">=3.10",  # or your target Python version
    zip_safe=False,
)
