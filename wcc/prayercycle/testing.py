from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import wcc.prayercycle


WCC_PRAYERCYCLE = PloneWithPackageLayer(
    zcml_package=wcc.prayercycle,
    zcml_filename='testing.zcml',
    gs_profile_id='wcc.prayercycle:testing',
    name="WCC_PRAYERCYCLE")

WCC_PRAYERCYCLE_INTEGRATION = IntegrationTesting(
    bases=(WCC_PRAYERCYCLE, ),
    name="WCC_PRAYERCYCLE_INTEGRATION")

WCC_PRAYERCYCLE_FUNCTIONAL = FunctionalTesting(
    bases=(WCC_PRAYERCYCLE, ),
    name="WCC_PRAYERCYCLE_FUNCTIONAL")
