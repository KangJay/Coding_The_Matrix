#Chapter 0: The Function and other mathematical and computational preliminaries 

## 0.1 Set terminlogy and notation 
* A set is a collection of mathematical objects in which each object is unique (occurs only once) 
* '∈' is used to denote if an object belongs in a set. Eg. a ∈ {a, b, c, d} means a belongs to this set. 
    * The order in the set does not matter. 
* If set S1's elements are contained in another set, S2, then S1 ⊆ S2. Meaning S1 is **contained** in set S2. 
* **Cardinality** refers to how many elements a set has 
    * Denoted by | set | --> Eg. | S1 | = cardinality of set S1 = # of elements in S1. 

## 0.2 Cartesian Product 
* The cartesian product of two sets *A* and *B* is the set of all pairs (a, b) where a ∈ A and b ∈ B 
    * Eg. if A = {1, 2, 3} and B = {a, b}, then their cartesian product is {(1, a), (2, a), (3, a), (1, b), (2, b), (3, b)}
* Cardinality of the cartesian product of two sets is the product of the cardinalities of both sets.
    * For the example above, this is | A | * | B | = 3 * 2 = 6. 

## 0.3 The Function
* A function is a **rule** that, for a set of inputs representing the elements of a set, assigns an output. 
    * This means this function maps each element of a set to a possible output. 
    * The set of possible inputs from set *D* is the **domain of the function**. AKA the *pre-image*
* *Formally* a function is a (possibly infinite) set of pairs (a, b) in which no two pairs share the same first entry. 
    * Meaning the mapping of an input to an output is unique. The same input cannot have 2 outputs. 
    * Eg. A doubling function WITH domain {1, 2, 3, ...} is {(1, 2), (2, 4), (3, 6), ...}. 
    * Domain itself can consist of pairs of numbers. 
* If the function is denoted as *f*, the image of q, under *f*, is denoted as *f*(q). if r = *f*(q) then function *f* maps q to r. 
