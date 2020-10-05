# A2 - Magic Squares (CCC 2016 J2 Modified)

You will be modifying the given function called **magic()**

The function determines if the **4 x 4 square** is considered **"magic"**.

The square is considered magic if:

- All the rows (horizontal) adds up to the same number **AND**
- All the columns (vertical) adds up to the same number

**The array for the magic function has 4 string values; example:**

```
['16 3 2 13', '5 10 11 8', '9 6 7 12', '4 15 14 1']
```


Which would create:


```
16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1
```

If the array is magic, the function returns **True**; otherwise, it returns **False**

Example 1

```
# Input
['16 3 2 13', '5 10 11 8', '9 6 7 12', '4 15 14 1']

# Output
magic
```

Example 2

```
# Input
['5 10 1 3', '10 4 2 3', '1 2 8 5', '3 3 5 0']

# Output
not magic
```
