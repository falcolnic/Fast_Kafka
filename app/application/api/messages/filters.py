from pydantic import BaseModel

from infra.repositories.filters.messages import GetMessagesFilters as GetMessageInfraFilters


class GetMessagesFilters(BaseModel):
    limit: int = 10
    offset: int = 0

    def to_infra(self):
        return GetMessageInfraFilters(limit=self.limit, offset=self.offset)
