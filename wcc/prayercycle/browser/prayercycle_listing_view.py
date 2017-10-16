from five import grok
from Products.ATContentTypes.interfaces.topic import IATTopic
from plone.app.collection.interfaces import ICollection

grok.templatedir('templates')


class PrayerCycleListingCollectionView(grok.View):
    grok.context(ICollection)
    grok.name('prayercycle_listing_view')
    grok.template('prayercycle_listing_view')
    
    pass
    