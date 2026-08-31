pipeline {
    agent any

        stages {

            stage('Checkout') {
                steps {
                    checkout scm
                }
            }

            stage('Build') {
                steps {
                    dir('app') {
			sh 'python3 --version'
			sh 'python3 -m venv venv'
			sh 'venv/bin/pip install -r requirements.txt'
			sh 'venv/bin/python manage.py check'
		    }
                }
            }

            stage('Test') {
                steps {
                    echo 'Running application tests'
                }
            }
        }
    }
