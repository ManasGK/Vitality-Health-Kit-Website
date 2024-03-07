from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from tinydb import TinyDB, Query
import redis



app = FastAPI()

r=redis.Redis(host="redis-10528.c322.us-east-1-2.ec2.cloud.redislabs.com", port=10528, username="default", password="manickam", decode_responses=True)

# app.mount("/static", StaticFiles(directory="static"), name="static")



templates = Jinja2Templates(directory="templates")

db = TinyDB('mydbfile.json')

currentUser = "Manas"

TempList = "Temperatures" + currentUser
RecentTempOfUser = r.lindex(TempList, 0)
print(RecentTempOfUser)

HeartRateList = "HeartRates" + currentUser
RecentHeartRateofUser = r.lindex(HeartRateList, 0)
print(RecentHeartRateofUser)



@app.get("/dashboard", response_class=HTMLResponse)
async def read_item_dashboard(request: Request):
   return templates.TemplateResponse(
       request=request,
       name="home.html",
       context={"RecentHeartRateofUser" : int(RecentHeartRateofUser), "RecentTempOfUser" : int(RecentTempOfUser)}
   )

# For the results page

# @app.get("/results", response_class=HTMLResponse) # Shows that /app is the endpoint (makes it unique page) ---- responseclass=HTMLResponse whows that the output file on the server will be in HTML
# async def read_item(request: Request): # A function to read the item
#    return templates.TemplateResponse( # This Built in Function, processes the template file, and generates the final HTML content
#        request=request,
#        name="about.html",
#        context={"data": data[0]}
#    )

