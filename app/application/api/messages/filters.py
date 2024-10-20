from pydantic import BaseModel

from infra.repositories.filters.messages import (
    GetAllChatsFilters as GetAllChatsInfraFilters,
    GetMessagesFilters as GetMessageInfraFilters,
)


class GetMessagesFilters(BaseModel):
    limit: int = 10
    offset: int = 0

    def to_infra(self):
        return GetMessageInfraFilters(limit=self.limit, offset=self.offset)


class GetAllChatsFilters(BaseModel):
    limit: int = 10
    offset: int = 0

    def to_infra(self):
        return GetAllChatsInfraFilters(limit=self.limit, offset=self.offset)
