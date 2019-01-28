##########################################################################
## Modify the variables so that all of the statements evaluate to True. ##
##########################################################################

var1 = 33
var6 = 35.1
var2 = "queen"
var3 = [1, 2, 3, 4, "abc"]
var4 = (1, 2, "Hello, we are playing with Python!", 4, "abc")
var5 = {
  "happy": 7,
  "egg": "salad",
  "tuna": "fish"
}

############################################
## Don't edit anything below this comment ##
############################################

# integers
print(type(var1) is int)
print(type(var6) is float)
print(var1 < 35)
print(var1 <= var6)

# strings
print(type(var2) is str)
print(var2[4] == 'n' and var2[0] == "q")

# lists
print(type(var3) is list)
print(len(var3) == 5)

# tuples
print(type(var4) is tuple)
print(var4[2] == "Hello, we are playing with Python!")

# dictionaries
print(type(var5) is dict)
print("happy" in var5)
print(7 in var5.values())
print(var5.get("egg") == "salad")
print(len(var5) == 3)
print(var5["tuna"] == "fish")
print(len(var5) == 3)
