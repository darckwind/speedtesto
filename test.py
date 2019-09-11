import speedtest as sp
import json

def cancer():
    narnia = sp.Speedtest()
    narnia.get_best_server()
    responce = {
        "SpeedTestUploadauto-py-to-exe":narnia.upload()/1e+6,
        "SpeedTestDownload":narnia.download()/1e+6,
        "SpeedTestLatency":narnia.results.ping
    }

    return (responce)

with open('Speedtest.json' ,'w') as outfile:
    json.dump(cancer(),outfile)