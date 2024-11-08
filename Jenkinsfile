pipeline {
    agent any
    environment {
        VIRTUAL_ENV = 'venv'
    }
    stages {
        stage('Setup') {
            steps {
                script {
                    if (!fileExists("${env.WORKSPACE}/${VIRTUAL_ENV}")) {
                        bat "python-m venv ${VIRTUAL_ENV}"
                    }
                    bat "source ${VIRTUAL_ENV}/bin/activate && pip install-r requirements.txt"
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    bat "source ${VIRTUAL_ENV}/bin/activate && flake8 app.py"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat "source ${VIRTUAL_ENV}/bin/activate && pytest"
                }
            }   
        }

        stage('Deploy') {
            steps {
                script {
                    // Deployment logic, e.g., pushting to a remote server
                    echo "Deploying application..."
                }
            }
        }
    }   
    post {
        always {
            cleanWs()
        }
    }
}
