from textfsm import TextFSM
import os,sys

os.chdir(sys.path[0]) 

def parse_from_file():
    stdout = """       Destination        Gateway                      Dist/Metric Last Change
           -----------        -------                      ----------- -----------
      B EX 0.0.0.0/0          via 192.0.2.73                  20/100        4w0d
                              via 192.0.2.201
                              via 192.0.2.202
                              via 192.0.2.74
      B IN 192.0.2.76/30     via 203.0.113.183                200/100        4w2d
      B IN 192.0.2.204/30    via 203.0.113.183                200/100        4w2d
      B IN 192.0.2.80/30     via 203.0.113.183                200/100        4w2d
      B IN 192.0.2.208/30    via 203.0.113.183                200/100        4w2d"""
    
    with open("route1.textfsm", "r+") as f:
        fsm = TextFSM(f)
    res = fsm.ParseTextToDicts(stdout)
    print(res)


if __name__ == '__main__':
    parse_from_file()