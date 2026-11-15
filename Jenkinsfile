pipeline {
    agent any

    environment {
        // Make this Python installation visible to the Jenkins service.
        // Change this path if Python is installed somewhere else.
        PATH = "C:\\Users\\piyus\\AppData\\Local\\Programs\\Python\\Python310;C:\\Users\\piyus\\AppData\\Local\\Programs\\Python\\Python310\\Scripts;${env.PATH}"
    }

    options {
        // Checkout is performed explicitly in the Checkout stage.
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 --version'
                    } else {
                        bat 'python --version'
                    }
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m venv .venv'
                        sh '.venv/bin/python -m pip install --upgrade pip'
                        sh '.venv/bin/python -m pip install -r requirements.txt'
                    } else {
                        bat 'python -m venv .venv'
                        bat '.venv\\Scripts\\python -m pip install --upgrade pip'
                        bat '.venv\\Scripts\\python -m pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '.venv/bin/python -m pytest -q'
                    } else {
                        bat '.venv\\Scripts\\python -m pytest -q'
                    }
                }
            }
        }
    }
}
