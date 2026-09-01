pipeline {
    agent any

        environment {
        DB_NAME = 'bankdb'
        DB_HOST = 'postgres-db'
        DB_PORT = '5432'

        DB_CREDS = credentials('postgres-db-credentials')

	DB_USER = "${DB_CREDS_USR}"
        DB_PASSWORD = "${DB_CREDS_PSW}"   
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
			sh 'venv/bin/python manage.py test'
		}

             }
          }
      }
  }
