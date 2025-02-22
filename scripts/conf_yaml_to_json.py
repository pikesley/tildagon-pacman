import json
from pathlib import Path

import yaml

sources = [
    "conf",
    "conf/ghost",
    "conf/pacman",
]

for item in sources:
    try:
        source = yaml.safe_load(Path(f"{item}.yaml").read_text(encoding="utf-8"))
        Path(f"{item}.json").write_text(json.dumps(source, indent=2))

    except FileNotFoundError:
        pass
