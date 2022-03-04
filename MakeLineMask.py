from read_vald import create_linemask

# Each filename encodes the mask temperature, log g, metalicity, and microturbulence
masks = ['t3250_g5.0_m0.0_vmic1',
         't3500_g5.0_m-0.5_vmic1',
         't3500_g5.0_m0.0_vmic1',
         't3500_g5.0_m0.5_vmic1',
         't3750_g5.0_m0.0_vmic1',
         't4000_g4.0_m0.0_vmic1',
         't4000_g5.0_m0.0_vmic0',
         't4000_g5.0_m0.0_vmic1',
         't4250_g4.0_m0.0_vmic0',
         't4250_g4.0_m0.0_vmic1',
         't4250_g4.0_m0.0_vmic2']

# Here we assume that the input VALD file is named mask + extension
extension = '_total'

# Select only lines that have a minimum depth with respect to the continuum
depth_min = 0.01

create_linemask(masks, extension, depth_min, rlt = False)
