# https://tildagon.badge.emfcamp.org/tildagon-apps/reference/ctx/#adding-images
import os
import platform

if "MicroPython" not in platform.platform():
    ASSET_PATH = f"{os.getcwd()}/"  # noqa: PTH109

else:
    apps = os.listdir("/apps")
    path = ""
    ASSET_PATH = "apps/"

    if "pikesley_tildagon_pacman" in apps:
        ASSET_PATH = "/apps/pikesley_tildagon_pacman/"

    if "pacman" in apps:
        ASSET_PATH = "apps/pacman/"
