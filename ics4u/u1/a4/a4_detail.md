# A4 - CCC 2014 S1 Party Invitation

You are hosting a party and do not have room to invite all of your friends. You use the following unemotional mathematical method to determine which friends to invite.

- Your friends are numbered: **1,2,…,K** ... and place them in a list in this order.
- You will then perform **M rounds**. In each round, **use the round's number to determine which friends to remove from the ordered list.**
- Each round will have a number; remove every friend that is at the multiple of the round's number
- For clarification please read the example below

You are to finish the function provided for you.

The function is to return a list of remaining guest

**Input Explanation**

```
# input 1: K (1 <= K <= 100)  --> number of friends
# input 2: M (1 <= M <= 10) --> number of removal rounds
# M many inputs: determines which multiple should be removed at each round
```

**Output**

```
Friends that are leftover after removals.
```

**Sample Input**
```
10
2
2
3
```

**Sample Output**
```
1
3
7
9
```

**Explanation:**
```
-- There are 10 friends: [1,2,3,4,5,6,7,8,9,10]
-- There are 2 rounds of removal:
---- First round, we remove everyone at multiples of 2
---- List becomes: [1,3,5,7,9]
---- Second round, we remove every 3rd people
---- List becomes: [1,3,7,9]
```
