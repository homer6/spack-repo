# Spack Repository

A collection of Spack packages

## Installation

To use this Spack repository in your Spack installation:

```bash
# Add the repository to your Spack installation
spack repo add https://github.com/homer6/spack-repo/spack

# Verify the repository was added successfully
spack repo list
```

## Available Packages

This repository currently provides the following packages:

- **kubernetes-c**: A Kubernetes Client Library for C

To install a package from this repository:

```bash
# Install the kubernetes-c package
spack install kubernetes-c
```

You can check what will be installed before actually installing:

```bash
# See what would be installed
spack spec homer6.kubernetes-c
```

## Repository Structure

```
spack-repo/
├── spack/
│   ├── packages/
│   │   └── kubernetes-c/
│   │       └── package.py
│   └── repo.yaml
└── README.md
```

## Development

If you want to contribute to this repository:

1. Fork the repository
2. Clone your fork
3. Make your changes
4. Submit a pull request

For package development, use Spack's development tools:

```bash
# Mark a package for development
spack develop homer6.kubernetes-c

# Install the package in development mode
spack install
```

## License

MIT License
