# 387. First Unique Character in a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Queue-blue) ![Topic](https://img.shields.io/badge/Topic-Counting-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 168 ms |
| Memory | 15.4 MB |
| Submission Date | 2026-11-11T21:22:54.317Z |
| Platform | leetcode |

## Problem Statement

<p>Given a string <code>s</code>, find the <strong>first</strong> non-repeating character in it and return its index. If it <strong>does not</strong> exist, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;leetcode&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The character <code>&#39;l&#39;</code> at index 0 is the first character that does not occur at any other index.</p>
</div>

<p>
```

**Example 2:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;loveleetcode&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>
</div>

<p>
```

**Example 3:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aabb&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>
</div>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
- <code>s</code> consists of only lowercase English letters.

## Solution

```py
class Solution(object):
    def firstUniqChar(self, s):
        from collections import Counter
        ran = Counter(s)
        for i in range(len(s)):
            if ran[s[i]] == 1:
                return i
        return -1
```

[View on LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)
