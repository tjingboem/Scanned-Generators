# Scanned-Generators

a Blue file containing the Scanned Matrix Generator, the Scanned Matrix Plot, the Scanned Trajectory Generator, the Scanned Trajectory Plot. Needs Blue (https://blue.kunstmusik.com/) and Matlabplot (https://matplotlib.org/stable/users/installing/index.html), Python3

MATRIX

A few things you should know about the format of creating the matrices with this Utility:
- makes use of the .matrxT extension and format, see https://csound.com/manual/GEN44.html
- starts counting at 1, ends at matrix size.
- starts at 1 but can start anywhere until matrix size.

- The Scanned Matrix Pattern Generator has 3 different ways of generating coordinates.
    1. Lines & Clusters: Lines are uninterrupted lines although the lines can contain spaces in between the nodes. Clusters are sections of lines.
    2. Random Pattern: a defined section of the Matrix can be populated with an adjustable number of nodes.
    3. Waves: sines and other waveforms can be used to generate a continuous flow of nodes.
- All the previous can be mixed.
- 'traditional' Patterns with 128 node points are to be found in the Preset list: string, strincircular, grid, cylinder and torus. See tutorials: https://www.csounds.com/scanned/

![Figure_1](https://github.com/user-attachments/assets/ca0317fb-bbf5-4682-a229-0789ea001c23)


TRAJECTORY  

For scans, the table does not have the same size as the other ftables used in scanu/scanu2. Can be higher, equal or smaller. There can even be empty values in the table.
A smaller size ftable makes a slice and repeats the scan of portion of the matrix nodes.

ifntraj ftgen   7, 0, 0, -23, "/home/menno/128-spiral-8,16,128,2,1over219.traj"     Here, let Csound determine the size of the elements by using '0'.

The format of the Trajectory is: NAME+NUMBER_maxVALUE_NUMBER.traj where:
1. NAME+NUMBER : the name and version number to identify this trajectory
2. _maxNUMBER  : the maximum value of the mass node you want to include
3. _NUMBER     : length of the trajectory. May be higher, equal or lower than the number of mass nodes in the Matrix.

Example: ifntraj ftgen   7, 0, 0, -23, "spiral01_max128_128.traj"   

The value must be between 0 and the max number of nodes in the matrix. 

![Screenshot from 2024-09-12 15-34-41](https://github.com/user-attachments/assets/67e593f0-06fd-4eeb-9565-07052140e55d)
