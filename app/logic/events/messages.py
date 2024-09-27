from dataclasses import dataclass

from domain.events.message import NewChatCreatedEvent
from infra.message_brokers.converters import convert_event_to_broker_message
from logic.events.base import EventHandler


@dataclass
class NewChatCreatedEventHandler(EventHandler[NewChatCreatedEvent, None]):
    async def handle(self, event: NewChatCreatedEvent) -> None:
        value=convert_event_to_broker_message(event=event)
        await self.message_broker.send_message(
            topic=self.broker_topic,
            value=value,
            key=str(event.event_id).encode(),
        )
        print(f"Processed event {event.title}")