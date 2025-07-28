import linkedList

linkedList.insert_start(5)
linkedList.insert_start(4)
linkedList.insert_start(3)
linkedList.insert_start(2)
linkedList.insert_start(1)
linkedList.insert_end(6)
linkedList.insert_end(7)
linkedList.insert_end(8)
linkedList.insert_end(9)
linkedList.insert_end(10)

linkedList.delete_end()
linkedList.delete_start()
linkedList.delete(8)

print('before reversal:')
linkedList.travese_forward()
linkedList.travese_backward()

print('head:', linkedList.head.data, end='\n')
print('tail:', linkedList.tail.data, end='\n')

linkedList.reverse_list()

print('after reversal:')
linkedList.travese_forward()
linkedList.travese_backward()

print('head:', linkedList.head.data, end='\n')
print('tail:', linkedList.tail.data, end='\n')