from template_attributes import TemplateAttributeField
from template_utils import TemplateUtils

def api_visible_decorator(func):

    def wrapper(*args, **kwargs):

        processed_dataclasses = TemplateUtils.repr(
            dataclazzes=kwargs.get("dataclazzes"),
            repr_type=TemplateAttributeField.API_VISIBLE
        )

        kwargs["dataclazzes"] = processed_dataclasses

        func(*args, **kwargs)

    return wrapper



def ui_visible_decorator(func):
    def wrapper(*args, **kwargs):

        processed_dataclasses = TemplateUtils.repr(
            dataclazzes=kwargs.get("dataclazzes"),
            repr_type=TemplateAttributeField.UI_VISIBLE
        )

        kwargs["dataclazzes"] = processed_dataclasses

        func(*args, **kwargs)

    return wrapper
