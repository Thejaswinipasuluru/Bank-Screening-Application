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
			sh 'pip3 install -r requirements.txt'
			sh 'python3 manage.py check'
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
