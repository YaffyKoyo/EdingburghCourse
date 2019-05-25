from os import listdir
from os.path import isfile, join
import csv

mypath = './data/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]

onlyfiles = [f for f in onlyfiles if f[-4:] == '.txt']
print(onlyfiles)

for filename in onlyfiles:
    with open(mypath+filename,'r') as f:
        lines_skipped_header = f.readlines()[7:]
        stripped = (line.strip() for line in lines_skipped_header)
        data = []
        for line in lines_skipped_header:
            if 'Site close' in line or 'Site Close' in line:
                continue
            if int(line[3:7]) in range(1999,2000): #choose year range
                s_year = line[3:7]
                s_month = line[9:11].strip(' ')
                s_tmax = line[14:18].strip(' ')
                s_tmin = line[21:26].strip(' ')
                s_af = line[30:34].strip(' ')
                s_rain = line[36:42].strip(' ')
                data.append({'year':int(s_year),
                            'month':int(s_month),
                             'tmax':float(s_tmax) if s_tmax!='---' else 0,
                             'tmin':float(s_tmin) if s_tmin!='---' else 0,
                               'af':float(s_af) if s_af!='---' else 0,
                             'rain':float(s_rain) if s_rain!='---' else 0,
                    })
        with open(mypath+filename[:-4]+'.csv','w',newline='') as csvFile:
            fields = ['year','month','tmax','tmin','af','rain']
            writer = csv.DictWriter(csvFile,fieldnames=fields)
            writer.writeheader()
            for item in data:
                writer.writerow(item)  