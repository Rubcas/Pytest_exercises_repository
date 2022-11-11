#basic test using assert to check if both set are the same

def test_sets_compare():
    set1 = set("abcd")
    set2 = set("aced")
    assert set1 == set2