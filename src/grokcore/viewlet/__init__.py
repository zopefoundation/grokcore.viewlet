##############################################################################
#
# Copyright (c) 2006-2007 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Grok
"""
from zope.interface import implements
from zope.component import adapts

from martian import ClassGrokker, InstanceGrokker, GlobalGrokker
from martian import baseclass
from martian.error import GrokError, GrokImportError

from grokcore.component import Adapter, MultiAdapter, GlobalUtility, Context
from grokcore.component.decorators import subscribe, adapter, implementer
from grokcore.component.directive import (
    context, name, title, description, provides, global_utility, direct)

from grokcore.security import Permission
from grokcore.security import Public
from grokcore.security import require

from grokcore.view import PageTemplate
from grokcore.view import PageTemplateFile
from grokcore.view import DirectoryResource
from grokcore.view import layer
from grokcore.view import template
from grokcore.view import templatedir
from grokcore.view import skin
from grokcore.view import url
from grokcore.view import path

from grokcore.formlib import action
from grokcore.formlib import AutoFields
from grokcore.formlib import Fields

from zope.event import notify
from zope.app.component.hooks import getSite
from zope.lifecycleevent import (
    IObjectCreatedEvent, ObjectCreatedEvent,
    IObjectModifiedEvent, ObjectModifiedEvent,
    IObjectCopiedEvent, ObjectCopiedEvent)

from zope.publisher.interfaces.browser import IBrowserRequest
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from zope.app.container.contained import (
    IObjectAddedEvent, ObjectAddedEvent,
    IObjectMovedEvent, ObjectMovedEvent,
    IObjectRemovedEvent, ObjectRemovedEvent,
    IContainerModifiedEvent, ContainerModifiedEvent)

from grok.components import Model, View
from grok.components import XMLRPC, REST, JSON
from grok.components import Traverser
from grok.components import Container, OrderedContainer
from grok.components import Site, LocalUtility, Annotation
from grok.components import Application, Form, AddForm, EditForm, DisplayForm
from grok.components import Indexes
from grok.components import Role
from grok.components import RESTProtocol, IRESTLayer
from grok.interfaces import IRESTSkinType
from grok.components import ViewletManager, Viewlet

from grok.directive import (local_utility, permissions, site,
                            viewletmanager, view, traversable, order)



# BBB These two functions are meant for test fixtures and should be
# imported from grok.testing, not from grok.
from grok.testing import grok, grok_component

# Our __init__ provides the grok API directly so using 'import grok' is enough.
from grok.interfaces import IGrokAPI
from zope.interface import moduleProvides
moduleProvides(IGrokAPI)
__all__ = list(IGrokAPI)