pipeline {
  agent any
  stages { 
    stage('Checkout') { 
      steps {
        checkout scm
      }
    }
    stage('Setup') { // Install any dependencies you need to perform testing
      steps {
        script {
          sh """
          python3 -m venv env
          . env/bin/activate
          pip install -r requirements.txt
          """
        }
      }
    }
    stage('Linting') { // Run pylint against your code
      steps {
        script {
          sh """
          pylint *.py
          """
        }
      }
    }
    stage('Unit Testing') { // Perform unit testing
      steps {
        script {
          sh """
          env/bin/pytest
          """
        }
      }
    }
  }
}