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
from Acquisition import aq_inner
from collective.contentleadimage.config import IMAGE_FIELD_NAME

from DateTime import DateTime

class ICurrentPrayerCycle(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    pass

class Assignment(base.Assignment):
    implements(ICurrentPrayerCycle)

    @property
    def title(self):
        return _('Current Prayer Cycle')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/currentprayercycle.pt')

    @property
    def available(self):
        return True if self.prayercycle() else False

    def prayercycle(self):
        # get current prayer cycle for date and context
        today = DateTime()
        brains = self.context.portal_catalog(startDate={
            'query': [today],
            'range': 'max'
        }, endDate={
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
        endDate = getattr(prayercycle, 'startDate', None)
        if endDate is not None:
            return endDate.strftime('%d %B %Y')
        return ''


class AddForm(base.NullAddForm):
    form_fields = form.Fields(ICurrentPrayerCycle)
    label = _(u"Add Current Prayer Cycle")
    description = _(u"")

    def create(self):
        return Assignment()
