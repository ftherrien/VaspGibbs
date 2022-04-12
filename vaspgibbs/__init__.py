from .thermo import compute_thermo
from .utils import read_outcar, read_poscar, prepare_incar, prepare_poscar
import pkg_resources 

__version__ = pkg_resources.require("vaspgibbs")[0].version
