#!/bin/python3
import os
import sys
import matplotlib.pyplot as plt

class Prase:
    def __init__(self, input_file):
        self.__input_file = input_file
        self.__output_file = input_file.split(".")[0]
        if os.path.exists(self.__output_file) == False:
            os.mkdir(self.__output_file)
        self.__mm = {} #pid : [timestamp, thread_name, malloc_free, diff]
    
    def read_csv(self):
        with open(self.__input_file, "r") as f:
            for line in f.readlines():
                split_list = line.split(",")
                if len(split_list) < 7:
                    continue
                #print(len(split_list))
                pid = split_list[1];timestamp = split_list[0];thread_name = split_list[2]; diff = split_list[7]
                if pid not in self.__mm:
                    self.__mm[pid] = []
                self.__mm[pid].append([timestamp, thread_name, diff])

    def plot(self):
        for key,item_list in self.__mm.items():
            timestamp_list = []; malloc_free_list = []; diff_list = []
            for item in item_list:
                timestamp_list.append(item[0])
                diff_list.append(int(item[2]))
            if "/" in item[1]:
                thread_name = item[1].replace("/", "_")
            else:
                thread_name = item[1]
            title = str(key) + "_" + thread_name
            plt.subplots(timestamp_list, diff_list, ".-", label="diff")
            plt.xticks([timestamp_list[0],timestamp_list[len(timestamp_list)//2],timestamp_list[-1]])
            plt.yticks([diff_list[0],diff_list[len(diff_list)//2],diff_list[-1]])
            plt.xlabel('timestamp')
            plt.ylabel("mem")
            plt.legend()
            plt.title(title)
            #plt.savefig(os.path.join(self.__output_file,title+".png"))
            #plt.close()
            plt.show()

if __name__ == "__main__":
    input_file = sys.argv[1]
    if os.path.exists(input_file) == False:
        print("{} is not exists!!!".format(input_file))
        exit(1)
    prase = Prase(input_file)
    prase.read_csv()
    prase.plot()
