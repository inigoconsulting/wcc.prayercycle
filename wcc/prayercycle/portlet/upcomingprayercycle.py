from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from wcc.prayercycle import MessageFactory as _
from DateTime import DateTime 

class IUpcomingPrayerCycle(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    pass

class Assignment(base.Assignment):
    implements(IUpcomingPrayerCycle)

    @property
    def title(self):
        return _('Upcoming Prayer Cycle')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/upcomingprayercycle.pt')

    @property
    def available(self):
        return True if self.prayercycle() else False

    def prayercycle(self):
        # get current prayer cycle for date and context
        today = DateTime()
        brains = self.context.portal_catalog(start={
            'query': [today],
            'range': 'min'
        },
        portal_type='wcc.prayercycle.prayercycle',
        sort_on='start', sort_order='ascending')

        if brains:
            prayercycle = brains[0].getObject()
            if (prayercycle.startDate.year,
                prayercycle.startDate.month,
                prayercycle.startDate.day) != (
                today.year(),
                today.month(),
                today.day()):
                    return prayercycle
            else:
                if len(brains) >= 2:
                    return brains[2].getObject()
                
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


class AddForm(base.NullAddForm):
    form_fields = form.Fields(IUpcomingPrayerCycle)
    label = _(u"Add Upcoming Prayer Cycle Portlet")
    description = _(u"Display upcoming prayer cycle")

    def create(self):
        return Assignment()
