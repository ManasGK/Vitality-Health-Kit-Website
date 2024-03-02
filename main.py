from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from tinydb import TinyDB, Query

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")



templates = Jinja2Templates(directory="templates")

db = TinyDB('mydbfile.json')


db.insert({"name": "Manass",
           "age":12,
           "Gender": "Male",
           "MostRecentHeartRate": 65,
           "MostRecentBloodPressure" : 90,
           "MostRecentTemperature" : 39.2})

user = Query()
data = db.search(user.name == 'Manas')

print(data)

# For the dashboard

@app.get("/dashboard", response_class=HTMLResponse)
async def read_item_dashboard(request: Request):
   return templates.TemplateResponse(
       request=request,
       name="home.html",
       context={"data": data[0]}
   )

# For the results page

@app.get("/results", response_class=HTMLResponse) # Shows that /app is the endpoint (makes it unique page) ---- responseclass=HTMLResponse whows that the output file on the server will be in HTML
async def read_item(request: Request): # A function to read the item
   return templates.TemplateResponse( # This Built in Function, processes the template file, and generates the final HTML content
       request=request,
       name="about.html",
       context={"data": data[0]}
   )

