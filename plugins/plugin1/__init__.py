from mixin import PluginMixin

class Plugin(PluginMixin):
    class Meta:
        name = "Plugin1"


class NotPluginClass:
    pass
