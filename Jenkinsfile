pipeline {
    agent any

    environment {
        EC2_USER = 'ec2-user'
        EC2_IP = '3.110.119.240'
        APP_NAME = 'crud-app'
        IMAGE_NAME = 'ypckoli/crud_app_image'
    }

    stages {
        stage('Deploy to EC2 and Build Docker') {
            steps {
                sshagent(['deccb537-61de-4b9b-9d88-9743f65e8e06']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no $EC2_USER@$EC2_IP '
                        echo "Pulling latest code..."
                        cd /home/project/2crud_app/crud-app_jenkins-automation/
                        git pull origin main

                        echo "Building Docker image..."
                        docker build -t $IMAGE_NAME .

                        echo "Stopping and removing old container..."
                        docker stop $APP_NAME || true
                        docker rm $APP_NAME || true

                        echo "Running container..."
                        docker run -d --name $APP_NAME -p 8000:8000 $IMAGE_NAME
                    '
                    """
                }
            }
        }
    }
}

