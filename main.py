from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import json
import redis

app = FastAPI()


r=redis.Redis(host="redis-14686.c277.us-east-1-3.ec2.redns.redis-cloud.com", port=14686, username="default", password="x9B8YhtC8g2KnfE5nFdB9zleCTe8t6qX", decode_responses=True)


templates = Jinja2Templates(directory="templates")

currentUser = "MANAS"

# Between here
# Get the most recent temperature, by going into the list and getting index 0
def GetUserData():
    TempList = "Temperatures" + currentUser
    RecentTempOfUser = r.lindex(TempList, 0)

    # Get the most recent HeartRate, by going into the list and getting index 0
    HeartRateList = "HeartRates" + currentUser
    RecentHeartRateofUser = r.lindex(HeartRateList, 0)

    # Get all the Heart Rates as Floats
    AllHeartRatesOfUser = r.lrange(HeartRateList, 0, -1)
    AllHeartRatesOfUser = [float(x) for x in AllHeartRatesOfUser]
    data_values_heartrate_json = json.dumps(AllHeartRatesOfUser)

    AllTempOfUser = r.lrange(TempList, 0, -1)
    AllTempOfUser = [float(x) for x in AllTempOfUser]
    data_values_temp_json = json.dumps(AllTempOfUser)

    return {
        "RecentTempOfUser": float(RecentTempOfUser),
        "RecentHeartRateofUser": float(RecentHeartRateofUser),
        "data_values_heartrate_json": data_values_heartrate_json,
        "data_values_temp_json": data_values_temp_json
    }

@app.post("/dashboard", response_class=HTMLResponse)
async def read_item_dashboard(request: Request):
    userData = GetUserData()
    return templates.TemplateResponse(
       request=request,
       name="home.html",
       context=userData
   )

@app.get("/dashboard", response_class=HTMLResponse)
async def read_item_dashboard(request: Request):
    userData = GetUserData()
    return templates.TemplateResponse(
       request=request,
       name="home.html",
       context=userData
   )

# For the results page

@app.get("/heartrate", response_class=HTMLResponse) # Shows that /app is the endpoint (makes it unique page) ---- responseclass=HTMLResponse whows that the output file on the server will be in HTML
async def read_item(request: Request): # A function to read the item
    userData = GetUserData()
    return templates.TemplateResponse( # This Built in Function, processes the template file, and generates the final HTML content
       request=request,
       name="HeartrateResults.html",
       context=userData
   )

@app.get("/temp", response_class=HTMLResponse) # Shows that /app is the endpoint (makes it unique page) ---- responseclass=HTMLResponse whows that the output file on the server will be in HTML
async def read_item(request: Request): # A function to read the item
    userData = GetUserData()
    return templates.TemplateResponse( # This Built in Function, processes the template file, and generates the final HTML content
       request=request,
       name="TempResults.html",
       context=userData
   )

@app.get("/bp", response_class=HTMLResponse) # Shows that /app is the endpoint (makes it unique page) ---- responseclass=HTMLResponse whows that the output file on the server will be in HTML
async def read_item(request: Request): # A function to read the item
    userData = GetUserData()
    return templates.TemplateResponse( # This Built in Function, processes the template file, and generates the final HTML content
       request=request,
       name="bpResults.html",
       context=userData
   )


@app.get("/", response_class=HTMLResponse) # Shows that /app is the endpoint (makes it unique page) ---- responseclass=HTMLResponse whows that the output file on the server will be in HTML
async def read_item(request: Request): # A function to read the item
    userData = GetUserData()
    return templates.TemplateResponse( # This Built in Function, processes the template file, and generates the final HTML content
       request=request,
       name="signup.html",
       context=userData,
   )

@app.get("/signup", response_class=HTMLResponse) # Shows that /app is the endpoint (makes it unique page) ---- responseclass=HTMLResponse whows that the output file on the server will be in HTML
async def read_item(request: Request): # A function to read the item
    userData = GetUserData()
    return templates.TemplateResponse( # This Built in Function, processes the template file, and generates the final HTML content
       request=request,
       name="signup.html",
       context=userData
   )
