



# flags

##  Module Summary
  
Implements Flags type.
## Flags

### Flags Summary
  
  
Information about the memory layout of the array. The Flags object can be accessed dictionary-like. or by using lowercased attribute names. Short names are available for convenience when using dictionary-like access.  

### Parent Traits
  

- AnyType
- UnknownDestructibility

### Fields
  
  
* C_CONTIGUOUS `Bool`  
    - C_CONTIGUOUS (C): The data is in a C-style contiguous segment.  
* F_CONTIGUOUS `Bool`  
    - F_CONTIGUOUS (F): The data is in a Fortran-style contiguous segment.  
* OWNDATA `Bool`  
    - OWNDATA (O): The array owns the underlying data buffer.  
* WRITEABLE `Bool`  
    - The data area can be written to. If it is False, the data is read-only and be blocked from writing. The WRITEABLE field of a view or slice is inherited from the array where it is derived. If the parent object is not writeable, the child object is  also not writeable. If the parent object is writeable, the child object may  be not writeable.  
* FORC `Bool`  
    - F_CONTIGUOUS or C_CONTIGUOUS.  

### Functions

#### __init__


```rust
__init__(c_contiguous: Bool, f_contiguous: Bool, owndata: Bool, writeable: Bool) -> Self
```  
Summary  
  
Initializes the Flags object with provided information.  
  
Args:  

- c_contiguous: The data is in a C-style contiguous segment.
- f_contiguous: The data is in a Fortran-style contiguous segment.
- owndata: The array owns the underlying data buffer.
- writeable: The data area can be written to. If owndata is False, writeable is forced to be False.


```rust
__init__(out self, shape: NDArrayShape, strides: NDArrayStrides, owndata: Bool, writeable: Bool)
```  
Summary  
  
Initializes the Flags object according the shape and strides information.  
  
Args:  

- shape: The shape of the array.
- strides: The strides of the array.
- owndata: The array owns the underlying data buffer.
- writeable: The data area can be written to. If owndata is False, writeable is forced to be False.
- self


```rust
__init__(shape: Tuple[Int, Int], strides: Tuple[Int, Int], owndata: Bool, writeable: Bool) -> Self
```  
Summary  
  
Initializes the Flags object according the shape and strides information.  
  
Args:  

- shape: The shape of the array.
- strides: The strides of the array.
- owndata: The array owns the underlying data buffer.
- writeable: The data area can be written to. If owndata is False, writeable is forced to be False.

#### __copyinit__


```rust
__copyinit__(other: Self) -> Self
```  
Summary  
  
Initializes the Flags object by copying the information from another Flags object.  
  
Args:  

- other: The Flags object to copy information from.

#### __getitem__


```rust
__getitem__(self, key: String) -> Bool
```  
Summary  
  
Get the value of the fields with the given key. The Flags object can be accessed dictionary-like. Short names are available for convenience.  
  
Args:  

- self
- key: The key of the field to get.
