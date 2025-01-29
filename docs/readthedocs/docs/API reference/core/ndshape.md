



# ndshape

##  Module Summary
  
Implements NDArrayShape type.
## Aliases
  
`Shape`: 
## NDArrayShape

### NDArrayShape Summary
  
  
Implements the NDArrayShape.  

### Parent Traits
  

- AnyType
- Stringable
- UnknownDestructibility
- Writable

### Fields
  
  
* ndim `Int`  
    - Number of dimensions of array.  

### Functions

#### __init__


```rust
__init__(out self, shape: Int)
```  
Summary  
  
Initializes the NDArrayShape with one dimension.  
  
Args:  

- self
- shape: Size of the array.


```rust
__init__(out self, *shape: Int)
```  
Summary  
  
Initializes the NDArrayShape with variable shape dimensions.  
  
Args:  

- self
- \*shape: Variable number of integers representing the shape dimensions.


```rust
__init__(out self, *shape: Int, *, size: Int)
```  
Summary  
  
Initializes the NDArrayShape with variable shape dimensions and a specified size.  
  
Args:  

- self
- \*shape: Variable number of integers representing the shape dimensions.
- size: The total number of elements in the array.


```rust
__init__(out self, shape: List[Int])
```  
Summary  
  
Initializes the NDArrayShape with a list of shape dimensions.  
  
Args:  

- self
- shape: A list of integers representing the shape dimensions.


```rust
__init__(out self, shape: List[Int], size: Int)
```  
Summary  
  
Initializes the NDArrayShape with a list of shape dimensions and a specified size.  
  
Args:  

- self
- shape: A list of integers representing the shape dimensions.
- size: The specified size of the NDArrayShape.


```rust
__init__(out self, shape: VariadicList[Int])
```  
Summary  
  
Initializes the NDArrayShape with a list of shape dimensions.  
  
Args:  

- self
- shape: A list of integers representing the shape dimensions.


```rust
__init__(out self, shape: VariadicList[Int], size: Int)
```  
Summary  
  
Initializes the NDArrayShape with a list of shape dimensions and a specified size.  
  
Args:  

- self
- shape: A list of integers representing the shape dimensions.
- size: The specified size of the NDArrayShape.


```rust
__init__(out self, shape: Self)
```  
Summary  
  
Initializes the NDArrayShape with another NDArrayShape.  
  
Args:  

- self
- shape: Another NDArrayShape to initialize from.


```rust
__init__(out self, ndim: Int, initialized: Bool)
```  
Summary  
  
Construct NDArrayShape with number of dimensions.  
  
Args:  

- self
- ndim: Number of dimensions.
- initialized: Whether the shape is initialized. If yes, the values will be set to 1. If no, the values will be uninitialized.

#### __copyinit__


```rust
__copyinit__(out self, other: Self)
```  
Summary  
  
Initializes the NDArrayShape from another NDArrayShape.  
  
Args:  

- self
- other: Another NDArrayShape to initialize from.

#### __getitem__


```rust
__getitem__(self, index: Int) -> Int
```  
Summary  
  
Get shape at specified index.  
  
Args:  

- self
- index

#### __setitem__


```rust
__setitem__(mut self, index: Int, val: Int)
```  
Summary  
  
Set shape at specified index.  
  
Args:  

- self
- index
- val

#### __eq__


```rust
__eq__(self, other: Self) -> Bool
```  
Summary  
  
Check if two shapes are identical.  
  
Args:  

- self
- other

#### __ne__


```rust
__ne__(self, other: Self) -> Bool
```  
Summary  
  
Check if two arrayshapes don't have identical dimensions.  
  
Args:  

- self
- other

#### __contains__


```rust
__contains__(self, val: Int) -> Bool
```  
Summary  
  
Check if any of the dimensions are equal to a value.  
  
Args:  

- self
- val

#### __len__


```rust
__len__(self) -> Int
```  
Summary  
  
Get number of dimensions of the array described by arrayshape.  
  
Args:  

- self

#### __repr__


```rust
__repr__(self) -> String
```  
Summary  
  
Return a string of the shape of the array described by arrayshape.  
  
Args:  

- self

#### __str__


```rust
__str__(self) -> String
```  
Summary  
  
Return a string of the shape of the array.  
  
Args:  

- self

#### write_to


```rust
write_to[W: Writer](self, mut writer: W)
```  
Summary  
  
  
  
Parameters:  

- W
  
Args:  

- self
- writer

#### size_of_array


```rust
size_of_array(self) -> Int
```  
Summary  
  
Returns the total number of elements in the array.  
  
Args:  

- self

#### join


```rust
join(*shapes) -> Self
```  
Summary  
  
Join multiple shapes into a single shape.  
  
Args:  

- \*shapes: Variable number of NDArrayShape objects.
