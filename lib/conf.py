import json

from .asset_path import ASSET_PATH

with open(ASSET_PATH + "conf.json") as j:  # noqa: PTH123
    conf = json.loads(j.read())

sprite_data = {}
for sprite in ["pacman", "ghost"]:
    with open(ASSET_PATH + f"conf/{sprite}.json") as j:  # noqa: PTH123
        sprite_data[sprite] = json.loads(j.read())
