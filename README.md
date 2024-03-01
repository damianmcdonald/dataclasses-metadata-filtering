# Dataclasses field metadata for filtering

Demo project that demonstrates how the `metadata` attribute of [Python Dataclasses Field](https://docs.python.org/3/library/dataclasses.html) can be leveraged to provide class level attribute behaviour such as representation filtering.

A `TemplateAttributes` dataclass defines the field metadata.

```python
from typing import Any
from dataclasses import dataclass, asdict


@dataclass
class TemplateAttributes:
    ui_visible: bool = False
    api_visible: bool = False

    def dict(self) -> dict[str, Any]:
        return asdict(self)
```

This `TemplateAttributes` dataclass is then used as the `metadata` attribute of the specific _Template_ dataclasses fields.

```python
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
```

Finally, these _Template_ dataclasses can be passed to a utility function which interprets the field metadata and filters out fields whose metadata is marked as not visible.

```python
import dataclasses
from dataclasses import dataclass
from typing import Any

from template_attributes import TemplateAttributeField


class TemplateUtils:

    @staticmethod
    def repr(
            dataclazzes: list[dataclass],
            repr_type: TemplateAttributeField
        ) -> list[dict[str, Any]]:
        
        results = []

        for dataclazz in dataclazzes:

            fields = dataclasses.fields(dataclazz)

            allowed_fields = {}

            for field in fields:

                metadata = field.metadata

                if metadata.get(repr_type.value, False) == True:

                    allowed_fields[field.name] = getattr(dataclazz, field.name)

            if allowed_fields:

                results.append(allowed_fields)

        return results
```

A `runner.py` is provided which shows the usage and execution results of dataclasses field metadata filtering.

```bash
python3 runner.py 

Tests

#################################

Instantiate templates with template attributes

ComputeTemplate(instance_type='c24.xlarge', instance_count=6, instance_secret='You should not see me!')

ApplicationTemplate(version='2023.6', precision='DOUBLE', secret='You should not see me!')

Apply representations

API Visible

[
    {
        "instance_type": "c24.xlarge",
        "instance_count": 6
    },
    {
        "version": "2023.6"
    }
]

UI Visible

[
    {
        "instance_count": 6
    },
    {
        "version": "2023.6",
        "precision": "DOUBLE"
    }
]
```
