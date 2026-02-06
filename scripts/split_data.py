import pandas as pd


source_file = "D:\Projects\Fintech_DE_Project\data\source\source_data.csv"
destination = "D:\Projects\Fintech_DE_Project\data"

df = pd.read_csv(source_file)

N_PARTS = 5
size =  len(df)//N_PARTS  ##size of each file
start = 0


for file in range (1,N_PARTS+1):
    
    if file < N_PARTS:
        end = start + size 
    else:
        end = len(df)

    df_split = df.iloc[start:end]
    
    df_split.to_csv(f"{destination}\\transactions_batch_{file:02d}.csv", index=False)
    
    start = end

print("\n Split completed successfully!")