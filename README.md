<img src="http://techfutures.org/wp-content/uploads/2016/01/cssi-2.jpg"/>

## Google Computer Science Summer Institute(CSSI) Final Project: Flappy Potato
This is the code for Flappy Potato as written by Gurvinder Singh, Sandra Ibrahim, and Jonathan Edwards. This project was completed during our tenure at CSSI NYC 2018. This project has been / will be updated for various reasons including but not limited to feature additions, bug fixes, etc.
* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Deployment](#deployment)

### Getting Started ###
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. These instructions will also help you deploy your code to app engine. See prerequisites & notes on how to deploy the project on a live system.

### Prerequisites ###
* Install Python - You must have [Python 2.7](https://www.python.org/downloads/release/python-2715/) installed on your local system. This project has not been tested on any version after Python 2.7.
* Install Google Cloud SDK
  * Download the [Google Cloud SDK](https://cloud.google.com/sdk/docs/)
  * Navigate to the extracted folder and add Cloud SDK tools to your path: `./google-cloud-sdk/install.sh`
  * Run gcloud init to initialize the Cloud SDK: `./google-cloud-sdk/bin/gcloud init`
    * Optional: Install the Extra Libraries component for Python, which includes the graphy and Django libraries: `gcloud components install app-engine-python-extras`
  * Update: If you already have the Google Cloud SDK installed, you can run the following command to update the SDK to the latest version: `gcloud components update`

### Deployment ###
* Open your text editor or IDE of choice
* Testing
  * [Local Development Server](https://cloud.google.com/appengine/docs/standard/python/tools/using-local-server) - run the dev_appserver.py command from the directory that contains your app's configuration file:
    `dev_appserver.py configuration-file.yaml`
  * [Deploying to App Engine](https://cloud.google.com/appengine/docs/standard/python/tools/uploadinganapp) - run the gcloud app deploy command from within the root directory of your application where your configuration file(s) are located: ```gcloud app deploy configuration-file.yaml```
