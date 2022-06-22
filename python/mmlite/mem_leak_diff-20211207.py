#!/bin/python3
import os
import re
import sys
import time
import numpy as np
import matplotlib.pyplot as plt

class Prase:
    def __init__(self, input_file):
        self.__input_file = input_file
        self.__output_file = input_file.split(".")[0]
        if os.path.exists(self.__output_file) == False:
            os.mkdir(self.__output_file)
        self.__mm = {} #pid : [timestamp, thread_name, malloc_free, diff]
        self.__combine = {}
    
    def read_csv(self):
        with open(self.__input_file, "r") as f:
            for line in f.readlines():
                split_list = line.split(",")
                if len(split_list) < 7:
                    continue
                pid = split_list[2];timestamp = split_list[0];thread_name = split_list[3]; diff = split_list[8]
                if pid not in self.__mm:
                    self.__mm[pid] = []
                self.__mm[pid].append([timestamp, thread_name, diff])

    def plot(self):
        for key,item_list in self.__mm.items():
            for item in item_list:
                timeArray = time.strptime("1970-01-01 " + item[0].split(".")[0], "%Y-%m-%d %H:%M:%S")
                timestamp = int(time.mktime(timeArray));diff = int(item[2])
                thread_name = ""
                for c in item[1]:
                    if c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z':
                        thread_name += c
                if thread_name not in self.__combine:
                    self.__combine[thread_name] = {}
                if timestamp not in self.__combine[thread_name]:
                    self.__combine[thread_name][timestamp] = diff
                self.__combine[thread_name][timestamp] += diff
                
        timestamp = []
        for key, item_list in self.__combine.items():
            item_list = sorted(item_list.items(), key=lambda x:x[0])
            timestamp_list = [time.strftime("%H:%M:%S", time.localtime(item[0])) for item in item_list]
            diff_list = [item[1] for item in item_list]
            if str(key) in ['processtotal', 'PRED', 'MATC', 'PERC', 'PLAN', 'REFE']:
              plt.plot(timestamp_list, diff_list, ".-", label=key)
            print(str(key))
            #plt.annotate(str(key),xy=(2, 1),xytext=(3,1.5),arrowprops=dict(facecolor='black', shrink=0.05),)
        timestamp_list = sorted(timestamp_list)
        plt.xticks([timestamp_list[0],timestamp_list[len(timestamp_list)//2],timestamp_list[-1]])
        plt.xlabel('timestamp')
        plt.ylabel("mem")
        plt.legend()
        plt.title(self.__input_file)
        plt.show()
        

if __name__ == "__main__":
    input_file = sys.argv[1]
    if os.path.exists(input_file) == False:
        print("{} is not exists!!!".format(input_file))
        exit(1)
    prase = Prase(input_file)
    prase.read_csv()
    prase.plot()
