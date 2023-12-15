#3公里以内收费13元 超出3公里以外，每公里基本单价2.3元/公里 空驶费：超过15公里后每公里加收1.15元空驶费


userInput = float(input("请输入里程:"))
if userInput <= 3:
    feiyong = 13.0
elif userInput >3 and userInput <=15:
    feiyong = 13+(userInput-3)*2.3
else:
    feiyong = 13+(userInput-3)*2.3+(userInput-15)*1.15


# 打印费用信息    
print("你需要支付%.1f"%(feiyong))

