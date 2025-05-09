'''Animation text using python in terminal'''
import sys
import time 

x = '''your mornung eyes i can walk yoou will be mine no there wann in this 
        lyfe i imagine you and i will walk togeth
        **      **
     ***    **    ***
    ***      *     ***
     **             **
       **         **
         **     **
             *
                '''

def animatd_text(text):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(0.05)

animatd_text(x)

