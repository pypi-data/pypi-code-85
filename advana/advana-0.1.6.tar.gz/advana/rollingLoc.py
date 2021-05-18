import pandas as pd

def rollingLoc(unit, ref, trademark):
    
    roll = unit.loc[unit['Trademark']==trademark]
    ref = ref.loc[ref['Trademark']==trademark]
    
    roll_loc = pd.merge(roll, ref[['SerialNumber', 'Status']], on='SerialNumber', how='left')
    roll_loc = roll_loc.reset_index(drop=True)
    
    roll_loc = roll_loc.sort_values(by=['Date']).drop_duplicates(subset='SerialNumber', keep='first')
    roll_loc = roll_loc.groupby(['Operator Name', 'WeekNo', 'Status'])['SerialNumber'].nunique()

    def to_frame(sets):
        sets = sets.to_frame().reset_index()
        return sets 
    
    roll_loc = to_frame(roll_loc)
    roll_loc['Trademark'] = trademark
    
    return roll_loc