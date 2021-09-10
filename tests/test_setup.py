import os
import pytest

ENV_VARS = ["API_KEY", "USERNAME", "PASSWORD"]

@pytest.mark.parametrize("var", ENV_VARS)
def test_variables(var):
    msg = "A TMDB API key, Username and Password are required to work with this project. Please set this in .env at the Project Root"
    assert os.environ.get(var) is not None, msg


