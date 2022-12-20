"""
We check here that specifying grok.view() on module level works.
grok.view() on module level will make the viewlet manager be
associated with the CaveView, so nothing is found for BoneView
and an error should occur.

Set up a content object in the application root::

  >>> root = getRootFolder()
  >>> root['fred'] = Fred()

Traverse to the view on the model object. We get the viewlets
registered for the default layer, with the anybody permission::

  >>> from zope.testbrowser.wsgi import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/fred/@@boneview")
  Traceback (most recent call last):
  ...
  zope.contentprovider.interfaces.ContentProviderLookupError: cave

"""

import grokcore.viewlet as grok


class Fred(grok.Context):
    pass


class CaveView(grok.View):
    def render(self):
        return "Cave"


class BoneView(grok.View):
    pass


grok.view(CaveView)


class CaveManager(grok.ViewletManager):
    grok.name('cave')
