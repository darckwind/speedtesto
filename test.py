import speedtest as sp
import json, subprocess, os, sys,getopt

def cancer():
    # start services of speedtest
    narnia = sp.Speedtest()
    # fix server
    server_data = [{'url': 'http://dallas02.speedtest.windstream.net/speedtest/upload.php', 'lat': '32.7766', 'lon': '-96.7969', 'name': 'Dallas, TX', 'country': 'United States', 'cc': 'US', 'sponsor': 'Windstream', 'id': '17386', 'host': 'dallas02.speedtest.windstream.net:8080', 'd': 7855.541337725319}]
    narnia.get_best_server(server_data)
    #format json of responce
    responce = {
        "SpeedTestUpload":narnia.upload()/1e+6,
        "SpeedTestDownload":narnia.download()/1e+6,
        "SpeedTestLatency":narnia.results.ping,
        "PingServer":ping_real()
    }
    return(responce)
def ping_real():
    res_con = []
    proc = subprocess.Popen(['ping','45.79.49.144'],universal_newlines=6,stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        res_con.append(line.rstrip())

    res_con = res_con[: len(res_con) - 6]
    res_con.pop(0)
    res_con.pop(0)
    return res_con

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
    name = str(outputfile+"/Speedtest.json")
    with open(name, 'w') as outfile:
        json.dump(cancer(), outfile)

if __name__ == "__main__":
    main(sys.argv[1:])
