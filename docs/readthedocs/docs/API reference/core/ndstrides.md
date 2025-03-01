



# ndstrides

##  Module Summary
  
Implements NDArrayStrides type.
## Aliases
  
`Strides`: An alias of the NDArrayStrides.
## NDArrayStrides

### NDArrayStrides Summary
  
  
Presents the strides of `NDArray` type.  

### Parent Traits
  

- AnyType
- Sized
- Stringable
- UnknownDestructibility
- Writable

### Fields
  
  
* ndim `Int`  
    - Number of dimensions of array. It must be larger than 0.  

### Functions

#### __init__


```rust
__init__(out self, *strides: Int)
```  
Summary  
  
Initializes the NDArrayStrides from strides.  
  
Args:  

- \*strides: Strides of the array.
- self


```rust
__init__(out self, strides: List[Int])
```  
Summary  
  
Initializes the NDArrayStrides from a list of strides.  
  
Args:  

- strides: Strides of the array.
- self


```rust
__init__(out self, strides: VariadicList[Int])
```  
Summary  
  
Initializes the NDArrayStrides from a variadic list of strides.  
  
Args:  

- strides: Strides of the array.
- self


```rust
__init__(strides: Self) -> Self
```  
Summary  
  
Initializes the NDArrayStrides from another strides. A deep-copy of the elements is conducted.  
  
Args:  

- strides: Strides of the array.


```rust
__init__(out self, shape: NDArrayShape, order: String = String("C"))
```  
Summary  
  
Initializes the NDArrayStrides from a shape and an order.  
  
Args:  

- shape: Shape of the array.
- order: Order of the memory layout (row-major "C" or column-major "F"). Default is "C". Default: String("C")
- self


```rust
__init__(out self, *shape: Int, *, order: String)
```  
Summary  
  
Overloads the function `__init__(shape: NDArrayShape, order: String)`. Initializes the NDArrayStrides from a given shapes and an order.  
  
Args:  

- \*shape: Shape of the array.
- order: Order of the memory layout (row-major "C" or column-major "F"). Default is "C".
- self


```rust
__init__(out self, shape: List[Int], order: String = String("C"))
```  
Summary  
  
Overloads the function `__init__(shape: NDArrayShape, order: String)`. Initializes the NDArrayStrides from a given shapes and an order.  
  
Args:  

- shape: Shape of the array.
- order: Order of the memory layout (row-major "C" or column-major "F"). Default is "C". Default: String("C")
- self


```rust
__init__(out self, shape: VariadicList[Int], order: String = String("C"))
```  
Summary  
  
Overloads the function `__init__(shape: NDArrayShape, order: String)`. Initializes the NDArrayStrides from a given shapes and an order.  
  
Args:  

- shape: Shape of the array.
- order: Order of the memory layout (row-major "C" or column-major "F"). Default is "C". Default: String("C")
- self


```rust
__init__(out self, ndim: Int, initialized: Bool)
```  
Summary  
  
Construct NDArrayStrides with number of dimensions. This method is useful when you want to create a strides with given ndim without knowing the strides values. `ndim == 0` is allowed in this method for 0darray (numojo scalar).  
  
Args:  

- ndim: Number of dimensions.
- initialized: Whether the strides is initialized. If yes, the values will be set to 0. If no, the values will be uninitialized.
- self

#### __copyinit__


```rust
__copyinit__(other: Self) -> Self
```  
Summary  
  
Initializes the NDArrayStrides from another strides. A deep-copy of the elements is conducted.  
  
Args:  

- other: Strides of the array.

#### __getitem__


```rust
__getitem__(self, index: Int) -> Int
```  
Summary  
  
Gets stride at specified index.  
  
Args:  

- self
- index: Index to get the stride.

#### __setitem__


```rust
__setitem__(mut self, index: Int, val: Int)
```  
Summary  
  
Sets stride at specified index.  
  
Args:  

- self
- index: Index to get the stride.
- val: Value to set at the given index.

#### __eq__


```rust
__eq__(self, other: Self) -> Bool
```  
Summary  
  
Checks if two strides have identical dimensions and values.  
  
Args:  

- self
- other: The strides to compare with.

#### __ne__


```rust
__ne__(self, other: Self) -> Bool
```  
Summary  
  
Checks if two strides have identical dimensions and values.  
  
Args:  

- self
- other

#### __contains__


```rust
__contains__(self, val: Int) -> Bool
```  
Summary  
  
Checks if the given value is present in the strides.  
  
Args:  

- self
- val

#### __len__


```rust
__len__(self) -> Int
```  
Summary  
  
Gets number of elements in the strides. It equals to the number of dimensions of the array.  
  
Args:  

- self

#### __repr__


```rust
__repr__(self) -> String
```  
Summary  
  
Returns a string of the strides of the array.  
  
Args:  

- self

#### __str__


```rust
__str__(self) -> String
```  
Summary  
  
Returns a string of the strides of the array.  
  
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
  
Returns a deep copy of the strides.  
  
Args:  

- self

#### swapaxes


```rust
swapaxes(self, axis1: Int, axis2: Int) -> Self
```  
Summary  
  
Returns a new strides with the given axes swapped.  
  
Args:  

- self
- axis1: The first axis to swap.
- axis2: The second axis to swap.
