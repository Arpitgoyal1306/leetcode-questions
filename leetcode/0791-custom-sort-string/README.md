# 791. Custom Sort String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 12.1 MB |
| Submission Date | 2026-11-15T10:13:10.765Z |
| Platform | leetcode |

## Problem Statement

<p>You are given two strings <code>order</code> and <code>s</code>. All the characters of <code>order</code> are <strong>unique</strong> and were sorted in some custom order previously.</p>

<p>Permute the characters of <code>s</code> so that they match the order that <code>order</code> was sorted. More specifically, if a character <code>x</code> occurs before a character <code>y</code> in <code>order</code>, then <code>x</code> should occur before <code>y</code> in the permuted string.</p>

<p>Return <em>any permutation of </em><code>s</code><em> that satisfies this property</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> order = &quot;cba&quot;, s = &quot;abcd&quot; </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> &quot;cbad&quot; </span></p>

<p><strong>Explanation: </strong> <code>&quot;a&quot;</code>, <code>&quot;b&quot;</code>, <code>&quot;c&quot;</code> appear in order, so the order of <code>&quot;a&quot;</code>, <code>&quot;b&quot;</code>, <code>&quot;c&quot;</code> should be <code>&quot;c&quot;</code>, <code>&quot;b&quot;</code>, and <code>&quot;a&quot;</code>.</p>

<p>Since <code>&quot;d&quot;</code> does not appear in <code>order</code>, it can be at any position in the returned string. <code>&quot;dcba&quot;</code>, <code>&quot;cdba&quot;</code>, <code>&quot;cbda&quot;</code> are also valid outputs.</p>
</div>

<p>
```

**Example 2:**

```
</p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> order = &quot;bcafg&quot;, s = &quot;abcd&quot; </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> &quot;bcad&quot; </span></p>

<p><strong>Explanation: </strong> The characters <code>&quot;b&quot;</code>, <code>&quot;c&quot;</code>, and <code>&quot;a&quot;</code> from <code>order</code> dictate the order for the characters in <code>s</code>. The character <code>&quot;d&quot;</code> in <code>s</code> does not appear in <code>order</code>, so its position is flexible.</p>

<p>Following the order of appearance in <code>order</code>, <code>&quot;b&quot;</code>, <code>&quot;c&quot;</code>, and <code>&quot;a&quot;</code> from <code>s</code> should be arranged as <code>&quot;b&quot;</code>, <code>&quot;c&quot;</code>, <code>&quot;a&quot;</code>. <code>&quot;d&quot;</code> can be placed at any position since it&#39;s not in order. The output <code>&quot;bcad&quot;</code> correctly follows this rule. Other arrangements like <code>&quot;dbca&quot;</code> or <code>&quot;bcda&quot;</code> would also be valid, as long as <code>&quot;b&quot;</code>, <code>&quot;c&quot;</code>, <code>&quot;a&quot;</code> maintain their order.</p>
</div>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= order.length &lt;= 26</code>
- <code>1 &lt;= s.length &lt;= 200</code>
- <code>order</code> and <code>s</code> consist of lowercase English letters.
- All the characters of <code>order</code> are <strong>unique</strong>.

## Solution

```py
class Solution(object):
    def customSortString(self, order, s):
        from collections import Counter
        freq = Counter(s)
        ans = ""
        for ch in order:
            ans += ch * freq[ch]
            freq[ch] = 0
        ans += ''.join(freq.elements())
        return ans
```

[View on LeetCode](https://leetcode.com/problems/custom-sort-string/)
