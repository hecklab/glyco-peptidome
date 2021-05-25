#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Copyright 2020 Reidi002 <Reidi002@BMS-3QCN543>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import os
import pandas as pd

# This script combines multiple xlsx output files from Byonic

# 1. Generate list of xlsx workbooks

fileList = []
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if ".xlsx" in name:
            name = os.path.join(root, name)
            fileList.append(name)


# 2. Combine the data while adding a column with the original file name

sheetName = "Spectra"
df = pd.DataFrame()
for fileName in fileList:
    print("Reading", fileName)
    data = pd.read_excel(fileName, sheet_name=sheetName, ignore_Index=True)
    fileName = fileName.split("\\")[-1]
    fileName = fileName.split(".")[0]
    data["filename"] = fileName
    df = df.append(data)

# 3. Store xlsx workbook data

print("Writing data to file...")
df.to_excel("Combined.xlsx")

print("Done!")
