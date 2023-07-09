# Execution Commands
```
gcloud auth login

gcloud compute instances create testvm --zone=us-east1-b \
--machine-type=n1-highmem-8 \
--image=centos-7-v20210817 \
--image-project=centos-cloud \
--boot-disk-size="50GB"

gcloud compute instances add-metadata testvm --metadata=important-data="2 plus 2 equals 4"


$ gcloud compute instances describe testvm --zone=us-east1-b --format="json(metadata)"

$ gcloud compute instances describe testvm --zone=us-east1-b --format="json(metadata)"
{
  "metadata": {
    "fingerprint": "6XsNCqncpxo=",
    "items": [
      {
        "key": "important-data",
        "value": "2 plus 2 equals 4"
      }
    ],
    "kind": "compute#metadata"
  }
}
```