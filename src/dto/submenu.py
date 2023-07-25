from pydantic import UUID4, BaseModel, ConfigDict


class SubmenuBaseDTO(BaseModel):
    title: str
    description: str


class SubmenuGetDTO(SubmenuBaseDTO):
    model_config = ConfigDict(from_attributes=True)
    id: UUID4


class SubmenuGetExtDTO(SubmenuGetDTO):
    dishes_count: int
