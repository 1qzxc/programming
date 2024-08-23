from mylist import MyList


def main():
    list_ = MyList(1, 2, 3)
    list_.print()   # output: 1 2 3
     
    list_.append(4)
    list_.print()   # output: 1 2 3 4
      
    tail = MyList(5, 6)
    list_ += tail   # shallow copy, see examples below
    list_.print()   # output: 1 2 3 4 5 6
       
    tail._value = 0
    tail.print()    # output: 0 6; element 5 in tail is changed
    list_.print()   # output: 1 2 3 4 5 6; element 5 in list_ is NOT changed
        
    list_ += [7, 8]
    list_.print()   # output: 1 2 3 4 5 6 7 8
    list_ += ()
    list_.print()   # output: 1 2 3 4 5 6 7 8
         
    for elem in list_:
        print(2 ** elem)    # output: 2 4 8 16 32 64 128 256
              
    list_.print_reversed()  # output: 8 7 6 5 4 3 2 1
               
    empty_list = MyList()
    empty_list.print()  # empty output
                
    list_with_single_none_element = MyList(None)
    list_with_single_none_element.print()  # output: None


    list1 = MyList(1,2)
    list2 = MyList(3,4)
    list3 = list1 + list2
    list3.print()
    list2.print()
    list1.print()

if __name__ == "__main__":
    main()
