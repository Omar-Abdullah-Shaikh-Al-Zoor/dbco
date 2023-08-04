from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dbco/__init__.py
from dbco import __version__ as version

setup(
	name="dbco",
	version=version,
	description="Custom application customized for DBCO company",
	author="Advanced Resources",
	author_email="ar@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
