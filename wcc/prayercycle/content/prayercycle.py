from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from wcc.prayercycle import MessageFactory as _
from plone.multilingualbehavior.directives import languageindependent

# Interface class; used to define content-type schema.

class IPrayerCycle(form.Schema, IImageScaleTraversable):
    """
    Prayer cycle content type
    """

    languageindependent('startDate')
    startDate = schema.Datetime(
        title=_(u"Start Date"),
        description=u'',
        required=True,
    )

    languageindependent('startDate')
    endDate = schema.Datetime(
        title=_(u"End Date"),
        description=u'',
        required=True,
    )
