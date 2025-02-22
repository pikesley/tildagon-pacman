from lib.sprite_train import SpriteTrain


def test_sprite_train():
    """Test."""
    st = SpriteTrain()

    assert st.chaser == "ghosts"
    assert [sprite.name for sprite in st.sprites] == [
        "pacman",
        "blinky",
        "pinky",
        "inky",
        "clyde",
    ]


def test_reordering():
    """Test."""
    st = SpriteTrain()
    st.chaser = "pacman"
    st.reorder()

    assert [sprite.name for sprite in st.sprites] == [
        "blinky",
        "pinky",
        "inky",
        "clyde",
        "pacman",
    ]


def test_recolouring():
    """Test."""
    st = SpriteTrain()
    st.chaser = "ghosts"
    st.recolour()

    assert [ghost.is_blue for ghost in st.ghosts] == [False] * 4

    st.chaser = "pacman"
    st.recolour()
    assert [ghost.is_blue for ghost in st.ghosts] == [True] * 4


def test_alignment():
    """Test."""
    st = SpriteTrain()
    st.rescale(1.0)

    st.align(direction="right", offset=0)
    assert [sprite.x for sprite in st.sprites] == [0.0, -55.0, -110.0, -165.0, -220.0]
    assert [sprite.facing for sprite in st.sprites] == ["right"] * 5

    st.align(direction="up", offset=100)
    assert [sprite.y for sprite in st.sprites] == [100.0, 155.0, 210.0, 265.0, 320.0]


def test_off_screen():
    """Test."""
    st = SpriteTrain()
    st.rescale(1.0)

    st.align(direction="left", offset=140)
    assert st.off_screen

    st.align(direction="right", offset=0)
    assert not st.off_screen
