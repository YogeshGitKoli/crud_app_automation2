pipeline {
    agent any

    environment {
        EC2_USER = 'ec2-user'
        EC2_IP = '13.203.208.217'  // EC2 public IP
        //PROJECT_DIR = '/home/ec2-user/django-project'
    }

    stages {
        stage('Checkout main branch') {
            steps {
                git branch: 'main', url: 'https://github.com/yogeshGit11/crud_app.git'
            }
        }


        stage('Deploy to EC2') {
            steps {
                sshagent(['ec2-ssh']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no $EC2_USER@$EC2_IP '
                        cd /home/project/crud_app
                        git pull origin main
                        source env/bin/activate
                        pip install -r requirements.txt
                        python manage.py migrate
                        python manage.py collectstatic --noinput
                        sudo systemctl restart gunicorn
                    '
                    """
                }
            }
        }
    }
}

