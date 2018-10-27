<img src="http://techfutures.org/wp-content/uploads/2016/01/cssi-2.jpg"/>

## Google Computer Science Summer Institute(CSSI) Final Project: Flappy Potato
This is the code for Flappy Potato as written by Gurvinder Singh, Sandra Ibrahim, and Jonathan Edwards. This project was completed during our tenure at CSSI NYC 2018. This project has been / will be updated for various reasons including but not limited to feature additions, bug fixes, etc.

* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
  * Install Python
  * Install Google Cloud SDK
* [Deployment](#deployment)
* [Built With](#built-with)
  * Jinja2
  * Webapp2
  * NDB
* [Authors](#authors)
  * Jonathan Edwards
  * Sandra Ibrahim
  * Gurvinder Singh
* [License](#license)

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
* Testing and Debugging
  * [Local Development Server](https://cloud.google.com/appengine/docs/standard/python/tools/using-local-server) - run the `dev_appserver.py configuration-file.yaml` command from within the root directory of your application where your configuration file(s) are located.
  * [Deploying to App Engine](https://cloud.google.com/appengine/docs/standard/python/tools/uploadinganapp) - run the ```gcloud app deploy configuration-file.yaml``` command from within the root directory of your application where your configuration file(s) are located.

### Built With ###
* [Jinja2](http://jinja.pocoo.org/docs) - Template engine used to display data sent from backend.
* [Webapp2](https://webapp2.readthedocs.io/en/latest/) - Lightweight Python web framework.
* [NDB](https://cloud.google.com/appengine/docs/standard/python/ndb/) - Google Datastore NDB Client Library used for storing names & scores.

### Authors ###
* [Jonathan Edwards](https://github.com/jonthnedw)
* [Sandra Ibrahim](https://github.com/sandraibrahim)
* [Gurvinder Singh](https://github.com/tubbyyyy)

### License ###
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for more details.
