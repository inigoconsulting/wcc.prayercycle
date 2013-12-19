from plone.indexer.decorator import indexer
from wcc.prayercycle.content.prayercycle import IPrayerCycle


@indexer(IPrayerCycle)
def prayercycle_start(context, **kwarg):
    return context.startDate

@indexer(IPrayerCycle)
def prayercycle_end(context, **kwarg):
    return context.endDate
