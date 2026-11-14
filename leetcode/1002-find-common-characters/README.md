# 1002. Find Common Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 32 ms |
| Memory | 12.4 MB |
| Submission Date | 2026-11-14T06:04:44.797Z |
| Platform | leetcode |

## Problem Statement

<p>Given a string array <code>words</code>, return <em>an array of all characters that show up in all strings within the </em><code>words</code><em> (including duplicates)</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<pre><strong>Input:</strong> words = ["bella","label","roller"]
<strong>Output:</strong> ["e","l","l"]
</pre><p>
```

**Example 2:**

```
</p>
<pre><strong>Input:</strong> words = ["cool","lock","cook"]
<strong>Output:</strong> ["c","o"]
</pre>
<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= words.length &lt;= 100</code>
- <code>1 &lt;= words[i].length &lt;= 100</code>
- <code>words[i]</code> consists of lowercase English letters.

## Solution

```py
class Solution(object):
    def commonChars(self, words):
        from collections import Counter
        common = Counter(words[0])
        for i in range(1, len(words)):
            common = common & Counter(words[i])
        return list(common.elements())
```

[View on LeetCode](https://leetcode.com/problems/find-common-characters/)
