pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh'echo "begining build"'
                sh '''
                 echo "secound step build"
                 ls -lah 
                 '''          
            }
        }
    }
}