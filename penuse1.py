data = "I am {}.\n" +\
        "My spirit animal is {} , \n" +\
        "because {}. \n"+ \
        "When not in school, I love to {}. \n"+ \
        "I dream of being a/an {} int the future."

mydata ={"name" : "Sophia Marie Penus",
        "animal": "Dog",
        "reason":"Im sweet and territorial",
        "hobby" :"draw,paint,code and surf net",
        "dream" :"Computer Engineer"
        }
      
print(data.format(mydata["name"],mydata["animal"],mydata["reason"],mydata["hobby"],mydata["dream"]))