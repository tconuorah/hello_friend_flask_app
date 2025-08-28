pipeline {
    agent any
    environment {
        IMAGE_NAME = 'tconuorah/hello_friend_flask_app-test'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/tconuorah/hello_friend_flask_app'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat """
                docker build -t %IMAGE_NAME%:latest .
                """
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat """
                    echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    docker push %IMAGE_NAME%:latest
                    docker logout
                    """
                }
            }
        }
    }
}
