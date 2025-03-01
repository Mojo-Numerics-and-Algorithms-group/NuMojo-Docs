# Installation

### Use magic CLI

You can use the following command in the terminal to install `numojo`.

```console
magic add numojo 
```

### Add in toml file

You can add `numojo` in the dependencies section of your toml file.

```toml
[dependencies]
numojo = "=0.6"
```

### Build package

This approach involves building a standalone package file `mojopkg`.

1. Clone the repository.
2. Build the package using `magic run package`.
3. Move the `numojo.mojopkg` into the directory containing the your code.

### Include NuMojo's path for compiler and LSP

This approach does not require building a package file. Instead, when you compile your code, you can include the path of NuMojo repository with the following command:

```console
mojo run -I "../NuMojo" example.mojo
```

This is more flexible as you are able to edit the NuMojo source files when testing your code.

In order to allow VSCode LSP to resolve the imported `numojo` package, you can:

1. Go to preference page of VSCode.
2. Go to `Mojo › Lsp: Include Dirs`
3. Click `add item` and write the path where the Numojo repository is located, e.g. `/Users/Name/Programs/NuMojo`.
4. Restart the Mojo LSP server.

Now VSCode can show function hints for the Numojo package!

Then you can copy the mojopkg file into the location that you are running your code.