from collective.grok import gs
from wcc.prayercycle import MessageFactory as _

@gs.importstep(
    name=u'wcc.prayercycle', 
    title=_('wcc.prayercycle import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.prayercycle.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
