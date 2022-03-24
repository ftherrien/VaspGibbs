# VaspGibbs

A simple way to get Gibbs free energy from Vasp calculations

## Installation

`pip install` coming soon. For now copy `vasp_gibbs` to you working directory or add this folder to your `PATH`:
     git clone https://github.com/ftherrien/VaspGibbs.git
     echo "export PATH=$PATH:$PWD/VaspGibbs" >> $HOME/.bashrc
     source $HOME/.bashrc

## Usage

In a folder with a finished vasp calculation, run
    vasp_gibbs

`vasp_gibbs` will rerun vasp to get vibration modes and output the gibbs free energy of your system.

Use `-o` (only) or `-t`(top) to specify a set of atoms for which to calculate vibration modes. Examples:

 * `-o C O` would only compute vibration modes associated with C and O keeping all other atoms fixed.
 *`-o 1 3 6` would compute vibration modes associated with the first, third and sixth atoms in the POSCAR keeping all other atoms fixed.
 *`-t 10` would compute vibration modes associated with the first 10 atoms starting from the top of the unit cell along the c axis.

This can be useful when computing free energy differences between systems where one part of the system does not change, e.g. adsorption free energies.

To run vasp in parallel call:
   vasp_gibbs -n [number of proc] -m [mpi executable] -v [vasp executable]

By default `srun` and `vasp_std are used.

**Under development**

Currently working on reading the OUTCAR and computing gibbs free energy corrections. The features stated above should already work.

