import pandas as pd
import numpy as np

d = ("""100 3.5562 1.032 71.1 2.00 9.34 2.54 0.786
150 2.3364 1.012 103.4 4.426 13.8 5.84 0.758
200 1.7458 1.007 132.5 7.590 18.1 10.3 0.737
250 1.3947 1.006 159.6 11.44 22.3 15.9 0.720
300 1.1614 1.007 184.6 15.89 26.3 22.5 0.707
350 0.9950 1.009 208.2 20.92 30.0 29.9 0.700
400 0.8711 1.014 230.1 26.41 33.8 38.3 0.690
450 0.7740 1.021 250.7 32.39 37.3 47.2 0.686
500 0.6964 1.030 270.1 38.79 40.7 56.7 0.684
550 0.6329 1.040 288.4 45.57 43.9 66.7 0.683
600 0.5804 1.051 305.8 52.69 46.9 76.9 0.685
650 0.5356 1.063 322.5 60.21 49.7 87.3 0.690
700 0.4975 1.075 338.8 68.10 52.4 98.0 0.695
750 0.4643 1.087 354.6 76.37 54.9 109 0.702
800 0.4354 1.099 369.8 84.93 57.3 120 0.709
850 0.4097 1.110 384.3 93.80 59.6 131 0.716
900 0.3868 1.121 398.1 102.9 62.0 143 0.720
950 0.3666 1.131 411.3 112.2 64.3 155 0.723
1000 0.3482 1.141 424.4 121.9 66.7 168 0.726
1100 0.3166 1.159 449.0 141.8 71.5 195 0.728
1200 0.2902 1.175 473.0 162.9 76.3 224 0.728
1300 0.2679 1.189 496.0 185.1 82 257 0.719
1400 0.2488 1.207 530 213 91 303 0.703
1500 0.2322 1.230 557 240 100 350 0.685
1600 0.2177 1.248 584 268 106 390 0.688
1700 0.2049 1.267 611 298 113 435 0.685
1800 0.1935 1.286 637 329 120 482 0.6833
1900 0.1833 1.307 663 362 128 534 0.677
2000 0.1741 1.337 689 396 137 589 0.672
2100 0.1658 1.372 715 431 147 646 0.667
2200 0.1582 1.417 740 468 160 714 0.655
2300 0.1513 1.478 766 506 175 783 0.647
2400 0.1448 1.558 792 547 196 869 0.630
2500 0.1389 1.665 818 589 222 960 0.613
3000 0.1135 2.726 955 841 486 1570 0.536""")

table_cols = ['T [K]','ρ [kg/m3]','Cp (kJ/kg*K)',
              'µe7 [Ns/m2]','νe6 [m2/s]','ke3 [w/mK]',
              'αe6 [m2/s]','Pr']

d = d.split('\n')
datalist = []

for piece in d:
    #print(f"piece = {piece}")
    #print(f"type = {type(piece)}")
    arr = [float(s) for s in piece.split(' ')]
    datalist.append(arr)

datalist = np.asarray(datalist)
df = pd.DataFrame(datalist, columns=table_cols)
#print(np.shape(datalist))
#print(df)

temperatures = df['T [K]']

while True:
    T = input("Please input a temperature: ")
    try:
        T = float(T)
        break
    except ValueError:
        print("Please input a number.")

for idx, temp in enumerate(temperatures):
    #print(f"item {idx} = {temp}")50
    if T == temp:
        #print(f"T = Temp at {idx}: {temp}\n ")
        print(df.iloc[[idx]])
        break
    elif T < temp:
        #print(f"T < Temp at {idx}: {temp}\n ")
        bot = temperatures[idx-1]
        #print(f"bounds = {bot, temp}")
        interp_data = {}
        slope = (T - bot)/(temp - bot)
        #print(f"slope = {slope}")
        for column, label in zip(df, table_cols):
            col = df[column]
            interp_val = col[idx-1] + slope*(col[idx] - col[idx-1])
            interp_data[label] = round(interp_val, 4)

        idf = pd.DataFrame([interp_data])
        print(idf)
        break
    


