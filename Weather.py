import pywapi
import string

google_result = pywapi.get_weather_from_google('30005')

print google_result
def getCurrentWather():
    city = google_result['forecast_information']['city'].split(',')[0]
    print "It is " + string.lower(google_result['current_conditions']['condition']) + " and " + google_result['current_conditions']['temp_c'] + " degree centigrade now in "+ city+".\n\n"
    return "It is " + string.lower(google_result['current_conditions']['condition']) + " and " + google_result['current_conditions']['temp_c'] + " degree centigrade now in "+ city

def getDayOfWeek(dayOfWk):
    #dayOfWk = dayOfWk.encode('ascii', 'ignore')
    return dayOfWk.lower()

def getWeatherForecast():
    #need to translate from sun/mon to sunday/monday
    dayName = {'sun': 'Sunday', 'mon': 'Monday', 'tue': 'Tuesday', 'wed': 'Wednesday', 'thu': 'Thursday', 'fri': 'Friday', 'sat': 'Saturday', 'sun': 'Sunday'}
    
    forcastall = []
    for forecast in google_result['forecasts']:
        dayOfWeek = getDayOfWeek(forecast['day_of_week']);
        print " Highest is " + forecast['high'] + " and "+ "Lowest is " + forecast['low'] + " on " +  dayName[dayOfWeek]
        forcastall.append(" Highest is " + forecast['high'] + " and "+ "Lowest is " + forecast['low'] + " on " +  dayName[dayOfWeek])
    return forcastall