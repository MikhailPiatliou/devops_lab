import conf
import datetime
import json
import psutil
import time

count = 1
while True:
    cpu = str(psutil.cpu_percent(interval=1))
    dused = str(psutil.disk_usage("/").used)
    dfree = str(psutil.disk_usage("/").free)
    vmused = str(psutil.virtual_memory().used)
    vmfree = str(psutil.virtual_memory().free)
    ioread = str(psutil.disk_io_counters().read_count)
    iowrite = str(psutil.disk_io_counters().write_count)
    netsent = str(psutil.net_io_counters().bytes_sent)
    netrcvd = str(psutil.net_io_counters().bytes_recv)
    ts = datetime.datetime.fromtimestamp(time.time()).\
        strftime("%Y-%m-%d %H:%M:%S")

    if conf.output == "txt":
        print("SNAPSHOT " + str(count) + "\n"
              + "Time: " + ts + "\n"
              + "CPU load: " + cpu + "\n"
              + "Disk usage: " + dused + "\n"
              + "Free disk space: " + dfree + "\n"
              + "Memory usage: " + vmused + "\n"
              + "Free memory: " + vmfree + "\n"
              + "Read operations: " + ioread + "\n"
              + "Write operations: " + iowrite + "\n"
              + "Sent bytes: " + netsent + "\n"
              + "Received bytes: " + netrcvd + "\n",
              file=open("log.txt", "a")
              )
        time.sleep(conf.interval)
    elif conf.output == "json":
        json_dict = {"SNAPSHOT": count,
                     "Time": ts,
                     "CPU load": cpu,
                     "Disk usage": dused,
                     "Free disk space": dfree,
                     "Memory usage": vmused,
                     "Free memory": vmfree,
                     "Write operations": iowrite,
                     "Received bytes: ": netrcvd,
                     "Sent bytes": netsent,
                     "Received bytes": netrcvd
                     }
        with open("log.json", "a") as dj:
            json.dump(json_dict, dj)
        time.sleep(conf.interval)
    print("OK")
    count += 1
