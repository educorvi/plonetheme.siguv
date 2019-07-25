# -*- coding: utf-8 -*-
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from plonetheme.siguv import _
from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


NavigationStatusVocabulary = SimpleVocabulary(
    [SimpleTerm(value=u'enabled',
                title=_(u'siguv_settings_navigation_status_enabled',
                        default=u'Enabled')),
     SimpleTerm(value=u'disabled',
                title=_(u'siguv_settings_navigation_status_disabled',
                        default=u'Disabled')),
     SimpleTerm(value=u'collapsed',
                title=_(u'siguv_settings_navigation_status_collapsed',
                        default=u'Zugeklappt'))],
)


class ISettings(Interface):

    navigation_status = schema.Choice(
        title=_(
            u'controlpanel_siguv_settings_navigation_status_title',
            default='Navigation Status'),
        description=_(
            u'controlpanel_siguv_settings_navigation_status_description',
            default=(u'Select if the main navigation is enabled, disabled or always active.'),  # noqa: 501
        ),
        vocabulary=NavigationStatusVocabulary,
        default='enabled',
        required=True,
    )


class SettingsEditForm(RegistryEditForm):
    schema = ISettings
    schema_prefix = 'plonetheme.siguv'
    label = _(u'siguv_settigns_title', default=u'Siguv Settings')


ControlPanelView = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)
