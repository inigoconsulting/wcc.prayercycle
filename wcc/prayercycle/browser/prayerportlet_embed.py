from five import grok
from DateTime import DateTime
from Products.CMFCore.interfaces import ISiteRoot

grok.templatedir('templates')

class CurrentPrayerCycleEmbedView(grok.View):
    grok.name('currentprayercycle_embed')
    grok.template('currentprayercycle_embed')
    grok.context(ISiteRoot)

    def prayercycle(self):
        # get current prayer cycle for date and context
        today = DateTime()
        brains = self.context.portal_catalog(start={
            'query': [today],
            'range': 'max'
        }, end={
            'query': [today],
            'range': 'min'
        },
        portal_type='wcc.prayercycle.prayercycle')

        if brains:
            return brains[0].getObject()
        return None

    def startDate(self):
        prayercycle = self.prayercycle()
        startDate = getattr(prayercycle, 'startDate', None)
        if startDate is not None:
            return startDate.strftime('%d %B %Y')
        return ''

    def endDate(self):
        prayercycle = self.prayercycle()
        endDate = getattr(prayercycle, 'endDate', None)
        if endDate is not None:
            return endDate.strftime('%d %B %Y')
        return ''

