# shelve模块练习
import shelve

shelf_file = shelve.open("mydata")
cats = ["Tom", "Pooks", "Simon"]
shelf_file["cats"] = cats
shelf_file.close()

shelf_file = shelve.open("mydata")
print(type(shelf_file))
print(shelf_file["cats"])
shelf_file.close()
