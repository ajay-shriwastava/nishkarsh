##### Building the image locally   
$ gcloud auth login     
$ gcloud config set project iisc-cds7-grp7     
$ gcloud config set account ACCOUNT    
$ export DOCKER_BUILDKIT=0    
$ export COMPOSE_DOCKER_CLI_BUILD=0    
$ docker build --tag gr7-capstone .    
$ docker images
     
##### Running locally     
$  docker run -d -p 5000:5000 gr7-capstone    
$  https://localhost:5000
     
##### Deploying to google cloud     
$ gcloud auth configure-docker us-central1-docker.pkg.dev      
$ docker tag gr7-capstone:latest us-central1-docker.pkg.dev/iisc-cds7-grp7/gr7-capstone-repo/gr7-capstone:latest         
$ docker push us-central1-docker.pkg.dev/iisc-cds7-grp7/gr7-capstone-repo/gr7-capstone:latest    
$ Go to Console => Cloud Run => Select Image => Deploy       






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