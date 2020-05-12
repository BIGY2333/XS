# Computational Process Organization - Lab1
*Yao_Wangze  Sun_wei*

*laboratory work number ———— 2*

*variant description： Dynamic array (you can use built-in list inside node with ﬁxed size).*

## synopsis ##
In this lab,we should use development tools and to design algorithms in mutable and immutable styles,analyze different approaches algorithms and data structures design.Besides,develop unit and property-based tests.The selected data structure should be implemented in two way: as a mutable object (interaction with an object can modify it); as an immutable object (interaction with an object cannot change it).For each version of a library (mutable and immutable),we should implement ten feature.

## contribution summary for each group member ##
![Alt text](/fig/YaoWangze.png)
## explanation of taken design decisions and analysis ##
1. Test mutable version :
Here, a list is used to represent a dynamic array, and the list index method is used for addition and deletion.  Size, search, etc. use the methods that come with the list. Mapping is to convert the list to the corresponding type. Iteration is to use the self-incrementing variable method to return the corresponding value of the current object.
2. Test immutable version :
Here, a list is also used to represent a dynamic array, we achieved the features like size, add, remove and so on. They are also confirmed useful through immutable_test.py. They achieved the basic features,for example mapping is to convert the list to the corresponding type.
3. Possible implementation errors
Sometimes when the list is empty, its type maybe cause the error when test it.Sometimes it will be in endless loop or report errors directly.
## operation result ##
![Alt text](/fig/1.png)

![Alt text](/fig/2.jpg)
## conclusion ##
A mutable object means interaction with an object can modify it, an immutable object means interaction with an object cannot change it.Mutable version and immutable version both can achieved the features are asked for. But the runtime of them has difference.