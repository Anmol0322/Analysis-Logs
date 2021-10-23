import os
import datetime
import time

def read_file(file_path,filename):
    with open(file_path, 'r') as f:
        print("\nx---------x------------x")
        print("Filename: " + filename)
        content = f.read()
        colist = content.split("\n")
        count = 0
        cur = datetime.datetime.now()
        t = cur - datetime.timedelta(minutes=10)
        dd = cur.strftime("%d")
        mm = cur.strftime("%m")
        yy = cur.strftime("%y")
        dd1 = t.strftime("%d")
        mm1 = t.strftime("%m")
        yy1 = t.strftime("%y")
        monthDict = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'July',
                     '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
        mm = monthDict[mm]
        mm1 = monthDict[mm1]
        dt = dd + "/" + mm + "/20" + yy
        dt1 = dd1 + "/" + mm1 + "/20" + yy1
        while (t.minute != cur.minute):
            for line in colist:
                current_time = t.strftime("%H:%M")
                if dt in line and current_time in line and "500" in line:
                    count += 1
                    print(line)
                elif dt1 in line and current_time in line and "500" in line:
                    count += 1
                    print(line)
            t = t + datetime.timedelta(minutes=1)
        print("Status code 500: " + str(count))
        print("x---------x------------x\n")
        f.close()

def file_exist(file):
    cur = datetime.datetime.now()
    cutoff = cur - datetime.timedelta(minutes=11)
    newMod = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(file)))
    if newMod > str(cutoff):
        file_path = f"{path}/{file}"
        read_file(file_path, file)

if __name__ == '__main__':
    while(True):
        path=input("Enter path of logs directory: ")
        # path = "/home/aman/Aman/Opcito_DevOps/NewProjectUS/playground10/logs"
        if os.path.exists(path):
             os.chdir(path)
             for file in sorted(os.listdir()):
                if file.startswith("http-"):
                    if file.endswith(".log"):
                        file_exist(file)
             break
        else:
            print("Given path is wrong. Please provide logs directory ...\n")
            continue

