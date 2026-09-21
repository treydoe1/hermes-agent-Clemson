from providers import get_provider_profile, provider_source


def test_clemson_rcd_profile_discovered_with_aliases():
    profile = get_provider_profile("clemson-rcd")

    assert profile is not None
    assert profile.name == "clemson-rcd"
    assert profile.base_url == "https://llm.rcd.clemson.edu/v1"
    assert profile.api_mode == "chat_completions"
    assert profile.auth_type == "api_key"
    assert profile.env_vars == ("CLEMSON_RCD_API_KEY",)
    assert profile.fallback_models == ("rcd/qwen3.8-27b-fp8",)
    assert profile.default_aux_model == "rcd/qwen3.8-27b-fp8"
    assert provider_source("clemson-rcd") == "bundled"

    assert get_provider_profile("clemson") is profile
    assert get_provider_profile("rcd") is profile
