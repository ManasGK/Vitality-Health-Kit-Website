from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from tinydb import TinyDB, Query
import json
import redis



app = FastAPI()

r=redis.Redis(host="redis-10528.c322.us-east-1-2.ec2.cloud.redislabs.com", port=10528, username="default", password="manickam", decode_responses=True)


templates = Jinja2Templates(directory="templates")

db = TinyDB('mydbfile.json')

currentUser = "MANAS"

# Get the most recent temperature, by going into the list and getting index 0
TempList = "Temperatures" + currentUser
RecentTempOfUser = r.lindex(TempList, 0)
print(RecentTempOfUser)

# Get the most recent HeartRate, by going into the list and getting index 0
HeartRateList = "HeartRates" + currentUser
RecentHeartRateofUser = r.lindex(HeartRateList, 0)
print(RecentHeartRateofUser)

# Get all the Heart Rates as Floats
AllHeartRatesOfUser = r.lrange(HeartRateList, 0, -1)
AllHeartRatesOfUser = [float(x) for x in AllHeartRatesOfUser]
data_values_json = json.dumps(AllHeartRatesOfUser)

@app.get("/dashboard", response_class=HTMLResponse)
async def read_item_dashboard(request: Request):
   return templates.TemplateResponse(
       request=request,
       name="home.html",
       context={"RecentHeartRateofUser" : float(RecentHeartRateofUser), "RecentTempOfUser" : float(RecentTempOfUser)}
   )

# For the results page

@app.get("/heartrate", response_class=HTMLResponse) # Shows that /app is the endpoint (makes it unique page) ---- responseclass=HTMLResponse whows that the output file on the server will be in HTML
async def read_item(request: Request): # A function to read the item
   return templates.TemplateResponse( # This Built in Function, processes the template file, and generates the final HTML content
       request=request,
       name="HeartrateResults.html",
       context={"AllHeartRatesOfUser" : data_values_json}
   )

@app.get("/temp", response_class=HTMLResponse) # Shows that /app is the endpoint (makes it unique page) ---- responseclass=HTMLResponse whows that the output file on the server will be in HTML
async def read_item(request: Request): # A function to read the item
   return templates.TemplateResponse( # This Built in Function, processes the template file, and generates the final HTML content
       request=request,
       name="TempResults.html",
       context={}
   )

@app.get("/bp", response_class=HTMLResponse) # Shows that /app is the endpoint (makes it unique page) ---- responseclass=HTMLResponse whows that the output file on the server will be in HTML
async def read_item(request: Request): # A function to read the item
   return templates.TemplateResponse( # This Built in Function, processes the template file, and generates the final HTML content
       request=request,
       name="bpResults.html",
       context={}
   )