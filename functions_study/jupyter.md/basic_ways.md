```Javascript
    const is2p2 = checkThatTwoPlusTwoEqualsFourAMillionTimes;
    is2p2();
    console.log(is2p2.name);
    //输出结果： checkThatTwoPlusTwoEqualsFourAMillionTimes
    
```

##   put CSV into one file

### 将该文件夹下的所有文件名存入列表
```Python
    filepath = 'C:\\Users\\Tang\\Desktop\\OPP-115\\annotations'
    csv_name_list = os.listdir(filepath)
```

### 获取列表的长度
```Python
    length = len(csv_name_list)
```


### 读取第一个CSV文件并包含表头，用于后续的csv文件拼接
```Python
    f= open(csv_name_list[0],encoding = "utf-8")
    df = pd.read_csv( f)
```

 

### 读取第一个CSV文件并保存

```Python
    SaveDestination = 'C:\\Users\\Tang\\Documents\\GitHub\\SKLEARN\\y3project\\opp_operation_data'
    SaveFileName = 'all.csv'
    df.to_csv(SaveDestination + '\\' + SaveFileName,encoding = "utf_8_sig",index = False )
```


### 循环遍历列表中各个CSV文件名，并完成文件拼接

```Python
    for i in range(1,totalLength):
        df = pd.read_csv(filepath+ '\\' + csv_name_list[i])
        df.to_csv(SaveDestination + '\\' + SaveFileName,encoding = "utf_8_sig",index = False,header=False,mode = 'a+')
```

## dataframe 中的一列中的数据统一去除掉前n位
```Python
    df.iloc[:,1]
    df[1] = df[1].map(lambda x: str(x)[33:])
    #在同一列中去除掉前33位
```