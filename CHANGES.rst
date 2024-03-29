Changes
=======

4.1 (unreleased)
----------------

- Nothing changed yet.


4.0 (2023-08-28)
----------------

* Add support for Python 3.7, 3.8, 3.9, 3.10, 3.11.

* Drop support for Python 2.7, 3.4, 3.5, 3.6.


3.1.0 (2018-02-05)
------------------

* viewletmanager.viewlets should be a list so we can iterate over it several
  times in consumer code instead of having to remember it's an iterable we can
  only list once.

3.0.1 (2018-01-12)
------------------

* Rearrange tests such that Travis CI can pick up all functional tests too.

3.0.0 (2018-01-04)
------------------

* Python 3 compatibility.

1.11 (2012-09-04)
-----------------

* Make the ``has_render()`` and ``has_no_render()`` symmetrical to those
  in grokcore.view, grokcore.layout and grokcore.formlib, where a
  ``render.base_method`` attribute is checked.

1.10.1 (2012-05-02)
-------------------

* Do not require the role extra from grokcore.security.

1.10 (2012-05-02)
-----------------

* Use the component registration api from grokcore.component.

* Update how the static resources are found on a ``ViewletManager``
  and a ``Viewlet``, following the new name ``__static_name__`` set by
  the template association.

1.9 (2011-06-28)
----------------

* Introduce the `available()` method on viewlet component. The viewlet
  manager will filter out unavailable viewlet by calling this method. The
  `available()` method is called *after* the viewlet's `update()` is called,
  but *before* the `render()` is called.

1.8 (2010-12-16)
----------------

* Update to use TemplateGrokker from grokcore.view to associate
  viewlet and viewletmanager templates.

1.7 (2010-11-03)
----------------

* The computed default value for the viewletmanager directive is now defined
  in the directiv itself, not as a separate function that needs to be passed
  along.

1.6 (2010-11-01)
----------------

* Upped version requirements for martian, grokcore.component, and grokcore.view.

* Move the order directive to grokcore.component.

* Move the view directive to grokcore.view.

1.5 (2010-10-18)
----------------

* Make package comply to zope.org repository policy.

* Update functional tests to use Browser implementation of zope.app.wsgi
  instead of zope.app.testing.

* Reduce dependencies (zope.app.pagetemplate no longer necessary).

1.4.1 (2010-02-28)
------------------

* Dropped the dependency on ``zope.app.zcmlfiles``.

* Cleaned the code to remove unused imports and ensure the pep8 syntax.

* Updated tests to have a return value consistency. The
  grokcore.viewlet viewlet manager implementation requires viewlets to
  return unicode strings. Now, viewlets return unicode strings in the
  test packages.

1.4 (2010-02-19)
----------------

* Define test requires.

1.3 (2009-09-17)
----------------

* Reverted the use of grokcore.view.CodeView. We now require
  ``grokcore.view`` 1.12.1 or newer. As of ``grokcore.view`` 1.12, the
  CodeView/View separation has been undone.

1.2 (2009-09-16)
----------------

* Remove the reference to the grok.View permission that is no longer in
  grokcore.security 1.2

* Use the grok.zope.org/releaseinfo information instead of our own
  copy of ``versions.cfg``, for easier maintenance.


1.1 (2009-07-20)
----------------

* Adapted tests to new grokcore.view release: switched from View to CodeView.

* Add grok.View permissions to functional tests (requires grokcore.security
  1.1)

1.0 (2008-11-15)
----------------

* Created ``grokcore.viewlet`` in November 2008 by factoring
  ``zope.viewlet``-based components, grokkers and directives out of
  Grok.
