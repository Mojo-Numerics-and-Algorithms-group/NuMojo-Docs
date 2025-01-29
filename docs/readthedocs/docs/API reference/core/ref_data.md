



# ref_data

##  Module Summary
  

## RefData

### RefData Summary
  
  
  

### Parent Traits
  

- AnyType
- Bufferable
- UnknownDestructibility

### Fields
  
  
* ptr `UnsafePointer[SIMD[float16, 1]]`  

### Functions

#### __init__


```rust
__init__(out self, size: Int)
```  
Summary  
  
Allocate given space on memory. The bytes allocated is `size` * `byte size of dtype`.  
  
Args:  

- self
- size


```rust
__init__(out self, ptr: UnsafePointer[SIMD[float16, 1]])
```  
Summary  
  
Reads the underlying data of another array.  
  
Args:  

- self
- ptr

#### __moveinit__


```rust
__moveinit__(out self, owned other: Self)
```  
Summary  
  
  
  
Args:  

- self
- other

#### get_ptr


```rust
get_ptr(self) -> UnsafePointer[SIMD[float16, 1]]
```  
Summary  
  
  
  
Args:  

- self
