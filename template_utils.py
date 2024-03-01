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


