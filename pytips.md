# Python Automation #

[TOC]

## List ##
- list is mutable.
- modifying a list change the value but the id.

### Tricks ###

1. Multiple Assignment Trick  
assign multiple variables with the values in a list in one line of code.

```python
lst = [value1,value2,value3,...]
v1, v2, v3, ... = lst
```

### Functions ###

1. enumerate() Function  
call the enumerate() function returning the index of the item and the item itself

```python
for index, item in enumerate(list):
    ......
```

2. random.choice and random.shuffle Functions  
**random.choice()** return a randomly selected item from the list  
**random.shuffle()** reorder the items in a list

### Methods ###

1. index() Method to Find a Value  
**index()** to be passed a value, returning the index of the value or a **ValueError** error.

```python
>>> lst = [value1
          ,value2
          ,value3
          ,...
          ]
>>> lst.index('valuen')
```

2.append() and insert() to Add Values  
returning none
```python
list.append(valuen)
```

```python
list.insert(index,value)
```

Both give the new value of the list as its return value, returning none.

3. remove() to Remove Values
returning none
```python
list.remove(value)
del list[index]
```

4. sort() method to Sort the Values
returning none
```python
list.sort([reverse=True],[key=str.lower])
```

5. reverse() Method to Reverse the values  
returning none
```python
list.reverse()
```

## Tuple ##
- tuple is unmutable.
- tuple with a trailing comma after the value inside the parenthese indiciating itself tuple.
- Use function list() or tuple() to convert types.

## References ##
- mutable data types share the id when modifying.
- unmutable data types create a new id.

### The copy Module's copy() and deepcopy() Functions ###
- **copy.copy** can be used to make a duplicate copy of a mutable value like a list or dictionary.
- **copy.deepcopy** copy the inner lists inside the list as well.

```python
import copy
lst = copy.copy(ls0)
lst = copy.deepcopy(ls0)
```

## Dictionaries And Structure Data ##
- a *directionary* is a mutable collection.

### vs. Lists ###
- dictionary is unordered. so the order of value doesn't matter .
- use key values to access the associated value using square brackets.

### Check Whether a Key or Valu Exists in a Dictionary ###
- operators like *in* and *not in*.

### Methods: keys(), values(), items(), get(), setdefault() ###

1. keys, values(), items()
```python
for i in list.keys():
for i in list.values():
for i in list.items():
```
- These methods return **no true lists** but special data types (dict_keys, dict_values, dict_items) which can be used in **loops**.
- The dict_items value returned by the items method are tuples of the key and value.

2. The get() Method 
- *get()* method takes two arguments: the key of the value to retrieve and fallback value to return if that key does not exist.
```python
dict.get(key, fallback_value)
```

3. Method: setdefault() 
- The first argument passed to the method is the key to check for, and the second argument is the value to set at that key if the key does not exist.
- If the key does exist, the *set default()* method returns the key's value.
```python
dict.setdefault(key,value)
```


