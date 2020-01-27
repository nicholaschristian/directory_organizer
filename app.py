import os, shutil
import time

class DirectoryCleaner:
    def __init__(self, abs_path_to_directory):
        if abs_path_to_directory:
            self.dir = abs_path_to_directory
            self.extensions = set()
            self.getFileExtensions()
            self.createExtensionDiretories()

    def getFileExtensions(self):
        files = os.listdir(self.dir)

        for file in files:
            extension = os.path.splitext(file)[1]
            if extension:
                self.extensions.add(extension)

    def createExtensionDiretories(self):
        print("Checking if directories exist...")
        for extension in self.extensions:
            f = str(extension).replace('.', '')
            if os.path.exists("{}/{}".format(self.dir, f)):
                print("Directory Exists")
            else:
                try:
                    os.mkdir("{}/{}".format(self.dir, f))
                    print("Directory {} created".format(extension))
                except Exception as e:
                    print(e)

    def sortFiles(self):
        print("Sorting {}".format(self.dir))
        files =  os.listdir(self.dir)
        try:
            for ext in self.extensions:
                for file in files:
                    if ext in file:
                        # f: file extension without .
                        f = str(ext).replace('.', '')
                        # if the file to be moved exists in target directory
                        try:
                            shutil.move(src="{}/{}".format(self.dir, file), dst="{}/{}".format(self.dir, f))
                        except:
                            filename_without_extension = file.replace(".{}".format(f), '')
                            os.rename("{}/{}".format(self.dir,file), "{}/{}/{}_{}.{}".format(self.dir, f, filename_without_extension, int(time.time()) ,f))

        except Exception as e:
            print(e)

    def listExtensions(self):
        return self.extensions

if __name__ == '__main__':
    dir = input("Enter absolute path to directory. ")
    confirm = input("Are you sure you want to execute this task? ")

    if confirm == "y":
        x = DirectoryCleaner(abs_path_to_directory=dir)
        x.sortFiles()
    else:
        print("Task Cancelled By User")
