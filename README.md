# line-masks
Routines to create formatted atomic line masks compatible with most LSD codes (e.g., https://github.com/folsomcp/LSDpy).
We start from an original VALD line list file (available at http://vald.astro.uu.se/) extracted using the 'Extract Stellar' mode and the extraction format 'short format'. 

The simple usage in the command line is 
```terminal
python MakeLineMask.py
```



You can find some example line masks extracted from VALD in the folder 'atomic_masks'. 
We rename the orginal file from VALD to something in the format: t4000_g4.0_m0.0_vmic1_total. Here, 
  - 't4000' corresponds to an effective temperature of 4000 K, 
  - 'g4.0' corresponds to a log g (cm/s^2) = 4.0, 
  - 'm0.0' corresponds to a metalicity M/H = 0.0, and 
  - 'vmic1' stands for a microturbulent velocity of 1 km/s.
In this example, the formatted mask that we create will then be named 't4000_g4.0_m0.0_vmic1'.







