from typing import Annotated

from fastapi import APIRouter, status
from fastapi.params import Depends

from src.api.dependencies import MenuRepo, get_menu_repo
from src.dto.menu import MenuBaseDTO, MenuGetDTO, MenuGetExtDTO

router = APIRouter(tags=["menus"])
Repo = Annotated[MenuRepo, Depends(get_menu_repo)]


@router.get("/menus")
async def get_menus(repo: Repo) -> list[MenuGetExtDTO]:
    return await repo.get_all()


@router.get("/menus/{menu_id}")
async def get_menu_item(menu_id: str, repo: Repo) -> MenuGetExtDTO:
    return await repo.get(item_id=menu_id)


@router.post("/menus", status_code=status.HTTP_201_CREATED)
async def create_menu_item(menu: MenuBaseDTO, repo: Repo) -> MenuGetDTO:
    item = await repo.create(**menu.model_dump())
    await repo.commit()
    return item


@router.patch("/menus/{menu_id}")
async def change_menu_item(menu_id: str, menu: MenuBaseDTO, repo: Repo) -> MenuGetDTO:
    item = await repo.update(item_id=menu_id, **menu.model_dump())
    await repo.commit()
    return item


@router.delete("/menus/{menu_id}")
async def delete_menu_item(menu_id: str, repo: Repo) -> None:
    await repo.delete(item_id=menu_id)
    await repo.commit()
