# -*- coding: utf-8 -*-
from Acquisition import aq_get
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.testing.zope import installProduct
from plone.testing.zserver import ZSERVER_FIXTURE

import collective.sidebar
import nva.footerviewlet
import nva.testbootstrap
import plonetheme.siguv
import plonetheme.tokyo


class PlonethemeSiguvLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        request = aq_get(app, 'REQUEST')
        request.environ['HTTP_ACCEPT_LANGUAGE'] = 'de'
        self.loadZCML(package=collective.sidebar)
        self.loadZCML(package=plonetheme.tokyo)
        self.loadZCML(package=plonetheme.siguv)
        self.loadZCML(package=nva.footerviewlet)
        self.loadZCML(package=nva.testbootstrap)
        installProduct(app, 'collective.sidebar')
        installProduct(app, 'plonetheme.tokyo')
        installProduct(app, 'plonetheme.siguv')
        installProduct(app, 'nva.footerviewlet')
        installProduct(app, 'nva.testbootstrap')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.siguv:default')
        portal.acl_users.userFolderAddUser(
            SITE_OWNER_NAME, SITE_OWNER_PASSWORD, ['Manager'], [])


PLONETHEME_SIGUV_FIXTURE = PlonethemeSiguvLayer()


PLONETHEME_SIGUV_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_SIGUV_FIXTURE,),
    name='PlonethemeSiguvLayer:IntegrationTesting',
)


PLONETHEME_SIGUV_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_SIGUV_FIXTURE,),
    name='PlonethemeSiguvLayer:FunctionalTesting',
)


PLONETHEME_SIGUV_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        ZSERVER_FIXTURE,
        PLONETHEME_SIGUV_FIXTURE,
    ),
    name='PlonethemeSiguvLayer:AcceptanceTesting',
)
