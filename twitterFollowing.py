import twint
import pickle 



print('Start')


file2 = open("screenNames3.pkl",'rb')
x = pickle.load(file2)
#Graziano change this to 20000
x = x[5600:]
for i in range(len(x)):
    print("--- Break ---")
    print(x.iloc[i].values[0])
    config = twint.Config()
    config.Username = str(x.iloc[i].values[0])
    

    twint.run.Following(config)
print('Done')


