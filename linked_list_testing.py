import harrys_linked_list_module

alist = harrys_linked_list_module.HarrysLinkedList()
alist.appendItem("apple")
alist.appendItem("banana")
alist.appendItem("orange")
alist.appendItem("pear")

print(alist)
print(alist.size())
alist.removeItem(2)
print(alist)
print(alist.size())