#in command prompt
# make a directory on desktop or your desired location and navigate to that directory using
##cd directory_name
# then install virtual environment using
##pip3 install virtualenv
#now make a directory inside the directory you created using
##virtualenv directory_name
#to enter into virtualenv use
##source directory_name/bin/activate
#and now you have enetered into virtualenv in the folder you just created
#to deactivate thr virtualenv or to come out of it type
##deactivate

#to make a requirement file use
##pip3 freeze > requirements.txt
#to downlaad a specific packagr from this file use
##pip3 install package_name==version or copy paste from the requirements file
#to download all the packages of the requirements file use
##pip3 install -r requirements.txt

#to make a virtualenv such that it contains all the packages you have in your python outside vitualenv then use
##virtualenv --system-site-packages priyansh2

