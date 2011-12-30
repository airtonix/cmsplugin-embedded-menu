import os

from django.db import models
from cms.models.pluginmodel import CMSPlugin

from .lib.choices import (
  DynamicTemplateChoices,
  PageAttributeDynamicChoices,
)

TEMPLATE_PATH = os.path.join("cmsplugin_menu", "layouts")

class MenuPluginSettings(CMSPlugin):
    """ Stores options for cmsplugin that Embeds a menu
    """

    TEMPLATE_CHOICES = DynamicTemplateChoices(
            path=TEMPLATE_PATH,
            include='.html',
            exclude='default')

    root = models.ForeignKey("cms.Page", default=1,
      help_text="""Menu tree starts from this page.""")

    start_level = models.IntegerField(default=0,
      help_text="""Should the root page also be included in the output?""")

    depth = models.IntegerField(default=0,
      help_text="""How many levels deep to look for menu items to show?""")
