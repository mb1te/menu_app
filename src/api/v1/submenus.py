from typing import Annotated

from fastapi import APIRouter, status
from fastapi.params import Depends

from src.api.dependencies import SubmenuRepo, get_submenu_repo
from src.dto.submenu import SubmenuBaseDTO, SubmenuGetDTO, SubmenuGetExtDTO

router = APIRouter(tags=["submenus"])
Repo = Annotated[SubmenuRepo, Depends(get_submenu_repo)]


@router.get("/menus/{menu_id}/submenus")
async def get_submenus(menu_id: str, repo: Repo) -> list[SubmenuGetExtDTO]:
    return await repo.get_all(menu_id=menu_id)


@router.get("/menus/{menu_id}/submenus/{submenu_id}")
async def get_submenu_item(submenu_id: str, repo: Repo) -> SubmenuGetExtDTO:
    return await repo.get(item_id=submenu_id)


@router.post("/menus/{menu_id}/submenus", status_code=status.HTTP_201_CREATED)
async def create_submenu_item(
    menu_id: str, submenu: SubmenuBaseDTO, repo: Repo
) -> SubmenuGetDTO:
    item = await repo.create(menu_id=menu_id, **submenu.model_dump())
    await repo.commit()
    return item


@router.patch("/menus/{menu_id}/submenus/{submenu_id}")
async def change_submenu_item(
    submenu_id: str, submenu: SubmenuBaseDTO, repo: Repo
) -> SubmenuGetDTO:
    item = await repo.update(item_id=submenu_id, **submenu.model_dump())
    await repo.commit()
    return item


@router.delete("/menus/{menu_id}/submenus/{submenu_id}")
async def delete_submenu_item(submenu_id: str, repo: Repo):
    await repo.delete(item_id=submenu_id)
    await repo.commit()
