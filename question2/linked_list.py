#! /usr/bin/env python

"""
Author : Allan Davis

Answer to question 2 for CCP Games

run: python test_linked_list.py
"""

#import pdb
class Data(object):
    def __init__(self):
        pass
    
class Node(object):
    def __init__(self, next = None, data= Data()):
        self.next = next        
        self.data = data
    
class LinkedList(object):
    
    def __init__(self):
        self.count = 0
        self.root = None
    
    def add_node(self, node):
        if self.root == None:
            self.root = node
            self.count = 1
        else:
            current_node = self.root
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node
            self.count += 1
    
    def find(self, index):
        
        if self.root == None:
            None
        else:
            current_node = self.root
            counter = 0
            while current_node.next != None:
                if counter == index:
                    break
                counter += 1
                current_node = current_node.next
            
        return current_node
    
    def swap(self, index1, index2):
        #pdb.set_trace()
        floater = self.find(index2)
        previous = self.find(index2 -1)
        previous.next = floater.next
        swapee = self.find(index1)
        floater.next = swapee.next
        if self.root == swapee:
            self.root = floater
        else:
            swap_previous = self.find(index1 -1)
            swap_previous.next = floater
        swapee.next = previous.next
        previous.next = swapee
    
    def __str__(self):
        str = ""
        if self.root == None:
            str = "None"
        else:
            current_node = self.root
            while current_node.next != None:
                str += "{0}, ".format(current_node.data)
                current_node = current_node.next
            str += current_node.data
        return str