import os
import shutil
import time

def root():

	
	del_folders = 0
	del_files = 0


	path = "/Delete_path"
	days = 30
	seconds = time.time() - (days * 24 * 60 * 60)


	if os.path.exists(path):

		
		for mainFolder, folders, files in os.walk(path):

			if seconds >= get_file_or_folder_age(mainFolder):


				remove_folder(mainFolder)
				del_folders += 1 

				break

			else:

	
				for folder in folders:

			
					folder_path = os.path.join(mainFolder, folder)

					if seconds >= get_file_or_folder_age(folder_path):

				
						remove_folder(folder_path)
						del_folders += 1 

				for file in files:

					file_path = os.path.join(mainFolder, file)

					if seconds >= get_file_or_folder_age(file_path):

						remove_file(file_path)
						del_files += 1 

		else:

	
			if seconds <= get_file_or_folder_age(path):

				remove_file(path)
				del_files += 1 # incrementing count

	else:

		print(f'"{path}" cannnot be accesed, it may have been removed, sorry for that')
		del_files += 1 # incrementing count

	print(f"Total folders deleted: {del_files}")
	print(f"Total files deleted: {del_folders}")


def remove_folder(path):

	if not shutil.rmtree(path):

		print(f"{path} removed succesfully!")

	else:

		print(f"Unable to delete  "+path)



def remove_file(path):

	if not os.remove(path):

	
		print(f"{path}  removed successfully")

	else:

		print("Unable to delete "+path)


def get_file_or_folder_age(path):


	ctime = os.stat(path).st_ctime


	return ctime


if __name__ == '__main__':
	

    root()