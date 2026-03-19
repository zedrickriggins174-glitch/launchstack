"""
  Application configuration via environment variables.

  Railway injects these automatically from your project's Variables tab.
    For local development, create a .env file from .env.example.
    """

    from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Supabase
    supabase_url: str
    supabase_service_key: str

      # Clerk (JWT verification)
      clerk_jwks_url: str

      # Redis (caching)
      redis_url: str

      # App
      app_name: str = "My App"
      debug: bool = False

      class Config:
        env_file = ".env"


  settings = Settings()
