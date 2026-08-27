# `numojo.routines.io.files`

File I/O for arrays.

Functions for reading and writing arrays to and from files.

Exports
-------
- `loadtxt`: Load array from text file.
- `savetxt`: Save array to text file.

## Functions


<div class="fn-card" markdown="1">

### `load`

```mojo
def load[dtype: DType = DType.float64](file: String, allow_pickle: Bool = False, fix_imports: Bool = True, encoding: String = "ASCII", *, max_header_size: Int = Int(10000)) -> NDArray[dtype]
```

Load arrays or pickled objects from .npy, .npz or pickled files.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `file` (`String`) `[imm]`: The file to read. File-like objects must support the seek() and read() methods.
- `allow_pickle` (`Bool`) `[imm]`: Allow loading pickled object arrays stored in npy files.
- `fix_imports` (`Bool`) `[imm]`: Only useful when loading Python 2 generated pickled files on Python 3.
- `encoding` (`String`) `[imm]`: What encoding to use when reading Python 2 strings.
- `max_header_size` (`Int`) `[imm]`: Maximum allowed size of the header.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `save`

```mojo
def save[dtype: DType = DType.float64](fname: String, array: NDArray[dtype], allow_pickle: Bool = True)
```

Save an array to a binary file in NumPy .npy format.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `fname` (`String`) `[imm]`: File or filename to which the data is saved.
- `array` (`NDArray[dtype]`) `[imm]`: Array data to be saved.
- `allow_pickle` (`Bool`) `[imm]`: Allow saving object arrays using Python pickles.

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `loadtxt`

```mojo
def loadtxt[dtype: DType = DType.float64](fname: String, comments: String = "#", delimiter: String = " ", skiprows: Int = Int(0), ndmin: Int = Int(0)) -> NDArray[dtype]
```

Load data from a text file.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `fname` (`String`) `[imm]`: File, filename, list, or generator to read.
- `comments` (`String`) `[imm]`: The characters or list of characters used to indicate the start of a comment.
- `delimiter` (`String`) `[imm]`: The string used to separate values.
- `skiprows` (`Int`) `[imm]`: Skip the first skiprows lines.
- `ndmin` (`Int`) `[imm]`: The returned array will have at least ndmin dimensions.

<div class="prose-label">Returns</div>

- `NDArray[dtype]`

!!! failure "Raises"


</div>

<div class="fn-card" markdown="1">

### `savetxt`

```mojo
def savetxt[dtype: DType = DType.float64](fname: String, array: NDArray[dtype], fmt: String = "%.18e", delimiter: String = " ", newline: String = "\n", header: String = "", footer: String = "", comments: String = "#")
```

Save an array to a text file.

<div class="prose-label">Parameters</div>

- `dtype` (`DType`)

<div class="prose-label">Args</div>

- `fname` (`String`) `[imm]`: If the filename ends in .gz, the file is automatically saved in compressed gzip format.
- `array` (`NDArray[dtype]`) `[imm]`: 1D or 2D array_like data to be saved to a text file.
- `fmt` (`String`) `[imm]`: A single format (%10.5f), a sequence of formats, or a multi-format string.
- `delimiter` (`String`) `[imm]`: String or character separating columns.
- `newline` (`String`) `[imm]`: String or character separating lines.
- `header` (`String`) `[imm]`: String that will be written at the beginning of the file.
- `footer` (`String`) `[imm]`: String that will be written at the end of the file.
- `comments` (`String`) `[imm]`: String that will be prepended to the header and footer strings.

!!! failure "Raises"


</div>
