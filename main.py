import requests


def get_location(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        location_info = {
            'IP': data['query'],
            'Country': data['country'],
            'Region': data['regionName'],
            'City': data['city'],
            'ZIP': data['zip'],
            'Latitude': data['lat'],
            'Longitude': data['lon'],
            'ISP': data['isp'],
            'Org': data['org'],
            'AS': data['as']
        }
        return location_info
    else:
        return {'error': 'Неверный IP-адрес или достигнут лимит запросов'}


if __name__ == "__main__":
    ip_address = input("Введите IP-адрес: ")
    location = get_location(ip_address)
    if 'error' in location:
        print(location['error'])
    else:
        for key, value in location.items():
            print(f"{key}: {value}")
