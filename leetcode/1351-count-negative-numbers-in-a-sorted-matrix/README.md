# 1351. Count Negative Numbers in a Sorted Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Matrix-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 3 ms |
| Memory | 19.9 MB |
| Submission Date | 2026-10-28T16:44:36.818Z |
| Platform | leetcode |

## Problem Statement

<p>Given a <code>m x n</code> matrix <code>grid</code> which is sorted in non-increasing order both row-wise and column-wise, return <em>the number of <strong>negative</strong> numbers in</em> <code>grid</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
<strong>Output:</strong> 8
<strong>Explanation:</strong> There are 8 negatives number in the matrix.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> grid = [[3,2],[1,0]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>m == grid.length</code>
- <code>n == grid[i].length</code>
- <code>1 &lt;= m, n &lt;= 100</code>
- <code>-100 &lt;= grid[i][j] &lt;= 100</code>

## Solution

```py
class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for i in grid:
            for j in i:
                if j < 0:
                    count += 1
        return count

```

[View on LeetCode](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)
