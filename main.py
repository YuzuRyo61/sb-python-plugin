import sys
import os
import inspect
import importlib
import glob

sys.path.append(os.path.join(os.path.dirname(__file__), 'plugins'))
sys.path.append(os.path.join(os.path.dirname(__file__)))

from mixin import PluginMixin


if __name__ == "__main__":
    plugin_dir = glob.glob('plugins/**/*.py')
    plugin_mod = []
    for pd in plugin_dir:
        mod_imported = importlib.import_module(pd.replace('.py', '').replace('/', '.').replace('\\', '.'))
        for _, mod in inspect.getmembers(mod_imported, inspect.isclass):
            if issubclass(mod, PluginMixin) and not mod == PluginMixin:
                plugin_mod.append(mod)

    for pm in plugin_mod:
        print(pm.Meta.name)
