"""Clemson Research Computing LLM provider profile."""

from providers import register_provider
from providers.base import ProviderProfile

CLEMSON_RCD_MODEL = "rcd/qwen3.8-27b-fp8"

clemson_rcd = ProviderProfile(
    name="clemson-rcd",
    aliases=("clemson", "rcd"),
    display_name="Clemson RCD LLMs",
    description="Clemson Research Computing LLM gateway (OpenAI-compatible)",
    signup_url="https://llm.rcd.clemson.edu/",
    env_vars=("CLEMSON_RCD_API_KEY",),
    base_url="https://llm.rcd.clemson.edu/v1",
    auth_type="api_key",
    api_mode="chat_completions",
    fallback_models=(CLEMSON_RCD_MODEL,),
    default_aux_model=CLEMSON_RCD_MODEL,
)

register_provider(clemson_rcd)
