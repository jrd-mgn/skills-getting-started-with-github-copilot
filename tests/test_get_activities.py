def test_get_all_activities(client):
    """Test that GET /activities returns all activities"""
    # Arrange
    expected_activity_names = {
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball Team",
        "Tennis Club",
        "Drama Club",
        "Art Studio",
        "Debate Team",
        "Science Club"
    }

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert set(activities.keys()) == expected_activity_names
    assert len(activities) == 9


def test_activity_has_required_fields(client):
    """Test that each activity has the required structure"""
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    assert response.status_code == 200
    for activity_name, activity_data in activities.items():
        assert set(activity_data.keys()) == required_fields
        assert isinstance(activity_data["participants"], list)
        assert isinstance(activity_data["max_participants"], int)


def test_activities_have_initial_participants(client):
    """Test that activities have correct initial participant counts"""
    # Arrange
    expected_counts = {
        "Chess Club": 2,
        "Programming Class": 2,
        "Gym Class": 2,
        "Basketball Team": 1,
        "Tennis Club": 1,
        "Drama Club": 2,
        "Art Studio": 1,
        "Debate Team": 2,
        "Science Club": 1
    }

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    assert response.status_code == 200
    for activity_name, expected_count in expected_counts.items():
        assert len(activities[activity_name]["participants"]) == expected_count
