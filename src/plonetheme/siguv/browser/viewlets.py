# -*- coding: utf-8 -*-

from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class CollapsibleNav(GlobalSectionsViewlet):

    index = ViewPageTemplateFile('templates/collapsible_nav.pt')

    def return_navtree(self, path=None):
        if path:
            return self.navtree.get(path, [])
        return self.navtree.get(self.navtree_path, [])
