<h1 align="center">
<img src="https://raw.githubusercontent.com/ftherrien/VaspGibbs/3e20b2fadb4c5cdf328a1a3194374cf6318bf84a/docs/VGlogo.svg" height="130">

VaspGibbs
</h1>
<br>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7874413.svg)](https://doi.org/10.5281/zenodo.7874413)
[![PyPI](https://img.shields.io/pypi/v/vaspgibbs)](https://pypi.org/project/VaspGibbs/)

## Installation

```
pip install VaspGibbs
```
## Usage

In a folder with a finished vasp calculation, run
```
vasp_gibbs
```

`vasp_gibbs` will rerun Vasp to obtain vibration modes and output the gibbs free energy of your system.

Use `-o` (only) or `-t`(top) to specify a set of atoms for which to calculate vibration modes. Examples:

 * `-o C O` would only compute vibration modes associated with C and O keeping all other atoms fixed.
 * `-o 0 2 5` would compute vibration modes associated with the first, third and sixth atoms in the POSCAR keeping all other atoms fixed. (Counts from 0)
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

#### Rotational properties
|     Property     |          Value          |
| :--------------: | :---------------------: |
|      Sigma       |            x            |
|   **P. axes**    |                         |
|       I~1        |       x        eV/THz^2 |
|       I~2        |       x        eV/THz^2 |
|       I~3        |       x        eV/THz^2 |


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
* https://uregina.ca/~eastalla/entropy.pdf (https://doi.org/10.1063/1.473958)

## Citation

```
@software{therrien2023vaspgibbs,
  author       = {Félix Therrien},
  title        = {{VaspGibbs: A simple way to obtain Gibbs free 
                   energy from Vasp calculations}},
  month        = apr,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v0.2.1},
  doi          = {10.5281/zenodo.7874413},
  url          = {https://doi.org/10.5281/zenodo.7874413}
}
```

## Under development

Results have been checked with [J. Phys. Chem. C 2013, 117, 49](https://pubs.acs.org/doi/abs/10.1021/jp407468t). More validation needs to be done; use with care.

*Next steps:* more testing, add to pypi, PV term for solids with Murnaghan equation, hindered translator and rotor?

Let me know if you would like new features to be added!

