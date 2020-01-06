from . import hello_world_github

def test_hello_world_github():
    assert hello_world_github.apply("Jane") == "hello Jane"
