pipeline{
    agent any 
    stages{
        stage("Cloning the repository"){
            steps{
                sh 'echo "Cloning the repository"'
                sh 'git clone https://github.com/SamahaAnwar/MLOps_Task2.git'
            }
        }
        stage("Install Dependencies") {
            steps{
                sh '''echo "Installing Dependencies"
                pip install -r requirements.txt
                '''
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
                dir('MLOps_Task2'){
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