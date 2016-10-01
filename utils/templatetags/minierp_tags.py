from django import template
from import_export.admin import ImportMixin, ExportMixin
register = template.Library()

@register.simple_tag(name='has_export_feature', takes_context=True)
def has_export_feature(context):
	obj = context['cl']
	issubclass(obj, ExportMixin)
	return True

@register.simple_tag(name='has_import_feature', takes_context=True)
def has_import_feature(value, context):
	issubclass(value, ImportMixin)
	return True
