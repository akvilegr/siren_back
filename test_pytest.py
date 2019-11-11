import main


def test_read_file():
    assert main.read_file("test.txt") == ["000325175", "005420021", "005420120", "005420120"]
