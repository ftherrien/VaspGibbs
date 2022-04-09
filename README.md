# VaspGibbs

A simple way to get Gibbs free energy from Vasp calculations

## Installation

`pip install` coming soon. For now copy `vasp_gibbs` to you working directory or add this folder to your `PATH`:
```
git clone https://github.com/ftherrien/VaspGibbs.git
echo "export PATH=$PATH:$PWD/VaspGibbs" >> $HOME/.bashrc
source $HOME/.bashrc
```

## Usage

In a folder with a finished vasp calculation, run
```
vasp_gibbs
```

`vasp_gibbs` will rerun vasp to get vibration modes and output the gibbs free energy of your system.

Use `-o` (only) or `-t`(top) to specify a set of atoms for which to calculate vibration modes. Examples:

 * `-o C O` would only compute vibration modes associated with C and O keeping all other atoms fixed.
 * `-o 1 3 6` would compute vibration modes associated with the first, third and sixth atoms in the POSCAR keeping all other atoms fixed.
 * `-t 10` would compute vibration modes associated with the first 10 atoms starting from the top of the unit cell along the c axis.

This can be useful when computing free energy differences between systems where one part of the system does not change, e.g. adsorption free energies.

To run vasp in parallel call:
```
vasp_gibbs -n [number of proc] -m [mpi executable] -v [vasp executable]
```

By default `srun` and `vasp_std` are used.

VaspGibbs will compute the moment of inertia and symmetry of your molecule and compute rotational and translational contributions if you specify that the system is a molecule with the '-m' flag.

The thermodynamic quantities can ve found in the `VaspGibbs.md` file. Note that the output file is in markdown language!

## Online Ressources

* https://pubs.acs.org/doi/abs/10.1021/jp407468t (Supporting Information)
* https://gaussian.com/thermo/
* https://wiki.fysik.dtu.dk/ase/ase/thermochemistry/thermochemistry.html
* https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Statistical_Thermodynamics_(Jeschke)/06%3A_Partition_Functions_of_Gases/6.04%3A_Rotational_Partition_Function


## **Under development**

The features stated above should already work. Currently all quantities are calculated and printed in `VaspGibbs.md` but features are mostly untested: use with care. The `molecule` feature (rotation, translation) is untested.

*Next steps:* more testing, setup.py, pypi  

