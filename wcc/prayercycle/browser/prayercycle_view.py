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
        startDate = getattr(self.context, 'startDate', None)
        endDate = getattr(self.context, 'endDate', None)

        if startDate and endDate is not None:
            startYear = startDate.strftime('%Y')
            startMonth = startDate.strftime('%B')
            endYear = endDate.strftime('%Y')
            endMonth = endDate.strftime('%B')

            if (startMonth == endMonth) and (startYear == endYear):
                return startDate.strftime('%d')
            elif (startMonth != endMonth) and (startYear == endYear):
                return startDate.strftime('%d %B')
            else:
                return startDate.strftime('%d %B %Y')
        return ''

    def endDate(self):
        endDate = getattr(self.context, 'endDate', None)
        if endDate is not None:
            return endDate.strftime('%d %B %Y')
        return ''
