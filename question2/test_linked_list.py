#! /usr/bin/env python

from unittest import TestCase, main
import linked_list

"""
Author : Allan Davis

Answer to question 2 for CCP Games

run: python test_linked_list.py
"""

class LinkedListTest(TestCase):
    def test_swap3(self):
        ll = linked_list.LinkedList()
        ll.add_node(linked_list.Node(data = "Node 1"))
        ll.add_node(linked_list.Node(data = "Node 2"))
        ll.add_node(linked_list.Node(data = "Node 3"))
        self.assertEquals(ll.__str__(), "Node 1, Node 2, Node 3")
        ll.swap(0,2)
        self.assertEquals(ll.__str__(), "Node 3, Node 2, Node 1")
        
    def test_swap5(self):
        ll = linked_list.LinkedList()
        ll.add_node(linked_list.Node(data = "Node 1"))
        ll.add_node(linked_list.Node(data = "Node 2"))
        ll.add_node(linked_list.Node(data = "Node 3"))
        ll.add_node(linked_list.Node(data = "Node 4"))
        ll.add_node(linked_list.Node(data = "Node 5"))
        self.assertEquals(ll.__str__(), "Node 1, Node 2, Node 3, Node 4, Node 5")
        ll.swap(1,3)
        self.assertEquals(ll.__str__(), "Node 1, Node 4, Node 3, Node 2, Node 5")
        
if __name__ == '__main__':
    main()