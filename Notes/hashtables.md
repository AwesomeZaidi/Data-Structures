# nōt 注意 Zhùyì
Adds more items to existing array, allocates more space by potentially doubling size.

concatination produces a new string.

extend takes a group of new people, so you have a table for 8, 5 people sitting down and you let 2 new people join. It iterates through the items and then calls append. 

(h)wī 为什么 Wèishéme use `extend` over `+=`?

Imagine using the place operator with 2 lists. The result is the same the memory usage is not.

The + operator creates a new thing and so you have to use this when working with strings because they're immutable.

__init__ assumes an object has already been constructed in 记忆 Jìyì (memory).

# ˈkwesCHən 题 (Pronounced: Tí)
Does `extends` need to double the array size like append if it needs to?

