import requests
import subprocess
import json

EVENT = #Enter your event name here.
IFTTT_URL = "https://maker.ifttt.com/trigger/{}/with/key/#Enter your key here"

def getSysTemp():
    gpuTemp = subprocess.check_output(["/opt/vc/bin/vcgencmd", " measure_temp"]).decode()
    cpuTemp = subprocess.check_output(["cat", "/sys/class/thermal/thermal_zone0/temp"]).decode()
    cpuTemp = int((cpuTemp))/1000
    return "The GPU temp is {} and the CPU temp is {}".format(gpuTemp, str(cpuTemp)) 

def getMemUsage():
    return subprocess.check_output(["egrep", "--color", "Mem|Cache|Swap", "/proc/meminfo"]).decode()

def getCpuUsage():
    cpuUsage = subprocess.Popen(("grep", "cpu ", "/proc/stat"), stdout=subprocess.PIPE)
    percentage = subprocess.check_output(('awk', '{usage=($2+$4)*1000/($2+$4+$5)} END {print usage "%"}'), stdin = cpuUsage.stdout)
    return percentage.decode()

def post_ifttt_webhook(event, value1, value2, value3):
    data = {'value1': value1, 'value2': value2, 'value3': value3}
    ifttt_event_url = IFTTT_URL.format(event)
    requests.post(ifttt_event_url, json=data)

def main():
    memUsage = getMemUsage()
    cpuUsage = getCpuUsage()
    temp = getSysTemp()
    post_ifttt_webhook(EVENT, cpuUsage, memUsage, temp)

if __name__ == '__main__':
    main()
