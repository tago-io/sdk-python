import toml

with open("pyproject.toml") as f:
    pyproject = toml.load(f)
    __version__ = pyproject["tool"]["poetry"]["version"]

from .modules.Account.Account import Account
from .modules.Analysis.Analysis import Analysis
from .modules.Device.Device import Device
from .modules.Services.Services import Services
