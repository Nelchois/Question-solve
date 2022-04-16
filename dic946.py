from setuptools import find_namespace_packages


count = int(input())
country_dic = {}
for _ in range(count):
   country, capital = input().split()
   country_dic.update({country: capital})
print(country_dic)
find_capital = input()
print(country_dic.get(find_capital, "Unknown Country"))