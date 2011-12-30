from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from cms.menu_bases import CMSAttachMenu
from menus.base import (
  Menu,
  Modifier,
  NavigationNode
)
from menus.menu_pool import menu_pool
from menus.templatetags.menu_tags import (
  cut_levels,
  cut_after,
  flatten,
)

from models import (
  Settings,
  TEMPLATE_PATH,
)

class MenuPlugin(CMSPluginBase):
    model = Settings
    name = _("Embedded Menu")
    render_template = "cmsplugin_menu/menu.html"

    def render(self, context, instance, placeholder):

        try:
            # If there's an exception (500), default context_processors may not be called.
            request = context['request']
        except KeyError:
            return "error"

        levels = 100

        root_id = 'home'
        namespace = 'home'
        from_level = 1
        to_level = 100
        extra_inactive = 100
        extra_active = 100
        next_page = False


        nodes = menu_pool.get_nodes(request)
        children = []
        for node in nodes:
            if node.selected:
                cut_after(node, levels, [])
                children = node.children
                for child in children:
                    child.parent = None
                children = menu_pool.apply_modifiers(children, request, post_cut=True)
        context.update({
            'children':children,
            'from_level':0,
            'to_level':0,
            'extra_inactive':0,
            'extra_active':0
        })
        return context

plugin_pool.register_plugin(CMSMenu)
