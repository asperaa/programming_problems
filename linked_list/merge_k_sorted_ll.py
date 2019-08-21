"""Merge k sorted linked list Complexity of O(n*k) anbd constant space"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return

    def print_list(self):       
        temp  = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
    def get_length(self, arr):
        count = 0
        lar = 0
        for i in range(len(arr)):
            temp = arr[i]
            while temp:
                if temp.val >= lar:
                    lar = temp.val
                temp = temp.next
                count += 1
                
        return count, lar
    
    def merge_k_sorted_list(self, arr):
        k = len(arr)
        length, largest = self.get_length(arr)
        temp = arr[0]
        result = None
        result_head = None
        index = 0
        for _ in range(length):
            i = 0
            lar = largest
            while i < k:
                if not arr[i]:
                    i += 1
                    continue             
                if arr[i].val <= lar:
                    temp = arr[i]
                    lar = temp.val
                    index = i
                i += 1

            if not result:
                result = temp
                result_head = result
                temp = temp.next
                arr[index] = temp
            else:
                result.next = temp
                temp = temp.next
                arr[index] = temp
                result = result.next

        return result_head
if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()

    l1.append(1)
    l1.append(3)
    l1.append(10)
    l1.append(15)

    l2.append(5)
    l2.append(7)
    l2.append(12)
    l2.append(16)
    l2.append(18)
    
    l3.append(2)
    # l3.append(6)
    # l3.append(19)
    arr = [l1.head, l2.head, l3.head]
    result = l1.merge_k_sorted_list(arr)
    while result:
        print(result.val, end=" ")
        result = result.next
    print()