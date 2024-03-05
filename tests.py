from infini.loader import Loader
from infini.input import Input
from ipm import api
from ipm.models.ipk import InfiniProject

ipk = InfiniProject()
api.build(".")
api.install(f"dist/{ipk.default_name}", force=True)

loader = Loader()
loader.load("ndice")
loader.close()

commands = [
    ".r",
    ".rd",
    ".rd6",
    ".r3d6",
    ".r3d6*5",
    ".r20#d6",
    ".r3d6 毁灭人类",
    ".r20#3d6 毁灭人类",
]

core = loader.into_core()

for command in commands:
    for output in core.input(Input(command)):
        print(output)
