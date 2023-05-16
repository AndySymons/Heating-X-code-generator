import pathlib
import uuid
from typing import Any

import jinja2
import yaml

TEMPLATE_DIR = pathlib.Path('templates')
OUTPUT_DIR = pathlib.Path('output')


def read_config() -> dict[str, Any]:
    """Read the configuration file."""
    with open('config.yaml') as f:
        return yaml.safe_load(f)


def read_templates() -> jinja2.Environment:
    """Read the templates."""
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates'),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def generate_uuid() -> uuid.UUID:
    """Generate a UUID."""
    return uuid.uuid4()


def generate() -> None:
    """Generate the files."""
    config = read_config()
    templates = read_templates()
    templates.globals.update(generate_uuid=generate_uuid)

    for template in templates.list_templates():
        template = templates.get_template(template)
        output = (OUTPUT_DIR / template.name).with_suffix('')
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(template.render(config=config))


if __name__ == '__main__':
    generate()
