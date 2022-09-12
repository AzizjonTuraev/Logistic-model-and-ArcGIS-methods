#=========================================================================================
####################################### Preamble #########################################
#=========================================================================================
##
##    Project Title: <Identifiying neighbour counties for each German county>
##    ====================================================================================
##
##    Description:      This python script is used to geoprocess <...> data.
##                    
##    Author:		Mr. Azizjon Turaev 
##    E-mail            azizturayev20@gmail.com
##    Created: 	        2022-09-11
##    Last modified: 	2022-09-11
##    ArcGIS Version:	10.8.1
##
##    ====================================================================================
##
#-----------------------------------------------------------------------------------------
############## Import ArcPy package to access geoprocessing tools in ArcGIS ##############
#-----------------------------------------------------------------------------------------

print("Launching ArcGIS 10.8.1")
import arcpy
from arcpy.sa import *


#-----------------------------------------------------------------------------------------
################################### Set the environment ##################################
#-----------------------------------------------------------------------------------------

### Set the working directory
print("Set the working directory")
import os

# Return the directory path of this script
work_dir = os.path.dirname(os.path.realpath(__file__))

arcpy.env.workspace = "..\\" # NEVER USE single backslash (\) or use (/) instead
input_dir = os.path.join(work_dir, "..\\input\\")
temp_dir = os.path.join(work_dir, "..\\temporary\\")
output_dir = os.path.join(work_dir, "..\\output\\")
tools_dir = os.path.join(work_dir, "..\\tools\\")
os.chdir(output_dir)

### Check out extensions
print("Enabling ArcGIS Spatial Analyst extension")
arcpy.CheckOutExtension("spatial")

### Load required toolboxes
arcpy.ImportToolbox(os.path.join(tools_dir, "Excel_and_CSV_Conversion_Tools\\ExcelTools\\Excel and CSV Conversion Tools.tbx"))

### Allow the overwriting of output files
arcpy.env.overwriteOutput = True # This command is CASE-SENSITIVE

#-----------------------------------------------------------------------------------------
####################################  Local variables #################################### 
#-----------------------------------------------------------------------------------------

### File name of Geodatabase
GDB_name = "GDB.gdb"

### Set directories
#data_dir = "<Insert directory path here>"

### Inputs (add file extension if necessary)
#inputFile = os.path.join(data_dir, "<inputFile>.<file extension>")
gadm40_DEU_2 = os.path.join(input_dir, "gadm40_DEU_shp\\gadm40_DEU_2.shp")


### Intermediates (add file extension if necessary)
#tempFile = os.path.join(temp_dir, "<tempFile>.<file extension>")

### Outputs (add file extension if necessary)
#outputFile = os.path.join(output_dir, "<outputFile>.<file extension>")
gadm40_DEU_2_PolygonNeighbor = os.path.join(output_dir, GDB_name, "german_counties_neighbours")
german_counties_neighbours = os.path.join(output_dir, "neighbours.csv")
neighbours_xls = os.path.join(output_dir, "neighbours.xls")

#=========================================================================================
###################################### Geoprocessing #####################################
#=========================================================================================
try:

#-----------------------------------------------------------------------------------------
#################################### Create file GDBs ####################################
#-----------------------------------------------------------------------------------------

    ### Execute CreateFileGDB
#    print("Process: Create file GDBs")
#    arcpy.CreateFileGDB_management(temp_dir, GDB_name)
#    arcpy.CreateFileGDB_management(output_dir, GDB_name)

#-----------------------------------------------------------------------------------------
################################## Geoprocessing Commands ################################
#-----------------------------------------------------------------------------------------

    ### Paste geoprocessing commands here!

    # Process: Polygon Neighbors
    print("Process: Polygon Neighbors")
    arcpy.PolygonNeighbors_analysis(gadm40_DEU_2, gadm40_DEU_2_PolygonNeighbor, "NAME_2", "NO_AREA_OVERLAP", "BOTH_SIDES", "", "KILOMETERS", "SQUARE_MILES")

    # Process: Table To CSV
    print("Process: TableToCSV")
    arcpy.TableToCSV_tableconversion(gadm40_DEU_2_PolygonNeighbor, german_counties_neighbours, "COMMA")

    # Process: Table To Excel
    print("Process: TableToExcel")
    arcpy.TableToExcel_conversion(gadm40_DEU_2_PolygonNeighbor, neighbours_xls, "NAME", "CODE")



    ### Print message if geoprocessing is done
    print("Geoprocessing Done")


#-----------------------------------------------------------------------------------------
################################## Delete temporary files ################################
#-----------------------------------------------------------------------------------------
    
##    print("Deleting temporary files...")
##    arcpy.env.workspace = "..\\temporary\\"
##
##    ### For intermediate file geodatabases
##    GDBpath = os.path.join(temp_dir, GDB_name)
##    arcpy.Delete_management(GDBpath)
##
##    ### For intermediate shapefiles
##    fcList = arcpy.ListFeatureClasses("temp*")
##    for fc in fcList:
##        print(fc + " is being deleted")
##        arcpy.Delete_management(fc)
##
##    ### For intermediate rasterfiles
##    rasList = arcpy.ListRasters("temp*")
##    for ras in rasList:
##        print(ras + " is being deleted")
##        arcpy.Delete_management(ras)
##
##    print("...Done")

#-----------------------------------------------------------------------------------------
########################## Return geoprocessing specific errors ##########################
#-----------------------------------------------------------------------------------------  

except arcpy.ExecuteError:
    print arcpy.GetMessages()

#-----------------------------------------------------------------------------------------
############################# Return any other type of error #############################
#-----------------------------------------------------------------------------------------

except:
    print("There has been a non-geoprocessing error")

#-----------------------------------------------------------------------------------------
###################################### Closing ArcGIS ####################################
#-----------------------------------------------------------------------------------------

### Release the memory
print("Closing ArcGIS 10.8.1")
del arcpy










