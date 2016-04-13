

class Heap:
    
   def __init__(self, heap):
      print "start"
      self.heap = heap
       
   def heapify(self, i):
      max_ind = i
      value = self.heap[i]
      left = self.left(i)
      right = self.right(i)
      if self.is_in(left) and self.heap[left] > value:
         max_ind = left
      elif self.is_in(left) and self.heap[right] > value:
         max_ind = right
      
      if max != i:
         self._exchange(i, max_ind)
         self.heapify(max_ind)
         
   def _exchange(self, a, b):
      tmp = self.heap[a]
      self.heap[a] = self.heap[b]       
      self.heap[b] = tmp
      
   def parent(self, i):
      return i/2
    
   def left(self, i):
      return 2*i
    
   def right(self, i):
      return 2*i+1
   
   def is_in(self, i):
      print len(self.heap)
      if i < 0:
         return False
      
      return i < len(self.heap)
    
def main():
    h = Heap()
    print "parent 3 %s" % h.parent(3)
    print "left 3 %s" % h.left(3)
    print "right 3 %s" % h.right(3)
    
    
if __name__ == '__main__':
    main()