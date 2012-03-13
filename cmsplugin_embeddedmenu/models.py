import os

from django.db import models
from django.utils.translation import ugettext_lazy as _

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
	menu_title = models.CharField(_("Menu Title"),
		blank=True, null=True, max_length=256,
		help_text=_("""Title of the menu"""))
	sub_title = models.CharField(_("Sub Title"),
		blank=True, null=True, max_length=256,
		help_text=_("""Sub Title of the menu"""))
	description = models.TextField(_("Description"),
		blank=True, null=True,
		help_text=_("""Description for the menu"""))

	container_template = models.CharField(_("Plugin Template"),
		choices = DynamicTemplateChoices(
			path = ApplicationSettings.CONTAINER_TEMPLATE_PATH,
			include = '.html'),
		max_length = 256,
		help_text = _("""Use this template to render the menu container"""))

	tree_template = models.CharField(_("Tree Template",)
		choices = DynamicTemplateChoices(
			path = ApplicationSettings.MENU_TEMPLATE_PATH,
			include = '.html'),
		max_length = 256,
		help_text = _("""Use this template to render a menu branch"""))

	item_template = models.CharField(_("Leaf Template"),
		choices = DynamicTemplateChoices(
			path = ApplicationSettings.ITEM_TEMPLATE_PATH,
			include = '.html'),
		max_length = 256,
		help_text = _("""Use this template to render a leaf(a menu item) of a menu branch."""))

	root = models.ForeignKey("cms.Page",
		default = 1,
		help_text = _("""Menu tree starts from this page."""))

	include_root = models.BooleanField(_("Include Root"),
		default = True,
		help_text = _("""Shall the menu also include the root menu item specified?"""))

	start_level = models.IntegerField(_("Start Level"), default = 0,
		help_text = _("""Should the root page also be included in the output?"""))

	depth = models.IntegerField(_("Depth"), default = 0,
		help_text = _("""How many levels deep to look for menu items to show?"""))
