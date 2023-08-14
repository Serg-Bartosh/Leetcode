# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by
# splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

def mergeTwoLists(list1: [], list2: []) -> []:
    itarator1 = iter(list1)
    itarator2 = iter(list2)
    result = []
    while True:
        values_iter1 = next(itarator1, None)
        values_iter2 = next(itarator2, None)
        if values_iter1 is None and values_iter2 is None:
            break

        if values_iter1 is None:
            result.append(values_iter2)
            continue
        if values_iter2 is None:
            result.append(values_iter1)
            continue

        result.append(min(values_iter1, values_iter2))
        result.append(max(values_iter1, values_iter2))

    return result


# test №1
list1 = []
list2 = []
print(mergeTwoLists(list1, list2))
# test №2
list1 = []
list2 = [1, 3, 5, 7]
print(mergeTwoLists(list1, list2))
# test №3
list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7]
print(mergeTwoLists(list1, list2))
# test №4
list1 = [1, 3, 5]
list2 = [2, 4, 6, 8, 10]
print(mergeTwoLists(list1, list2))
# test №5
list1 = [3, 3, 3]
list2 = [3, 3, 3]
print(mergeTwoLists(list1, list2))
