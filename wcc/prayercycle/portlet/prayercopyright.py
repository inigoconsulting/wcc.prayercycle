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
from wcc.prayercycle.content.prayercycle import IPrayerCycle

class IPrayerCopyright(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    pass

class Assignment(base.Assignment):
    implements(IPrayerCopyright)

    @property
    def title(self):
        return _('Prayer Copyright')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/prayercopyright.pt')

    @property
    def available(self):
        return IPrayerCycle.providedBy(self.context)

class AddForm(base.NullAddForm):
    form_fields = form.Fields(IPrayerCopyright)
    label = _(u"Add Prayer Copyright")
    description = _(u"")

    def create(self):
        return Assignment()
