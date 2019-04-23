# Notes
Abstract data types are more generic.

Stacks and queues enforce rules on lists.

Maps/Dictionary
Unordered collection, no such thing as a first and last.
Get and set values.

# What I need to know about Sets

Set
Half way in between - unordered collection with single elements.
Not  items in a list of keys, values in dicts, it's what math nerds call it.
Sets are concerned with membership not order. There is some order but its arbitrary, doesn't really matter as long as you're in the set.

A set is an unordered, unique collection of elements. 

Since sets can only have distinct values and can never contain duplicates.

Sets can contain literally any kind of element or object!

The two most important operations that are performed on sets are intersections and unions.

## Intersection
The intersection of two sets is often denoted in shorthand like this: X ∩ Y.

The intersection represents where two sets — you guessed it — intersect!

In other words, it yields all of the elements that exist within both of the sets.

A good way keyword to remember how intersections work is the word *and*: the elements that exists in both X and Y.

## Union
The union of two sets is often denoted in shorthand like this: X ∪ Y.

The union represents the entirety of two sets, or the two sets when they’ve been united together.

A good way keyword to remember how intersections work is the word *or*: the elements that exists in both X or Y.


Intersections and unions are great, but they’re only scratching the surface of set theory.

There are two operations that turn up quite a bit in computer science: *set differences* and *relative complements*

## Set Differences

Set differences are how we can figure out the difference between two sets.

In other words, we can determine what a set looks like without any of the elements that are contained in the other set. 

Another way to write this is X — Y.

## Relative complements

Relative complements are basically the opposite of set differences.

For example, the relative complement of Y as compared to X will return all of the elements in set Y that don’t appear in set X.

We can denote the relative complement by using the short hand Y ∖ X, which is actually results in the exact same returned set as Y— X.

Effectively, we’re simply subtracting set X from set Y, and answering the question: what exists in Y that doesn’t exist in X?

Sometimes, when we have two sets, we might want to find the opposite of the intersection of the two sets.

Well, the proper term for what we’re looking for in this case is something called the symmetric difference of our two sets, which is also sometimes referred to as the disjunctive union.

## Symmetric Difference

The symmetric difference yields all of the elements that exist within either of the two sets, but do not exist at the intersection (X ∩ Y) of them.

The symmetric difference is basically the same as find the relative complement of set X and set Y.

If we super mathematical about it, finding the symmetric difference is the same as finding the union of relative complements of set X and of set Y. We could write that out as: `X △ Y= (X ∖ Y) ∪ (Y ∖ X)`.

All we really need to do in order to find the symmetric difference of two sets is ask ourselves: what elements exist in set X that don’t exist in set Y, and which elements exist in Y that don’t exist in X?In other words: which elements are unique to each set, and don’t occur within both of them?

In JavaScript

```
    var s = new Set();

    s.add(2); 
    // Set { 2}
    s.add(45); 
    // Set { 2, 45}
    s.add(45); 
    // Set { 2, 45}
    s.add('hello world!'); 
    // Set { 2, 45, 'hello world!' }

    s.has(2); 
    // true
    s.has('cats'); 
    // false

    s.size; 
    // 3

    s.delete(45); 
    // Set { 2, 'hello world!' }

    s.has(45);    
    // false
```

When/Why to use Sets?

For one thing, they can be pretty time-efficient.

`O(x + y)`

In order to find the intersection, union or difference/compliment we have to traverse throug the entire length of both set x and y.

But, basic operations can be done in constant time such as add, remove length, and find.

Hash tables are often used to implement a set under the hood due to unique keys, unimportance of order, and they provide a quick O(1) access time!

"Relational databases are based almost entirely upon set theory."

In fact, if you’ve ever worked with or queried a database, or had to write SQL, you’re probably familiar with the idea of finding records at the intersection of a table.

A SQL `INNER JOIN` is just the intersection of two sets.

Finding the `LEFT JOIN` of two tables is nothing more than finding the set difference or the relative complement of the two tables.

A SQL query that calls for a `FULL OUTER JOIN` is merely returning the union of two sets.

Read More: https://medium.com/basecs/set-theory-the-method-to-database-madness-5ec4b4f05d79

Concrete Data Structs
Arrays
 - static
 - dynamic
Linked List
  - signly
  doubly
Hash Table

Trees
