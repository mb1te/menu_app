from pydantic import UUID4, BaseModel, ConfigDict


class MenuBaseDTO(BaseModel):
    title: str
    description: str


class MenuGetDTO(MenuBaseDTO):
    model_config = ConfigDict(from_attributes=True)
    id: UUID4


class MenuGetExtDTO(MenuGetDTO):
    submenus_count: int
    dishes_count: int
