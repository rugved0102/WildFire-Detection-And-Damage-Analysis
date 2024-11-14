# Wildfire Detection Project
In this project, we created a U-net deep learning model that takes any satellite imagery and detects the wildfire burning scar. <br/>
The model is trained on Databricks, and the application is deployed on Streamlit. <br/>

### Installation 
Clone this repo and direct to the `./app` folder. <br/>
- **Method 1:** Run with Python IDE<br/>
Go to the folder`/app` and then in your terminal please type the following code: <br/>
`streamlit run app.py` <br/>
Please make sure you have the dependency installed is the same as listed in the "requirement.txt"

- **Method 2:** Run with Docker<br/>
You probably need to download docker before you start running the app. <br/>
Then under the folder `./app` in terminal, please add this command `docker build -f Dockerfile -t app:latest .`. This is going to create the docker image and build the corresponding docker container. <br/>
For your better usage, the trained model has been stored in the docker container. <br/>
Then please use the code `docker run -p 8501:8501 app:latest`, this is going to open the app for you. <br/>
Use your favourite browser, and type `http://localhost:8501/` and you should be able to open our app. <br/>
After you done with the app, please remember to stop the container. <br/>
