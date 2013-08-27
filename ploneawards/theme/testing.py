# -*- coding: utf-8 -*-

from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing.z2 import ZSERVER_FIXTURE


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import ploneawards.theme
        self.loadZCML(package=ploneawards.theme)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'ploneawards.theme:default')

FIXTURE = Fixture()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='ploneawards.theme:Integration',
)

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, ZSERVER_FIXTURE),
    name='ploneawards.theme:Functional',
)
