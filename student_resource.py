from fastapi import FastAPI, HTTPException  # Importing necessary modules
from uuid import UUID  # Importing UUID for generating unique identifiers

app = FastAPI()  # Creating a FastAPI instance

students = {}  # Initializing an empty dictionary to store student data
student_data = {"id": 0, "name": "", "age": 0, "sex": "", "height": 0}  # Data structure template for student

# Endpoint for the home route
@app.get("/")
def home():
    """
    Endpoint to welcome users to the student resource API.

    Returns:
        dict: A welcome message.
    """
    return {"message": "Welcome to my student resource API"}

# Endpoint to create a new student resource
@app.post("/students")
def create_student_resource(name: str, age: int, sex: str, height: float):
    """
    Endpoint to create a new student resource.

    Args:
        name (str): The name of the student.
        age (int): The age of the student.
        sex (str): The gender of the student.
        height (float): The height of the student.

    Returns:
        dict: A success message along with the data of the newly created student.
    """
    new_student = student_data.copy()  # Creating a new student object based on the template
    new_student["id"] = str(UUID(int=len(students) + 1))  # Generating a unique ID for the student
    new_student["name"] = name
    new_student["age"] = age
    new_student["sex"] = sex
    new_student["height"] = height

    students[new_student["id"]] = new_student  # Adding the new student to the dictionary of students
    return {"message": "Student resource created successfully", "data": new_student}

# Endpoint to retrieve a specific student resource by ID
@app.get("/students/{id}")
def retrieve_student_resource(id: str):
    """
    Endpoint to retrieve a specific student resource by ID.

    Args:
        id (str): The unique ID of the student.

    Returns:
        dict: The data of the requested student.
    
    Raises:
        HTTPException: If the requested student is not found.
    """
    student = students.get(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return {"data": student}

# Endpoint to retrieve all student resources
@app.get("/students")
def retrieve_all_students_resource():
    """
    Endpoint to retrieve all student resources.

    Returns:
        dict: All student data.
    """
    return students

# Endpoint to update an existing student resource
@app.put("/students/{id}")
def update_student_resource(id: str, name: str, age: int, sex: str, height: float):
    """
    Endpoint to update an existing student resource.

    Args:
        id (str): The unique ID of the student to be updated.
        name (str): The updated name of the student.
        age (int): The updated age of the student.
        sex (str): The updated gender of the student.
        height (float): The updated height of the student.

    Returns:
        dict: A success message along with the updated data of the student.

    Raises:
        HTTPException: If the student to be updated is not found.
    """
    student = students.get(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student["name"] = name
    student["age"] = age
    student["sex"] = sex
    student["height"] = height

    return {"message": "Student resource updated successfully", "data": student}

# Endpoint to delete a student resource
@app.delete("/students/{id}")
def delete_student_resource(id: str):
    """
    Endpoint to delete a student resource.

    Args:
        id (str): The unique ID of the student to be deleted.

    Returns:
        dict: A success message confirming the deletion of the student.

    Raises:
        HTTPException: If the student to be deleted is not found.
    """
    student = students.get(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    del students[id]  # Deleting the student from the dictionary of students
    return {"message": "Student resource deleted successfully"}
