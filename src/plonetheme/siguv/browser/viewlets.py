# -*- coding: utf-8 -*-

from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class NavigationViewlet(GlobalSectionsViewlet):

    index = ViewPageTemplateFile('templates/navigation.pt')

    def return_navtree(self, path=None):
        if not path:
            path = self.navtree_path
        return self.navtree.get(path, [])

    def get_navigation_class(self):
        # Fetch from settings if navigation is enabled (default),
        # disabled or always-active.
        return 'enabled'

    def get_item_class(self, item, sub):
        # We don't compute 'sub' from item as it expensive
        # and it was already computed in the page template
        css_class = u'nav-item'
        if sub:
            css_class += u' dropdown'
        if item and 'id' in item and self.selected_portal_tab == item['id']:
            css_class += u' active'
        return css_class
