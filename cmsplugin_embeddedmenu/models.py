import os

from django.db import models
from cms.models.pluginmodel import CMSPlugin

from .lib.choices import (
  DynamicTemplateChoices,
  PageAttributeDynamicChoices,
)

TEMPLATE_PATH = os.path.join("cmsplugin_embeddedmenu", "layouts")
CONTAINER_TEMPLATE_PATH = os.path.join(TEMPLATE_PATH, "containers")
MENU_TEMPLATE_PATH = os.path.join(TEMPLATE_PATH, "menus")
ITEM_TEMPLATE_PATH = os.path.join(TEMPLATE_PATH, "items")

class MenuPluginSettings(CMSPlugin):
    """ Stores options for cmsplugin that Embeds a menu
    """

    container_template = models.CharField("Container Template",
      choices = DynamicTemplateChoices(
            path=CONTAINER_TEMPLATE_PATH,
            include='.html',
            exclude='default'), max_length=256,
      help_text="""Use this template to render the menu container""")

    tree_template = models.CharField("Menu Template",
      choices = DynamicTemplateChoices(
            path=MENU_TEMPLATE_PATH,
            include='.html',
            exclude='default'), max_length=256,
      help_text="""Use this template to render a menu branch""")

    item_template = models.CharField("Menu Item Template",
      choices = DynamicTemplateChoices(
            path=ITEM_TEMPLATE_PATH,
            include='.html',
            exclude='default'), max_length=256,
      help_text="""Use this template to render the menu item.""")

    root = models.ForeignKey("cms.Page", default=1,
      help_text="""Menu tree starts from this page.""")

    include_root = models.BooleanField("Include Root", default=True,
      help_text="""Shall the menu also include the root menu item specified?""")

    start_level = models.IntegerField(default=0,
      help_text="""Should the root page also be included in the output?""")

    depth = models.IntegerField(default=0,
      help_text="""How many levels deep to look for menu items to show?""")
