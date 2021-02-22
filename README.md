# Filed Assignment Solution

The project includes post, get, put and delete APIs to perform CRUD operations on audio files. The project contains 72 test cases to validate the application.


## Project Setup
Below are the steps to set up the project for evaluation:
1. Clone the Git repository using ```git clone repository_url```.
2. After cloning the project, go to the project directory.
3. src contains the source code of the project.

## Virtual Environment Setup
1. Open command prompt(Windows) or terminal(Linux) and go to project directory.
2. Make sure you have virtualenv installed on your system.
3. If not already installed, run ```pip install virtualenv``` to install virtualenv on your system.
4. Create a virtual environment using ```virtualenv filed_env```.
5. Run ```.\filed_env\Scripts\activate``` command to enable virtualenv environment.
6. Install project requirements from requirements.txt using ```pip install -r requirements.txt``` command.
7. Run ```pip freeze``` command to check packages installed.

## Steps to hit and run endpoints
**Prerequisite - MongoDB**
1. After enabling the virtual environment, run the ```flask run``` command to start the flask server.
2. Use postman to hit endpoints.

## Create API(/create_audio)
### Input
Accepts 3 parameters as form-data named audioFileType(Text),
audioFileMetaData(Text) and audioFile(File).
1. audioFileType allows only (song, podcast, and audiobook) as its value.(Eg - audiobook)
2. audioFileMetaData accepts a json containing required fields for audioFileType.(Eg - { "book_title": "sachin_voice","duration": "4","narrator":"Sachin","author":"Rohit"})
3. audioFile accepts any audio file from disk storage.

### Sample Create Input
![create_sample_input](https://github.com/sachdevasachin434/filed_assignment/blob/master/images/sample_create_input.png?raw==True)
### Output
1. Returns {"result": f"Audio Inserted, File ID: {file_id}"} and status code as 200 if no validation error.
2. Returns {"result": str(err)} and status code as 400 if any validation error is raised.

## Delete API(/delete_audio/<audioFileType>/<audioFileID>)
### Input
Accepts 2 path parameters named audioFileType and audioFileID.
1. audioFileType allows only (song, podcast, and audiobook) as its value.
2. audioFileID that is returned by create API.

### Sample Delete Input
![delete_sample_input](https://github.com/sachdevasachin434/filed_assignment/blob/master/images/sample_delete_input.png?raw==True)
### Output
1. Returns {"result": "Please pass audioFileType as song, podcast or audiobook."}
and status code 400 if audioFileType is not valid.
2. Returns {"result": "Audio Deleted Successfully."} and status code 200 if there is
record in MongoDB for required audioFileID.
3. Returns {"result": str(err)} and status code 400 if no record is found for passed audioFileID or any validation error is raised.

## Update API(/update_audio/<audioFileType>/<audioFileID>)
### Input
Accepts 2 path parameters named audioFileType and audioFileID.
1. audioFileType allows only (song, podcast, and audiobook) as its value.
2. audioFileID for which update operation is required. The user can only pass those fields for which updation is required.
### Sample Update Input
![update_sample_input](https://github.com/sachdevasachin434/filed_assignment/blob/master/images/sample_update_input.png?raw==True)
### Output
1. Returns {"result": "Please pass audioFileType as song, podcast or audiobook."}
and status code 400 if audioFileType is not valid.
2. Returns {"result": "Updated Document for the required audioFileId."} and status
code 200 if there is record in MongoDB for required audioFileID.
3. Returns {"result": str(err)} and status code 400 if no record is found for passed audioFileID or any validation error is raised

## Get API(/get_audio/<audioFileType>/<audioFileID>)(Avoid postman, instead hit api from chrome or browser.)
### Input
Accepts 2 path parameters named audioFileType and audioFileID.
1. audioFileType allows only (song, podcast, and audiobook) as its value.
2. audioFileID for which audio file is required.
### Output
1. Returns {"result": "Please pass audioFileType as song, podcast or audiobook."}
and status code 400 if audioFileType is not valid.
2. Returns audio file as attachment and status code 200 if there is record in MongoDB for required audioFileID.
3. Returns {"result": str(err)} and status code 400 if no record is found for passed
audioFileID or any validation error is raised.
## Get API(/get_audio/<audioFileType>)(Avoid postman, instead hit api from chrome or browser.)
### Input
Accepts 2 path parameters named audioFileType and audioFileID.
1. audioFileType allows only (song, podcast, and audiobook) as its value.
### Output
1. Returns {"result": "Please pass audioFileType as song, podcast or audiobook."}
and status code 400 if audioFileType is not valid.
2. Returns zip file(contains all audio files of audioFileType) as attachment and status code 200 if there is record in MongoDB for required audioFileType.
3. Returns {"result": str(err)} and status code 400 if no record is found for passed audioFileType or any validation error is raised.

## Run Test Cases
cd /parent_directory/filed_assignment/src
pytest

### The application is running perfectly. If anything is required from my side, feel free to contact me at +917015920459 or mail to sachdevasachin434@gmail.com.