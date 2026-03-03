# `numojo.routines.io.files`

File I/O (numojo.routines.io.files)

This module provides functions for reading and writing arrays to and from files.

## Functions


<div class="fn-card" markdown="1">

### `load`

```mojo
load[dtype: DType = DType.float64](file: String, allow_pickle: Bool = False, fix_imports: Bool = True, encoding: String = "ASCII", *, max_header_size: Int = 10000) -> NDArray[dtype]
```

Load arrays or pickled objects from .npy, .npz or pickled files.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `file` (`String`): The file to read. File-like objects must support the seek() and read() methods.
- `allow_pickle` (`Bool`): Allow loading pickled object arrays stored in npy files.
- `fix_imports` (`Bool`): Only useful when loading Python 2 generated pickled files on Python 3.
- `encoding` (`String`): What encoding to use when reading Python 2 strings.
- `max_header_size` (`Int`): Maximum allowed size of the header.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `save`

```mojo
save[dtype: DType = DType.float64](fname: String, array: NDArray[dtype], allow_pickle: Bool = True)
```

Save an array to a binary file in NumPy .npy format.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `fname` (`String`): File or filename to which the data is saved.
- `array` (`NDArray`): Array data to be saved.
- `allow_pickle` (`Bool`): Allow saving object arrays using Python pickles.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `loadtxt`

```mojo
loadtxt[dtype: DType = DType.float64](fname: String, comments: String = "#", delimiter: String = " ", skiprows: Int = 0, ndmin: Int = 0) -> NDArray[dtype]
```

Load data from a text file.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `fname` (`String`): File, filename, list, or generator to read.
- `comments` (`String`): The characters or list of characters used to indicate the start of a comment.
- `delimiter` (`String`): The string used to separate values.
- `skiprows` (`Int`): Skip the first skiprows lines.
- `ndmin` (`Int`): The returned array will have at least ndmin dimensions.

**Returns:**

- `NDArray`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `savetxt`

```mojo
savetxt[dtype: DType = DType.float64](fname: String, array: NDArray[dtype], fmt: String = "%.18e", delimiter: String = " ", newline: String = "\n", header: String = "", footer: String = "", comments: String = "#")
```

Save an array to a text file.

**Parameters:**

- `dtype` (`DType`)

**Args:**

- `fname` (`String`): If the filename ends in .gz, the file is automatically saved in compressed gzip format.
- `array` (`NDArray`): 1D or 2D array_like data to be saved to a text file.
- `fmt` (`String`): A single format (%10.5f), a sequence of formats, or a multi-format string.
- `delimiter` (`String`): String or character separating columns.
- `newline` (`String`): String or character separating lines.
- `header` (`String`): String that will be written at the beginning of the file.
- `footer` (`String`): String that will be written at the end of the file.
- `comments` (`String`): String that will be prepended to the header and footer strings.

!!! failure "Raises"


</div>
