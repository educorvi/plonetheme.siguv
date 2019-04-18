# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone.browserlayer import utils
from plonetheme.siguv.interfaces import IPlonethemeSiguvLayer
from plonetheme.siguv.testing import PLONETHEME_SIGUV_INTEGRATION_TESTING  # noqa
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.siguv is properly installed."""

    layer = PLONETHEME_SIGUV_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.qi = get_installer(self.portal)

    def test_product_installed(self):
        """Test if plonetheme.siguv is installed."""
        self.assertTrue(self.qi.is_product_installed('plonetheme.siguv'))

    def test_browserlayer(self):
        """Test that IPlonethemeSiguvLayer is registered."""
        self.assertIn(IPlonethemeSiguvLayer, utils.registered_layers())

    def test_product_uninstalled(self):
        """Test if plonetheme.siguv is cleanly uninstalled."""
        self.assertTrue(self.qi.is_product_installed('plonetheme.siguv'))
        self.qi.uninstall_product('plonetheme.siguv')
        self.assertFalse(self.qi.is_product_installed('plonetheme.siguv'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeSiguvLayer is removed."""
        self.assertTrue(self.qi.is_product_installed('plonetheme.siguv'))
        self.qi.uninstall_product('plonetheme.siguv')
        self.assertNotIn(IPlonethemeSiguvLayer, utils.registered_layers())
