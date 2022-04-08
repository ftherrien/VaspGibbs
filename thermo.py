import numpy as np

tol = 1e-5

h = 0.004135667696923859 # eV/THz

kb = 8.6173332621452e-5 # eV/K

conv_I = 1.03642697e-4 #from A*(Da)**2 to eV/THz**2

# Electronic contributions
class Elec:
    def __init__(self):
        # Assuming excited states energy are much higher than Kb*T
        with open("OUTCAR", "r") as f:
            outcar = f.read()
    
        nelect = int(re.findall("NELECT\s*=\s*([\0-9]+)", outcar)[-1])
    
        nup = int(re.findall("NUPDOWN\s*=\s*([\0-9]+)", outcar)[-1])
    
        if nup != -1:
            self.Z = nup + 1
        else:
            self.Z = nelect%2 + 1
    
    self.S =  kb * np.log(self.Z)
    
    self.E = 0

# Vibratonal contributions
class Vib:
    def __inti__(self, T, freq):
        # Harmonic oscillator approximation, breaks down at high temperatures
        self.Z =  np.prod(1 / (1 - np.exp( - h * freq / (kb * T))))
    
        self.S =  kb * (np.sum( h * freq / (kb * T) / (np.exp( h * freq / (kb * T)) - 1)) + np.log(self.Z))
    
        self.E = np.sum( h * freq / (np.exp( h * freq / (kb * T)) - 1))

# Rotational contributions
class Rot:
    def __init__(T, cell, atoms):
        # Rigid rotor approximation, only applies to smaller molecules
    
        if len(atoms) == 1:
            self.Z =  1
            self.S =  0
            self.E =  0
            return
    
        masses = get_masses(atoms)
    
        I_mat = get_inertia(cell, atoms, masses)
    
        sigma = get_symmetry_number(cell, atoms, masses, I)
    
        if la.det(I_mat) < tol:
            self.Z = 1 / sigma * (8 * np.pi**2 * kb * T / h**2)**(3/2) * np.sqrt(np.pi * la.det(I_mat))
            self.E = 3/2*kb*T
        else:
            I,_ = la.eigh(I_mat)
            I = np.sort(I)
            self.Z = 1 / sigma * 8 * np.pi**2 * kb * T * I[2] / h**2
            self.E = kb*T
            
        self.S =  kb * np.log(self.Z) + self.E/T

# Translational contributions
class Trans:
    def __init__(T, P, cell, atoms):
        # Ideal gas approximation

        masses = get_masses(atoms)

        self.Z = (2*np.pi*np.sum(masses)*kb*T/h^2)**(3/2)*kb*T/P
        self.S = kb * (np.log(self.Z) + 5/2)
        self.E = 3/2*kb*T

def get_masses(atoms):
    with open("POTCAR", "r") as f:
        potcar = f.read()
    elements = np.array(re.findall("TITEL\s*=\s*\w+\s*(\w+)", potcar))
    mass_elem = np.array([float(a) for a in re.findall("POMASS\s*=\s*([0-9.]+)\s*", potcar)])
    
    masses = np.zeros(len(atoms))
    for i, a in enumerate(atoms):
        masses[i] = mass_elem(elements==a[0])[0]

    return masses

def get_center_of_mass(cell, atoms, masses):
    cm = np.zeros(3)
    for i,e in enumerate(atoms):
        cm += masses[i]*cell.dot(e[1])/np.sum(masses)
    return cm

def get_inertia(cell, atoms, masses):

    cm = get_center_of_mass(cell, atoms, masses)

    I = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            for k,e in enumerate(atoms): 
                I[i,j] += masses[k]*((la.norm((cell.dot(e[1])-cm)) if i==j else 0) - (cell[i,:].dot(e[1])-cm[i])*(cell[j,:].dot(e[1])-cm[j]))
    return I * conv_I

def rot_mat(u, theta):
   u = u/la.norm(u)

   P = u.reshape((3,1)).dot(u.reshape((1,3)))
   Q = np.array([[0,-u[2],u[1]], [u[2], 0, -u[0]], [-u[1], u[0], 0]])

   return  P + (np.eye(3) - P)*np.cos(theta) + Q*np.sin(theta)

def rotate_mol(cell, atoms, cm, u, theta):

    R = rot_mat(u, theta)
    icell = la.inv(cell)

    for k,e in enumerate(atoms):
        elem, pos, sel = e
        pos = icell.dot(R.dot(cell.dot(pos)-cm)+cm)
        atoms[k] = (elem, pos, sel)

    return atoms

def is_same(cell, atoms1, atoms2):
    for elem1, pos1, _ in atoms1:
        for elem2, pos2, _ in atoms2:
            if elem1 == elem2 and la.norm(cell.dot(pos1 - pos2)) < tol:
                break
        else:
            break
    else:
        return True

    return False


def get_symmetry_number(cell, atoms, masses, I_mat):
    # Assuming rotational symmetry axis are always principal axes 
    
    cm = get_center_of_mass(cell, atoms, masses)

    I, R = la.eigh(I_mat)

    _,reps = np.unique([e for e,_,_ in atoms], return_counts=True)

    for i in range(3):
        sig_axis = 1
        for j in range(1, max(reps)):
            rotated_atoms = rotate_mol(cell, atoms, cm, R[:,i], 2*np.pi/(j+1))
            if is_same(cell, atoms, rotated_atoms):
                sig_axis = j+1
        sig *= sig_axis

    return sig

def compute_thermo(T, freq, cell, atoms):
    print("Gibbs corrections:", file=vgout)

    E_zpe = 1 / 2 * h * np.sum(freq)

    # electronic contribution

    print("E_zpe : %f"%(E_zpe), file=vgout)
