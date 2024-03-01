import json
from dataclasses import dataclass

from template_attributes import TemplateAttributes
from templates import ComputeTemplate, ApplicationTemplate
from template_decorators import api_visible_decorator, ui_visible_decorator


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


@api_visible_decorator
def print_api(dataclazzes: list[dataclass]):
    print(json.dumps(dataclazzes, indent=4))


print_api(
    dataclazzes=[
        test_compute_template,
        test_application_template
    ]
)


print("")
print("UI Visible")
print("")

@ui_visible_decorator
def print_ui(dataclazzes: list[dataclass]):
    print(json.dumps(dataclazzes, indent=4))


print_ui(
    dataclazzes=[
        test_compute_template,
        test_application_template
    ]
)