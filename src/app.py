"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
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
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice and play basketball with the school team",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore your creativity through painting and drawing",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
    },
    "Drama Club": {
        "description": "Act, direct, and produce plays and performances",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["ella@mergington.edu", "scarlett@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging problems and participate in math competitions",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["james@mergington.edu", "benjamin@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["charlotte@mergington.edu", "henry@mergington.edu"]
    }
}


# In-memory user database
users = {
    "michael@mergington.edu": {
        "name": "Michael Johnson",
        "grade": 10,
        "groups": ["Chess Club"],
        "mentor": None,
        "responsibilities": ["Club President"],
        "team": "Chess Team"
    },
    "daniel@mergington.edu": {
        "name": "Daniel Smith",
        "grade": 10,
        "groups": ["Chess Club"],
        "mentor": "michael@mergington.edu",
        "responsibilities": [],
        "team": "Chess Team"
    },
    "emma@mergington.edu": {
        "name": "Emma Wilson",
        "grade": 11,
        "groups": ["Programming Class"],
        "mentor": None,
        "responsibilities": ["Class Leader"],
        "team": "Programming Team"
    },
    "sophia@mergington.edu": {
        "name": "Sophia Brown",
        "grade": 11,
        "groups": ["Programming Class"],
        "mentor": "emma@mergington.edu",
        "responsibilities": [],
        "team": "Programming Team"
    },
    "john@mergington.edu": {
        "name": "John Davis",
        "grade": 9,
        "groups": ["Gym Class"],
        "mentor": None,
        "responsibilities": [],
        "team": "Gym Team"
    },
    "olivia@mergington.edu": {
        "name": "Olivia Miller",
        "grade": 9,
        "groups": ["Gym Class"],
        "mentor": "john@mergington.edu",
        "responsibilities": [],
        "team": "Gym Team"
    },
    "liam@mergington.edu": {
        "name": "Liam Garcia",
        "grade": 12,
        "groups": ["Soccer Team"],
        "mentor": None,
        "responsibilities": ["Captain"],
        "team": "Soccer Team"
    },
    "noah@mergington.edu": {
        "name": "Noah Rodriguez",
        "grade": 12,
        "groups": ["Soccer Team"],
        "mentor": "liam@mergington.edu",
        "responsibilities": [],
        "team": "Soccer Team"
    },
    "ava@mergington.edu": {
        "name": "Ava Martinez",
        "grade": 10,
        "groups": ["Basketball Team"],
        "mentor": None,
        "responsibilities": [],
        "team": "Basketball Team"
    },
    "mia@mergington.edu": {
        "name": "Mia Anderson",
        "grade": 10,
        "groups": ["Basketball Team"],
        "mentor": "ava@mergington.edu",
        "responsibilities": [],
        "team": "Basketball Team"
    },
    "amelia@mergington.edu": {
        "name": "Amelia Taylor",
        "grade": 11,
        "groups": ["Art Club"],
        "mentor": None,
        "responsibilities": ["Club Organizer"],
        "team": "Art Team"
    },
    "harper@mergington.edu": {
        "name": "Harper Thomas",
        "grade": 11,
        "groups": ["Art Club"],
        "mentor": "amelia@mergington.edu",
        "responsibilities": [],
        "team": "Art Team"
    },
    "ella@mergington.edu": {
        "name": "Ella Jackson",
        "grade": 9,
        "groups": ["Drama Club"],
        "mentor": None,
        "responsibilities": [],
        "team": "Drama Team"
    },
    "scarlett@mergington.edu": {
        "name": "Scarlett White",
        "grade": 9,
        "groups": ["Drama Club"],
        "mentor": "ella@mergington.edu",
        "responsibilities": [],
        "team": "Drama Team"
    },
    "james@mergington.edu": {
        "name": "James Harris",
        "grade": 12,
        "groups": ["Math Club"],
        "mentor": None,
        "responsibilities": ["Math Tutor"],
        "team": "Math Team"
    },
    "benjamin@mergington.edu": {
        "name": "Benjamin Clark",
        "grade": 12,
        "groups": ["Math Club"],
        "mentor": "james@mergington.edu",
        "responsibilities": [],
        "team": "Math Team"
    },
    "charlotte@mergington.edu": {
        "name": "Charlotte Lewis",
        "grade": 10,
        "groups": ["Debate Team"],
        "mentor": None,
        "responsibilities": [],
        "team": "Debate Team"
    },
    "henry@mergington.edu": {
        "name": "Henry Walker",
        "grade": 10,
        "groups": ["Debate Team"],
        "mentor": "charlotte@mergington.edu",
        "responsibilities": [],
        "team": "Debate Team"
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(
            status_code=400,
            detail="Student is already signed up"
        )

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str):
    """Unregister a student from an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is signed up
    if email not in activity["participants"]:
        raise HTTPException(
            status_code=400,
            detail="Student is not signed up for this activity"
        )

    # Remove student
    activity["participants"].remove(email)
    return {"message": f"Unregistered {email} from {activity_name}"}


@app.get("/users")
def get_users():
    """Get all user profiles"""
    return users


@app.get("/users/{email}")
def get_user(email: str):
    """Get a specific user's profile"""
    if email not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[email]


@app.post("/users")
def create_user(email: str, name: str, grade: int):
    """Create a new user profile"""
    if email in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[email] = {
        "name": name,
        "grade": grade,
        "groups": [],
        "mentor": None,
        "responsibilities": [],
        "team": None
    }
    return {"message": f"User {email} created"}
