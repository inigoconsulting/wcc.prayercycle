from five import grok
from plone.directives import dexterity, form
from wcc.prayercycle.content.prayercycle import IPrayerCycle

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IPrayerCycle)
    grok.require('zope2.View')
    grok.template('prayercycle_view')
    grok.name('view')


    def startDate(self):
        context=self.context
        startDate = getattr(context, 'startDate', None)
        if startDate is not None:
            return startDate
        return ''

    def endDate(self):
        context=self.context
        endDate = getattr(context, 'endDate', None)
        if endDate is not None:
            return endDate
        return ''
