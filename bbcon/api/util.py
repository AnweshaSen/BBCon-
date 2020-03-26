import herepy
import json

routingApi = herepy.RoutingApi('API_KEY')

def get_min_duration(src, dest):
    response = routingApi.car_route([src['latitude'], src['longitude']],
                                [dest['latitude'], dest['longitude']],
                                [herepy.RouteMode.car, herepy.RouteMode.fastest])
    result = json.load(response)
    return result['routes']['sections'][0]['summary']['duration']