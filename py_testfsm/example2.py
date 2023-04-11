from textfsm import TextFSM
import os,sys

os.chdir(sys.path[0]) 

def parse_from_file():
    stdout = "18:42:41.321 CST Sun Jan 1 2023"
    
    with open("route2.textfsm", "r+") as f:
        fsm = TextFSM(f)
    res = fsm.ParseTextToDicts(stdout)
    print(res)


if __name__ == '__main__':
    parse_from_file()