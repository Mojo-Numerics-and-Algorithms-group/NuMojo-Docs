# Clone NuMojo
rm -rf .temp
rm -rf numojo
mkdir .temp
mkdir numojo
git clone --depth 1 https://github.com/Mojo-Numerics-and-Algorithms-group/NuMojo .temp
cp -R .temp/numojo ./
cp -R .temp/mojoproject.toml mojoproject.toml

# Build package
magic run mojo package numojo

# Build docs
rm -Rf docs/readthedocs/docs/autodocs
magic run mojo doc numojo -o docs/readthedocs/docs.json
python docs/readthedocs/docs.py

# Clean up
rm -rf .temp
rm -rf numojo
rm numojo.mojopkg
rm mojoproject.toml