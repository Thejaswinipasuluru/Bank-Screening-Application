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
                    echo 'Building Bank Screening application'
                }
            }

            stage('Test') {
                steps {
                    echo 'Running application tests'
                }
            }
        }
    }
