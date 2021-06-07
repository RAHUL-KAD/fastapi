from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'details':{'name':'rahul'}}

@app.get('/about')
def about():
    return {'about us':{'company name':'Codicals'}}