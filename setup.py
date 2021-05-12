plugin_identifier = "onlineprinterplugin"
plugin_package = "octoprint_onlineprinterplugin"
plugin_name = "OnlinePrinterPlugin"
plugin_version = "1.0.0"
plugin_description = """A simple plugin that adds a lot of stuff to your OctoPrint"""
plugin_author = "mytja"
plugin_author_email = "mytja@protonmail.com"
plugin_url = "https://github.com/mytja/OnlinePrinterPlugin"
plugin_license = "GPLv3"
plugin_requires = ["pyserial"]

from setuptools import setup

try:
	import octoprint_setuptools
except:
	print("Could not import OctoPrint's setuptools, are you sure you are running that under "
	      "the same python installation that OctoPrint is installed under?")
	import sys
	sys.exit(-1)

setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
	identifier=plugin_identifier,
	package=plugin_package,
	name=plugin_name,
	version=plugin_version,
	description=plugin_description,
	author=plugin_author,
	mail=plugin_author_email,
	url=plugin_url,
	license=plugin_license,
	requires=plugin_requires
)

setup(**setup_parameters)