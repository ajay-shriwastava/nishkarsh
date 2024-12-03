##### One Time Authentication Set up if changing account or project
$ cd ~/workspace/projects/nishkarsh/src/webUI
$ workon nishkarsh
$ gcloud config set account abc@gmail.com
$ gcloud config set project nishkarsh
$ gcloud auth application-default set-quota-project nishkarsh

##### Building the image locally   
$ cd ~/workspace/projects/nishkarsh/src/webUI
$ workon nishkarsh
$ gcloud auth login     
$ gcloud config set project nishkarsh    
$ gcloud config set account ACCOUNT    
$ export DOCKER_BUILDKIT=0    
$ export COMPOSE_DOCKER_CLI_BUILD=0    
$ docker build --tag nishkarsh .    
$ docker images
     
##### Running locally     
$ docker run -d -p 5000:5000 nishkarsh   
$ docker attach <IMG_ID>
$ https://localhost:5000
     
##### Deploying to google cloud  
$ Cloud Console => Artifact Registry => Create docker Repository nishkarsh-repo in us-central1
$ gcloud auth configure-docker us-central1-docker.pkg.dev      
$ docker tag nishkarsh:latest us-central1-docker.pkg.dev/nishkarsh/nishkarsh-repo/nishkarsh:latest         
$ docker push us-central1-docker.pkg.dev/nishkarsh/nishkarsh-repo/nishkarsh:latest    
$ Go to Console => Cloud Run => Deploy Container => Service => Select Image => Container Port : 5000 => Deploy       


##### Some useful docker commands
- $ docker ps -a: To see all the running containers in your machine.     
- $ docker stop <container_id>: To stop a running container.     
- $ docker rm <container_id>: To remove/delete a docker container(only if it stopped).     
- $ docker image ls: To see the list of all the available images with their tag, image id, creation time and size.     
- $ docker rmi <image_id>: To delete a specific image.     
- $ docker rmi -f <image_id>: To delete a docker image forcefully     
- $ docker rm -f (docker ps -a | awk '{print$1}'): To delete all the docker container available in your machine     
- $ docker image rm <image_name>: To delete a specific image     
- $ docker system prune -a: To clean the docker environment, removing all the containers and images.     






$ echo ${GOOGLE_CLOUD_PROJECT}    
$ export GOOGLE_CLOUD_PROJECT=iisc-cds7-grp7    
$ gcloud config set project iisc-cds7-grp7    
$ export REGION=us-central1    
$ gcloud compute networks subnets update default \
  --region=${REGION} \
  --enable-private-ip-google-access     
$ gcloud compute networks subnets describe default \
  --region=${REGION} \
  --format="get(privateIpGoogleAccess)"       
$ export BUCKET=iisc-cds7-grp7-mmtd    
$ gcloud storage ls gs://${BUCKET} --buckets gs://iisc-cds7-grp7-mmtd/    
$ export DATASET=mmtd    
$ bq  --location=${REGION} mk -d ${DATASET}   
Dataset 'iisc-cds7-grp7:mmtd' successfully created.    
$ bq ls    
$ export PHS_CLUSTER_NAME=mmtd-spark-cluster    
$  gcloud dataproc clusters create ${PHS_CLUSTER_NAME} \
   --region=${REGION} \
   --single-node \
   --enable-component-gateway \
   --properties=spark:spark.history.fs.logDirectory=gs://${BUCKET}/phs/*/spark-job-history    
Go to Data Proc Cluster : https://console.cloud.google.com/dataproc/clusters    

$ git clone https://github.com/GoogleCloudPlatform/devrel-demos.git       
$ cd devrel-demos/data-analytics/next-2022-workshop/dataproc-serverless       
Open citibike.py in the Cloud Shell Editor to browse the code.     
Click Open Terminal to return to the Cloud Shell terminal.     
$ git clone https://github.com/ajay-shriwastava/PersonalisedMusicRecommendation.git       