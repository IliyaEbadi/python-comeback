#Logic1-cigarParty
#When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.

def cigar_party(cigars, is_weekend):
  if is_weekend and cigars  >= 40:
    return True
  elif cigars>= 40 and cigars <= 60:
    return True
  else:
    return False
#Logic1-date_fashion

#You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

#Logic-1 > squirrel_play
def squirrel_play(temp, is_summer):
  if temp >= 60 and temp <= 90 and not is_summer:
    return True
  elif temp >= 60 and temp<= 100 and is_summer:
    return True
  else:
    return False

#Logic-1 > caught_speeding

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed = speed - 5

    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2
#Logic-1 > sorta_sum

def sorta_sum(a, b): 
  if (a + b) >= 10 and (a + b) <= 19:
    return 20
  else:
    return a + b

#List-1 > first_last6

def first_last6(nums):
  if nums[0]==6 or nums[-1] == 6:
    return True
  else:
    return False
#List-1 > common_end
def common_end(a, b):
  if a[0] == b[0] or a[-1]== b[-1]:
    return True
  else:
    return False

#List-1 > sum3
def sum3(nums):
  sum = 0
  for i in range(len(nums)):
    sum += nums[i]
  return sum

#List-1 > rotate_left3

def rotate_left3(nums):
    result = []
    for i in range(1, len(nums)):
        result.append(nums[i])

    result.append(nums[0])

    return result
#List-1 > reverse3

def reverse3(nums):
    result = []

    for i in range(len(nums) - 1, -1, -1):
        result.append(nums[i])

    return result

#List-1 > max_end3

def max_end3(nums):
    if nums[0] > nums[-1]:
        largest = nums[0]
    else:
        largest = nums[-1]

    nums[0] = largest
    nums[1] = largest
    nums[2] = largest

    return nums