# 1207. Unique Number of Occurrences

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1 ms |
| Memory | 12.3 MB |
| Submission Date | 2026-11-13T01:13:21.019Z |
| Platform | leetcode |

## Problem Statement

<p>Given an array of integers <code>arr</code>, return <code>true</code> <em>if the number of occurrences of each value in the array is <strong>unique</strong> or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> arr = [1,2,2,1,1,3]
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> arr = [1,2]
<strong>Output:</strong> false
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> arr = [-3,0,1,-3,1,1,1,-3,10,0]
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= arr.length &lt;= 1000</code>
- <code>-1000 &lt;= arr[i] &lt;= 1000</code>

## Solution

```py
class Solution(object):
    def uniqueOccurrences(self, arr):
        from collections import Counter

        freq = Counter(arr)

        if len(set(freq.values())) != len(freq):
            return False
        return True

```

[View on LeetCode](https://leetcode.com/problems/unique-number-of-occurrences/)
