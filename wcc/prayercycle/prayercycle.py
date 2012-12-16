from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid, Interface

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from wcc.prayercycle import MessageFactory as _


# Interface class; used to define content-type schema.

class IPrayerCycle(form.Schema, IImageScaleTraversable):
    """
    Prayer cycle
    """

    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/prayercycle.xml to define the content type
    # and add directives here as necessary.

    form.model("models/prayercycle.xml")


# View class
# The view will automatically use a similarly named template in
# prayercycle_templates.
# Template filenames should be all lower case.


class IPrayerCycleProvider(Interface):
    pass

class PrayerCycleProvider(grok.Adapter):
    grok.implements(IPrayerCycleProvider)
    grok.context(IPrayerCycle)

    def __init__(self, context):
        self.context = context

    def startDate(self):
        return getattr(self.context, 'startDate', None)

    def endDate(self):
        return getattr(self.context, 'endDate', None)

class Index(dexterity.DisplayForm):
    grok.context(IPrayerCycle)
    grok.require('zope2.View')
    grok.name('view')

    def provider(self):
        return IPrayerCycleProvider(self.context)

    def startDate(self):
        startDate = self.provider().startDate()
        if startDate is not None:
            return startDate.strftime('%d %B %Y')
        return ''

    def endDate(self):
        endDate = self.provider().endDate()
        if endDate is not None:
            return endDate.strftime('%d %B %Y')
        return ''       
