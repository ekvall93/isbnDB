
import requests
import pickle 
import time
from tqdm import tqdm


### Enter your api-key ####
api_key = ""

#####Each batch contains 50k isbn, run one for each day.####
batch = pickle.load(open("./data/batch3_.pkl", "rb"))
batch_iter = 3
#batch = pickle.load(open("./data/batch4_.pkl", "rb"))
#batch_iter = 4
#batch = pickle.load(open("./data/batch5_.pkl", "rb"))
#batch_iter = 5


for i, isbn in enumerate(tqdm(batch)):
    r=requests.get(f"https://api.pro.isbndb.com/book/{isbn}", 
    headers={"Authorization":api_key})

    bookData[isbn] = r.json()

    time.sleep(0.25)

    if i % 10 == 0 and i > 0:
        pickle.dump(bookData, open(f"summaryBatch/batch_{batch_iter}.pkl", "wb"))
        

pickle.dump(bookData, open(f"summaryBatch/batch_{batch_iter}_part1.pkl", "wb"))
