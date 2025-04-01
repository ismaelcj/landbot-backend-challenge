from uuid import uuid4

from src.customer_assistance.domain.assistance import Assistance
from src.customer_assistance.domain.assistance_created_event import AssistanceCreatedEvent
from src.customer_assistance.domain.assistance_topic import AssistanceTopic
from src.shared.domain.value_object.custom_uuid import Uuid


class TestAssistance:
    def test_assistance_initialization(self):
        assistance_id = Uuid(str(uuid4()))
        topic = AssistanceTopic.SALES
        description = "Customer needs help with sales"

        assistance = Assistance(assistance_id, topic, description)

        assert assistance._id == assistance_id
        assert assistance._topic == topic
        assert assistance._description == description
        assert len(assistance._domain_events) == 0

    def test_assistance_create_factory_method(self):
        assistance_id = Uuid(str(uuid4()))
        topic = AssistanceTopic.PRICING
        description = "Customer has pricing questions"

        assistance = Assistance.create(assistance_id, topic, description)

        assert assistance._id == assistance_id
        assert assistance._topic == topic
        assert assistance._description == description
        
        domain_events = assistance.pull_domain_events()
        assert len(domain_events) == 1
        
        event = domain_events[0]
        assert isinstance(event, AssistanceCreatedEvent)
        assert event.aggregate_id == assistance_id.value
        assert event.topic == topic.value
        assert event.description == description
        assert event.event_name() == "landbot.customer_assistance.assistance.created"

    def test_assistance_domain_events_are_cleared_after_pulling(self):
        assistance_id = Uuid(str(uuid4()))
        topic = AssistanceTopic.SALES
        description = "Customer needs help with sales"
        assistance = Assistance.create(assistance_id, topic, description)
        
        first_pull = assistance.pull_domain_events()
        second_pull = assistance.pull_domain_events()
        
        assert len(first_pull) == 1
        assert len(second_pull) == 0 
