pipeline{
    agent any
    environment{
        urlRegistry = "https://registry.hub.docker.com/"
        registry = "oziel4ever/api-flask-oziel"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }

    stages {

        stage('Getting resources...'){
            steps{
                git url: 'https://github.com/Oziel-Silva/api_rest_with_flask.git', branch: 'pipeline'
            }
        }

        stage('Building our image...'){
            steps{
                script {
                    dockerImage = docker.build(registry + ":$BUILD_NUMBER", "-f ./Dockerfile .")
                }
            }
        }

        stage('Pushing image to repository...'){
            steps{
                script{
                    docker.withRegistry(urlRegistry, registryCredential ){    
                        dockerImage.push("$BUILD_NUMBER")
                    }
                }
            }
        }
    }
}
