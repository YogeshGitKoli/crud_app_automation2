pipeline {
    agent any

    environment {
        EC2_USER = 'ec2-user'
        EC2_IP = '3.110.119.240'  // EC2 public IP
        //PROJECT_DIR = '/home/ec2-user/django-project'
    }

    stages {
        stage('Checkout main branch') {
            steps {
            git branch: 'main', 
                url: 'git@github.com:YogeshGitKoli/crud-app_jenkins-automation.git',
                //credentialsId: '43b7b09d-fcea-4d94-846c-222d6eaf20f5'
		credentialsId: 'b32c81e4-81da-467b-b5f5-8a74f841ebcf'
         }
        }


        stage('Deploy to EC2') {
            steps {
                //sshagent(['b92ba81e-0f10-4d52-adbd-c67b09d58233']) {
		sshagent(['deccb537-61de-4b9b-9d88-9743f65e8e06']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no $EC2_USER@$EC2_IP '
                        cd /home/project/crud_app
                        git pull origin main
                        source env/bin/activate
                        pip install -r requirements.txt
                        python manage.py migrate
                        python manage.py collectstatic --noinput
                        sudo systemctl restart gunicorn
			sudo systemctl restart nginx
                    '
                    """
                }
            }
        }
    }
}

