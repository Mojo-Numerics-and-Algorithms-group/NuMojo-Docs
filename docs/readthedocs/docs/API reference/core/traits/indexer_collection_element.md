



# indexer_collection_element

##  Module Summary
  

## IndexerCollectionElement

### IndexerCollectionElement Summary
  
  
The IndexerCollectionElement trait denotes a trait composition of the `Indexer` and `CollectionElement` traits.  

### Parent Traits
  

- AnyType
- CollectionElement
- Copyable
- Indexer
- Intable
- Movable
- UnknownDestructibility
  

### Functions

#### __copyinit__


```rust
__copyinit__(out self: _Self, existing: _Self, /)
```  
Summary  
  
Create a new instance of the value by copying an existing one.  
  
Args:  

- existing: The value to copy.
- self

#### __moveinit__


```rust
__moveinit__(out self: _Self, owned existing: _Self, /)
```  
Summary  
  
Create a new instance of the value by moving the value of another.  
  
Args:  

- existing: The value to move.
- self

#### __index__


```rust
__index__(self: _Self) -> index
```  
Summary  
  
Convert to index.  
  
Args:  

- self

#### __int__


```rust
__int__(self: _Self) -> Int
```  
Summary  
  
Get the integral representation of the value.  
  
Args:  

- self
