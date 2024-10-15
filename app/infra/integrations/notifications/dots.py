from dataclasses import dataclass


@dataclass(frozen=True)
class Notification:
    # TODO UserID
    title: str
    text: str
