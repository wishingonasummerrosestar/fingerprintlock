from lock import assess_password_strength, check_password

badpasswords = [
    "admin123",
    "Password123",
    "Admin123",
    "abcdefg",
    "ABCdefg",
    "Abc123",
    "superadmindexiaorongdoumeinidetian",
    "SuperAdmin"
]

goodpasswords = [
    "WishingonNGC6809",
    "Fluffycat01",
    "Bottlecaps7",
    "7V4A0mxo4"
]


def test_assess_password_strength():
    for bad_password in badpasswords:
        assert assess_password_strength(bad_password) == False, f"should have failed: {bad_password}"
    for good_password in goodpasswords:
        assert assess_password_strength(good_password) == True, f"should have passed: {good_password}"

def test_check_password():
    assert check_password("GongHeiFatChoy2026") == False
    assert check_password("6b776f54bbec707d7c2de810900c55e15304c4ad688f3e3827e49dbef80ef65c") == False
    assert check_password("c6182e1dbb2a34822310e067f010b09c8624b3123301ff455ec4462595fe205d") == False
    assert check_password("longMAjingshen2026") == False