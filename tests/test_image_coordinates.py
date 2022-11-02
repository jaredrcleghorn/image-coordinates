def test_image_coordinates(client):
    # data
    dimensions = [3, 3]
    corners = [[1, 1], [3, 1], [1, 3], [3, 3]]
    solution = [
        [[1, 3], [2, 3], [3, 3]],
        [[1, 2], [2, 2], [3, 2]],
        [[1, 1], [2, 1], [3, 1]],
    ]

    response = client.post("/", json={"dimensions": dimensions, "corners": corners})
    assert response.json == solution
