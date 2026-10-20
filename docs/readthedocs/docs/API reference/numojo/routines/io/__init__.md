# `numojo.routines.io.__init__`

File I/O operations and array formatting for NuMojo.

Exports
-------
- `load`, `loadtxt`: Functions for reading arrays from files.
- `save`, `savetxt`: Functions for writing arrays to files.
- `load_npy`, `save_npy`: Pure-Mojo NumPy `.npy` reader/writer (no Python).
- `load_torch`, `save_torch`: Pure-Mojo PyTorch `.pt` reader/writer for a
  single plain tensor (no Python).
- `set_printoptions`: Configure array printing options.
- `PrintOptions`: Array printing configuration.
- `format_floating_scientific`: Scientific notation formatting.

