import numpy as np
import matplotlib.pyplot as plt


def read_VALD_linelist(filename) :
    ###################################################################################################
    # For now the code is very simple and It requires to comment usign '#' the first lines (header)   #
    # and the last lines (footer) which do not contain the informations about the absorptin lines.    #
    # Each absorption line contains the following information:                                        #
    #                                                                                                 #
    #                                                 Damping parameters   Lande  Central             #
    #Spec Ion      WL_vac(nm) Excit(eV) Vmic log gf*  Rad.   Stark  Waals  factor  depth  Reference   # 
    ###################################################################################################
    
    loc = {}
    loc["filename"] = filename
    
    loc["species"], loc["ion"] = [], []
    loc["wave_nm_vacuum"], loc["wave_nm"] = [], []
    loc["excit_eV"] = []
    loc["vmic"] = []
    loc["loggf"] = []
    loc["rad"], loc["stark"], loc["waals"] = [], [], []
    loc["lande"] = []
    loc["depth"] = []
    loc["ref"] = []
    loc["species_code"] = []
    
    f = open(filename, 'r')
    
    for line in f:
        if line[0] != '#':
            cols = line.split(',')
            
            loc["species"].append(cols[0][1:-1].split()[0])
            loc["ion"].append(int(cols[0][1:-1].split()[1]))
            loc["wave_nm_vacuum"].append(float(cols[1]))
            loc["excit_eV"].append(float(cols[2]))
            loc["vmic"].append(float(cols[3]))
            loc["loggf"].append(float(cols[4]))
            loc["rad"].append(float(cols[5]))
            loc["stark"].append(float(cols[6]))
            loc["waals"].append(float(cols[7]))
            loc["lande"].append(float(cols[8]))
            loc["depth"].append(float(cols[9]))
            loc["species_code"].append(species_code(cols[0][1:-1].split()[0], int(cols[0][1:-1].split()[1])))

    loc["species"] = np.array(loc["species"])
    loc["ion"] = np.array(loc["ion"])
    loc["wave_nm_vacuum"] = np.array(loc["wave_nm_vacuum"])
    loc["wave_nm"] = convert_vacuum_to_air_wl(loc["wave_nm_vacuum"], air_density=1.0)
    loc["excit_eV"] = np.array(loc["excit_eV"])
    loc["vmic"] = np.array(loc["vmic"])
    loc["loggf"] = np.array(loc["loggf"])
    loc["rad"] = np.array(loc["rad"])
    loc["stark"] = np.array(loc["stark"])
    loc["waals"] = np.array(loc["waals"])
    loc["lande"] = np.array(loc["lande"])
    loc["depth"] = np.array(loc["depth"])
    loc["species_code"] = np.array(loc["species_code"])
    
    return loc


def species_code(species,ion):
    atomic_number = {'H':100, 'He':200,'Li':300, 'Be':400, 'B':500, 'C':600, 'N':700, 'O':800, 'F':900, 'Ne':1000, 'Na':1100, 'Mg':1200, 'Al':1300, 'Si':1400, 'P':1500, 'S':1600, 'Cl':1700, 'Ar':1800, 'K':1900, 'Ca':2000, 'Sc':2100, 'Ti':2200, 'V':2300, 'Cr':2400, 'Mn':2500, 'Fe':2600, 'Co':2700, 'Ni':2800, 'Cu':2900, 'Zn':3000, 'Ga':3100, 'Ge':3200, 'As':3300, 'Se':3400, 'Br':3500, 'Kr':3600, 'Rb':3700, 'Sr':3800, 'Y':3900, 'Zr':4000, 'Nb':4100, 'Mo':4200, 'Tc':4300, 'Ru':4400, 'Rh':4500, 'Pd':4600, 'Ag':4700, 'Cd':4800, 'In':4900, 'Sn':5000, 'Sb':5100, 'Te':5200, 'I':5300, 'Xe':5400, 'Cs':5500, 'Ba':5600, 'La':5700, 'Ce':5800, 'Pr':5900, 'Nd':6000, 'Pm':6100, 'Sm':6200, 'Eu':6300, 'Gd':6400, 'Tb':6500, 'Dy':6600, 'Ho':6700, 'Er':6800, 'Tm':6900, 'Yb':7000, 'Lu':7100, 'Hf':7200, 'Ta':7300, 'W':7400, 'Re':7500, 'Os':7600, 'Ir':7700, 'Pt':7800, 'Au':7900, 'Hg':8000, 'Tl':8100, 'Pb':8200, 'Bi':8300, 'Po':8400, 'At':8500, 'Rn':8600, 'Fr':8700, 'Ra':8800, 'Ac':8900, 'Th':9000, 'Pa':9100, 'U':9200, 'Np':9300, 'Pu':9400, 'Am':9500, 'Cm':9600, 'Bk':9700, 'Cf':9800, 'Es':9900, 'Fm':10000, 'Md':10100, 'No':10200, 'Lr':10300, 'Rf':10400, 'Db':10500, 'Sg':10600, 'Bh':10700, 'Hs':10800, 'Mt':10900, 'Ds ':11000, 'Rg ':11100, 'Cn ':11200, 'Nh':11300, 'Fl':11400, 'Mc':11500, 'Lv':11600, 'Ts':11700, 'Og':11800}
    try:
       SC = float(int(atomic_number[species]) + ion - 1)/100.
    except: #If molecules
       SC = 100. 
    return SC


def nrefrac(wavelength, density=1.0):
   """Calculate refractive index of air from Cauchy formula.
   Input: wavelength in nm, density of air in amagat (relative to STP,
   e.g. ~10% decrease per 1000m above sea level).
   Returns N = (n-1) * 1.e6.
   """

   # The IAU standard for conversion from air to vacuum wavelengths is given
   # in Morton (1991, ApJS, 77, 119). For vacuum wavelengths (VAC) in
   # Angstroms, convert to air wavelength (AIR) via:

   #  AIR = VAC / (1.0 + 2.735182E-4 + 131.4182 / VAC^2 + 2.76249E8 / VAC^4)

   wl2inv = (1.e3/wavelength)**2
   refracstp = 272.643 + 1.2288 * wl2inv  + 3.555e-2 * wl2inv**2
   return density * refracstp

def convert_vacuum_to_air_wl(vacuum_wavelength, air_density=1.0) :
    air_wavelength = vacuum_wavelength / ( 1. + 1.e-6 * nrefrac(vacuum_wavelength, density=air_density))
    return air_wavelength

def convert_air_to_vacuum_wl(air_wavelength, air_density=1.0) :
    vacuum_wavelength = air_wavelength * ( 1. + 1.e-6 * nrefrac(air_wavelength, density=air_density))
    return vacuum_wavelength



def create_linemask(masks, extension, depth_min, rlt = False, JF = False):
    '''
    In this routine we assume that the input VALD file is named mask + extension
    
    :param masks: list contaning the name of the masks that will be created.
    :param extension: str, the input VALD file should be named mask + extension
    :param depth_min: threshold for the line depths. Only lines with depth larger than depth_min are included in the mask created. 
    :param rlt: Flag to decide if you want to remove lines falling in the telluric band (True: removes, False: doesn't)
    '''
    # Telluric water bands in nm
    wtl = (950, 1081, 1328, 1784, 2380)
    wtu = (979, 1169, 1492, 2029, 2500)

    # Directory where the masks are (we can as well modify the function to give this quantity as an argument)
    MASK_DIR = './atomic_masks/'
    for maskname in masks:
        vald = read_VALD_linelist(MASK_DIR + maskname + extension)        
        count1 = 0
        count2 = 0
        with open(MASK_DIR + maskname, 'w') as file:
            file.write("{0:d}\n".format(vald['wave_nm_vacuum'][vald['depth'] > depth_min].shape[0]))
            for idic in range(vald['ion'].shape[0]): 
                 if (vald['depth'][idic] > depth_min):
                     if rlt and (True in [(vald['wave_nm_vacuum'][idic] > wl) and (vald['wave_nm_vacuum'][idic] < wu) for  (wl,wu) in zip(wtl,wtu)]): 
                         if JF: 
                             flag = 1 #don't use line (Jean-Francois notation)
                         else:
                             flag = 0 #don't use line
                         count1 += 1
                     elif vald['lande'][idic] <= 0.: #remove some lande numbers
                         if JF: 
                             flag = 1 #don't use line (Jean-Francois notation)
                         else:
                             flag = 0 #don't use line
                         count2 += 1
                     elif vald['lande'][idic] == 99.00: #remove molecular lines with unknow lande factor
                         if JF: 
                             flag = 1 #don't use line (Jean-Francois notation)
                         else:
                             flag = 0 #don't use line
                         count2 += 1
                     else:
                         if JF: 
                             flag = 0 #use line (Jean-Francois notation)
                         else:
                             flag = 1 #use line
                     file.write("{0:.4f}  {1:.2f}  {2:.3f}  {3:.3f}  {4:.3f}  {5:d}\n".format(vald['wave_nm_vacuum'][idic], vald['species_code'][idic], vald['depth'][idic], vald['excit_eV'][idic], vald['lande'][idic], flag))
        
        
        print('\n--------')
        print('Creating mask: ' + maskname)
        print('\n')
        print('There are %d lines with depth larger than %1.2f ' %(vald['wave_nm_vacuum'][vald['depth'] > depth_min].shape[0], depth_min) )
        print('and %d lines fall in the telluric water band and %d have a lande factor <= 0' %(count1, count2))
        print('We consider thus a total of %d lines to compute LSD profiles' %(vald['wave_nm_vacuum'][vald['depth'] > depth_min].shape[0] - count1 - count2))
        print('--------')
    
