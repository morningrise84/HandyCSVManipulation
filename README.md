## What is this?

A simple but handy script for small CSV manipulation: the script basically adds a column to an existing .csv file and populate each row with a standard value


## Use case

- A .csv file is generated, ready to be loaded into a target system
- An attribute which is not defined in the .csv file would normally get populated with a default value in the target system
What if, occasionally, a different value would need to be passed from the .csv file?
 
Available options: 
A) When needed, manually edit the .csv file to add the column
B) Apply the transformation somewhere else (ETL?) with a specific logic (when to add the column or not)
C) When needed, simply have a script to run after the .csv generation <--- HERE WE ARE! :-D


## Usage

- Replace "TARGETFILE.csv" with the actual .csv file
- Replace "COLUMNNAME" to define the name of the new column
- Replace "DEFAULTVALUE" with the value you would like to assign to each row in the newly created column

Please note:
- By default, the script overrides the initial .csv file: you might need to specify different source and target .csv files
- By default, the script is encoding to "cp1252": you might need to specify a different encoding
