from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from infra.integrations.notifications.dots import Notification


@dataclass
class BaseNotificationClient(ABC):

    @abstractmethod
    def send_message(self, Notification: Notification):
        ...
