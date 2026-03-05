def test_successful_signup(client):
    """Test that a student can successfully sign up for an activity"""
    # Arrange
    activity_name = "Chess Club"
    email = "new_student@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]
    assert email in response.json()["message"]


def test_duplicate_signup_rejected(client):
    """Test that a student cannot sign up twice for the same activity"""
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already signed up

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()


def test_signup_for_nonexistent_activity(client):
    """Test that signing up for a non-existent activity returns 404"""
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "student@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_signup_with_valid_email_format(client):
    """Test that signup works with properly formatted email addresses"""
    # Arrange
    activity_name = "Art Studio"
    email = "john.doe@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert email in response.json()["message"]
