import random
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

fluids = {
  # fluidID: [Fluid]
  1: ['Skim Milk'],
  2: ['Nitric Acid'],
  3: ['Water'],
  4: ['Motor Oil']
}

def generate_weighted_flow(fluid_index):
    if fluid_index ==1:                   # Skim Milk
        flow = [400, 600, 800]
    elif fluid_index == 2:                # Nitric Acid
        flow = [800, 600, 400]
    elif fluid_index == 3:                # Water
        flow = [400, 800, 600]
    elif fluid_index == 4:                # Motor Oil
        flow = [600, 400, 800]
        
    weights = [6, 10, 3]
    index = random.choices(range(len(flow)), weights=weights)[0]
    return f"{flow[index]}"

def generate_weighted_temperature(fluid_index):
    if fluid_index ==1:                   # Skim Milk
        temperatures = [90, 5, 20]
    elif fluid_index == 2:                # Nitric Acid
        temperatures = [20, 5, 10]
    elif fluid_index == 3:                # Water
        temperatures = [80, 40, 10]
    elif fluid_index == 4:                # Motor Oil
        temperatures = [80, 90, 40]
        
    weights = [7, 10, 5]
    index = random.choices(range(len(temperatures)), weights=weights)[0]
    return f"{temperatures[index]}"

def generate_weighted_pumpfamily(fluid_index, temperature):
    if fluid_index ==1:                   # Skim Milk
        if temperature > 80:                
            pump_family = ['A10', 'IP1', 'IP2']     
        else:
            pump_family = ['IP2', 'A10', 'IP2']
    
    elif fluid_index == 2:                # Nitric Acid
        pump_family = ['A10', 'IP3', 'IP2']
    
    elif fluid_index == 3:                # Water
        if temperature > 70:
            pump_family = ['IP2', 'A10', 'IP2']
        else:
            pump_family = ['IP2', 'IP3', 'A10']
    
    elif fluid_index == 4:                # Motor Oil
        if temperature > 85:
            pump_family = ['A10', 'IP1', 'IP2']
        else:
            pump_family = ['A10', 'IP3', 'IP2']
        
    weights = [7, 10, 5]
    index = random.choices(range(len(pump_family)), weights=weights)[0]
    return f"{pump_family[index]}"

def generate_weighted_housing(fluid_index):
    if fluid_index == 2:
        housing = ['BX100', 'AX100', 'CX100']
    else:
        housing = ['BX100', 'CX100', 'AX100']
        
    weights = [6, 10, 3]
    index = random.choices(range(len(housing)), weights=weights)[0]
    return f"{housing[index]}"

def generate_weighted_elastomers():
    conn_elastomers = ['Viton', 'Kalrez', 'Vespel']
        
    weights = [7, 10, 5]
    index = random.choices(range(len(conn_elastomers)), weights=weights)[0]
    return f"{conn_elastomers[index]}"

def generate_dataset():
    columns_needs = ['Liquid', 'Flow', 'Temperature']
    df1 = pd.DataFrame(columns = columns_needs)

    columns_tech = ['Pump_Family', 'Housing_Material', 'Connection_Elastomers']
    df2 = pd.DataFrame(columns = columns_tech)

    df = pd.concat([df1, df2], axis=1)
    record_number = 0
    for fluid_index in range(1,5):
        
        if fluid_index == 1:
            num_records = int(np.random.normal(loc=100, scale=1000))
        elif fluid_index == 2:
            num_records = int(np.random.normal(loc=130, scale=1000))
        elif fluid_index == 3:
            num_records = int(np.random.normal(loc=140, scale=1000))
        elif fluid_index == 4:
            num_records = int(np.random.normal(loc=120, scale=1000))
            
        for i in range(num_records):
            flow = generate_weighted_flow(fluid_index)
            temperature = generate_weighted_temperature(fluid_index)
            pump_family = generate_weighted_pumpfamily(fluid_index, int(temperature))
            housing = generate_weighted_housing(fluid_index)
            elastomers = generate_weighted_elastomers()
            
            record_number += 1
            df.loc[record_number] = [fluids[fluid_index][0], flow, temperature, pump_family, housing, elastomers]
    return df
