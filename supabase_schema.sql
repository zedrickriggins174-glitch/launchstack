-- Supabase schema for FastAPI + Clerk starter
-- Run this in your Supabase SQL Editor

create extension if not exists "uuid-ossp";

create table if not exists items (
      id          uuid primary key default uuid_generate_v4(),
      user_id     text not null,
      name        text not null,
      description text default '',
      created_at  timestamptz default now(),
      updated_at  timestamptz default now()
  );

create index if not exists idx_items_user_id on items(user_id);
