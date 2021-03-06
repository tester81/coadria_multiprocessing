#!/usr/bin/python
# -*- coding: utf-8 -*-
import multiprocessing
import sys
import time
import os # for urandom
from base64 import b64encode # for urandom



a = []      # \  
            #  >   these represent dictionary values / fields    
b = []      # /


msgs = {'process_id': a, 'message': b}   # dictionary represents table 'messages' with process_id and message keys/rows



def worker1(queue):

    while True:
        name = multiprocessing.current_process().name  # name is Process-1



        post = queue.get()      # receiving
        print 'worker1' + ' received ' + post + ' successfully!'
        a.append(post) 
        print 'worker1' + ' received the following messages so far ', a
        


        rand = os.urandom(5)     # sending
        rand = b64encode(rand).decode('utf-8')
        rand = str(rand)       
        queue.put(rand)          
        print name + ' wrote a message! ' + rand
        time.sleep(30)







        # rand = os.urandom(5)
        # rand = b64encode(rand).decode('utf-8')
        # rand = str(rand)

        # print 'Process 1 inserting random chars'
 
        # time.sleep(3)



        # if 'a' in c[2]:
        #     print c[2] 
        # elif 'a' not in c[2]:
        #     print 'message doesn\'t contain a letter "a"'
        # else:
        #     print 'message not found'

        # time.sleep(.5)


def worker2(queue):

    while True:
        name = multiprocessing.current_process().name  # Process-2



        rand = os.urandom(5)    # sending
        rand = b64encode(rand).decode('utf-8')
        rand = str(rand)       
        queue.put(rand )
        print name + ' wrote a message! ' + rand 
        time.sleep(30)

    
        post2 = queue.get()    # receiving
        print 'worker2' + ' received ' + post2 + ' successfully!'
        b.append(post2) 
        print 'worker2' + ' received the following messages so far ', b








        # rand = os.urandom(5)
        # rand = b64encode(rand).decode('utf-8')
        # rand = str(rand)

        # time.sleep(3)


        
        # if 'b' in c[2]:
        #     print c[2] 
        # elif 'b' not in c[2]:
        #     print 'message doesn\'t contain a letter "b"'
        # else:
        #     print 'message not found'

        # time.sleep(.5)



if __name__ == '__main__':
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=worker1, args=(queue,))
    p2 = multiprocessing.Process(target=worker2, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()