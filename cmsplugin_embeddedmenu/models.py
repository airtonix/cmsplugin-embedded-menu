import os

from django.db import models
from cms.models.pluginmodel import CMSPlugin
from appconf import AppConf

from .lib.choices import (
	DynamicTemplateChoices,
)


class ApplicationSettings(AppConf):
	TEMPLATE_PATH = os.path.join("cmsplugin_embeddedmenu", "layouts")
	CONTAINER_TEMPLATE_PATH = os.path.join(TEMPLATE_PATH, "containers")
	MENU_TEMPLATE_PATH = os.path.join(TEMPLATE_PATH, "menus")
	ITEM_TEMPLATE_PATH = os.path.join(TEMPLATE_PATH, "items")

class MenuPluginSettings(CMSPlugin):
	""" Stores options for cmsplugin that Embeds a menu
	"""
#	title = models.CharField(max_length=128, blank=True, null=True)

	container_template = models.CharField("Plugin Template",
		choices = DynamicTemplateChoices(
			path = ApplicationSettings.CONTAINER_TEMPLATE_PATH,
			include = '.html'),
		max_length = 256,
		help_text = """Use this template to render the menu container""")

	tree_template = models.CharField("Tree Template",
		choices = DynamicTemplateChoices(
			path = ApplicationSettings.MENU_TEMPLATE_PATH,
			include = '.html'),
		max_length = 256,
		help_text = """Use this template to render a menu branch""")

	item_template = models.CharField("Leaf Template",
		choices = DynamicTemplateChoices(
			path = ApplicationSettings.ITEM_TEMPLATE_PATH,
			include = '.html'),
		max_length = 256,
		help_text = """Use this template to render a leaf(a menu item) of a menu branch.""")

	root = models.ForeignKey("cms.Page",
		default = 1,
		help_text = """Menu tree starts from this page.""")

	include_root = models.BooleanField("Include Root",
		default = True,
		help_text = """Shall the menu also include the root menu item specified?""")

	start_level = models.IntegerField(default = 0,
		help_text = """Should the root page also be included in the output?""")

	depth = models.IntegerField(default = 0,
		help_text = """How many levels deep to look for menu items to show?""")
