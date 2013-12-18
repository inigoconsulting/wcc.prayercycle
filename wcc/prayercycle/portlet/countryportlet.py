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
from plone.api.portal import get_tool

class ICountryportlet(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    pass

class Assignment(base.Assignment):
    implements(ICountryportlet)

    @property
    def title(self):
        return _('Country portlet')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/countryportlet.pt')

    @property
    def available(self):
        return True

    def get_country(self, value):
        catalog = get_tool(name='portal_catalog')
        country =  catalog(portal_type="wcc.churches.country", countries=value)
        if country:
            return country[0]


class AddForm(base.NullAddForm):
    form_fields = form.Fields(ICountryportlet)
    label = _(u"Add Country portlet")
    description = _(u"")

    def create(self):
        return Assignment()
