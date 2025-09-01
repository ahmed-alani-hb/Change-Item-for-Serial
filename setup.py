from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

setup(
    name="change_item_for_serial",
    version="0.0.1",
    description="Utility app to change item code for Serial No records",
    author="",
    author_email="",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"],
)
