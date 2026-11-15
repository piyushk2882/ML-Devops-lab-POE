pipeline {
    agent any

    environment {
    PATH = "C:\\Users\\piyus\\AppData\\Local\\Programs\\Python\\Python310;C:\\Users\\piyus\\AppData\\Local\\Programs\\Python\\Python310\\Scripts;${env.PATH}"
}


    options {
        // The Checkout stage below performs the repository checkout explicitly.
        skipDefaultCheckout(true)
    }

    stages {
        stage('Run Python') {
            steps {
                bat 'python --version'
            }
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
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
                        bat 'py -3 -m venv .venv'
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
