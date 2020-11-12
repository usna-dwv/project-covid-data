import pandas as pd
from pathlib import Path

def compare_csv(left_csv, right_csv):
    # Check if left and right files exist
    if not Path(left_csv).exists():
        print(f'ERROR: {left_csv} does not exist.')
        return
        
    if not Path(right_csv).exists():
        print(f'ERROR: {right_csv} does not exist.')
        return

    # Load files and original file
    left_df = pd.read_csv(left_csv)
    right_df = pd.read_csv(right_csv)

    # Check shapes
    left_shape = left_df.shape
    right_shape = right_df.shape
    
    if left_shape != right_shape:
        print(f'ERROR: {left_csv} has shape {left_shape}, but {right_csv} has shape {right_shape}.')
        return

    # Check columns
    left_columns = list(left_df.columns)
    right_columns = list(right_df.columns)
    
    if left_columns != right_columns:
        print(f'ERROR: {left_csv} and {right_csv} have different columns (different names or different order).')
        return

    # Check values
    fraction_match_cols = (left_df == right_df).sum() / left_df.shape[0]
    print('Fraction of matching values in each column')
    print('==========================================')
    print(fraction_match_cols)

    fraction_match = (left_df == right_df).sum().sum() / left_df.size
    print('')
    print('Fraction of matching values =', fraction_match)