# 242. Valid Anagram

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 27 ms |
| Memory | 12.4 MB |
| Submission Date | 2026-11-10T17:32:42.346Z |
| Platform | leetcode |

## Problem Statement

<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an <span data-keyword="anagram">anagram</span> of <code>s</code>, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;anagram&quot;, t = &quot;nagaram&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p>
```

**Example 2:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;rat&quot;, t = &quot;car&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code>
- <code>s</code> and <code>t</code> consist of lowercase English letters.

## Solution

```py
class Solution(object):
    from collections import Counter
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)

        
```

[View on LeetCode](https://leetcode.com/problems/valid-anagram/)
