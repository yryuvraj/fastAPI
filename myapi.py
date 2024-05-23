from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "year 12"
    },
    2: {
        "name": "Alice",
        "age": 16,
        "class": "year 11"
    },
    3: {
        "name": "Bob",
        "age": 16,
        "class": "year 11"
    }
}

# amzn.com/create-user
# here create-user is a path parameter or an endpoint in terms of FastAPI
# @app.get("/create-user") we fetch in this manner 

# HTTP Methods used in RESTful APIs
    # GET is a method to fetch the data
    # POST is a method to send the data
    # PUT is a method to update the data
    # DELETE is a method to delete the data
    # PATCH is a method to update the data partially
    
@app.get("/") # index
def index():
    return {"name": "First Data"} # dict


# cmd line command to run the server - "uvicorn myapi:app --reload"
# visit 127.0.0.1:8000/docs in the browser for swagger ui, cool stuff -> no need to use bruno or postman
# removes the use of third party api testing applications

@app.get("/get-student/{student_id}") # path parameter
def get_student(student_id: int = Path(None, description="Enter the student ID", gt=0, lt=3)):
    return students[student_id]