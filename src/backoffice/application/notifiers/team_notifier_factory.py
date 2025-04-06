from src.backoffice.application.notifiers.team_notifier_base import TeamNotifierBase
from src.backoffice.domain.value_objects.team_notifier_method import TeamNotifierMethod


class TeamNotifierFactory:

    notifiers = {}

    @classmethod
    def register(cls, name):
        def inner_wrapper(wrapped_class: TeamNotifierBase) -> TeamNotifierBase:
            if not name in cls.notifiers:
                cls.notifiers[name] = wrapped_class
            return wrapped_class
        return inner_wrapper

    @classmethod
    def get_notifier(cls, method: TeamNotifierMethod):
        return cls.notifiers[method]
