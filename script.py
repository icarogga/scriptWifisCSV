import os
import subprocess
import time
import pandas as pd
import numpy as np

className = 'Cozinha'

def stringToPercent(value):
    if value != 0 and len(value.split('/')) > 1:
        values = value.split('/')
        return round((int(values[0]) / int(values[1])) * 100, 2)
    else:
        return int(value)

def getWifi():
    output = ''
    try:
        output = subprocess.check_output("sudo iwlist scan |grep -e ESSID -e Quality", shell=True)
    except:
        time.sleep(2000)
        getWifi()

    output = str(output)
    outputs = output.split('\\n')

    new_out = []
    for out in outputs:
        out = out.replace('                    ', '')
        out = out.replace("b'", '')
        out = out.split('  ')[0]
        if "'" not in out:
            new_out.append(out)

    quality = []
    essid = []
    rooms = []
    for i in range(0, len(new_out)):
        if(i % 2 == 0):
            quality.append(new_out[i].replace('Quality=', ''))
            rooms.append(className)
        else:
            essid.append(new_out[i].replace('ESSID:', '').replace('"', ''))

    my_csv = pd.read_csv('my_wifi.csv')

    data = np.array([quality])
    new_read = pd.DataFrame(data=data, columns=essid)

    new_read['Class'] = [className]
    new_read = new_read.fillna(0)
    categorical_cols = new_read[new_read.columns].select_dtypes(exclude=['int64','float64']).columns
    for col in categorical_cols:
        if 'Class' not in col:
            new_read[col] = new_read[col].apply(stringToPercent)

    my_csv = pd.concat([my_csv, new_read])
    my_csv = my_csv.fillna(0)
    print(my_csv[33:].head(17))
    my_csv.to_csv('my_wifi.csv', index=False)  

getWifi()
