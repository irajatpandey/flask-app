pipeline {
   agent { label 'my-agent' } 

    environment {
        IMAGE_NAME = "my-flask-app"
        CONTAINER_NAME = "flask-container"
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "Cloning repository..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests..."
                sh "docker run --rm ${IMAGE_NAME} pytest"
            }
        }

        stage ('Push to Artifactory') {
            steps {
                echo "Pushing the ${IMAGE_NAME} to artifactory"
                withCredentials([usernamePassword(credentialsId: 'artifactoryCred', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                        sh '''
                        docker login -u ${USER} -p ${PASS} learndevopskill.jfrog.io
                        docker tag my-flask-app:latest learndevopskill.jfrog.io/docker-trial/my-flask-app:latest
                        docker push learndevopskill.jfrog.io/docker-trial/my-flask-app:latest
                        '''
                }

            }
        }

        stage('Deploy Container') {
            steps {
                echo "Deploying application..."
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
                sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
            }
        }
    }
}
