# daily-coding
This repository contains solutions for the 
[Daily Coding Problem](https://www.dailycodingproblem.com/)
in python.

### Problems
<hr style="height: 2px">

#### Problem 0
The number 6174 is known as Kaprekar's contant, after the mathematician who discovered an associated property: for all four-digit numbers with at least two distinct digits, repeatedly applying a simple procedure eventually results in this value. The procedure is as follows:\
For a given input x:
* create two new numbers that consist of the digits in x in ascending and descending order.
* Subtract the smaller number from the larger number.

[Solution](https://github.com/MattTitmas/daily-coding/blob/main/solutions/day0.py)
<hr>

#### Problem 1
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

[Solution](https://github.com/MattTitmas/daily-coding/blob/main/solutions/day1.py)
<hr>

#### Problem 2
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

[Solution](https://github.com/MattTitmas/daily-coding/blob/main/solutions/day2.py)
<hr>

#### Problem 3
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

[Solution](https://github.com/MattTitmas/daily-coding/blob/main/solutions/day3.py)
<hr>

#### Problem 4

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

[Solution](https://github.com/MattTitmas/daily-coding/blob/main/solutions/day4.py)
<hr>

#### Problem 5

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair. For example, `car(cons(3, 4))` returns 3, and `cdr(cons(3, 4))` returns 4.

Given this implementation of cons:
```
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```
Implement `car` and `cdr`.

[Solution](https://github.com/MattTitmas/daily-coding/blob/main/solutions/day5.py)
<hr>

#### Problem 6

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an `add(element)` which adds the element to the end, and a `get(index)` which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to `get_pointer` and `dereference_pointer` functions that converts between nodes and memory addresses.

[Solution](https://github.com/MattTitmas/daily-coding/blob/main/solutions/day6.py)
<hr>

#### Problem 7

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

[Solution](https://github.com/MattTitmas/daily-coding/blob/main/solutions/day7.py)
<hr>

#### Problem 7

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```
[Solution](https://github.com/MattTitmas/daily-coding/blob/main/solutions/day8.py)
<hr>

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be `0` or negative.

For example, `[2, 4, 6, 2, 5]` should return `13`, since we pick `2`, `6`, and `5`. `[5, 1, 1, 5]` should return `10`, since we pick `5` and `5`.

Follow-up: Can you do this in O(N) time and constant space?

[Solution](https://github.com/MattTitmas/daily-coding/blob/main/solutions/day9.py)