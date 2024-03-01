from typing import Any
from enum import Enum
from dataclasses import dataclass, asdict


class TemplateAttributeField(Enum):
    UI_VISIBLE = "ui_visible"
    API_VISIBLE = "api_visible"


@dataclass
class TemplateAttributes:
    ui_visible: bool = False
    api_visible: bool = False

    def dict(self) -> dict[str, Any]:
        return asdict(self)