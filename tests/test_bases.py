from django.urls import reverse


def test_get_home_page(client):
    """
    Test the GET request to the home page.

    Args:
        client: The test client.

    Returns:
        None
    """
    response = client.get(reverse("index"))
    assert response.status_code == 200
