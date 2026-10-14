from pathlib import Path

#prints current working directory
print(Path.cwd())

#list all folders and files in the cwd if we do not pass any argument in the Path()
for p in Path().iterdir():
    print(p)

#making objects of the files and folders
my_file=Path("Pathlib.py")
my_dir=Path("directory")

#printing the name of the object
print(my_file)
print(my_file.name)

#printing the extension of the file
print(my_file.suffix)

#printing the name without the extension of the file
print(my_file.stem)

#making an object of a new file within a directory (the new file does not need to exist)
new_file=my_dir/"new.txt"

print(my_file)
print(new_file)
print(my_dir)

#check if a file or folder exists
print(my_file.exists())
print(new_file.exists())

#getting the parent directory 
print(my_dir.parent)
print(new_file.parent)

#getting the absolute path
print(my_dir.absolute())
print(new_file.absolute())

#getting the absolute path of the parent
print(my_dir.parent.absolute())

#resolve method also gives the absolute path as well as it solves some misunderstood issues by the absolute method
p=Path("..")
print(p.absolute())
print (p.resolve())

# __file__ is a special variable that points to the current file
path=Path(__file__)
print(path.resolve())

#sometimes the resolve method also cannot resolve some misunderstanding

# home_folder=Path("~/anaconda3").resolve()
# print(home_folder)

#we can use the expand user method for solving such issues

# home_folder=Path("~/anaconda3").expanduser()
# print(home_folder)

#we can also use the home method for this purpose
home_folder=Path.home() / "anaconda3"
print(home_folder)
