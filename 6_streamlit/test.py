import pandas as pd

#Initializing the file path to create a dataframe object and return the content in csv to it.
def loading_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        #stl.error(f"Error in reading the data file: {e}")
        return pd.DataFrame()
    

    
#Initializing the dataframe object from the csv file for training the RAG pipeline.
df= pd.read_csv('6_streamlit\\myfile.csv')

print(df)