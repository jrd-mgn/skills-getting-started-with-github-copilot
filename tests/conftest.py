import pytest
from fastapi.testclient import TestClient
from src import app as app_module


@pytest.fixture
def client():
    """Provides a TestClient for the FastAPI app with fresh data for each test"""
    # Reset activities to initial state before each test
    app_module.activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Competitive basketball team for tournaments and games",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["alex@mergington.edu"]
        },
        "Tennis Club": {
            "description": "Learn tennis skills and compete in matches",
            "schedule": "Saturdays, 10:00 AM - 12:00 PM",
            "max_participants": 10,
            "participants": ["jessica@mergington.edu"]
        },
        "Drama Club": {
            "description": "Stage productions, acting, and theatrical performances",
            "schedule": "Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 25,
            "participants": ["lucas@mergington.edu", "ava@mergington.edu"]
        },
        "Art Studio": {
            "description": "Painting, drawing, and visual arts exploration",
            "schedule": "Tuesdays and Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["isabella@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop argumentation and public speaking skills",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 20,
            "participants": ["noah@mergington.edu", "mia@mergington.edu"]
        },
        "Science Club": {
            "description": "Explore STEM topics through experiments and projects",
            "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 24,
            "participants": ["ethan@mergington.edu"]
        }
    }
    
    return TestClient(app_module.app)
