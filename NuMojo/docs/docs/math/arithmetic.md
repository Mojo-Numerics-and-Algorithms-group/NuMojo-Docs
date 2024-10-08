



# arithmetic

##  Module Summary
  
Implements array arithmetic
## Aliases
  
`ln`: Natural Log equivelent to log
## add


```rust
add[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform addition on two arrays.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
add[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Perform addition on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
add[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform addition on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.


```rust
add[dtype: DType, backend: Backend = Vectorized](owned *values: Variant[NDArray[dtype], SIMD[dtype, 1]]) -> NDArray[$0]
```  
Summary  
  
Perform addition on a list of arrays and a scalars.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- \*values: A list of arrays or Scalars to be added.

## sub


```rust
sub[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform subtraction on two arrays.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
sub[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
sub[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.

## diff


```rust
diff[dtype: DType = float64](array: NDArray[dtype], n: Int) -> NDArray[$0]
```  
Summary  
  
Compute the n-th order difference of the input array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A array.
- n: The order of the difference.

## copysign


```rust
copysign[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Copy the sign of the first NDArray and apply it to the second NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.

## mod


```rust
mod[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise modulo of array1 and array2.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
mod[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
mod[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.

## mul


```rust
mul[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise product of array1 and array2.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
mul[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Perform multiplication on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
mul[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform multiplication on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.


```rust
mul[dtype: DType, backend: Backend = Vectorized](owned *values: Variant[NDArray[dtype], SIMD[dtype, 1]]) -> NDArray[$0]
```  
Summary  
  
Perform multiplication on a list of arrays an arrays and a scalars.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- \*values: A list of arrays or Scalars to be added.

## div


```rust
div[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise quotent of array1 and array2.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
div[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
div[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.

## floor_div


```rust
floor_div[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise quotent of array1 and array2.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
floor_div[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
floor_div[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.

## fma


```rust
fma[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shape.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.
- array3: A NDArray.


```rust
fma[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype], simd: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shape  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.
- simd: A SIMD[dtype,1] value to be added.

## remainder


```rust
remainder[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise remainders of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.

## cbrt


```rust
cbrt[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise cuberoot of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array: A NDArray.

## rsqrt


```rust
rsqrt[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise reciprocal squareroot of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## sqrt


```rust
sqrt[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise squareroot of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## exp2


```rust
exp2[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Calculate elementwise two to the power of NDArray[i].  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## exp


```rust
exp[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Calculate elementwise euler's constant(e) to the power of NDArray[i].  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## expm1


```rust
expm1[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Calculate elementwise euler's constant(e) to the power of NDArray[i] minus1.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## scalb


```rust
scalb[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Calculate the scalb of array1 and array2.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array1: A NDArray.
- array2: A NDArray.

## log


```rust
log[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise natural logarithm of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## log2


```rust
log2[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise logarithm base two of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## log10


```rust
log10[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise logarithm base ten of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## log1p


```rust
log1p[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise natural logarithm of 1 plus NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## tabs


```rust
tabs[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise absolute value of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## tfloor


```rust
tfloor[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise round down to nearest whole number of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## tceil


```rust
tceil[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise round up to nearest whole number of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## ttrunc


```rust
ttrunc[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise remove decimal value from float whole number of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## tround


```rust
tround[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise round NDArray to whole number.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.

## roundeven


```rust
roundeven[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Performs elementwise banker's rounding on the elements of a NDArray.  
  
Parameters:  

- dtype: The dtype of the input and output array.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: Array to perform rounding on.

## nextafter


```rust
nextafter[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Computes the nextafter of the inputs.  
  
Parameters:  

- dtype: The dtype of the input and output array. Constraints: must be a floating-point type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array1: The first input argument.
- array2: The second input argument.

## invert


```rust
invert[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise invert of an array.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

The array must be either a boolean or integral array.  
  
Args:  

- array: A NDArray.
