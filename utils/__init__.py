import uuid


def generate_unique_id():
    return str(uuid.uuid4()).replace("-", "")

#
# def number_sort(number_list: list):
#     number = insertion_sort(number_list)
#
#
# # print(number_sort([4, 5, 6, 7]))
#
#
# def insertion_sort(list1):
#     for i in range(1, len(list1)):
#         value = list1[i]
#         j = i - 1
#         while j >= 0 and value < list1[j]:
#             list1[j + 1] = list1[j]
#             j -= 1
#         list1[j + 1] = value
#     return list1
#
#
# def reverse_insertion_sort(list2):
#     first = 0
#     last = len(list2) - 1
#     u_last = len(list2) - 1
#     while first < last:
#         l = last + 1
#         if list2[last] > list2[last - 1]:
#             list2[last], list2[last - 1] = list2[last - 1], list2[last]
#         else:
#             while l < u_last:
#                 if list2[l] < list2[l + 1]:
#                     list2[l], list2[l + 1] = list2[l + 1], list2[l]
#                 l += 1
#         # if list2[last]
#         last -= 1
#     return list2
#
#
# lists = [10, 5, 13, 8, 2]
# # print("The unsorted list is:", lists)
# #
# print("The sorted list1 is:", reverse_insertion_sort(lists))
