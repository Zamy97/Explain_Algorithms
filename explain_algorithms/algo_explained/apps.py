from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AlgoExplainedConfig(AppConfig):
    name = "explain_algorithms.algo_explained"

    verbose_name = "Explain_Algo"

    def ready(self):
        try:
            # noinspection PyUnresolvedReferences
            from . import signals  # noqa F401
        except ImportError:
            pass
