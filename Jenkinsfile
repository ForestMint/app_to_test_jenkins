pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Setup') {
            steps {
                echo "Cleaning and setting up virtual environment"
                sh 'python3 -m venv $VENV_DIR'
                sh './$VENV_DIR/bin/pip install --upgrade pip'
                sh './$VENV_DIR/bin/pip install -r requirements.txt || true'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running unit tests"
                sh './$VENV_DIR/bin/python -m unittest test_script.py'
            }
        }
    }

    post {
        always {
            echo "Pipeline completed"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}