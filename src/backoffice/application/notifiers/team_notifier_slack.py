from pprint import pprint

from src.backoffice.application.notifiers.team_notifier_base import TeamNotifierBase
from src.backoffice.application.notifiers.team_notifier_factory import TeamNotifierFactory
from src.backoffice.domain.value_objects.team_notifier_method import TeamNotifierMethod


@TeamNotifierFactory.register(TeamNotifierMethod.SLACK.value)
class TeamNotifierSlack(TeamNotifierBase):
    def notify(self):
        pprint("TeamNotifierSlack.notify")
