# 2351. First Letter to Appear Twice

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Bit_Manipulation-blue) ![Topic](https://img.shields.io/badge/Topic-Counting-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 12.1 MB |
| Submission Date | 2026-11-08T20:37:27.879Z |
| Platform | leetcode |

## Problem Statement

<p>Given a string <code>s</code> consisting of lowercase English letters, return <em>the first letter to appear <strong>twice</strong></em>.</p>

<p><strong>Note</strong>:</p>

<ul>
	<li>A letter <code>a</code> appears twice before another letter <code>b</code> if the <strong>second</strong> occurrence of <code>a</code> is before the <strong>second</strong> occurrence of <code>b</code>.</li>
	<li><code>s</code> will contain at least one letter that appears twice.</li>
</ul>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;abccbaacz&quot;
<strong>Output:</strong> &quot;c&quot;
<strong>Explanation:</strong>
The letter &#39;a&#39; appears on the indexes 0, 5 and 6.
The letter &#39;b&#39; appears on the indexes 1 and 4.
The letter &#39;c&#39; appears on the indexes 2, 3 and 7.
The letter &#39;z&#39; appears on the index 8.
The letter &#39;c&#39; is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;abcdd&quot;
<strong>Output:</strong> &quot;d&quot;
<strong>Explanation:</strong>
The only letter that appears twice is &#39;d&#39; so we return &#39;d&#39;.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>2 &lt;= s.length &lt;= 100</code>
- <code>s</code> consists of lowercase English letters.
- <code>s</code> has at least one repeated letter.

## Solution

```py
class Solution(object):
    def repeatedCharacter(self, s):
        for i in range(len(s)):
            count = 0
            for j in range(i + 1):
                if s[i] == s[j]:
                    count += 1
            if count == 2:
                return s[i]
```

[View on LeetCode](https://leetcode.com/problems/first-letter-to-appear-twice/)
