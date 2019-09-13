import speedtest as sp
import json

def cancer():
    narnia = sp.Speedtest()
    server_data = [{'url': 'http://dallas02.speedtest.windstream.net/speedtest/upload.php', 'lat': '32.7766', 'lon': '-96.7969', 'name': 'Dallas, TX', 'country': 'United States', 'cc': 'US', 'sponsor': 'Windstream', 'id': '17386', 'host': 'dallas02.speedtest.windstream.net:8080', 'd': 7855.541337725319}]
    narnia.get_best_server(server_data)
    responce = {
        "SpeedTestUpload":narnia.upload()/1e+6,
        "SpeedTestDownload":narnia.download()/1e+6,
        "SpeedTestLatency":narnia.results.ping,
    }
    return(responce)

def main():
    with open('Speedtest.json', 'w') as outfile:
        json.dump(cancer(), outfile)

if __name__ == "__main__":
    main()