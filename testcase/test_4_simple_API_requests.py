import requests
from datetime import timedelta

response = requests.get("https://randomfox.ca/floof")


def test_4_method1():  # simple 200 code.
    assert response.status_code == 200, "Assertion Error #4.1 - status code is not 200"


def test_4_method2():  # foxes should be randomized.
    fox = list()
    for i in range(3):
        response = requests.get("https://randomfox.ca/floof")
        fox.append(response.text)
    print(fox)
    assert fox[0] is not fox[1] is not fox[2], "Assertion Error #4.2 - foxes are not randomized"


def test_4_method3():  # to check elapsed time from request instance.
    response = requests.get("https://randomfox.ca/floof")
    print(response.elapsed)
    assert response.elapsed < timedelta(seconds=1), "Assertion Error #4.3 - request took too long"
