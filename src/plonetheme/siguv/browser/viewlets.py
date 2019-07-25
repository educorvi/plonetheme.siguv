# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class NavigationViewlet(GlobalSectionsViewlet):

    index = ViewPageTemplateFile('templates/navigation.pt')

    def return_navtree(self, path=None):
        if not path:
            path = self.navtree_path
        return self.navtree.get(path, [])

    @staticmethod
    def get_navigation_class():
        """
        Fetch from settings if navigation is enabled (default), disabled
        or collapsed.
        """
        return api.portal.get_registry_record(
            name='plonetheme.siguv.navigation_status',
            default='enabled',
        )

    def get_item_class(self, item, sub):
        # We don't compute 'sub' from item as it expensive
        # and it was already computed in the page template
        css_class = u'nav-item'
        if sub:
            css_class += u' dropdown'
        if item and 'id' in item and self.selected_portal_tab == item['id']:
            css_class += u' active'
        return css_class
