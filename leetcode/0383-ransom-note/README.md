# 383. Ransom Note

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Counting-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 74 ms |
| Memory | 12.1 MB |
| Submission Date | 2026-11-11T08:40:36.929Z |
| Platform | leetcode |

## Problem Statement

<p>Given two strings <code>ransomNote</code> and <code>magazine</code>, return <code>true</code><em> if </em><code>ransomNote</code><em> can be constructed by using the letters from </em><code>magazine</code><em> and </em><code>false</code><em> otherwise</em>.</p>

<p>Each letter in <code>magazine</code> can only be used once in <code>ransomNote</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<pre><strong>Input:</strong> ransomNote = "a", magazine = "b"
<strong>Output:</strong> false
</pre><p>
```

**Example 2:**

```
</p>
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "ab"
<strong>Output:</strong> false
</pre><p>
```

**Example 3:**

```
</p>
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "aab"
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= ransomNote.length, magazine.length &lt;= 10<sup>5</sup></code>
- <code>ransomNote</code> and <code>magazine</code> consist of lowercase English letters.

## Solution

```py
class Solution(object):
    from collections import Counter
    def canConstruct(self, ransomNote, magazine):
        a = Counter(magazine)
        b = Counter(ransomNote)
        for i in b:
            if b[i] > a[i]:
                return False
        return True
```

[View on LeetCode](https://leetcode.com/problems/ransom-note/)
