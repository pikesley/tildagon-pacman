from lib.sprites.pacman import Pacman


def test_simple_pacman():
    """Test."""
    pac = Pacman()

    assert pac.name == "pacman"
    assert pac.y == 0
