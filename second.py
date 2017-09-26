item_list=["james",75,["first","baby"],("football","orange"),{"position":"first"}]

def extract_list(item_list):
    for item in item_list:
      if type(item)==list or type(item)==tuple:
          extract_list(item)
    print (item)
        elif type(item)==dict:
         for key in item:
             print (item[key])
      else:
            print(item)

extract_list (item_list)
