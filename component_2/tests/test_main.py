import pytest
from click.testing import CliRunner
from component_2.main import hello


def test_hello():
    runner = CliRunner()
    result = runner.invoke(hello, ["--count", "3", "--name", "Test"])
    assert result.exit_code == 0
    assert "Hello, Test!\n" * 3 == result.output
