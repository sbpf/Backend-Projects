import httplib2
import json, requests

def findVenue(queryString,location):
    #1 Geocode the location
    lat,lng = getGeoCode(location)

    #Get restaurants from foursquare
    result = getFirstMatchingLocation(lat,lng,queryString)
    print result['response']['venues'][0]['name']
    print result

def getGeoCode(location):
    google_api_key = "YOUR API KEYS"
    locationString = location.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString,google_api_key))
    h = httplib2.Http()
    response,content = h.request(url, 'GET')    
    result = json.loads(content)
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    print("lat = %s , lng = %s"%(latitude,longitude))
    return(latitude,longitude)

def getFirstMatchingLocation(lat,lng,queryString):
    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
    client_id='YOUR CLIENT ID',
    client_secret='YOUR CLIENT SECRET',
    v='20180323',
    ll=str(lat)+','+str(lng), 
    query=queryString,
    limit=1
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    return data

findVenue('coffee','San Jose, California')
