import httplib2
import json

def getGeoCodeLocation(inputString):
    google_api_key = "INSERT_YOUR_API_KEY"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString,google_api_key))
    h = httplib2.Http()
    response,content = h.request(url, 'GET')
    result = json.loads(content)

    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    print("lat = %s , lng = %s"%(latitude,longitude))
    return(latitude,longitude)

getGeoCodeLocation("Bangalore,India")   
