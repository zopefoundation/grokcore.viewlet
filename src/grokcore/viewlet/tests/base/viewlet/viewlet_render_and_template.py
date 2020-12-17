"""
A viewlet is not allowed to define its own render method and have a template
associated with it at the same time.

  # PY2 - remove '+IGNORE_EXCEPTION_DETAIL'  when dropping Python 2 support:
  >>> grok.testing.grok(__name__)  # doctest: +IGNORE_EXCEPTION_DETAIL
  Traceback (most recent call last):
    ...
  zope.configuration.config.ConfigurationExecutionError: \
  martian.error.GrokError: Multiple possible ways to render viewlet \
  <class \
  'grokcore.viewlet.tests.base.viewlet.viewlet_render_and_template.Viewlet'>. \
  It has both a 'render' method as well as an associated template.

"""

import grokcore.viewlet as grok
from zope.interface import Interface


class ViewletManager(grok.ViewletManager):
    grok.name('foo')
    grok.context(Interface)


class Viewlet(grok.Viewlet):
    grok.viewletmanager(ViewletManager)
    grok.context(Interface)

    def render(self):
        return u"Render method but also a template!"
