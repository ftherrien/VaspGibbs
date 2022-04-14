# VaspGibbs

A simple way to get Gibbs free energy from Vasp calculations

## Installation

```
pip install git+https://github.com/ftherrien/VaspGibbs
```

*Latest version:* 0.0.2 (beta)

## Usage

In a folder with a finished vasp calculation, run
```
vasp_gibbs
```

`vasp_gibbs` will rerun Vasp to obtain vibration modes and output the gibbs free energy of your system.

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

VaspGibbs will automatically compute the moment of inertia and symmetry of your molecule and compute rotational and translational contributions if you specify that the system is a molecule with the `-m` flag.

The temperature and pressure can be set using the `-T` and `-P` flags.

### Output

All outputs can be found in the VaspGibbs.md file. It contains the following information:

#### Energy corrections
|      Type      |       Z        |     E (eV)     |    S (eV/K)    |     F (eV)     |
| :------------: | :------------: | :------------: | :------------: | :------------: |
|      ZPE       |      N/A       |        x       |      N/A       |      N/A       |
|   Electronic   |        x       |        x       |        x       |        x       |
|  Vibrational   |        x       |        x       |        x       |        x       |
|   Rotational   |        x       |        x       |        x       |        x       |
| Translational  |        x       |        x       |        x       |        x       |

#### Thermodynamic Quantities
|     Quantity      |        Value        |
| :---------------: | :-----------------: |
|     Enthalpy      |          x      eV  |
|      Entropy      |          x     eV/K |
| Gibbs Free Energy |          x      eV  |
|     G - E_dft     |          x      eV  |
|        TS         |          x      eV  |

## Online Ressources

* https://pubs.acs.org/doi/abs/10.1021/jp407468t (Supporting Information)
* https://gaussian.com/thermo/
* https://wiki.fysik.dtu.dk/ase/ase/thermochemistry/thermochemistry.html
* https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Statistical_Thermodynamics_(Jeschke)/06%3A_Partition_Functions_of_Gases/6.04%3A_Rotational_Partition_Function
* https://vaspkit.com/tutorials.html#thermo-energy-correction 

## Under development

The features stated above should already work. Currently all quantities are calculated and printed in `VaspGibbs.md` but more validation needs to be done.

*Next steps:* more testing, add to pypi, PV term for solids with Murnaghan equation

Let me know if you would like new features to be added!  

