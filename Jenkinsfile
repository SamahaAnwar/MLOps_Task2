pipeline{
    agent any
    stages{
        stage("Cloning the repository"){
            steps{
                echo "Cloning the repository"
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], 
                          userRemoteConfigs: [[url: 'https://github.com/SamahaAnwar/MLOps_Task2.git']]])

            }
        }
        stage("Install Dependencies") {
            steps{
                echo "Installing Dependencies"
                bat 'make install'
                
            }
        }
        stage("Testing"){
            steps{
                sh '''echo "Testing"
                pytest test.py'''                     
            }
        }
        stage("Deployement"){
            steps{
                sh 'echo "Deploying"'
                script{
                    // Get the current branch name
                    def branchName = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()

                    // Check the branch name and deploy accordingly
                    if (branchName == 'main') {
                        echo "Deploying to production"
                    } else {
                        echo "Deploying to UAT"
                    }
                }
            }
        }
    }
}