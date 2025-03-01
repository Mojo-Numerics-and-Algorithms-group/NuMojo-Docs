



# own_data

##  Module Summary
  

## OwnData

### OwnData Summary
  
  
  

### Parent Traits
  

- AnyType
- UnknownDestructibility

### Fields
  
  
* ptr `UnsafePointer[SIMD[dtype, 1]]`  

### Functions

#### __init__


```rust
__init__(out self, size: Int)
```  
Summary  
  
Allocate given space on memory. The bytes allocated is `size` * `byte size of dtype`.  
  
Args:  

- size
- self


```rust
__init__(out self, ptr: UnsafePointer[SIMD[dtype, 1]])
```  
Summary  
  
Do not use this if you know what it means. If the pointer is associated with another array, it might cause dangling pointer problem.  
  
Args:  

- ptr
- self

#### __moveinit__


```rust
__moveinit__(out self, owned other: Self)
```  
Summary  
  
  
  
Args:  

- other
- self

#### get_ptr


```rust
get_ptr(self) -> UnsafePointer[SIMD[dtype, 1]]
```  
Summary  
  
  
  
Args:  

- self
