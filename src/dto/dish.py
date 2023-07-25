from pydantic import UUID4, BaseModel, ConfigDict


class DishBaseDTO(BaseModel):
    title: str
    description: str
    price: str


class DishGetDTO(DishBaseDTO):
    model_config = ConfigDict(from_attributes=True)
    id: UUID4
