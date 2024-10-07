def c_to_f(c):
    return c * 9/5 + 32

def test_c_to_f():
    assert c_to_f(0) == 32
    assert c_to_f(100) == 212
    assert c_to_f(-40) == -40
    assert c_to_f(37) == 98.6

if __name__ == "__main__":
    test_c_to_f()
    print("All passed")
