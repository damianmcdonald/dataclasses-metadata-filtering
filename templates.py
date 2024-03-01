from dataclasses import dataclass, field

from template_attributes import TemplateAttributes

@dataclass
class ComputeTemplate:

    instance_type: str = field(
        metadata=TemplateAttributes(
            api_visible=True
        ).dict()
    )

    instance_count: int = field(
        metadata=TemplateAttributes(
            ui_visible=True,
            api_visible=True
        ).dict()
    )

    instance_secret: str = field(
        metadata=TemplateAttributes().dict()
    )


@dataclass
class ApplicationTemplate:

    version: str = field(
        metadata=TemplateAttributes(
            ui_visible=True,
            api_visible=True
        ).dict()
    )

    precision: str = field(
        metadata=TemplateAttributes(
            ui_visible=True,
            api_visible=False
        ).dict()
    )

    secret: str = field(
        metadata=TemplateAttributes().dict()
    )


