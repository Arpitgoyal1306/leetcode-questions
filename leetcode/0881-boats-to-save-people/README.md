# 881. Boats to Save People

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Two_Pointers-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Timsort-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 71 ms |
| Memory | 16.4 MB |
| Submission Date | 2026-10-29T06:17:03.098Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an array <code>people</code> where <code>people[i]</code> is the weight of the <code>i<sup>th</sup></code> person, and an <strong>infinite number of boats</strong> where each boat can carry a maximum weight of <code>limit</code>. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most <code>limit</code>.</p>

<p>Return <em>the minimum number of boats to carry every given person</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> people = [1,2], limit = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 boat (1, 2)
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> people = [3,2,2,1], limit = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 boats (1, 2), (2) and (3)
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> people = [3,5,3,4], limit = 5
<strong>Output:</strong> 4
<strong>Explanation:</strong> 4 boats (3), (3), (4), (5)
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= people.length &lt;= 5 * 10<sup>4</sup></code>
- <code>1 &lt;= people[i] &lt;= limit &lt;= 3 * 10<sup>4</sup></code>

## Solution

```py
class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i = 0
        j = len(people) - 1
        count = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            count += 1
        return count
        
```

[View on LeetCode](https://leetcode.com/problems/boats-to-save-people/)
