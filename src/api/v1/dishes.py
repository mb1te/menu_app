from typing import Annotated

from fastapi import APIRouter, status
from fastapi.params import Depends

from src.api.dependencies import DishRepo, get_dish_repo
from src.dto.dish import DishBaseDTO, DishGetDTO

router = APIRouter(tags=["dishes"])
Repo = Annotated[DishRepo, Depends(get_dish_repo)]


@router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes")
async def get_dishes(submenu_id: str, repo: Repo) -> list[DishGetDTO]:
    return await repo.get_all(submenu_id=submenu_id)


@router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
async def get_dish_item(dish_id: str, repo: Repo) -> DishGetDTO:
    return await repo.get(item_id=dish_id)


@router.post(
    "/menus/{menu_id}/submenus/{submenu_id}/dishes", status_code=status.HTTP_201_CREATED
)
async def create_dish_item(
    submenu_id: str, dish: DishBaseDTO, repo: Repo
) -> DishGetDTO:
    item = await repo.create(submenu_id=submenu_id, **dish.model_dump())
    await repo.commit()
    return item


@router.patch("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
async def change_dish_item(dish_id: str, dish: DishBaseDTO, repo: Repo) -> DishGetDTO:
    item = await repo.update(item_id=dish_id, **dish.model_dump())
    await repo.commit()
    return item


@router.delete("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
async def delete_dish_item(dish_id: str, repo: Repo):
    await repo.delete(item_id=dish_id)
    await repo.commit()
