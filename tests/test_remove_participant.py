def test_successful_participant_removal(client):
    """Test that a participant can be successfully removed from an activity"""
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already signed up
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert "Removed" in response.json()["message"]


def test_remove_nonexistent_participant(client):
    """Test that removing a non-participant returns 404"""
    # Arrange
    activity_name = "Chess Club"
    email = "nonexistent@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_remove_from_nonexistent_activity(client):
    """Test that removing from a non-existent activity returns 404"""
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_participant_count_decreases_after_removal(client):
    """Test that participant count decreases after successful removal"""
    # Arrange
    activity_name = "Drama Club"
    email = "lucas@mergington.edu"

    # Act - get count before
    activities_before = client.get("/activities").json()
    count_before = len(activities_before[activity_name]["participants"])

    # Act - remove participant
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    activities_after = client.get("/activities").json()
    count_after = len(activities_after[activity_name]["participants"])
    assert count_after == count_before - 1
    assert email not in activities_after[activity_name]["participants"]
