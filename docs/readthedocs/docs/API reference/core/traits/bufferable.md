



# bufferable

##  Module Summary
  

## Bufferable

### Bufferable Summary
  
  
Data buffer types that can be used as a container of the underlying buffer.  

### Parent Traits
  

- AnyType
- UnknownDestructibility
  

### Functions

#### __init__


```rust
__init__(out self: _Self, size: Int)
```  
Summary  
  
  
  
Args:  

- size
- self


```rust
__init__(out self: _Self, ptr: UnsafePointer[SIMD[float16, 1]])
```  
Summary  
  
  
  
Args:  

- ptr
- self

#### __moveinit__


```rust
__moveinit__(out self: _Self, owned other: _Self)
```  
Summary  
  
  
  
Args:  

- other
- self

#### get_ptr


```rust
get_ptr(self: _Self) -> UnsafePointer[SIMD[float16, 1]]
```  
Summary  
  
  
  
Args:  

- self
