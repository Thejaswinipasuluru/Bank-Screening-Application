pipeline {
    agent any

    environment {
        DB_NAME = 'bankdb'
        DB_HOST = 'postgres-db'
        DB_PORT = '5432'
        DB_CREDS = credentials('postgres-db-credentials')
    }

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
                dir('app') {
                    withCredentials([
                        usernamePassword(
                            credentialsId: 'postgres-db-credentials',
                            usernameVariable: 'DB_USER',
                            passwordVariable: 'DB_PASSWORD'
                        )
                    ]) {
                        sh 'venv/bin/python manage.py test'
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                dir('app') {
                    sh 'docker build -t bank-screening:${BUILD_NUMBER} .'
                }
            }
        }
    }
}