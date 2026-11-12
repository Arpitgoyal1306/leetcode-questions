# 169. Majority Element

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-Divide_and_Conquer-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Counting-blue) ![Topic](https://img.shields.io/badge/Topic-Boyer–Moore_Majority_Vote_Algorithm-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 39 ms |
| Memory | 13.6 MB |
| Submission Date | 2026-11-12T09:34:25.097Z |
| Platform | leetcode |

## Problem Statement

<p>Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.</p>

<p>The majority element is the element that appears more than <code>&lfloor;n / 2&rfloor;</code> times. You may assume that the majority element always exists in the array.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<pre><strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre><p>
```

**Example 2:**

```
</p>
<pre><strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>
<p>&nbsp;</p>
```

## Constraints

- <code>n == nums.length</code>
- <code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code>
- <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>
- The input is generated such that a majority element will exist in the array.

## Solution

```py
class Solution(object):
    from collections import Counter
    def majorityElement(self, nums):
        # Method 1

        res = Counter(nums)
        abc = res.most_common()
        if abc > (len(nums)/2):
            return abc[0][0]



        # Method 2

        # candidate = None
        # count = 0
        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     if num == candidate:
        #         count += 1
        #     else:
        #         count -= 1
        # return candidate
```

[View on LeetCode](https://leetcode.com/problems/majority-element/)
