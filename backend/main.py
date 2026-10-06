from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

students = {}
applications = []


@app.get("/")
def home():
    return {"message": "Smart Campus Backend is Running!"}


@app.post("/register")
def register(data: dict):
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return {
            "success": False,
            "message": "All fields are required"
        }

    students[email] = {
        "name": name,
        "password": password
    }

    return {
        "success": True,
        "message": "Registration successful"
    }


@app.post("/login")
def login(data: dict):
    email = data.get("email")
    password = data.get("password")

    if email not in students:
        return {
            "success": False,
            "message": "Invalid email or password"
        }

    if students[email]["password"] != password:
        return {
            "success": False,
            "message": "Invalid email or password"
        }

    return {
        "success": True,
        "message": "Login successful",
        "name": students[email]["name"],
        "email": email
    }


@app.post("/apply")
def apply_job(data: dict):
    email = data.get("email")
    job = data.get("job")

    if not email or not job:
        return {
            "success": False,
            "message": "Email and job are required"
        }

    if email not in students:
        return {
            "success": False,
            "message": "Please login first"
        }

    for application in applications:
        if application["email"] == email and application["job"] == job:
            return {
                "success": False,
                "message": "You have already applied"
            }

    applications.append({
        "email": email,
        "job": job,
        "status": "Applied"
    })

    return {
        "success": True,
        "message": "Your application has been submitted."
    }


@app.get("/applications")
def get_applications(email: str):
    result = []

    for application in applications:
        if application["email"] == email:
            result.append({
                "job": application["job"],
                "status": application["status"]
            })

    return {
        "success": True,
        "applications": result
    }
    