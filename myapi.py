from fastapi import FastAPI

app = FastAPI()

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

 

