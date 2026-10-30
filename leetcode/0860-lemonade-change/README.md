# 860. Lemonade Change

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Language](https://img.shields.io/badge/Language-python-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 2 ms |
| Memory | 14.9 MB |
| Submission Date | 2026-10-30T08:24:14.940Z |
| Platform | leetcode |

## Problem Statement

<p>At a lemonade stand, each lemonade costs <code>$5</code>. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a <code>$5</code>, <code>$10</code>, or <code>$20</code> bill. You must provide the correct change to each customer so that the net transaction is that the customer pays <code>$5</code>.</p>

<p>Note that you do not have any change in hand at first.</p>

<p>Given an integer array <code>bills</code> where <code>bills[i]</code> is the bill the <code>i<sup>th</sup></code> customer pays, return <code>true</code> <em>if you can provide every customer with the correct change, or</em> <code>false</code> <em>otherwise</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> bills = [5,5,5,10,20]
<strong>Output:</strong> true
<strong>Explanation:</strong> 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> bills = [5,5,10,10,20]
<strong>Output:</strong> false
<strong>Explanation:</strong> 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= bills.length &lt;= 10<sup>5</sup></code>
- <code>bills[i]</code> is either <code>5</code>, <code>10</code>, or <code>20</code>.

## Solution

```py
class Solution(object):
    def lemonadeChange(self, bills):
        five_dollar = 0
        ten_dollor = 0
        for i in bills:
            if i == 5:
                five_dollar += 1
            elif i == 10:
                if five_dollar >= 1:
                    five_dollar -= 1
                    ten_dollor += 1
                else:
                    return False
            else:
                if five_dollar > 0 and ten_dollor > 0:
                    five_dollar -= 1
                    ten_dollor -= 1
                elif five_dollar >= 3:
                    five_dollar -= 3
                else:
                    return False
        return True
```

[View on LeetCode](https://leetcode.com/problems/lemonade-change/)
