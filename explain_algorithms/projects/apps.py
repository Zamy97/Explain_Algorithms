from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    name = "explain_algorithms.projects"

    verbose_name = "projects"

    def ready(self):
        try:
            # noinspection PyUnresolvedReferences
            from . import signals  # noqa F401
        except ImportError:
            pass
