# line-masks
Routines to create formatted atomic line masks compatible with most LSD codes (e.g., https://github.com/folsomcp/LSDpy).

The simple usage in the command line is 
```terminal
python MakeLineMask.py
```


-----------------

We start from an original VALD line list file (available at http://vald.astro.uu.se/) extracted using the 'Extract Stellar' mode. 
For the example VALD files in the **atomic_masks** folder we use:
 - Starting wavelength = 950 nm
 - Ending wavelength   = 2600 nm 
 - Detection threshold = 0.01
 - Microturbulence = 1 km/s (and a few cases with 0 or 2 km/s)
 - Teff = [3250, 4250] K (in steps of 250 K)
 - log g = 4.0 or 5.0
 - Chemical composition = M/H: 0.0 (and a few cases with -0.5 or 0.5)
 - Extraction format = 'short format' 
 - Retrieve data via = ftp
 - Hyperfine structure = 'Include HFS splitting'
 - Require lines to have a known value of = 'Landé factor'
### Warning: 
You can vary these parameters to create your personal mask, but for our routine to work you should *always select the extraction format 'short format'* and *always ask for a know value of 'Landé factor'* (which is needed to compute LSD profiles).

-----------------

You can find some example line masks extracted from VALD in the folder **atomic_masks**. 
We rename the orginal file from VALD to something in the format: t4000_g4.0_m0.0_vmic1_total. Here, 
  - 't4000' corresponds to an effective temperature of 4000 K, 
  - 'g4.0' corresponds to a log g (cm/s^2) = 4.0, 
  - 'm0.0' corresponds to a metalicity M/H = 0.0, and 
  - 'vmic1' stands for a microturbulent velocity of 1 km/s.

In this example, the formatted mask that we create will then be named 't4000_g4.0_m0.0_vmic1'.







