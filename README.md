# Read-Write-excel-files
Different ways to R/W XLS&amp;XLSX files (a beginners journey)

LANDH battery systems can generate a spreadsheet using defined parameters. In my case, capacity, current, time (in  hours), and overpotential (voltage)

NEWARE battery systems*  exports a multiple page report.  We are only interested in voltage profiling data.  The data page(s) have 12 columns but with timestamps.  With multiple pages, concantenating is required, and admittedly I had help with this.  I am just publishing the simple code that has worked for me so far.    Presently we are working on extracting data directly from the data files for this instrument, but with their update about a year ago, the source code has change and people much more skilled than I am are working on this.   HOwever, this will work for the excel output files.
