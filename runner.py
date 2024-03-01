import json

from template_attributes import TemplateAttributes, TemplateAttributeField
from templates import ComputeTemplate, ApplicationTemplate
from template_utils import TemplateUtils


print("")
print("Tests")
print("")
print("#################################")
print("")

test_template_attributes = TemplateAttributes(
    ui_visible=False,
    api_visible=True
)

print("Instantiate templates with template attributes")
print("")

test_compute_template = ComputeTemplate(
    instance_type="c24.xlarge",
    instance_count=6,
    instance_secret="You should not see me!"
)

print(test_compute_template)
print("")

test_application_template = ApplicationTemplate(
    version="2023.6",
    precision="DOUBLE",
    secret="You should not see me!"
)

print(test_application_template)
print("")

print("Apply representations")
print("")

print("API Visible")
print("")

print(
    json.dumps(
        TemplateUtils.repr(
            dataclazzes=[
                test_compute_template,
                test_application_template
            ],
            repr_type=TemplateAttributeField.API_VISIBLE
        ),
        indent=4
    )
)

print("")
print("UI Visible")
print("")

print(
    json.dumps(
        TemplateUtils.repr(
            dataclazzes=[
                test_compute_template,
                test_application_template
            ],
            repr_type=TemplateAttributeField.UI_VISIBLE
        ),
        indent=4
    )
)