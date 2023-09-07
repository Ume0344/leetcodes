**Hash Table**
A data structure for fast retrival of data no matter how much is the data is. Because data is stored at 
indexes calulated through hash function. index number is related to actual data. eg, 
Mia, get ascii code of the M, I, A (77, 105, 97). Add them (279) and divide by the number of elements in array (lets say 11). The remainder will be 4, so MIA will be placed at index 4.

**Hash Map**
When data is stored using hashtable in key-value pairs, it is refered as hash-map.

**Hashing Algo**
To find an index from data (Just we did it for MIA).

Collisions
when two data gets thea same index through hashing function.

Collision resolution
Linear probing to put item at next available slot. (if index is 4 and there is akready an element there, put it at 5, if 5 is occupieed, put it to 6)

We can also store the colided data in linked list (MIA and ROY at 4, MIA -> ROY)
