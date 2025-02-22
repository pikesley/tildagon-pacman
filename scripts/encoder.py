from pathlib import Path

import yaml


def run_length_encode(data):
    """RLE a list."""
    result = []
    count = 0
    step = 0

    while step < len(data) - 1:
        current = data[step]
        step += 1
        nxt = data[step]

        if nxt == current:
            count += 1
        else:
            result.append({current: count + 1})
            count = 0
            current = nxt

    result.append({current: count + 1})

    return result


ghosts = yaml.safe_load(Path("conf/ghost.yaml").read_text())

encoded_ghosts = {}
encoded_ghosts["core"] = [run_length_encode(line) for line in ghosts["core"]]

encoded_ghosts["feet"] = {}
for item in ["out", "in"]:
    encoded_ghosts["feet"][item] = [
        run_length_encode(line) for line in ghosts["feet"][item]
    ]

encoded_ghosts["eyes"] = {}
for item in ["up", "down", "left", "right"]:
    encoded_ghosts["eyes"][item] = [
        run_length_encode(line) for line in ghosts["eyes"][item]
    ]

encoded_ghosts["dead-face"] = [run_length_encode(line) for line in ghosts["dead-face"]]

Path("conf/rle-ghost.yaml").write_text(yaml.dump(encoded_ghosts))

pac = yaml.safe_load(Path("conf/pacman.yaml").read_text())

encoded_pac = {}

encoded_pac["closed"] = [run_length_encode(line) for line in pac["closed"]]


for face in ["left", "right", "up", "down"]:
    encoded_pac[face] = {}
    for shape in ["wide", "narrow"]:
        encoded_pac[face][shape] = [
            run_length_encode(line) for line in pac[face][shape]
        ]

Path("conf/rle-pacman.yaml").write_text(yaml.dump(encoded_pac))
