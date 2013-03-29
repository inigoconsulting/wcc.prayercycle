from five import grok
from DateTime import DateTime
from Products.CMFCore.interfaces import ISiteRoot
from plone.app.layout.navigation.interfaces import INavigationRoot

grok.templatedir('templates')

class PrayerCycleTYPO3Module(grok.View):
    grok.name('currentprayercycle.xml')
    grok.context(INavigationRoot)

    def render(self):
        self.request.response.setHeader('Content-Type', 'text/xml')
        return '''<?xml version="1.0" encoding="utf-8" ?>
        <Module>
            <ModulePrefs title="Prayer cycle" />
            <Content type="url" href="%s" />
        </Module>''' % (self.context.absolute_url() +
                        '/currentprayercycle.html')

class CurrentPrayerCycleEmbedView(grok.View):
    grok.name('currentprayercycle.html')
    grok.template('currentprayercycle_embed')
    grok.context(INavigationRoot)

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

