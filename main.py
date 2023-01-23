while True:
      entered_list = input("Введите список  целых чисел, разделенных пробелом: ").split()

      try:
            num = int(input("Введите число: "))
            num_list = [int(i) for i in entered_list]
            break
      except ValueError:
          print("Были введены не правильные значения. Введите заново")


num_list.sort()
print("Отсортированный список", num_list)
def BinarySearch(num_list, num):
    first = 0
    last = len(num_list)
    while first < last:
        mid = (first+last)//2
        if num>num_list[mid]:
            first = mid+1
        else:
            last = mid
    return first-1 if 0 < first < len(num_list) else "Такого числа нет в диапазоне списка"
print("Номер позиции:", BinarySearch(num_list, num))