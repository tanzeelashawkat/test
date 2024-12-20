my_dict={"tamana" : (90,98,67,),
         "tanzila": (95,54,98),
         "mehreen" : (80,95,69)}
result=my_dict
print(result["tamana"])
avg_score=sum(result["tamana"]) / 3, sum(result["tanzila"])/3 ,sum(result["mehreen"])/3
print(avg_score)
print(max(avg_score))
