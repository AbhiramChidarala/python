#Match-Case Statement (also known as switch) = An Alternative to using many 'elif'
#                      Execute some code if a value matches a 'case' 
#                      Benefits: cleaner and syntax is more readable

#def day_of_week(day):
#    match day:
#        case 1:
#            return "It is sunday"
#        case 2:
#            return "It is monday"
#        case 3:
#            return "it is tuesday"
#        case 4:
 #           return "it is wednesday"
  #      case 5:
  #          return "it is thursday"
  #      case 6:
  #          return "it is friday"
  #      case 7:
  #          return "it is saterday"
  #      case _:
  #          return "not a valid day"
        
#print(day_of_week(1))

def is_weekend(day):
    match day:
        case "sunday"|"saturday":
            return True
        case "monday"|"tuesday"|"wednesday"|"thursday"|"friday":
            return False
        case _ :
            return False
print(is_weekend("monday"))