pipeline {
    agent any

    environment {
        EC2_USER = 'ec2-user'
        EC2_IP = '3.110.119.240'
        APP_NAME = 'crud-app'
        IMAGE_NAME = 'ypckoli/crud_app_image'
	DOCKER_CREDENTIALS = 'f2e5b30d-881e-42f0-aad2-f0a027ffb448'
    }

    stages {
        stage('Deploy to EC2 and Build Docker') {
            steps {
                /*sshagent(['deccb537-61de-4b9b-9d88-9743f65e8e06']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no $EC2_USER@$EC2_IP '
                        echo "Pulling latest code..."
                        cd /home/project/2crud_app/crud-app_jenkins-automation/
                        git pull origin main

                        echo "Building Docker image..."
                        docker build -t $IMAGE_NAME .

  			echo "Tagging image for Docker Hub..."
                        docker tag $IMAGE_NAME yogeshgitkoli/$IMAGE_NAME:latest

                        echo "Logging into Docker Hub..."
                        echo "\${DOCKER_HUB_PASSWORD}" | docker login -u "\${DOCKER_HUB_USERNAME}" --password-stdin

                        echo "Pushing image to Docker Hub..."
                        docker push yogeshgitkoli/$IMAGE_NAME:latest


                        echo "Stopping and removing old container..."
                        docker stop $APP_NAME || true
                        docker rm $APP_NAME || true

                        echo "Running container..."
                        docker run -d --name $APP_NAME -p 8000:8000 $IMAGE_NAME
                    '
                    """
                }*/
	sshagent(['deccb537-61de-4b9b-9d88-9743f65e8e06']) {
	    withCredentials([usernamePassword(credentialsId: 'f2e5b30d-881e-42f0-aad2-f0a027ffb448', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
        sh """
        ssh -o StrictHostKeyChecking=no $EC2_USER@$EC2_IP '
            echo "Pulling latest code..."
            cd /home/project/2crud_app/crud-app_jenkins-automation/
            git pull origin main

            echo "Building Docker image..."
            docker build -t $IMAGE_NAME .

            echo "Tagging image for Docker Hub..."
            docker tag $IMAGE_NAME:latest

            echo "Logging into Docker Hub..."
            echo "\${DOCKER_HUB_PASSWORD}" | docker login -u "\${DOCKER_HUB_USERNAME}" --password-stdin

            echo "Pushing image to Docker Hub..."
            docker push yogeshgitkoli/$IMAGE_NAME:latest

            echo "Stopping and removing old container..."
            docker stop $APP_NAME || true
            docker rm $APP_NAME || true

            echo "Running container..."
            docker run -d --name $APP_NAME -p 8000:8000 yogeshgitkoli/$IMAGE_NAME:latest
        '
        """
    }
}

            }
        }
    }
}

