from unittest.mock import Mock
import pytest

from src.customer_assistance.application.assistance_request_command_handler import AssistanceRequestCommandHandler
from src.customer_assistance.domain.assistance_repository import AssistanceRepository
from src.customer_assistance.domain.assistance import Assistance
from src.customer_assistance.domain.assistance_created_event import AssistanceCreatedEvent
from src.shared.domain.event.event_bus import EventBus

from tests.customer_assistance.domain.assistance_request_command_mother import AssistanceRequestCommandMother


class TestAssistanceRequestCommandHandler:
    def setup_method(self):
        self.assistance_repository = Mock(spec=AssistanceRepository)
        self.assistance_repository.exists.return_value = False
        self.event_bus = Mock(spec=EventBus)

        self.handler = AssistanceRequestCommandHandler(
            assistance_repository=self.assistance_repository,
            event_bus=self.event_bus
        )

    def test_handle_should_save_assistance(self):
        command = AssistanceRequestCommandMother.create()

        self.handler.handle(command)

        self.assistance_repository.save.assert_called_once()
        saved_assistance = self.assistance_repository.save.call_args[0][0]
        assert isinstance(saved_assistance, Assistance)
        primitives = saved_assistance.to_primitives()
        assert primitives['id'] == command.assistance_id
        assert primitives['topic'] == command.topic
        assert primitives['description'] == command.description

    def test_handle_should_publish_domain_events(self):
        command = AssistanceRequestCommandMother.create()

        self.handler.handle(command)

        self.event_bus.publish.assert_called_once()
        published_events = self.event_bus.publish.call_args[0][0]
        assert len(published_events) > 0
        assert any(isinstance(event, AssistanceCreatedEvent) for event in published_events)

    def test_handle_should_raise_value_error_when_id_already_exists(self):
        self.assistance_repository.exists.return_value = True
        command = AssistanceRequestCommandMother.create()
        
        with pytest.raises(
                ValueError,
                match=f"Assistance with id: '{command.assistance_id}' already exists"
        ):
            self.handler.handle(command)
        
        self.assistance_repository.save.assert_not_called()
        self.event_bus.publish.assert_not_called()
