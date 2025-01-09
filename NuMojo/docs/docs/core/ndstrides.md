



# ndstrides

##  Module Summary
  
Implements NDArrayStrides type.
## NDArrayStrides

### NDArrayStrides Summary
  
  
Implements the NDArrayStrides.  

### Parent Traits
  

- AnyType
- Stringable
- UnknownDestructibility
- Writable

### Fields
  
  
* offset `Int`  
* ndim `Int`  
    - Number of dimensions of array.  

### Functions

#### __init__


```Mojo
__init__(out self, *strides: Int, *, offset: Int = 0)
```  
Summary  
  
  
  
Args:  

- self
- \*strides
- offset Default: 0


```Mojo
__init__(out self, strides: List[Int], offset: Int = 0)
```  
Summary  
  
  
  
Args:  

- self
- strides
- offset Default: 0


```Mojo
__init__(out self, strides: VariadicList[Int], offset: Int = 0)
```  
Summary  
  
  
  
Args:  

- self
- strides
- offset Default: 0


```Mojo
__init__(out self, strides: Self)
```  
Summary  
  
  
  
Args:  

- self
- strides


```Mojo
__init__(out self, strides: Self, offset: Int = 0)
```  
Summary  
  
  
  
Args:  

- self
- strides
- offset Default: 0


```Mojo
__init__(out self, *shape: Int, *, offset: Int = 0, order: String = String("C"))
```  
Summary  
  
  
  
Args:  

- self
- \*shape
- offset Default: 0
- order Default: String("C")


```Mojo
__init__(out self, shape: List[Int], offset: Int = 0, order: String = String("C"))
```  
Summary  
  
  
  
Args:  

- self
- shape
- offset Default: 0
- order Default: String("C")


```Mojo
__init__(out self, shape: VariadicList[Int], offset: Int = 0, order: String = String("C"))
```  
Summary  
  
  
  
Args:  

- self
- shape
- offset Default: 0
- order Default: String("C")


```Mojo
__init__(out self, owned shape: NDArrayShape, offset: Int = 0, order: String = String("C"))
```  
Summary  
  
  
  
Args:  

- self
- shape
- offset Default: 0
- order Default: String("C")

#### __getitem__


```Mojo
__getitem__(self, index: Int) -> Int
```  
Summary  
  
  
  
Args:  

- self
- index

#### __setitem__


```Mojo
__setitem__(mut self, index: Int, val: Int)
```  
Summary  
  
  
  
Args:  

- self
- index
- val

#### __eq__


```Mojo
__eq__(self, other: Self) -> Bool
```  
Summary  
  
  
  
Args:  

- self
- other

#### __ne__


```Mojo
__ne__(self, other: Self) -> Bool
```  
Summary  
  
  
  
Args:  

- self
- other

#### __contains__


```Mojo
__contains__(self, val: Int) -> Bool
```  
Summary  
  
  
  
Args:  

- self
- val

#### __copy__


```Mojo
__copy__(mut self, other: Self)
```  
Summary  
  
  
  
Args:  

- self
- other

#### len


```Mojo
len(self) -> Int
```  
Summary  
  
  
  
Args:  

- self

#### __str__


```Mojo
__str__(self) -> String
```  
Summary  
  
  
  
Args:  

- self

#### write_to


```Mojo
write_to[W: Writer](self, mut writer: W)
```  
Summary  
  
  
  
Parameters:  

- W
  
Args:  

- self
- writer
