import speedtest as sp
import json, subprocess, os, sys,getopt


def cancer():
    # start services of speedtest
    import os, ssl

    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context

        narnia = sp.Speedtest()
    # fix server
    server_data = [{'url': 'http://dallas02.speedtest.windstream.net/speedtest/upload.php', 'lat': '32.7766', 'lon': '-96.7969', 'name': 'Dallas, TX', 'country': 'United States', 'cc': 'US', 'sponsor': 'Windstream', 'id': '17386', 'host': 'dallas02.speedtest.windstream.net:8080', 'd': 7855.541337725319}]
    narnia.get_best_server(server_data)

    #format json of responce
    responce = {
        "SpeedTestUpload":narnia.upload()/1e+6,
        "SpeedTestDownload":narnia.download()/1e+6,
        "SpeedTestLatency":narnia.results.ping,
        "PingServer":0.0
    }
    return(responce)
def main(argv):
    outputfile=''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ofile="])
    except getopt.GetoptError:
        print('test.exe -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.exe -o <outputfile>')
            sys.exit()
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if str(outputfile) == '':
        name="Speedtest.json"
    else:
        name = str(outputfile+"/Speedtest.json")
    
    with open(name, 'w') as outfile:
        json.dump({"SpeedTestUpload":0.00,"SpeedTestDownload":0.00,"SpeedTestLatency":0.00,"PingServer":0.00}, outfile)

    with open(name, 'w') as outfile:
        json.dump(cancer(), outfile)

    

if __name__ == "__main__":
    main(sys.argv[1:])
