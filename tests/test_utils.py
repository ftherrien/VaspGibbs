def test_prepare_poscar():
    from vaspgibbs.utils import prepare_poscar
    import numpy as np
    
    cell = np.array([[1,0,0],[0,1,0],[0,0,1]])
    atoms = [["C",[0,0,0],["T","T","T"]],["C",[0,0,0.5],["T","T","T"]]]
    tol = 1e-3
    
    list_atoms = []
    top = 0
    cell, atoms = prepare_poscar(cell, atoms, list_atoms, top, tol)
    
    # All atoms should be allowed to move, nothing is specified
    assert atoms == [["C",[0,0,0],["T","T","T"]],["C",[0,0,0.5],["T","T","T"]]]

    top = 1
    cell, atoms = prepare_poscar(cell, atoms, list_atoms, top, tol)
    # Only the first atom from the top sould be allowed to move
    assert atoms == [["C",[0,0,0],["F","F","F"]],["C",[0,0,0.5],["T","T","T"]]]

    top = 0
    list_atoms = [1]
    cell, atoms = prepare_poscar(cell, atoms, list_atoms, top, tol)
    # Only the second atom (index 1) should be allowed to move
    assert atoms == [["C",[0,0,0],["F","F","F"]],["C",[0,0,0.5],["T","T","T"]]]

    list_atoms = [2]
    try:
        cell, atoms = prepare_poscar(cell, atoms, list_atoms, top, tol)
    except RuntimeError:
        # The atom index cannot be greater than the number of atoms in the POSCAR file
        pass

    list_atoms = [-1]
    try:
        cell, atoms = prepare_poscar(cell, atoms, list_atoms, top, tol)
    except RuntimeError:
        # No atoms are allowed to move
        pass

    top = -1
    list_atoms = []
    try:
        cell, atoms = prepare_poscar(cell, atoms, list_atoms, top, tol)
    except RuntimeError:
        # No atoms are allowed to move
        pass
