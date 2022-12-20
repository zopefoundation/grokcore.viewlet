"""
When there are two or more viewletmanagers available in the module,
a viewlet will not auto-associate but instead raise an error.

  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
    ...
  martian.error.GrokError: Multiple possible viewletmanagers for \
  <class 'grokcore.viewlet.tests.base.viewlet.viewlet_ambiguous_manager.Viewlet'>, \
  please use the 'viewletmanager' directive.

"""  # noqa: E501 line too long

from zope.interface import Interface

import grokcore.viewlet as grok


class ViewletManager(grok.ViewletManager):
    grok.name('foo')
    grok.context(Interface)


class ViewletManager2(grok.ViewletManager):
    grok.name('bar')
    grok.context(Interface)


class Viewlet(grok.Viewlet):
    grok.context(Interface)

    def render(self):
        return "Render method"
