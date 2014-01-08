from collective.grok import gs
from Products.CMFCore.utils import getToolByName

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.prayercycle to 1006',
                description=u'Upgrade wcc.prayercycle to 1006',
                source='1005', destination='1006',
                sortkey=1, profile='wcc.prayercycle:default')
def to1006(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.prayercycle.upgrades:to1006')


@gs.upgradestep(title=u'Upgrade wcc.prayercycle to 1005',
                description=u'Upgrade wcc.prayercycle to 1005',
                source='1004', destination='1005',
                sortkey=1, profile='wcc.prayercycle:default')
def to1005(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.prayercycle.upgrades:to1005')

    catalog = getToolByName(context, 'portal_catalog')
    for brain in catalog(portal_type=['wcc.prayercycle.prayercycle'],
            Language='all'):
        obj = brain.getObject()
        obj.reindexObject()


@gs.upgradestep(title=u'Upgrade wcc.prayercycle to 1004',
                description=u'Upgrade wcc.prayercycle to 1004',
                source='1003', destination='1004',
                sortkey=1, profile='wcc.prayercycle:default')
def to1004(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.prayercycle.upgrades:to1004')


@gs.upgradestep(title=u'Upgrade wcc.prayercycle to 1003',
                description=u'Upgrade wcc.prayercycle to 1003',
                source='1002', destination='1003',
                sortkey=1, profile='wcc.prayercycle:default')
def to1003(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.prayercycle.upgrades:to1003')


@gs.upgradestep(title=u'Upgrade wcc.prayercycle to 1002',
                description=u'Upgrade wcc.prayercycle to 1002',
                source='1001', destination='1002',
                sortkey=1, profile='wcc.prayercycle:default')
def to1002(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.prayercycle.upgrades:to1002')
