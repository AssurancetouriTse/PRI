#-------------------------------------------------------------------------------
# Name:        dataConvereter
# Purpose:     library that makes a row from sql request into dictionnary
#
# Author:      remi huguenot
#
# Created:     18/01/2021
# Copyright:   (c) remi huguenot 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import json

def rowToDict(row):
    rowDict = []

    for (idBase, idBooktripv, idreceptv, validv, json_schedualv, json_schedulingv, json_pricev, json_pagesv, json_pricingv, updated_jsonv) in row :

        dict = {
            id : idBase,
            idBooktrip : idBooktripv,
            idRecept : idreceptv,
            valid : validv,
            json_scheual : json.dump(json_schedualv),
            json_scheduling : json.dump()

            }
