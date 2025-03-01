



# item

##  Module Summary
  
Implements Item type.
## Aliases
  
`item`: 
## Item

### Item Summary
  
  
Specifies the indices of an item of an array.  

### Parent Traits
  

- AnyType
- CollectionElement
- Copyable
- Movable
- Stringable
- UnknownDestructibility
- Writable

### Fields
  
  
* ndim `Int`  

### Functions

#### __init__


```rust
__init__[T: Indexer](*args: T) -> Self
```  
Summary  
  
Construct the tuple.  
  
Parameters:  

- T
  
Args:  

- \*args: Initial values.


```rust
__init__[T: IndexerCollectionElement](out self, args: List[T])
```  
Summary  
  
Construct the tuple.  
  
Parameters:  

- T
  
Args:  

- args: Initial values.
- self


```rust
__init__(out self, args: VariadicList[Int])
```  
Summary  
  
Construct the tuple.  
  
Args:  

- args: Initial values.
- self


```rust
__init__(out self, *, ndim: Int, initialized: Bool)
```  
Summary  
  
Construct Item with number of dimensions. This method is useful when you want to create a Item with given ndim without knowing the Item values.  
  
Args:  

- ndim: Number of dimensions.
- initialized: Whether the shape is initialized. If yes, the values will be set to 0. If no, the values will be uninitialized.
- self


```rust
__init__(out self, idx: Int, shape: NDArrayShape)
```  
Summary  
  
Get indices of the i-th item of the array of the given shape. The item traverse the array in C-order.  
  
Args:  

- idx: The i-th item of the array.
- shape: The strides of the array.
- self

#### __copyinit__


```rust
__copyinit__(other: Self) -> Self
```  
Summary  
  
Copy construct the tuple.  
  
Args:  

- other: The tuple to copy.

#### __del__


```rust
__del__(owned self)
```  
Summary  
  
  
  
Args:  

- self

#### __getitem__


```rust
__getitem__[T: Indexer](self, idx: T) -> Int
```  
Summary  
  
Gets the value at the specified index.  
  
Parameters:  

- T
  
Args:  

- self
- idx: The index of the value to get.

#### __setitem__


```rust
__setitem__[T: Indexer, U: Indexer](self, idx: T, val: U)
```  
Summary  
  
Set the value at the specified index.  
  
Parameters:  

- T
- U
  
Args:  

- self
- idx: The index of the value to set.
- val: The value to set.

#### __len__


```rust
__len__(self) -> Int
```  
Summary  
  
Get the length of the tuple.  
  
Args:  

- self

#### __iter__


```rust
__iter__(self) -> _ItemIter
```  
Summary  
  
Iterate over elements of the NDArray, returning copied value.  
  
Args:  

- self

#### __repr__


```rust
__repr__(self) -> String
```  
Summary  
  
  
  
Args:  

- self

#### __str__


```rust
__str__(self) -> String
```  
Summary  
  
  
  
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

#### offset


```rust
offset(self, strides: NDArrayStrides) -> Int
```  
Summary  
  
Calculates the offset of the item according to strides.  
  
Args:  

- self
- strides: The strides of the array.
