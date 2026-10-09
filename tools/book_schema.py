"""A small validator for the subset of JSON Schema that book.schema.json uses (no third-party library is needed).

Supported: type (string, integer, number, boolean, object, array, null, or a list of them), required, properties,
additionalProperties (boolean), items, enum, minItems. A mismatch returns a list of paths and reasons; an empty list is valid.
"""

TYPES = {"string": str, "integer": int, "number": (int, float), "boolean": bool, "object": dict, "array": list, "null": type(None)}


def _is(value, name):
    if name == "integer" and isinstance(value, bool):
        return False
    if name == "number" and isinstance(value, bool):
        return False
    return isinstance(value, TYPES[name])


def validate(value, schema, path="$"):
    errors = []
    t = schema.get("type")
    if t is not None:
        names = t if isinstance(t, list) else [t]
        if not any(_is(value, n) for n in names):
            return [f"{path}: expected {'/'.join(names)}, found {type(value).__name__}"]
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} is not one of {schema['enum']}")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing '{key}'")
        props = schema.get("properties", {})
        for key, sub in props.items():
            if key in value:
                errors += validate(value[key], sub, f"{path}.{key}")
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    errors.append(f"{path}: unexpected '{key}'")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: fewer than {schema['minItems']} items")
        if "items" in schema:
            for i, item in enumerate(value):
                errors += validate(item, schema["items"], f"{path}[{i}]")
    return errors
