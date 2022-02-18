from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in aj/__init__.py
from aj import __version__ as version

setup(
	name="aj",
	version=version,
	description="Ajan Indus",
	author="aj.com",
	author_email="aj.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
