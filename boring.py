
import random
nameslist=['janardhan','teja','rushi','vineetha','srikanth','sundar','vikas','sunil','sachin','jhansi','mrudula','aiswarya']


ch='y'
while ch !='n':
    print(random.choice(nameslist))
    ch=input('do you want to continue y/n')
