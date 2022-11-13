pipeline 

{

    agent
    {
        label 'docker-node'
    }
    

    environment 
    {
        DOCKERHUB_CREDENTIALS=credentials('docker-hub')
    }
    stages 

    {
        stage('Create docker network')

        {
            steps
            {
                sh 'docker network ls | grep exam-net || docker network create exam-net'
            }
        }

        stage('Clone the project') 

        {

            steps 

            {
                git branch: 'main', url: 'http://192.168.150.202:3000/vagrant/exam.git'
            }

        }

        stage('Build the images')

        {

            steps

            {

                sh 'cd client && docker image build -t img-client -f Dockerfile .'
                sh 'cd generator && docker image build -t img-generator -f Dockerfile .'
                sh 'cd storage && docker image build -t img-storage -f Dockerfile .'

            }

        }

        stage('Run the  applications in test mode')

        {

            steps

            {

                sh '''

                docker container rm -f con-client || true

                docker container run -d --name con-client --net exam-net -p 8080:5000 img-client

                docker container rm -f con-generator || true

                docker container run -d --name con-generator --net exam-net img-generator

                docker container rm -f con-storage || true

                docker container run -d --name con-storage --net exam-net -e MYSQL_ROOT_PASSWORD='ExamPa$$w0rd' img-storage

                '''

            }

        }
        stage('Testing application reachability')

        {

            steps

            {


                echo 'Test #1 - reachability'
                sh 'echo $(curl --write-out "%{http_code}" --silent --output /dev/null http://192.168.150.202:8080) | grep 200'
                
            }

        }
         stage('Stop and remove containers')

        {

            steps

            {

                sh '''

                docker container rm -f con-client con-storage con-generator

                '''

            }

        }
        stage('Login to Dockerhub') 
        {
            steps 
            {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }

        stage('Publishing img to dockerhub')

        {

            steps

            {

                echo 'Publish client img'
                sh 'docker image tag img-client zdravkov/img-client'
                sh 'docker push zdravkov/img-client'

                echo 'Publish generator img'
                sh 'docker image tag img-generator zdravkov/img-generator'
                sh 'docker push zdravkov/img-generator'

                echo 'Publish storage img'
                sh 'docker image tag img-storage zdravkov/img-storage'
                sh 'docker push zdravkov/img-storage'
            }

        }
         stage('Run the  applications in prod environment')

        {

            steps

            {

                sh '''

                docker container rm -f con-client || true

                docker container run -d --name con-client --net exam-net -p 80:5000 zdravkov/img-client

                docker container rm -f con-generator || true

                docker container run -d --name con-generator --net exam-net zdravkov/img-generator

                docker container rm -f con-storage || true

                docker container run -d --name con-storage --net exam-net -e MYSQL_ROOT_PASSWORD='ExamPa$$w0rd' zdravkov/img-storage

                '''

            }

        }


    }
}  