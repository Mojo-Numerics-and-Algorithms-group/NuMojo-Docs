



# ndshape

##  Module Summary
  
Implements NDArrayShape type.
## Aliases
  
`Shape`: An alias of the NDArrayShape.
## NDArrayShape

### NDArrayShape Summary
  
  
Presents the shape of `NDArray` type.  

### Parent Traits
  

- AnyType
- Representable
- Sized
- Stringable
- UnknownDestructibility
- Writable
- _CurlyEntryFormattable

### Fields
  
  
* ndim `Int`  
    - Number of dimensions of array. It must be larger than 0.  

### Functions

#### __init__


```rust
__init__(out self, shape: Int)
```  
Summary  
  
Initializes the NDArrayShape with one dimension.  
  
Args:  

- shape: Size of the array.
- self


```rust
__init__(out self, *shape: Int)
```  
Summary  
  
Initializes the NDArrayShape with variable shape dimensions.  
  
Args:  

- \*shape: Variable number of integers representing the shape dimensions.
- self


```rust
__init__(out self, *shape: Int, *, size: Int)
```  
Summary  
  
Initializes the NDArrayShape with variable shape dimensions and a specified size.  
  
Args:  

- \*shape: Variable number of integers representing the shape dimensions.
- size: The total number of elements in the array.
- self


```rust
__init__(out self, shape: List[Int])
```  
Summary  
  
Initializes the NDArrayShape with a list of shape dimensions.  
  
Args:  

- shape: A list of integers representing the shape dimensions.
- self


```rust
__init__(out self, shape: List[Int], size: Int)
```  
Summary  
  
Initializes the NDArrayShape with a list of shape dimensions and a specified size.  
  
Args:  

- shape: A list of integers representing the shape dimensions.
- size: The specified size of the NDArrayShape.
- self


```rust
__init__(out self, shape: VariadicList[Int])
```  
Summary  
  
Initializes the NDArrayShape with a list of shape dimensions.  
  
Args:  

- shape: A list of integers representing the shape dimensions.
- self


```rust
__init__(out self, shape: VariadicList[Int], size: Int)
```  
Summary  
  
Initializes the NDArrayShape with a list of shape dimensions and a specified size.  
  
Args:  

- shape: A list of integers representing the shape dimensions.
- size: The specified size of the NDArrayShape.
- self


```rust
__init__(shape: Self) -> Self
```  
Summary  
  
Initializes the NDArrayShape from another NDArrayShape. A deep copy of the data buffer is conducted.  
  
Args:  

- shape: Another NDArrayShape to initialize from.


```rust
__init__(out self, ndim: Int, initialized: Bool)
```  
Summary  
  
Construct NDArrayShape with number of dimensions. This method is useful when you want to create a shape with given ndim without knowing the shape values. `ndim == 0` is allowed in this method for 0darray (numojo scalar).  
  
Args:  

- ndim: Number of dimensions.
- initialized: Whether the shape is initialized. If yes, the values will be set to 1. If no, the values will be uninitialized.
- self

#### __copyinit__


```rust
__copyinit__(other: Self) -> Self
```  
Summary  
  
Initializes the NDArrayShape from another NDArrayShape. A deep copy of the data buffer is conducted.  
  
Args:  

- other: Another NDArrayShape to initialize from.

#### __getitem__


```rust
__getitem__(self, index: Int) -> Int
```  
Summary  
  
Gets shape at specified index.  
  
Args:  

- self
- index: Index to get the shape.

#### __setitem__


```rust
__setitem__(mut self, index: Int, val: Int)
```  
Summary  
  
Sets shape at specified index.  
  
Args:  

- self
- index: Index to get the shape.
- val: Value to set at the given index.

#### __eq__


```rust
__eq__(self, other: Self) -> Bool
```  
Summary  
  
Checks if two shapes have identical dimensions and values.  
  
Args:  

- self
- other: The shape to compare with.

#### __ne__


```rust
__ne__(self, other: Self) -> Bool
```  
Summary  
  
Checks if two shapes have identical dimensions and values.  
  
Args:  

- self
- other

#### __contains__


```rust
__contains__(self, val: Int) -> Bool
```  
Summary  
  
Checks if the given value is present in the array.  
  
Args:  

- self
- val

#### __len__


```rust
__len__(self) -> Int
```  
Summary  
  
Gets number of elements in the shape. It equals the number of dimensions of the array.  
  
Args:  

- self

#### __repr__


```rust
__repr__(self) -> String
```  
Summary  
  
Returns a string of the shape of the array.  
  
Args:  

- self

#### __str__


```rust
__str__(self) -> String
```  
Summary  
  
Returns a string of the shape of the array.  
  
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

#### copy


```rust
copy(self) -> Self
```  
Summary  
  
Returns a deep copy of the shape.  
  
Args:  

- self

#### join


```rust
join(self, *shapes: Self) -> Self
```  
Summary  
  
Join multiple shapes into a single shape.  
  
Args:  

- self
- \*shapes: Variable number of NDArrayShape objects.

#### size_of_array


```rust
size_of_array(self) -> Int
```  
Summary  
  
Returns the total number of elements in the array.  
  
Args:  

- self

#### swapaxes


```rust
swapaxes(self, axis1: Int, axis2: Int) -> Self
```  
Summary  
  
Returns a new shape with the given axes swapped.  
  
Args:  

- self
- axis1: The first axis to swap.
- axis2: The second axis to swap.
