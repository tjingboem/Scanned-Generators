# Scanned-Matrix-Pattern-Generator

MATRIX

A few things you should know about the format of creating the matrices with this Utility:
- make use of the .matrxT extension and format, see https://csound.com/manual/GEN44.html
- starts counting at 0, ends at matrix size -1.
- starts at 0 but can start anywhere until matrix size.
- can end before matrix -1
- values of X axis or Y axis should not get higher then matrix -1. Else an error will occur when using the Matrix in the csd.

- The Scanned Matrix Pattern Generator has 3 different ways of generating coordinates.
    1. Lines & Clusters: Lines are uninterrupted lines although the lines can contain spaces in between the nodes. Clusters are sections of lines.
    2. Random Pattern: a defined section of the Matrix can be populated with an adjustable number of nodes.
    3. Waves: sines and other waveforms can be used to generate a continuous flow of nodes.
- All the previous can be mixed.
- 'traditional' Patterns with 128 node points are to be found in the Preset list: string, strincircular, grid, cylinder and torus. See tutorials: https://www.csounds.com/scanned/


TRAJECTORY  

For scans, the table does not have the same size as the other ftables used in scanu/scanu2. Can be higher, equal or smaller. There can even be empty values in the table.
A smaller size ftable makes a slice and repeats the scan of portion of the matrix nodes.

ifntraj ftgen   7, 0, 0, -23, "/home/menno/128-spiral-8,16,128,2,1over219.traj"     Here, let Csound determine the size of the elements by using '0'.

The value must be between 0 and the max number of nodes in the matrix. 
