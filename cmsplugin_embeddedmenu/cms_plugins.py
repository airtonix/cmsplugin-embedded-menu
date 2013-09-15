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
from .forms import EmbedPagesAdminForm


from .models import (
	ApplicationSettings,
	MenuPluginSettings,
)


class MenuPlugin(CMSPluginBase):
		model = MenuPluginSettings
		name = _("Embedded Menu")
		render_template = "cmsplugin_embeddedmenu/base.html"
		admin_preview = False
		form = EmbedPagesAdminForm

		def render(self, context, instance, placeholder):

				try:
						# If there's an exception (500), default context_processors may not be called.
						request = context['request']
				except KeyError:
						return _("There is no `request` object in the context.")

				root_page = instance.root
				root_page_url = root_page.get_absolute_url()
				from_level = instance.start_level
				to_level = instance.depth

				nodes = menu_pool.get_nodes(request)

				children = list()
				root_node = None

				# Find the root node
				for node in nodes:
						if not root_node and node.url == root_page_url:
								root_node = node

				if root_node:
						if instance.include_root :
								children += (root_node, )
						else:
								children += root_node.children

				context.update({
						'MenuItems' : children,
						'MenuTitle' : instance.menu_title,
						'MenuSubtitle' : instance.sub_title,
				})
				return context

plugin_pool.register_plugin(MenuPlugin)

