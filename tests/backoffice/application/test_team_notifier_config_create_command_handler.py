from unittest.mock import Mock

import pytest

from src.backoffice.application.commands.team_notifier_config_create_command_handler import \
    TeamNotifierConfigCreateCommandHandler
from src.backoffice.domain.team_notifier_config import TeamNotifierConfig
from src.backoffice.domain.team_notifier_config_repository import TeamNotifierConfigRepository
from src.shared.domain.event.event_bus import EventBus
from tests.backoffice.domain.team_notifier_config_create_command_mother import TeamNotifierConfigCreateCommandMother


class TestTeamNotifierConfigCreateCommandHandler:
    def setup_method(self):
        self.config_repository = Mock(spec=TeamNotifierConfigRepository)
        self.config_repository.exists.return_value = False
        self.event_bus = Mock(espc=EventBus)

        self.handler = TeamNotifierConfigCreateCommandHandler(
            config_repository=self.config_repository,
            event_bus=self.event_bus
        )

    def test_handle_should_save_config(self):
        command = TeamNotifierConfigCreateCommandMother.create()

        self.handler.handle(command)

        self.config_repository.save.assert_called_once()
        saved_config = self.config_repository.save.call_args[0][0]
        assert isinstance(saved_config, TeamNotifierConfig)
        primitives = saved_config.to_primitives()
        assert primitives["topic"] == command.topic
        assert primitives["method"] == command.method
        assert primitives["destination"] == command.destination

    def test_handle_should_raise_value_error_when_topic_already_exists(self):
        self.config_repository.exists.return_value = True
        command = TeamNotifierConfigCreateCommandMother.create()

        with pytest.raises(
                ValueError,
                match=f"TeamNotifierConfig with topic '{command.topic}' already exists"
        ):
            self.handler.handle(command)

        self.config_repository.save.assert_not_called()
        
    def test_handle_should_check_if_topic_exists(self):
        command = TeamNotifierConfigCreateCommandMother.create()

        self.handler.handle(command)

        self.config_repository.exists.assert_called_once_with(command.topic)
