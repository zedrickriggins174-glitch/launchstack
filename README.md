# FastAPI + Clerk Auth + Supabase + Redis

Production-ready Python API starter with authentication, database, and caching. Deploy to Railway in one click.

## What's Included

- **FastAPI** - Modern Python web framework with automatic OpenAPI docs
- **Clerk** - User authentication via JWT verification (iOS, React, Next.js)
- **Supabase** - PostgreSQL database with instant REST API
- **Redis** - In-memory caching for fast responses
- **Railway** - One-click deploy with auto-scaling and health checks

## Quick Start

1. Deploy to Railway (click the button above)
2. Add a Redis plugin in Railway
3. Create a Supabase project and run `supabase_schema.sql`
4. Set up Clerk and copy your JWKS URL
5. Configure env vars in Railway's Variables tab

## Environment Variables

| Variable | Description |
|----------|-------------|
| `SUPABASE_URL` | Supabase project URL |
| `SUPABASE_SERVICE_KEY` | Service role key |
| `CLERK_JWKS_URL` | Clerk JWKS endpoint |
| `REDIS_URL` | Auto-injected by Railway Redis plugin |

## API Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/health` | No | Health check |
| GET | `/api/v1/items` | Yes | List items (cached) |
| POST | `/api/v1/items` | Yes | Create item |
| DELETE | `/api/v1/items/{id}` | Yes | Delete item |

## License

MIT
