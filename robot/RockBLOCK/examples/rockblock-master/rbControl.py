#!/usr/bin/env python

import lib.rockBlock as rockBlock
from lib.rockBlock import rockBlockProtocol

class RockBlockControl(rockBlockProtocol):
    
    ## initialize with serial device path
    def __init__(self, serial_dev):
        self.dev = serial_dev

    ## Send a MO message through rockblock over serial
    def mo_send(self, msg):
        try:
            rb = rockBlock.rockBlock(self.dev, self)
            rb.sendMessage(str(msg))
            rb.close()
        except (rockBlock.rockBlockException):
            print "mo_send: rockBlockException encountered"

    ## Indicate transmit started
    def rockBlockTxStarted(self):
        print "rockBlockTxStarted"

    ## Indicate transmit failed
    def rockBlockTxFailed(self):
        print "rockBlockTxFailed"
        
    ## Indicate transmit succeeded
    def rockBlockTxSuccess(self,momsn):
        print "rockBlockTxSuccess " + str(momsn)

    ## Receive MT message from rockblock over serial
    def mt_recv(self):
        try:
            rb = rockBlock.rockBlock(self.dev, self)
            rb.requestMessageCheck()
            rb.close()
        except (rockBlock.rockBlockException):
            print "mt_recv: rockBlockException encountered"

    ## Indicate receive started
    def rockBlockRxStarted(self):
        print "rockBlockRxStarted"

    ## Indicate receive failed
    def rockBlockRxFailed(self):
        print "rockBlockRxFailed"
        
    ## Receive succeeded; print mtmsn (message sequence #) and data
    def rockBlockRxReceived(self,mtmsn,data):
        print "rockBlockRxReceived " + str(mtmsn) + " " + data

    ## Print length of message queue
    def rockBlockRxMessageQueue(self,count):
        print "rockBlockRxMessageQueue " + str(count)
             
                     
if __name__ == '__main__':
    print "import this..."
