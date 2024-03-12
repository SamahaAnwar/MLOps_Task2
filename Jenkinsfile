pipeline{
    agent any 
    stages{
        stage("Cloning the repository"){
            steps{
                echo "Cloning the repository"
                git url: "https://github.com/SamahaAnwar/MLOps_Task2.git"
            }
        }
        stage("Install Dependencies") {
            steps{
                echo "Installing Dependencies"
                pip install -r requirements.txt
            }
        }
        stage("Testing"){
            steps{
                echo "Testing"
                pytest test.py                     
            }
        }
        stage("Deployement"){
            steps{
                echo "Deploying"
                script {
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