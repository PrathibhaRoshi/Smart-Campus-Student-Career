
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "sqlite:///./smartcampus.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    email = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, index=True)
    job = Column(String, nullable=False)
    status = Column(String, default="Applied")


Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Smart Campus Backend is Running!"}


@app.post("/register")
def register(data: dict):
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return {"success": False, "message": "All fields are required"}

    db = SessionLocal()
    try:
        email = email.strip().lower()
        existing = db.query(Student).filter(Student.email == email).first()

        if existing:
            return {"success": False, "message": "Email already registered"}

        student = Student(name=name.strip(), email=email, password=password)
        db.add(student)
        db.commit()

        return {"success": True, "message": "Registration successful"}
    finally:
        db.close()


@app.post("/login")
def login(data: dict):
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""

    db = SessionLocal()
    try:
        student = db.query(Student).filter(Student.email == email).first()

        if not student or student.password != password:
            return {"success": False, "message": "Invalid email or password"}

        return {
            "success": True,
            "message": "Login successful",
            "name": student.name,
            "email": student.email,
        }
    finally:
        db.close()


@app.post("/apply")
def apply_job(data: dict):
    email = (data.get("email") or "").strip().lower()
    job = (data.get("job") or "").strip()

    if not email or not job:
        return {"success": False, "message": "Email and job are required"}

    db = SessionLocal()
    try:
        student = db.query(Student).filter(Student.email == email).first()

        if not student:
            return {"success": False, "message": "Please login first"}

        existing = db.query(Application).filter(
            Application.email == email,
            Application.job == job,
        ).first()

        if existing:
            return {"success": False, "message": "You have already applied"}

        db.add(Application(email=email, job=job, status="Applied"))
        db.commit()

        return {
            "success": True,
            "message": "Your application has been submitted.",
        }
    finally:
        db.close()


@app.get("/applications")
def get_applications(email: str):
    db = SessionLocal()
    try:
        records = db.query(Application).filter(
            Application.email == email.strip().lower()
        ).all()

        return {
            "success": True,
            "applications": [
                {"job": record.job, "status": record.status}
                for record in records
            ],
        }
    finally:
        db.close()
