                                    # LIST QUES # 1

Country = ['Pakistan','Canada','Australia']
Capital = ['Islamabad','Otawa','Canberra']

# Using some list functions

print(Capital[1])
print(Capital.sort())
Capital.append('Dehli')
print(Capital)
print(Capital[-2])
print(Capital + Country)
print(Capital.pop())
print(Capital.clear())



ListOfLists = [['Tahir','Fakhir','Sami'],[90,88,86],['A','B','C']]
print(ListOfLists)
print(ListOfLists[2][-2])
print(ListOfLists[2].pop())
print(ListOfLists)
print(dir(Country))
Country.sort()
print(Country.count('Pakistan'))
print(Country.index('Australia'))
print(Country)
Country.reverse()
print('Reversed List:',Country)
Country.insert(0,'England')
print(Country)   
Country.extend(Capital)
print(Country)


                                        #LIST QUES # 2

def count_matching_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

# Sample list
sample_list = ['abc', 'xyx', 'aba', '1221']

result = count_matching_strings(sample_list)
print("Expected Result:", result)

