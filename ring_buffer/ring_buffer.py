
class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    

  def append(self, item):
      self.storage[self.current] = item
      self.current += 1
      if self.current == self.capacity:
        self.current = 0
        print('hello world')
      
      print(self.storage)
      
          
        
          
        
      
      
      
      
      
    

  def get(self):
    temp = []
    
    for i in range(0, len(self.storage)):
      if self.storage[i] is not None:
        temp.append(self.storage[i])
    return temp
   
       
       




































# class ListNode:
#   def __init__(self, value, prev=None, next=None):
#     self.value = value
#     self.prev = prev
#     self.next = next

# # """Wrap the given value in a ListNode and insert it
# # after this node. Note that this node could already
# # have a next node it is point to."""
#   def insert_after(self, value):
#       current_next = self.next
#       self.next = ListNode(value, self, current_next)
#       if current_next:
#         current_next.prev = self.next

# # """Wrap the given value in a ListNode and insert it
# # before this node. Note that this node could already
# # have a previous node it is point to."""
#   def insert_before(self, value):
#       current_prev = self.prev
#       self.prev = ListNode(value, current_prev, self)
#       if current_prev:
#         current_prev.next = self.prev

# # """Rearranges this ListNode's previous and next pointers
# # accordingly, effectively deleting this ListNode."""
#   def delete(self):
#       if self.prev:
#         self.prev.next = self.next
#       if self.next:
#         self.next.prev = self.prev


# class RingBuffer:
#   def __init__(self, capacity, node=None):
#     self.capacity = capacity
#     self.current = 0
#     self.head = node
#     self.tail = node
#     self.storage = [None]*capacity

#   def append(self, item):
#       print(self.head.next)
      
#       # new_list = []
#       # if self.tail == None:
#       #   self.tail = ListNode(item)
#       #   self.next = None
#       #   self.prev = None
#       # else:
#       #   pass
#         # cur = self.storage.tail
#         # new_node = ListNode(item)
#         # new_node.prev = cur
#         # self.storage.tail = new_node
#         # print(self.tail.prev.value)
#         # print(self.storage)

#       #self.delete(self.tail)
#       # new_node = ListNode(item)
#       # print(new_node.value)
#       # new_node.prev = None
#       # self.head = new_node
#       # print(self.storage)
   
   
  
#   def delete(self, item):
#       print(len(self.storage))
#       if len(self.storage) > 0:
#         cur = self.tail
#         if cur == None:
#           del cur
#       print(len(self.storage))
#       # cur = self.head # set current item to the head
      
#       # while cur: #while cur is not Null, so while list is NOT empty
#       #   if cur == self.head: #if the current value is equal to the value we want to delete, and if it's currently at the head of the list
        
#       #     ##Case 1 -- when the Node you want to delete is the head node, and it is also the only item
#       #     if not cur.next: #If not pointing to any node -- only node in list
#       #       cur = None # Removes current node we created for checking
#       #       self.head = None #removes node that matched, removes the head
            
#       #       return cur## List is now empty, return
          
#       #     #Case 2 - Delete Head node, but list is not empty (there is a next node)
#       #     else: #opposite of line 113, if next is pointing to a valid node
#       #       nxt = cur.next # set nxt == to the cur.next (the next item in the list (next to the head))
#       #       cur.next = None #We want to remove the pointer to the next item because it is being removed
#       #       #cur.prev = None  --- commented out because not needed, because head's previous already points to none
#       #       nxt.prev = None # setting this == to None because it's current prev was the deleted item
#       #       cur = None #get rid of element by setting it equal to None
#       #       self.head = nxt #move the status of the head to the nxt item
            
#       #       return nxt#return the list

          
#       #   else: #if data = key, but is not the head (elif from line 110)
#       #       #Case 3 -- When cur.next is NOT none, and NOT the head (if it has a prev and a next)
#       #       if cur.next: #if cur.next is true 
#       #         nxt = cur.next #set nxt to the next item
#       #         prev = cur.prev #set prev to the prev item -- see below
#       #         ##### ---- so in   A  B  C, if B is the cur, then cur.next (nxt) is C, and cur.prev (prev) is A
#       #         #### this is so we can get these to point to each other, looping around the 'deleted' item
#       #         prev.next = nxt #  so A.next is == C, skipping B
#       #         nxt.prev = prev # so C.prev == A skipping B
              
#       #         #kill off pointers that aren't doing anything
#       #         cur.next = None
#       #         cur.prev = None
#       #         cur = None #Get rid of node
              
#       #         return nxt # return list

#       #       #Case 4 if cur.next IS none, so if it is the tail
#       #       else: #if cur.next is none
#       #         prev = cur.prev # set the prev variable to the previous item
#       #         prev.next = None # Set to none because it will become the new tail
            
#       #       #kill off pointers that aren't doing anything
#       #         cur.prev = None
#       #         cur = None # get rid of node
#       #         print('calling delete')
#       #         return prev #return the list
#       #   cur = cur.next # moves to next pointer after each iteration through the list 
      

#   def get(self):
#     pass