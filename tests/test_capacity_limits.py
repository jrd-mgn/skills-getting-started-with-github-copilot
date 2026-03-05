def test_signup_when_capacity_available(client):
    """Test that a student can sign up when the activity has space"""
    # Arrange
    activity_name = "Tennis Club"
    email = "capacity_test@mergington.edu"

    # Act - get current count
    activities_before = client.get("/activities").json()
    participants_before = len(activities_before[activity_name]["participants"])

    # Act - sign up
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    activities_after = client.get("/activities").json()
    participants_after = len(activities_after[activity_name]["participants"])
    assert participants_after == participants_before + 1


def test_signup_rejected_when_activity_full(client):
    """Test that signup is rejected when activity reaches max capacity"""
    # Arrange
    activity_name = "Tennis Club"
    max_participants = 10
    # Sign up 9 students (1 already there, add 9 more to reach max capacity)
    for i in range(9):
        client.post(
            f"/activities/{activity_name}/signup",
            params={"email": f"student{i}@mergington.edu"}
        )

    # Act - try to exceed capacity
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": "overcapacity@mergington.edu"}
    )

    # Assert
    assert response.status_code == 400
    assert "full" in response.json()["detail"].lower()
