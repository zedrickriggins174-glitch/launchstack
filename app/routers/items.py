"""Example CRUD endpoints with Clerk auth, Supabase, and Redis cache."""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.auth import get_current_user
from app.db import get_supabase
from app.cache import cache_get, cache_set

router = APIRouter(tags=["items"])


class ItemCreate(BaseModel):
      name: str
      description: str = ""


@router.get("/items")
async def list_items(user: dict = Depends(get_current_user)):
      """List all items for the authenticated user (cached 5 min)."""
      user_id = user["sub"]
      cache_key = f"items:{user_id}"
      cached = await cache_get(cache_key)
      if cached is not None:
                return {"items": cached, "cached": True}
            db = get_supabase()
    result = db.table("items").select("*").eq("user_id", user_id).execute()
    await cache_set(cache_key, result.data, ttl_seconds=300)
    return {"items": result.data, "cached": False}


@router.post("/items", status_code=201)
async def create_item(item: ItemCreate, user: dict = Depends(get_current_user)):
      """Create a new item for the authenticated user."""
    user_id = user["sub"]
    db = get_supabase()
    result = db.table("items").insert({
              "name": item.name,
              "description": item.description,
              "user_id": user_id,
    }).execute()
    if not result.data:
              raise HTTPException(status_code=500, detail="Failed to create item")
          from app.cache import get_redis
    r = get_redis()
    await r.delete(f"items:{user_id}")
    return result.data[0]


@router.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: str, user: dict = Depends(get_current_user)):
      """Delete an item (only if it belongs to the authenticated user)."""
    user_id = user["sub"]
    db = get_supabase()
    result = db.table("items").delete().eq("id", item_id).eq("user_id", user_id).execute()
    if not result.data:
              raise HTTPException(status_code=404, detail="Item not found")
          from app.cache import get_redis
    r = get_redis()
    await r.delete(f"items:{user_id}")
