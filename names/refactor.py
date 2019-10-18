import sys
sys.path.append('./names')
from names import BinarySearchTree

import names_1
import names_2
class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = BinarySearchTree()

  def enqueue(self, value):
    self.storage.insert(names_1)
  
  def dequeue(self):
    self.storage.contains(names_2)

  def len(self):
    return self.size